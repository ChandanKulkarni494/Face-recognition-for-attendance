# Face-recognition-for-attendance
Face detection and recognition for attendance systems
## DESCRIPTION

This project is about the Face Detection and Face Recognition using OpenCV libraries and inbuilt haarcascade classifier to recognize the face of a student and marks his/her attendance in the database.

## Prerequisites
The following are the prerequisites for this project
1. Python 3.7
2. OpenCV, NumPy, PIL libraries in python
3. SQLite studio
4. PyCharm IDE [Optional]

## Installation

1. Install Python 3.7 and the above mentioned libraries
2. Install latest release of SQLite studio
3. Go to installed CV2 folder in Python library and copy the "haarcascade_frontalface_default.xml" file to your current working directory where the code is present. (ex: Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_default )

## Steps to run

1. Open SQLite studio and create a new database in the working directory of your code.
2. Replace DB_NAME in the code of all 4 files with the name of the database you have created (Ex: DB_NAME = "YourDBName.db").
3. With the webcam connected to your PC/Laptop, run the datasetGenerator.py file. Enter ID, Name and USN of student and hit enter. This will start capturing the face for about 50 frames.
4. Run trainner.py , which is used to train the classifier with the captured images. This will create trainer.yml in a folder named "trainer".
5. Then run the faceRecognizerGenerator.py file. The detected face will be marked with a green rectangle along with the name if the face is recognized. Upon successful recognition, press 'Q' to mark attendance.
NOTE: At the end of the day run the blank camera(with no faces present) and press 'Q' to count number of days present and mark absentees.
6. Check the database entries in the SQLite studio to confirm successful run. There should be two tables created in your database namely "RegisteredUsers" which contains data of all registered users during the capturing phase(step 3) and "AttendanceRegister" which contains attendance data of the students over the duration of five days starting from the date you ran the code.

## Troubleshooting

1. Makes sure all the code files, haarcascade_frontalface_default.xml, database file are in the same directory.
2. Install the required libraries before running the code : NumPy, OpenCV (CV2), Python Imaging Library ( PIL or Pillow ).
2. Change DB_NAME in the files according to your database name.
3. Make sure your webcam drivers are working properly.
4. The room should be adequately lit as the lighting condition is a drawback.


#### This is ideal for students looking for a final year project. Feel free to comment if you have any queries.
