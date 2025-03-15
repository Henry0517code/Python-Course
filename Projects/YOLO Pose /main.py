import cv2
from ultralytics import YOLO

# Load the YOLOv8 pose model (ensure the model file name is correct)
MODEL_PATH = "yolo11n-pose.pt"  # update filename if needed
pose_model = YOLO(MODEL_PATH)

# Video source configuration
VIDEO_SOURCE = "video.mp4"  # change to 0 for webcam
cap = cv2.VideoCapture(VIDEO_SOURCE)

# Define skeleton connection pairs (based on COCO keypoint indices)
SKELETON_PAIRS = [
    (0, 1), (0, 2), (1, 3), (2, 4),       # face: nose to eyes, eyes to ears
    (5, 6),                               # shoulders line
    (5, 7), (7, 9), (6, 8), (8, 10),       # arms: shoulder-elbow-wrist
    (5, 11), (6, 12),                      # torso: shoulders to hips
    (11, 12),                             # hips line
    (11, 13), (13, 15), (12, 14), (14, 16)  # legs: hip-knee-ankle
]


def draw_keypoints_and_skeleton(frame, keypoints, confs, conf_threshold=0.5):
    """
    Draws keypoints and skeleton lines on the provided frame.

    Args:
        frame (ndarray): The image frame.
        keypoints (array): Array of shape [17, 2] with x,y coordinates.
        confs (array): Array of shape [17] with confidence values.
        conf_threshold (float): Confidence threshold to draw a keypoint/skeleton.
    """
    # Draw keypoints as circles
    for idx, (point, conf) in enumerate(zip(keypoints, confs)):
        if conf > conf_threshold:
            x, y = point
            cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 255), -1)

    # Draw skeleton lines between pairs of keypoints
    for p1, p2 in SKELETON_PAIRS:
        if confs[p1] > conf_threshold and confs[p2] > conf_threshold:
            x1, y1 = keypoints[p1]
            x2, y2 = keypoints[p2]
            cv2.line(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # End of video or camera error

    # Run pose detection on the current frame
    pose_results = pose_model(frame, conf=0.5, verbose=False)

    # Check if keypoints were detected; if not, display the frame as is
    if pose_results[0].keypoints is None:
        cv2.imshow("Basketball Pose Analyzer", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
            break
        continue

    # Retrieve keypoints and confidence values from detection results
    keypoints_data = pose_results[0].keypoints
    keypoints_all = keypoints_data.xy  # Shape: [n, 17, 2]
    confs_all = keypoints_data.conf   # Shape: [n, 17]

    if keypoints_all is None or confs_all is None:
        break

    # Process each detected person in the frame
    for person_idx in range(len(keypoints_all)):
        person_keypoints = keypoints_all[person_idx]
        person_confs = confs_all[person_idx]
        draw_keypoints_and_skeleton(frame, person_keypoints, person_confs)

    # Display the frame with drawn skeletons
    cv2.imshow("Basketball Pose Analyzer", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
        break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()
