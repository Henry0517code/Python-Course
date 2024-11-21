import cv2
from deepface import DeepFace

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame reading was successful
    if ret:
        # Try to analyze the face using DeepFace
        try:
            # Perform analysis for emotion, age, gender, and race
            actions=['age']
            result = DeepFace.analyze(frame, actions=actions, enforce_detection=False)

            # Get the analysis results
            age = result[0]['age']
            # emotion = result[0]['dominant_emotion']
            # gender = result[0]['gender']
            # race = result[0]['dominant_race']

            # Display the analysis results on the frame
            cv2.putText(frame, f"Age: {age}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            # cv2.putText(frame, f"Emotion: {emotion}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            # cv2.putText(frame, f"Gender: {gender}", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            # cv2.putText(frame, f"Race: {race}", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        except Exception as e:
            print(f"Error analyzing face: {e}")

        # Display the frame with analysis results
        cv2.imshow('Emotion Recognition', frame)

        # Check if 'q' is pressed or the window is closed
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Emotion Recognition', cv2.WND_PROP_VISIBLE) < 1:
            break
    else:
        print("Error: Unable to capture frame.")
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()