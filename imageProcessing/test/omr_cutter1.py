import cv2
import numpy as np


def cutter1(img):

    # 사진 가공
    h, w, _ = img.shape
    img = cv2.resize(img, (w//2, h//2))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 5)
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_xy = np.array(contours)

    # x의 min과 max 찾기
    x_min, x_max = 0, 0
    value = list()
    for i in range(len(contours_xy)):
        for j in range(len(contours_xy[i])):
            # numpy 배열이 4차원 배열 행태라 x 값만 추출하기 위함
            value.append(contours_xy[i][j][0][0])
            x_min = min(value)
            x_max = max(value)

    # y의 min과 max 찾기
    y_min, y_max = 0, 0
    value = list()
    for i in range(len(contours_xy)):
        for j in range(len(contours_xy[i])):
            value.append(contours_xy[i][j][0][1])  # y 값만 추출하기 위함
            y_min = min(value)
            y_max = max(value)

    # x 최소, y 최소, 높이, 너비 구해서 자름 여백 없애는곳
    x = x_min
    y = y_min
    w = x_max-x_min
    h = y_max-y_min
    img_trim = thresh[y:y+h, x:x+w]
    
    # 잘린 이미지 저장
    num_cols = 4  # 행의 갯수
    _, size = img_trim.shape
    size = size // num_cols
    result = [255-img_trim[:, i:i+size]
              for i in range(0, len(img_trim[0])-size%num_cols, size)]
    for i in range(num_cols):
        cv2.imwrite(f'test/picture/cut_image_{i}.png', result[i])
    cv2.imwrite("test/picture/result.png", 255-img_trim)

    return result