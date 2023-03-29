import cv2
import json

import omr_cutter2 as ct
import omr_grader as gr


def reader(img):
    img = ct.cutter2(cv2.imread(img))
    result = [gr.grader(img[i]) for i in range(len(img))]
    answers = {i+1: str(result[i]) for i in range(len(result))}

    answer_json = json.dumps(answers)

    return answer_json


img = "test/picture/cut_image_3.png"
ans = reader(img)
print(ans)

# {"1": "3", "2": "3", "3": "3", "4": "2", "5": "2"}
