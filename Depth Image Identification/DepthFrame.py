import pyrealsense2 as rs
import numpy as np
import datetime

# Create a pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_device_from_file("Maman_Depth_vid.bag")
pipeline.start(config)

endTime = datetime.datetime.now() + datetime.timedelta(seconds=17)
# Loop over frames
while True:
    # Wait for the next frame
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()

    # Check if depth frame is valid
    if not depth_frame:
        continue

    # Retrieve depth data as NumPy array
    depth_image = np.asanyarray(depth_frame.get_data())

    # Perform depth calculations as needed
    print(depth_image)
    # # Break the loop after the video ends
    if datetime.datetime.now() >= endTime:
        break
# Stop the pipeline
pipeline.stop()
