import cv2
import numpy as np

# 가로로 자르는 함수
def cutter2(img):

    img_trim = img

# 높이를 문항 개수로 나누고 잘라 배열에 저장
    size, _ = img_trim.shape
    size = size // 20
    result = [img_trim[i:i+size]
              for i in range(0, len(img_trim)-size % 20, size)]

    return result