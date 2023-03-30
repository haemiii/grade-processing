import cv2
import json

import omr_cutter1 as ct1
import omr_cutter2 as ct
import omr_grader as gr


def reader(img):
    # 세로 자르기 사진
    img = ct1.cutter1(cv2.imread(img))
    # 가로 자르기 사진
    img = [ct.cutter2(img[i]) for i in range(len(img))]
    img = sum(img, [])
    result = [gr.grader(img[i]) for i in range(len(img))]
    answers = {i+1: str(result[i]) for i in range(len(result))}
    answer_json = json.dumps(answers)
    return answer_json

img = "./grade-processing/imageProcessing/test/images/mini55.png"
ans = reader(img)
print(ans)