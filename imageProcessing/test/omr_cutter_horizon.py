import cv2
import numpy as np

# 가로로 자르는 함수
def cutter2(img):    

    img_trim = cv2.imread("./grade-processing/imageProcessing/test/picture/cut_image_0.png")
    img_trim = cv2.cvtColor(img_trim, cv2.COLOR_BGR2GRAY)
    print(img_trim.shape)

# 높이를 문항 개수로 나누고 잘라 배열에 저장
    size, _ = img_trim.shape
    size = size // 20
    result = [255-img_trim[i:i+size] for i in range(0, len(img_trim)-size%5, size)]
    for i in range(20):
        cv2.imwrite(f'./grade-processing/imageProcessing/test/picture2/cut_image_{i}.png', result[i])
    cv2.imwrite("./grade-processing/imageProcessing/test/picture2/result.png", 255-img_trim)
    cv2.imshow('image', img_trim)
    cv2.waitKey(0)

    return result

# cutter2(0)