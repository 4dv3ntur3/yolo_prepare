import sys, os, re

gt_dir='/home/pej/Desktop/test_1000/labels/test/'
answer_dir = '/home/pej/platform_yolo/yolov5/runs/detect/exp/labels'

def load_bbox(folder):

    labels = []
    label_names = []
    bbox = []

    filenames = os.listdir(folder)
    filenames.sort()

    for filename in filenames:
        if ".jpg" not in filename and "test_data" not in filename:
            bb_true = {}

            gt = open(os.path.join(folder, filename), 'r')

            bb_array = []
            for line in gt:
                # print(line)
                vals = re.split('\s+', line.rstrip())

                if len(vals) == 5:
                    bb_array.append(vals)
                    # print(vals)

                if vals[0] in bb_true:
                    bb_true[vals[0]] += 1

                else:
                    bb_true[vals[0]] = 1

            labels.append(bb_array)
            label_names.append(filename)
            bbox.append(bb_true)

    return bbox, labels, label_names


gt_box, gt_labels, gt_label_names = load_bbox(gt_dir)
as_box, as_labels, as_label_names = load_bbox(answer_dir)


count = 0
for i in range(len(gt_box)):

    gt = gt_box[i]
    pred = as_box[i]

    gt_keys = len(gt.keys())
    pred_keys = len(pred.keys())

    if gt_keys != pred_keys:
        print(gt, pred)
        count += 1
        continue

    for k, v in gt.items():
        if pred[k] != v:
            count += 1
            print(gt, pred)
            print(gt_label_names[i])
            continue

total = len(gt_box)
error = count

print("total: ", len(gt_box), " error: ", error, " accuracy: ", 1 - (error/total))


