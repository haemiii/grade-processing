import cv2
import numpy as np
import omr_cutter1 as cf


def grader(img):

    gray = img
    thresh = 255-img

    # 윤곽선 찾기
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_idx_list = list(range(len(contours)))
    sorted_contours = [contours[i] for i in sorted(
        contour_idx_list, key=lambda x: cv2.boundingRect(contours[x])[0])]

    boxes = []
    for cnt in sorted_contours:
        area = cv2.contourArea(cnt)
        print(area)
        if 200 > area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            boxes.append((x, y, w, h))

    boxes = sorted(boxes, key=lambda coord: coord[1])
    newBoxes = sorted(boxes, key=lambda coord: coord[0])

    results = []
    for j in range(len(newBoxes)):
        x, y, w, h = newBoxes[j]
        roi = gray[y:y+h, x:x+w]
        total_pixels = roi.shape[0] * roi.shape[1]
        black_pixels = total_pixels - cv2.countNonZero(roi)
        if black_pixels > total_pixels/2:
            results.append(j+1)

    return results
