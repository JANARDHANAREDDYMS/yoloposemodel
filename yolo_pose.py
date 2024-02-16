# from ultralytics import YOLO
# import numpy

# model = YOLO('yolov8n-pose.pt')

# results = model("/Users/janardhanareddyms/Downloads/crowd_japan.mp4", show=True)

# extract_points = results.keypoints.xyn.cpu().numpy()[:2]
# type(extract_points)
# print(extract_points)


from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-pose.pt')

# Predict with the model
results = model("/Users/janardhanareddyms/Downloads/biles.jpg", show=True)
no_of_persons = results[0].keypoints.conf.size(0)

result_keypoint = results[0].keypoints
result_head  = result_keypoint.data[0:no_of_persons]
print(result_keypoint)
print(f"No of persons detected: {no_of_persons}")

for _ in range(no_of_persons):
    print(f"Head and toe cordinates for {_} person")
    print(result_head[_][0].numpy())
    print(result_head[_][16].numpy())

head_array = result_head.numpy()

# head_val,toe_val = head_array[0],head_array[16]


# print(result_head)
# for _ in range(no_of_persons):
    # print(result_keypoint)
# print(head_val)
# print(toe_val)


# print(result_keypoint)
# for frame_idx, result in enumerate(results):
#     extracted_points = result.keypoints.xyn.cpu().numpy()

#     for person_idx in range(len(extracted_points)):

#         print(f"Frame {frame_idx + 1} - Person 1 Keypoints:")
#         print(extracted_points[person_idx][:2]) 



