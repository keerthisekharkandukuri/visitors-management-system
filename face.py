import cv2
import face_recognition
import os
import numpy as np
import sys
# get list of files in directory
directory = "images"
files = os.listdir(directory)
num_files = len(files)
image_path = sys.argv[1]
image = cv2.imread(directory+'\\'+image_path) 
known_encodings = []   
face_locations = face_recognition.face_locations(image)
encoding = face_recognition.face_encodings(image, face_locations)
known_encodings.append(encoding)

tolerance =0.5

video_capture = cv2.VideoCapture("test.mp4")
flag=0
while True:
   
    ret, frame = video_capture.read()
  
    if(flag==1):
       break
    elif(flag==2):
       break
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        if np.any(face_distances <= tolerance):
          best_match_index = np.argmin(face_distances)
          print("face matched")
          flag=1
        else:
          print("not matched")
          flag=2
           
  
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

 
    cv2.imshow("Video", frame)

   
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video_capture.release()
cv2.destroyAllWindows()
