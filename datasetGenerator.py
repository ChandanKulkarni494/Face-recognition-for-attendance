import cv2
import sqlite3
DB_NAME="Facerecc.db"
# Start capturing video
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Register the users into database
def insertOrUpdate(face_id, face_name, face_usn):
    conn = sqlite3.connect(DB_NAME)
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS RegisteredUsers ( ID INTEGER, NAME VARCHAR, USN INTEGER);")
    c.execute("SELECT * FROM RegisteredUsers WHERE ID=?",[face_id])
    isRecordExist = 0
    for row in c:
        isRecordExist = 1
    if (isRecordExist == 1):
        c.execute("UPDATE RegisteredUsers SET Name=?,USN=? WHERE ID=?",(face_name,face_usn,face_id))
    else:
        c.execute("INSERT INTO RegisteredUsers VALUES(?,?,?)",(face_id,face_name,face_usn))
        #c.execute(cmd)
    conn.commit()
    conn.close()
    # For each person, one face id


face_id = input("Enter your ID: ")
face_name = input("Enter your name: ")
face_usn = input("Enter your USN: ")

insertOrUpdate(face_id, face_name, face_usn)

# Initialize sample face image
count = 0

# Start looping
while (True):

    # Capture video frame
    ret, image_frame = vid_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Loops for each faces
    for (x, y, w, h) in faces:
        # Increment sample face image
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)
        cv2.waitKey(100)

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # If image taken reach 100, stop taking video
    elif count > 50:
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()