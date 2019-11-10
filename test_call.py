import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./face_model/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1("./face_model/dlib_face_recognition_resnet_model_v1.dat")

cap = cv2.VideoCapture(0)  # 调整参数实现读取视频或调用摄像头
cap.set(propId=3, value=320)     #设置你想捕获的视频的宽度
cap.set(propId=4, value=240)
# win = dlib.image_window()

while 1:
    ret, frame = cap.read()
    cv2.imshow("CN", frame)

    get_num = detector(frame, 1)
    # shape = predictor(frame, get_num[0])
    # face_des = facerec.compute_face_descriptor(frame, shape)

    if len(get_num) > 0:
        # win.clear_overlay()
        # win.set_image(frame)
        # win.add_overlay(get_num)
        print(get_num.__len__())



    on = cv2.waitKey(1)
    if on == ord('q'):
        break
    elif on == ord('s'):
        cv2.imwrite('test.jpg', frame)

cap.release()
cv2.destroyAllWindows()
dlib.hit_enter_to_continue()