# -*- coding: utf-8 -*-
"""Openpose_datacollector.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iFk-Ugf1MNzu9HPlZFCh8IvADtKyTZtq
"""

!pip install opencv-python
import cv2

from google.colab import drive
drive.mount('/content/drive/')

BODY_PARTS = {0: "Nose", 1: "Neck", 2: "RShoulder", 3: "RElbow", 4: "RWrist",
                      5: "LShoulder", 6: "LElbow", 7: "LWrist", 8: "MidHip", 9: "RHip",
                      10: "RKnee", 11: "RAnkle", 12: "LHip", 13: "LKnee", 14: "LAnkle",
                      15: "REye", 16: "LEye", 17: "REar", 18: "LEar", 19: "LBigToe",
                      20: "LSmallToe", 21: "LHeel", 22: "RBigToe", 23: "RSmallToe", 24: "RHeel", 25: "Background"}

POSE_PAIRS = [[0, 1], [0, 15], [0, 16], [1, 2], [1, 5], [1, 8], [8, 9], [8, 12], [9, 10], [12, 13], [2, 3],
                      [3, 4], [5, 6], [6, 7], [10, 11], [13, 14], [15, 17], [16, 18], [14, 21], [19, 21], [20, 21],
                      [11, 24], [22, 24], [23, 24]]  


protoFile="/content/drive/MyDrive/openpose/pose_deploy.prototxt"
weightsFile="/content/drive/MyDrive/openpose/pose_iter_584000.caffemodel"

import os

path_dir="/content/drive/MyDrive/openpose/"
file_list=os.listdir(path_dir)
print(file_list)

import re

def solution(files):
    #길이 먼저 비교, 그 다음에 숫자(한자릿수, 두자릿수)
    arr=sorted(files,key=lambda x: (len(x),re.findall(r'\d+', x)))

    return arr
    # arr = [re.split("(\d+)", file) for file in file_list]
    # return ["".join(a) for a in sorted(arr, key=lambda x: (x[0].lower(), int(x[1])))]

jpg_img=[]
for tmp_file in file_list:
    if '.jpg' in tmp_file:
        img_name=path_dir+tmp_file
        jpg_img.append(img_name)
sorted_jpg_img=solution(jpg_img)

print(sorted_jpg_img)

def show_image(im, height=16, width=20):
    """
    Function to display an image
    
    Args:
        im ([numpy.ndarray])
        height ([int] or None)
        width ([int] or None)
    """
    plt.figure(figsize=(16,20))
    plt.imshow(im)
    plt.axis("off")
    plt.show()

from matplotlib import pyplot as plt
from IPython.display import Image
import numpy as np

net=cv2.dnn.readNetFromCaffe(protoFile,weightsFile)
all_points=[]
empty_img=np.zeros((100,100,3),np.uint8)
plt.figure(figsize=(5,5))

for img_name in sorted_jpg_img:
    image=cv2.imread(img_name)
    imageHeight,imageWidth,_=image.shape
    inpBlob=cv2.dnn.blobFromImage(image,1.0/255,(imageWidth,imageHeight),(0, 0, 0), swapRB=False, crop=False)

    # network에 넣어주기
    net.setInput(inpBlob)
    # 결과 받아오기
    output = net.forward()
    
    # output.shape[0] = 이미지 ID, [1] = 출력 맵의 높이, [2] = 너비
    H = output.shape[2]
    W = output.shape[3]
    print("이미지 ID : ", len(output[0]), ", H : ", output.shape[2], ", W : ",output.shape[3]) # 이미지 ID
    # 키포인트 검출시 이미지에 그려줌
    points = []
    for i in range(0,25):
        # 해당 신체부위 신뢰도 얻음.
        probMap = output[0, i, :, :]
    
        # global 최대값 찾기
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

        # 원래 이미지에 맞게 점 위치 변경
        x = (imageWidth * point[0]) / W
        y = (imageHeight * point[1]) / H

        # 키포인트 검출한 결과가 0.1보다 크면(검출한곳이 위 BODY_PARTS랑 맞는 부위면) points에 추가, 검출했는데 부위가 없으면 None으로    
        if prob > 0.1 :    
            cv2.circle(image, (int(x), int(y)), 3, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)       # circle(그릴곳, 원의 중심, 반지름, 색)
            cv2.putText(image, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, lineType=cv2.LINE_AA)
            points.append((int(x), int(y)))
        else :
            points.append(None)

    a,b=points[8]
    calib_points=[]
    for i in range(0,25):
        if points[i]:
            tmp_a,tmp_b=points[i]
            calib_points.append([tmp_a-a,tmp_b-b])
        else:
            calib_points.append([0,0])
    calib_points=np.array(calib_points)
    X=calib_points
    re_points = (X - X.min()) / (X.max() - X.min())
    re_points=re_points.round(2)
    re_points=(re_points*100).astype(np.uint8)

    # for pair in POSE_PAIRS:
    #     partA = pair[0]             # Head
    #     partB = pair[1]             # Neck

    #     if re_points[partA].all() and re_points[partB].all(): #frame1 - green
    #         cv2.line(empty_img, tuple(re_points[partA]), tuple(re_points[partB]), (0, 255, 0), 2)

    all_points.append(re_points)
    # show_image(empty_img,"Output-Keypoints")

!pip install openpyxl
import pandas as pd

df=pd.DataFrame.from_records(all_points)
df.head()

df.to_excel('/content/drive/MyDrive/openpose/openpose_test.xlsx')