from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-pose.pt')

# Predict with the model
results = model("/Users/janardhanareddyms/Desktop/crowd_mall.mp4", show=True,stream=True)
# no_of_persons = results[0].keypoints.conf.size(0)

# result_keypoint = results[0].keypoints
# result_head  = result_keypoint.data[0:no_of_persons]

# print(f"No of persons detected: {no_of_persons}")


for r in results:
    print(r.boxes)

# for _ in range(no_of_persons):
#     print(f"Head and toe cordinates for {_} person")
#     print(result_head[_][0].numpy())
#     print(result_head[_][16].numpy())

# head_array = result_head.numpy()