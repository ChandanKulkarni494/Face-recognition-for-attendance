import cv2
import sqlite3
# Import numpy for matrices calculations
import numpy as np
import database

DB_NAME="Facerecc.db"
i = 0
n = "null"
u = "null"
# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX


def getProfile(Id):
    conn = sqlite3.connect(DB_NAME)
    cmd = "SELECT * FROM RegisteredUsers WHERE ID=" + str(Id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    cursor.close()
    conn.close()
    return profile


def insertOrUpdate(face_id, face_name):
    print("ID = "+face_id)
    print("Name = "+face_name)
    conn = sqlite3.connect(DB_NAME)
    cmd = "SELECT * FROM Attendance WHERE ID=" + str(face_id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if (isRecordExist == 1):
        cmd = "UPDATE Attendance SET Name = " + face_name + "WHERE ID=" + face_id
    else:
        cmd = "INSERT INTO Attendance VALUES('" + str(face_id) + "','" + face_name + "','Present')"

    conn.execute(cmd)

    conn.commit()
    cursor.close()
    # cam.release();
    conn.close()


# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

# Loop
while True:
    # Read the video frame
    ret, im = cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    # For each face in faces
    for (x, y, w, h) in faces:

        # Recognize the face belongs to which ID
        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])

        # Create rectangle around the face
        cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)
        if conf < 70:
            profile = getProfile(Id)

            if (profile != None):
                # Put text describe who is in the picture
                cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
                cv2.putText(im, str(profile[1]), (x, y - 40), font, 2, (255, 255, 255), 3)
                i = profile[0]
                n = str(profile[1])
                u = str(profile[2])
        else:
            cv2.putText(im, "Unknown", (x, y - 40), font, 2, (255, 255, 255), 3)
    # Display the video frame with the bounded rectangle
    cv2.imshow('Recognizer', im)

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()
# Close all windows
cv2.destroyAllWindows()
print("ID = "+str(i))
day1=str(database.names[3]);
day2=str(database.names[4]);
day3=str(database.names[5]);
day4=str(database.names[6]);
day5=str(database.names[7]);
if (i == 0):
    td = input('Enter total number of Days passed to update absentees: ')
    #DB_NAME = 'facerecc.db'
    conn = sqlite3.connect(DB_NAME)
    conn.execute("INSERT INTO AttendanceRegister(ID,NAME,USN) SELECT ID,NAME,USN FROM RegisteredUsers EXCEPT SELECT ID,NAME,USN FROM AttendanceRegister;")
    print("Database Updated Successfully !")
    conn.execute("UPDATE AttendanceRegister SET totalclasses=0,totaldays=0 WHERE totaldays IS NULL;");
    conn.commit()
    cursor = conn.execute("Select totalDays from AttendanceRegister");
    match = cursor.fetchall()

    cursor.close()
    if (td == '1'):
        for record in match:
            #print(match)
            if record == (0,):
                conn.execute("update  AttendanceRegister set"+"\""+day1+"\""+"=0 ,totalDays=1 WHERE totalDays =0 ");
                conn.commit();
                print("Attendance Updated Successfully !")

    if (td == '2'):
        for record in match:
            #print(match)
            if record == (1,):
                conn.execute("UPDATE AttendanceRegister SET "+"\""+day2+"\""+"=0, totalDays=2 WHERE totalDays =1 ");
                conn.commit();
                print("Attendance Updated Successfully !");

    if (td == '3'):
        for record in match:
            if record == (2,):
                conn.execute("update  AttendanceRegister set "+"\""+day3+"\""+"=0,totalDays=3 WHERE totalDays =2 ");
                conn.commit();
                print("Attendance Updated Successfully !")

    if (td == '4'):
        for record in match:
            if record == (3,):
                conn.execute("update  AttendanceRegister set "+"\""+day4+"\""+"=0,totalDays=4 WHERE totalDays =3 ");
                print("Attendance Updated Successfully !")
                conn.commit()
    if (td == '5'):
        for record in match:
            if record == (4,):
                conn.execute("update  AttendanceRegister set "+"\""+day5+"\""+"=0,totalDays=5 WHERE totalDays =4 ");
                print("Attendance Updated Successfully !")
                conn.commit()

else:
    database.update_attendance(i, u, n, True)

