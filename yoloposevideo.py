import re
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-pose.pt')

# Predict with the model
results = model("/Users/janardhanareddyms/Desktop/crowd_mall2.mp4", show=True,stream=True)



# pattern = re.compile(r'\b(\d+)\s+persons\b')

# # Iterate over the generator
# for idx, r in enumerate(results, start=1):
    
#     # Extract information about each frame
#     frame_info = str(r)
    
#     # Use regex to find the persons count
#     match = pattern.search(frame_info)
    
#     if match:
#         persons_count = int(match.group(1))
#         print(f"Frame {idx}: Number of persons detected = {persons_count}")
#     else:
#         print(f"Frame {idx}: Unable to extract persons count")
for r in results:
    no_of_persons = r.keypoints.xy.size(0)
    print(f"No of persons detected {int(no_of_persons)}")

    keypoint_data = r.keypoints
    
    for _ in range(int(no_of_persons)):
        head_point = keypoint_data.xy[_][0].numpy()
        right_point = keypoint_data.xy[_][16].numpy()

        print(f"Head Point: {head_point}, Right Toe Point: {right_point}")

    # print(r.keypoints)
    # print(r.boxes)
#     print(r.probs)

# for _ in range(no_of_persons):
#     print(f"Head and toe cordinates for {_} person")
#     print(result_head[_][0].numpy())
#     print(result_head[_][16].numpy())

# head_array = result_head.numpy()