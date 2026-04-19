import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'images'
images = []
classNames = []

# ── Load images ──────────────────────────────────────────────────────────────
if not os.path.exists(path):
    print(f"Error: '{path}' directory not found!")
    exit()

for cl in os.listdir(path):
    img_path = f'{path}/{cl}'
    img = cv2.imread(img_path)
    if img is None:
        print(f"Warning: Could not load image {cl}")
        continue
    images.append(img)
    classNames.append(os.path.splitext(cl)[0])

if len(images) == 0:
    print("Error: No images found in 'images' directory!")
    exit()

print(f"Loaded {len(images)} images: {classNames}")


# ── Encode known faces ───────────────────────────────────────────────────────
def findEncodings(images):
    encodeList = []
    for i, img in enumerate(images):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(img)
        if len(face_encodings) == 0:
            print(f"Warning: No face found in image {classNames[i]}")
            continue
        encodeList.append(face_encodings[0])
    if len(encodeList) == 0:
        print("Error: No face encodings created!")
        exit()
    return encodeList


# ── Mark attendance (only once per person per day) ───────────────────────────
def markAttendance(name):
    # Create CSV with header if it doesn't exist
    if not os.path.exists('attendance.csv'):
        with open('attendance.csv', 'w') as f:
            f.write('Name,Date,Time\n')

    # Read existing records
    with open('attendance.csv', 'r') as f:
        data = f.readlines()

    today = datetime.now().strftime('%Y-%m-%d')

    # Check if this person is already marked TODAY
    already_marked = False
    for line in data:
        parts = line.strip().split(',')
        if len(parts) >= 2 and parts[0] == name and parts[1] == today:
            already_marked = True
            break

    # Only write if not already marked today
    if not already_marked:
        now = datetime.now()
        time_str = now.strftime('%H:%M:%S')
        with open('attendance.csv', 'a') as f:
            f.write(f'{name},{today},{time_str}\n')
        print(f"✅ Attendance marked — {name} at {time_str}")
        return True   # newly marked
    return False      # already marked


# ── Setup ────────────────────────────────────────────────────────────────────
encodeListKnown = findEncodings(images)
print("✅ Encoding complete. Starting camera...\n")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera!")
    exit()

# Track who has been marked in this session (to avoid spamming the CSV)
markedThisSession = set()

try:
    while True:
        success, img = cap.read()
        if not success:
            print("Error: Failed to capture frame")
            break

        # Shrink frame for faster processing
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame  = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches  = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis  = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()

                # Scale face box back to full size
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

                # Mark attendance if not already done this session
                if name not in markedThisSession:
                    newly_marked = markAttendance(name)
                    if newly_marked:
                        markedThisSession.add(name)

                # Choose box colour: green = just marked, blue = already done
                color = (0, 255, 0) if name in markedThisSession else (255, 150, 0)

                # Draw box and label
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                cv2.rectangle(img, (x1, y2), (x2, y2 + 40), color, cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 + 28),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

                # Show "MARKED" badge on top of box
                status_text = "MARKED" if name in markedThisSession else "PRESENT"
                cv2.putText(img, status_text, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

            else:
                # Unknown face — draw red box
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(img, "UNKNOWN", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        # Show count of marked students
        cv2.putText(img, f"Marked: {len(markedThisSession)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(img, "Press ESC to exit", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

        cv2.imshow('Attendance System', img)

        if cv2.waitKey(1) == 27:   # ESC key to quit
            break

except KeyboardInterrupt:
    print("\nStopped by user.")

finally:
    cap.release()
    cv2.destroyAllWindows()
    print(f"\n✅ Done! Attendance saved to attendance.csv")
    print(f"   Marked this session: {', '.join(markedThisSession) if markedThisSession else 'Nobody'}")
