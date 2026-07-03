import "./index.css";
import { Composition } from "remotion";
import { MyComposition } from "./Composition";
import videoData from "./video-data.json";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="MyComp"
        component={MyComposition}
        durationInFrames={videoData.totalDurationFrames}
        fps={videoData.fps}
        width={videoData.width}
        height={videoData.height}
      />
    </>
  );
};
