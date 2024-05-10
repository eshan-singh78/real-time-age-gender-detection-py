import cv2
from deepface import DeepFace

def detect_gender_age(image):
    faces = DeepFace.extract_faces(image, detector_backend='opencv')

    if len(faces) == 0:
        return None, None

    face = faces[0]

    result = DeepFace.analyze(image, actions=['gender', 'age'])

    if isinstance(result, list):
        result = result[0]

    gender = result['gender']
    age = int(result['age'])

    return gender, age

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame")
            break

        cv2.imshow('frame', frame)

        gender, age = detect_gender_age(frame)

        if gender is not None and age is not None:
            print("Gender:", gender)
            print("Age:", age)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
