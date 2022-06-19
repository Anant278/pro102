import cv2
import dropbox
import time
import random

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        global start_time
        start_time = time.time()
        result = False
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return img_name

take_snapshot()

def upload_file(img_name):
    access_token = "sl.BJ2uv5DHCJHDgj6JLAdt6gM8CcNXb144I3efsf8CArAPxU4ReAgtZwtw3-Zl7l51rh_4vPKmqn-TL1_IedhJl2_JxnkKAkUBJ_4aOvO8GunCaT0r698cYQ1G2C1WWmIr5yR-vRc"
    file = img_counter
    file_from = file
    file_to = "/Whitehall_pro-102"(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("files uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 300):
            name = take_snapshot()
            upload_file(name)
main()