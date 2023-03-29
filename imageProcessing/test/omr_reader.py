import cv2
import json

import omr_cutter_vertical as ct
import omr_grader as gr
import omr_cutter_horizon as ch

def reader(img):
    img = ct.cutter1(cv2.imread(img))
    img = ch.cutter2(img)
    result = [gr.grader(img[i]) for i in range(len(img))]
    answers = { i+1 : str(result[i]) for i in range(len(result))}

    answer_json = json.dumps(answers)
    
    return answer_json

img = "./grade-processing/imageProcessing/test/images/minijjang.png"
ans = reader(img)
print(ans)

# {"1": "3", "2": "3", "3": "3", "4": "2", "5": "2"}