import { useCurrentFrame, AbsoluteFill, Img } from "remotion";
import videoData from "./video-data.json";

export const MyComposition = () => {
  const frame = useCurrentFrame();

  // Find active shot
  const activeShot = videoData.shots.find(
    (shot) => frame >= shot.startFrame && frame < shot.endFrame
  ) || videoData.shots[0];

  if (!activeShot) {
    return (
      <AbsoluteFill style={{ backgroundColor: "black" }} />
    );
  }

  // Calculate local progress in active shot for soft transitions
  const localFrame = frame - activeShot.startFrame;
  const fadeDuration = 3; // 3 frames fade transition (0.1s)
  let opacity = 1;
  if (localFrame < fadeDuration) {
    opacity = localFrame / fadeDuration; // fade in
  } else if (activeShot.endFrame - frame < fadeDuration) {
    opacity = (activeShot.endFrame - frame) / fadeDuration; // fade out
  }

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#111",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        overflow: "hidden",
        fontFamily: "system-ui, -apple-system, sans-serif",
      }}
    >
      {/* Visual Image Render */}
      <div
        style={{
          width: "100%",
          height: "100%",
          position: "relative",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          opacity,
        }}
      >
        <Img
          src={activeShot.imageSrc}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
          }}
        />
      </div>

      {/* Styled High-Retention Subtitles */}
      <div
        style={{
          position: "absolute",
          bottom: "12%",
          left: "5%",
          right: "5%",
          display: "flex",
          justifyContent: "center",
          textAlign: "center",
          zIndex: 10,
        }}
      >
        <span
          style={{
            color: "#FFEA33", // Vibrant gold-yellow for high impact
            fontSize: "3.8rem",
            fontWeight: "900",
            textTransform: "uppercase",
            letterSpacing: "0.02em",
            lineHeight: "1.1",
            textShadow: `
              -4px -4px 0 #000,  
               4px -4px 0 #000,
              -4px  4px 0 #000,
               4px  4px 0 #000,
               0px  6px 12px rgba(0,0,0,0.9)
            `,
            padding: "10px 20px",
          }}
        >
          {activeShot.narration}
        </span>
      </div>
    </AbsoluteFill>
  );
};
