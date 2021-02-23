import cv2
import os, sys, re
import numpy as np

orig_dir='/home/pej/Desktop/test_1000/images/test'

size_dict = {}
def load_images(folder):

    images = []
    image_names = []

    filenames = os.listdir(folder)
    filenames.sort()

    for filename in filenames:
         if ".txt" not in filename:
            img = cv2.imread(os.path.join(folder, filename))

            if img is not None:
                # images.append(img)
                # image_names.append(filename)

                if img.shape[1] in size_dict:
                    size_dict[img.shape[1]] += 1

                else:
                    size_dict[img.shape[1]] = 1
    return size_dict

print(load_images(orig_dir))


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
