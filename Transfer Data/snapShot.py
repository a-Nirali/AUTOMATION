import cv2
import time
import random
import dropbox
start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    #initallizing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    #creating while loop to capture images every 5 min.
    while(result):
        ret,frame=videoCaptureObject.read()    
        #cv2 imwrite() is used to store image
        img_name="img"+ str(number)+".png"
        cv2.imwrite(img_name,frame)
        result=False

    return img_name
    print("snapShot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "yCUIiWPf-00AAAAAAAAAATLOGQHHxg-EQwSB2w7JSVkaoochwPVznS-WbnYfgyjH"
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()
           
         