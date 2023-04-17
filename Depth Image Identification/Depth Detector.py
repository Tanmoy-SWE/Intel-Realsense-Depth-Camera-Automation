import pyrealsense2 as rs
import numpy as np

# Open the bag file
pipeline = rs.pipeline()
config = rs.config()
config.enable_device_from_file("Maman_Depth_vid.bag")
pipeline.start(config)
depth_profile = pipeline.get_active_profile().get_stream(rs.stream.depth)

# Get the FPS and number of frames per second
fps = depth_profile.as_video_stream_profile().get_framerate()
duration = int(
    pipeline.get_active_profile().get_device().query_sensors()[0].get_info(rs.camera_info.camera_info_product_line))
frame_count = duration * fps

# Loop through each second and calculate the average depth
for i in range(frame_count // fps):
    # Get the frames for this second
    start_frame = i * fps
    end_frame = start_frame + fps - 1
    frames = []
    for j in range(start_frame, end_frame):
        # Get the depth frame
        frameset = pipeline.wait_for_frames()
        depth_frame = frameset.get_depth_frame()
        depth_image = np.asanyarray(depth_frame.get_data())
        frames.append(depth_image)

    # Calculate the average depth for this second
    average_depth = np.mean(frames)

    # Print the result
    print(f"Second {i + 1}: {average_depth} meters")

# Release resources
pipeline.stop()
