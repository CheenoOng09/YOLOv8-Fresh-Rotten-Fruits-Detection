import ultralytics
from ultralytics import YOLO

classids = ['fresh_potato']
# classids = ['fresh_bittergourd', 'fresh_capsicum','rotten_carrot', 'rotten_cucumber', 'rotten_okra', 'rotten_potato', 'rotten_tomato']
#'fresh_potato', 'rotten_bellpepper', 'rotten_bittergourd', 'rotten_capsicum',
for id in classids:
    model_path = './train_results/' + id + '_run/weights/best.pt'
    model = YOLO(model_path)
    data_path = './trainfolder/' + id + '/train/images'
    predicts = id + '_test'
    results = model.predict(source=data_path, classes=[25], save=True, save_txt=True, show_boxes=True, project='./predict_results', name=predicts)

# metrics = model.val(data='./trainfolder/rotten_capsicum/data.yaml', save_json=True, plots=True)
# print(metrics)