import ultralytics
from ultralytics import YOLO

import os
cwd = os.getcwd()
print(cwd)

classids = ['0_bellpepper_fresh', '1_bellpepper_rotten', '2_bitterground_fresh', '3_bitterground_rotten', '4_capsicum_fresh',
            '5_capsicum_rotten', '6_carrot_fresh', '7_carrot_rotten', '8_cucumber_fresh', '9_cucumber_rotten', '10_okra_fresh',
            '11_okra_rotten', '12_potato_fresh', '13_potato_rotten']
classids_all = 'total_img'


#for id in classids:
#    path = "/home/naeem/Documents/grocery/trainfolder/" + id + "/data.yaml"
#    runs = id + '_run'
#    model = YOLO("yolov8m.pt")
#    results = model.train(data=path, epochs=150, patience=200,
#                      project='/home/naeem/Documents/grocery/', name=runs, verbose=True)
#    print(path, runs)


path = "/home/naeem/Documents/grocery/traintestvalid/" + classids_all + "/data.yaml"
runs = classids_all + '_run'
model = YOLO("yolov8m.pt")
results = model.train(data=path, epochs=150, patience=200,
                      project='/home/naeem/Documents/grocery/reresult', name=runs, verbose=True)
print(path, runs)