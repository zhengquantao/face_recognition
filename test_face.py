# coding:utf-8
'''
本本次封装，我主要是做两张人脸对比。
就只人脸识别部分，简单应用。
# 调用注意事项，因为模型底层是外国人写的。所以路径图片名字千万别使用中文，这样它直接找不到
    好像是OpenCV的问题吧，一直没有解决。中文他会乱码。真的坑。
'''

import dlib
import cv2
# import glob
import time
import numpy as np


class FaceRecognition:

    def __init__(self, predictor_path, face_rec_model_path):
        self.predictor_path = predictor_path
        self.face_rec_model_path = face_rec_model_path
        self.detector = dlib.get_frontal_face_detector()
        self.shape_predictor = dlib.shape_predictor(self.predictor_path)
        self.face_rec_model = dlib.face_recognition_model_v1(self.face_rec_model_path)

    def face_detection(self, url_img):
        s1 = time.time()
        img = cv2.imread(url_img)
        s2 = time.time()
        print(s2-s1, '111111')
        dets = self.detector(img, 1)
        s3 = time.time()
        print(s3-s2, '222222')
        shape = self.shape_predictor(img, dets[0])
        s4 = time.time()
        print(s4-s3, '3333333')
        face_des = self.face_rec_model.compute_face_descriptor(img, shape)
        s5 = time.time()
        print(s5-s4, "44444")
        return face_des

    # 欧式距离
    def dist_o(self, dist_1, dist_2):
        dis = np.sqrt(sum((np.array(dist_1)-np.array(dist_2))**2))
        return dis

    def score(self, url_img_1, url_img_2):
        data1 = self.face_detection(url_img_1)
        data2 = self.face_detection(url_img_2)
        goal = self.dist_o(data1, data2)
        # 判断结果，如果goal小于0.6的话是同一个人，否则不是。我所用的是欧式距离判别
        return goal


predictor_path = "./face_model/shape_predictor_68_face_landmarks.dat"
face_rec_model_path = "./face_model/dlib_face_recognition_resnet_model_v1.dat"


face_ = FaceRecognition(predictor_path, face_rec_model_path)


img_1 = './faces/1.jpg'
img_2 = './faces/2.png'  # 000183_02159543
m = time.time()
goal = face_.score(img_1, img_2)
print(goal, time.time()-m, '---dddddddd---')
