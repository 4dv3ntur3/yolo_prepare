from cv2 import cv2
import numpy as np
import sys, os, re
from random import uniform


# 기본 이미지 사이즈
w = 1024
h = 768


######################## directory check

img_dir='/home/pej/platform_yolo/NEW_CLASSIFIED/delete/small'
label_dir='/home/pej/platform_yolo/NEW_CLASSIFIED/delete/small_label'

print("디렉토리 생성")
newdir = img_dir + "_magnified/"
os.makedirs(newdir)


def load_images(folder):
    images = []
    image_names = []

    filenames = os.listdir(folder)
    filenames.sort()

    for filename in filenames:
        if ".txt" not in filename:
            img = cv2.imread(os.path.join(folder,filename))

            if img is not None:
                images.append(img)
                image_names.append(filename)

    return images, image_names


def load_labels(folder):
    
    labels = []
    label_names = []

    filenames = os.listdir(folder)
    filenames.sort()

    for filename in filenames:
        if ".jpg" not in filename and "classes" not in filename: # 라벨 파일인 경우

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

            labels.append(bb_array)
            label_names.append(filename)

    return labels, label_names


# print(type(image_folder))

images, image_names = load_images(img_dir)
labels, label_names = load_labels(label_dir)

result_folder = newdir


# for i in range(len(label_names)):
#     img_name = image_names[i]
#     label_name = label_names[i]
#     img_name.replace(".jpg", "")
#     label_name.replace(".txt", "")

#     if(img_name != label_name):
#         print(image_names[i])
#         print(label_names[i])
#         print(i)
#         break

# # print(len(labels))
# # print(len(label_names))

# # labelname = labels[0][0][0]

# print(len(label_names))
# print(len(image_names))




print("파일 로딩 완료")

print("resize 시작: 확대")


bb_count = {}
count = 0
for i in range(len(images)):

    p = uniform(1.0, 1.16)

    image = images[i]

    # 밝기 조절
    # image = image*l

    # 255 넘어가는 것 clipping
    # image = np.clip(image, 0, 255)


    w = image.shape[1]
    h = image.shape[0]

    # resize
    resize = cv2.resize(image, dsize = (0, 0), fx=p, fy=p, interpolation=cv2.INTER_CUBIC)

    # resize된 이미지 크기
    w_new = resize.shape[1]
    h_new = resize.shape[0]

    # 홀수이면
    w_diff = w - w_new
    h_diff = h - h_new


    if w_diff % 2 != 0:
        crop_x_start = int(w_diff / 2)

    else:
        mag_x_start = int(w_diff / 2)
        left = mag_x_start
        right = mag_x_start


    if (h-h_new) % 2 != 0:
        mag_y_start = int(h_diff / 2)
        top = mag_y_start
        bottom = mag_y_start + 1

    else:
        mag_y_start = int(h_diff / 2)
        top = mag_y_start
        bottom = mag_y_start

    # 1024 * 768 crop
    crop_x_start = int((w_new - w) / 2)
    crop_x_end = int(crop_x_start + w)

    crop_y_start = int((h_new - h) / 2)
    crop_y_end = int(crop_y_start + h)
    cropped = resize[crop_y_start:crop_y_end, crop_x_start:crop_x_end] # (y, x)

    # 밝기 조절 

    # cropped = image[115:883, 154:1178]

    # print(resize.shape) # (y, x, channel)

    result = []
    labels_i = labels[i]

    # print(len(labels_i))

    count += 1
    # print(count)

    # print(labels_i)


    for j in range(len(labels[i])):

        # print(i, "번째 사진의 ", j, "번째 라벨")

        w = images[i].shape[1]
        h = images[i].shape[0]

        label_i = labels_i[j][0] # label 

        x = ((float(labels_i[j][1])) * w_new - crop_x_start) / float(w)
        y = ((float(labels_i[j][2])) * h_new - crop_y_start) / float(h)
        w = float(labels_i[j][3]) * p
        h = float(labels_i[j][4]) * p

        label = str(label_i)+' '
        x = str(x)+' '
        y = str(y)+' '
        w = str(w)+' '
        h = str(h)+'\n'

        result.append(label)
        result.append(x)
        result.append(y)
        result.append(w)
        result.append(h)

        if label_i in bb_count:
            bb_count[label_i] += 1

        else: 
            bb_count[label_i] = 1


    with open(result_folder+str(p)+"_"+label_names[i], mode='w') as file:
        file.writelines(result)

    cv2.imwrite(result_folder+str(p)+"_"+image_names[i], cropped)

    if count % 100 == 0:
        print(count)

print("끝")
print(bb_count)
print("배율: ", p)


