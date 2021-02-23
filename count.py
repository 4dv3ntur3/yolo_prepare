import cv2
import os, sys, re
import numpy as np

root='/home/pej/Desktop/alcohol_1407/'
orig_dir='/home/pej/Desktop/alcohol_1407/obj'
label_dir='/home/pej/Desktop/alcohol_1407/obj_label'

print("디렉토리 생성")
newdir = root + "compressed_1/"
os.makedirs(newdir)

def load_images(folder):
    images = []
    image_names = []

    filenames = os.listdir(folder)
    filenames.sort()

    for filename in filenames:
         if ".txt" not in filename:
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
                image_names.append(filename)

            print(filename)

    return images, image_names


def load_labels(folder):
    labels = []
    label_names = []

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

            labels.append(bb_array)
            label_names.append(filename)

    return labels, label_names

images, image_names = load_images(orig_dir)
labels, label_names = load_labels(label_dir)

result_folder = newdir


'''
for i in range(len(images)):
    image = images[i]


    result = []
    labels_i = labels[i]

    for j in range(len(labels[i])):

        # print(i, "번째 사진의 ", j, "번째 라벨")

        label_i = labels_i[j][0]  # label

        x = float(labels_i[j][1])
        y = float(labels_i[j][2])
        w = float(labels_i[j][3])
        h = float(labels_i[j][4])

        label = str(label_i) + ' '
        x = str(x) + ' '
        y = str(y) + ' '
        w = str(w) + ' '
        h = str(h) + '\n'

        result.append(label)
        result.append(x)
        result.append(y)
        result.append(w)
        result.append(h)

        # if label_i in bb_count:
        #     bb_count[label_i] += 1
        #
        # else:
        #     bb_count[label_i] = 1

    with open(result_folder + "_c_1_" + label_names[i], mode='w') as file:
        file.writelines(result)

    print(i)
    print(image_names[i])
    cv2.imwrite(result_folder + "_c_1_" + image_names[i], image)





#
#
# img1 = cv2.imread('./home/pej/Desktop/alcohol_1407/comp_1/.jpg')
#
# # cv2.imwrite('./new1.jpg', img1)
# #
# # img2 = cv2.imread('./new1.jpg')
#
# img2 = cv2.imread('./home/pej/')
#
#
# diff = img1 - img2
# diff2 = diff * diff
# print(diff2.sum())
#
#
# cv2.imshow("img0", img0)
# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
# cv2.waitKey(0)
'''
