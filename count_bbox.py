######################## 라벨 클래스별로 바운딩 박스 개수 계산 (즉 이미지에 들어 있는 클래스별 물체의 수)

import sys, os, re



# 개수를 셀 라벨 파일들이 있는 폴더
total_dir='/home/pej/Desktop/code_test'


def count_bbox(folder):
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
                # print(vals)

                # imgaug_vals = convertYolov3BBToImgaugBB(vals)
                # # print (imgaug_vals)

                # bb_array.append(ia.BoundingBox(x1 = imgaug_vals[1],
                #                             y1 = imgaug_vals[2],
                #                             x2 = imgaug_vals[3],
                #                             y2 = imgaug_vals[4],
                #                             label = imgaug_vals[0]))
                if len(vals) == 5:
                    bb_array.append(vals)
                    # print(vals)

                if vals[0] in bb_count:
                    bb_count[vals[0]] += 1

                else:
                    bb_count[vals[0]] = 1

            # labels.append(bb_array)
            # label_names.append(filename)

    bb_sorted = sorted(bb_count.items()) # reverse=True 넣어 주면 내림차순으로 정렬
    return bb_sorted


print(count_bbox(total_dir))