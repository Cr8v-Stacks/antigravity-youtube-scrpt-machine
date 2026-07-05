const fs = require('fs');
const path = require('path');

// Target paths
const workspaceRoot = path.join(__dirname, '..', '..');
const productionPacksDir = path.join(workspaceRoot, 'production-packs');

// Get arguments or use defaults
const packName = process.argv[2] || 'cadaver_synod';
const packDir = path.join(productionPacksDir, packName);
const mdFileName = `${packName}_shorts_pack.md`;
const mdFilePath = path.join(packDir, mdFileName);
const imagesDir = path.join(packDir, 'images');

console.log(`Reading production pack: ${mdFilePath}`);
console.log(`Source images directory: ${imagesDir}`);

if (!fs.existsSync(mdFilePath)) {
  console.error(`Error: Production pack file not found at ${mdFilePath}`);
  process.exit(1);
}

const mdContent = fs.readFileSync(mdFilePath, 'utf8');

// Parse target runtime
let targetDurationSeconds = 60; // fallback
const runtimeMatch = mdContent.match(/Target Runtime.*?\b(\d+):(\d+)\b/i);
if (runtimeMatch) {
  targetDurationSeconds = parseInt(runtimeMatch[1]) * 60 + parseInt(runtimeMatch[2]);
}

// Convert MM:SS to seconds
function parseTime(t) {
  const parts = t.trim().split(':').map(Number);
  if (parts.length === 2) {
    return parts[0] * 60 + parts[1];
  }
  return Number(t);
}

// Sanitize string for filename matching (lowercase, alphanumeric and underscores)
function sanitizeForFilename(str) {
  return str
    .toLowerCase()
    .replace(/[^a-z0-9\s_]/g, '')
    .trim()
    .replace(/\s+/g, '_');
}

// Setup Remotion public assets directory
const publicImagesDir = path.join(__dirname, '..', 'public', 'images');
if (!fs.existsSync(publicImagesDir)) {
  fs.mkdirSync(publicImagesDir, { recursive: true });
}

// Setup audio file if present in the topic directory
const mp3Files = fs.existsSync(packDir) ? fs.readdirSync(packDir).filter(f => f.endsWith('.mp3')) : [];
let hasAudio = false;
if (mp3Files.length > 0) {
  // Default to first .mp3 or matching prefix
  const matchedAudio = mp3Files.find(f => f.includes(packName) || f.startsWith('d1tools') || f.includes('audio'));
  const audioSrc = matchedAudio || mp3Files[0];
  const destAudioPath = path.join(__dirname, '..', 'public', 'audio.mp3');
  fs.copyFileSync(path.join(packDir, audioSrc), destAudioPath);
  hasAudio = true;
  console.log(`Copied audio track: ${audioSrc} -> public/audio.mp3`);
}


// Extract shots
const shotRegex = /^\s*(\d+)[\).]\s*(\d{1,2}:\d{2})\s*(?:-|\u2013)\s*(\d{1,2}:\d{2})\s*$/gm;
const shots = [];
let match;

// Parse the file manually using regex segments
const sections = mdContent.split(/^#+/m);
const shotSection = sections.find(s => s.trim().toLowerCase().startsWith('shot-by-shot image prompts') || s.trim().toLowerCase().startsWith('shot by shot image prompts'));

if (!shotSection) {
  console.error('Error: Shot-By-Shot Image Prompts section not found in markdown!');
  process.exit(1);
}

const shotLines = shotSection.split('\n');
let currentShot = null;

for (let i = 0; i < shotLines.length; i++) {
  const line = shotLines[i].trim();
  const timeMatch = line.match(/^(\d+)[\).]\s*(\d{1,2}:\d{2})\s*(?:-|\u2013)\s*(\d{1,2}:\d{2})$/);
  
  if (timeMatch) {
    if (currentShot) {
      shots.push(currentShot);
    }
    currentShot = {
      index: parseInt(timeMatch[1]),
      start: parseTime(timeMatch[2]),
      end: parseTime(timeMatch[3]),
      narration: '',
      prompt: '',
      imageFile: null
    };
  } else if (currentShot) {
    if (line.toLowerCase().startsWith('narration:')) {
      // Clean quotes and prefix
      currentShot.narration = line.replace(/^narration:\s*"/i, '').replace(/"\s*$/, '').trim();
    } else if (line.toLowerCase().startsWith('prompt a:')) {
      currentShot.prompt = line.replace(/^prompt a:\s*/i, '').trim();
    }
  }
}
if (currentShot) {
  shots.push(currentShot);
}

