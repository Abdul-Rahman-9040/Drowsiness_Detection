import cv2
import dlib
import numpy as np

# Load the pre-trained dlib facial landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(dlib.data.shape_predictor("shape_predictor_68_face_landmarks.dat"))

def calculate_ear(eye_points):
    # Calculate the Euclidean distances between the vertical eye landmarks
    A = np.linalg.norm(eye_points[1] - eye_points[5])
    B = np.linalg.norm(eye_points[2] - eye_points[4])
    # Calculate the Euclidean distance between the horizontal eye landmarks
    C = np.linalg.norm(eye_points[0] - eye_points[3])
    # Compute the EAR
    ear = (A + B) / (2.0 * C)
    return ear

def detect_drowsiness(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = detector(gray)
    
    for face in faces:
        landmarks = predictor(gray, face)
        landmarks = np.array([[p.x, p.y] for p in landmarks.parts()])

        # Eye landmarks for the left and right eyes
        left_eye = landmarks[36:42]
        right_eye = landmarks[42:48]

        # Calculate EAR for both eyes
        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)

        # Average EAR
        ear = (left_ear + right_ear) / 2.0

        # Drowsiness threshold
        if ear < 0.25:
            cv2.putText(frame, "Drowsiness detected!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "Alert", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the image
    cv2.imshow("Drowsiness Detection", frame)

def main():
    # Initialize webcam capture
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Detect drowsiness in the current frame
        detect_drowsiness(frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
