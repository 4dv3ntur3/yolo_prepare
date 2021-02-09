########################## labeling number 바꿔야 할 때

import sys, os, re

# 개수를 셀 라벨 파일들이 있는 폴더
total_dir='/home/pej/Desktop/only_soju'

print("디렉토리 생성")
newdir = total_dir + "_label_replaced/"
os.makedirs(newdir)


def replace_label(folder):
    labels = []
    label_names = []

    bb_count = {}

    filenames = os.listdir(folder)
    filenames.sort()

    for filename in filenames:
        if ".jpg" not in filename and "classes" not in filename:  # 라벨 파일인 경우

            # Obtain BB values from YOLOv3 annotation .txt file
            gt = open(os.path.join(folder, filename), 'r')

            bb_array = []
            for line in gt:
                # print(line)
                vals = re.split('\s+', line.rstrip())

                if len(vals) == 5:
                    bb_array.append(vals)
                    # print(vals)

                if vals[0] in bb_count:
                    bb_count[vals[0]] += 1

                else:
                    bb_count[vals[0]] = 1

            labels.append(bb_array)
            label_names.append(filename)

    # bb_sorted = sorted(bb_count.items()) # reverse=True 넣어 주면 내림차순으로 정렬
    # return bb_sorted
    return labels, label_names

labels, label_names = replace_label(total_dir)

print(labels[0])
print("\n"+label_names[0])

for i in range(len(label_names)):
    result = []
    labels_i = labels[i]
    for j in range(len(labels_i)):

        label_before = labels_i[j][0]

        if label_before == '9':
            label_new = '0'
        elif label_before == '10':
            label_new = '1'
        elif label_before == '11':
            label_new = '2'
        else:
            label_new = label_before

        x = float(labels_i[j][1])
        y = float(labels_i[j][2])
        w = float(labels_i[j][3])
        h = float(labels_i[j][4])

        label = str(label_new) + ' '
        x = str(x) + ' '
        y = str(y) + ' '
        w = str(w) + ' '
        h = str(h) + '\n'

        result.append(label)
        result.append(x)
        result.append(y)
        result.append(w)
        result.append(h)

    with open(newdir+label_names[i], mode='w') as file:
        file.writelines(result)

print("끝")