console.log(`Parsed ${shots.length} shots from markdown.`);

// Match with actual generated images in the images folder
let availableImages = [];
if (fs.existsSync(imagesDir)) {
  availableImages = fs.readdirSync(imagesDir).filter(f => f.endsWith('.png') || f.endsWith('.jpg') || f.endsWith('.jpeg'));
} else {
  console.warn(`Warning: Images directory ${imagesDir} does not exist yet. Using placeholder references.`);
}

const fps = 30;
const processedShots = [];

for (const shot of shots) {
  const sanitizedNarration = sanitizeForFilename(shot.narration);
  let searchName = sanitizedNarration;
  
  // Check if prompt specifies a reused image
  const reuseMatch = shot.prompt && shot.prompt.match(/reuses\s+([a-z0-9_-]+)/i);
  if (reuseMatch) {
    searchName = sanitizeForFilename(reuseMatch[1]);
    console.log(`Shot ${shot.index} specifies reuse of: ${searchName}`);
  }
  
  // Find a matching image file starting with or contained inside the narration/reused name
  let matchedFile = null;
  if (availableImages.length > 0) {
    matchedFile = availableImages.find(f => {
      const nameWithoutExt = f.replace(/\.[^/.]+$/, '').replace(/_\d+$/, ''); // remove extension and timestamp suffix
      return searchName.startsWith(nameWithoutExt) || nameWithoutExt.startsWith(searchName) || searchName.includes(nameWithoutExt);
    });
  }

  // If found, copy it to Remotion public folder
  let remotionImagePath = '';
  if (matchedFile) {
    const srcPath = path.join(imagesDir, matchedFile);
    const destFileName = `${shot.index}_${matchedFile}`;
    const destPath = path.join(publicImagesDir, destFileName);
    fs.copyFileSync(srcPath, destPath);
    remotionImagePath = `/images/${destFileName}`;
    console.log(`Matched & Copied: Shot ${shot.index} -> ${matchedFile}`);
  } else {
    // Check if it's one of the reused images or if we can find any file matching parts of it
    // Fallback: search for a prefix match in available files
    const prefix = sanitizedNarration.substring(0, 30);
    const partialMatch = availableImages.find(f => f.startsWith(prefix));
    if (partialMatch) {
      const srcPath = path.join(imagesDir, partialMatch);
      const destFileName = `${shot.index}_${partialMatch}`;
      const destPath = path.join(publicImagesDir, destFileName);
      fs.copyFileSync(srcPath, destPath);
      remotionImagePath = `/images/${destFileName}`;
      console.log(`Partial Matched & Copied: Shot ${shot.index} -> ${partialMatch}`);
    } else {
      console.log(`No image asset found for Shot ${shot.index}: "${shot.narration.substring(0, 30)}..."`);
      remotionImagePath = '/placeholder.png'; // fallback placeholder image
    }
  }

  processedShots.push({
    index: shot.index,
    startFrame: Math.round(shot.start * fps),
    endFrame: Math.round(shot.end * fps),
    durationFrames: Math.round((shot.end - shot.start) * fps),
    narration: shot.narration,
    imageSrc: remotionImagePath
  });
}

// Calculate total duration in frames
const totalDurationFrames = processedShots.length > 0 
  ? processedShots[processedShots.length - 1].endFrame 
  : targetDurationSeconds * fps;

const outputData = {
  packName,
  totalDurationFrames,
  fps,
  width: 1080,
  height: 1920, // 9:16 vertical orientation
  hasAudio,
  shots: processedShots
};

const outputFilePath = path.join(__dirname, '..', 'src', 'video-data.json');
fs.writeFileSync(outputFilePath, JSON.stringify(outputData, null, 2), 'utf8');
console.log(`Successfully compiled video data JSON to: ${outputFilePath}`);
console.log(`Total duration in frames: ${totalDurationFrames} (${(totalDurationFrames / fps).toFixed(2)} seconds)`);
