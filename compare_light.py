import cv2
import numpy as np
import sys, os, re
from random import uniform

# 픽셀값들의 평균 비교
#
# img = np.fromfile("/home/pej/Desktop/center/result_0.bin", dtype=np.uint8)
#
# img_sum = img.sum()
# avg = img_sum / len(img)
# print("sum: ", img_sum)
# print(avg)



gram_dir='/home/pej/Desktop/1920*1080/seeun_center'
intel_dir='/home/pej/Desktop/1920*1080/intel_center'

print("디렉토리 생성")
newdir = gram_dir + "_pixel_average/"
os.makedirs(newdir)

def load_images(folder):
    images = []
    image_names = []

    filenames = os.listdir(folder)
    filenames.sort()

    for filename in filenames:
         if ".txt" not in filename:
            img = cv2.imread(os.path.join(folder, filename))
            print(img.shape)
            print("============================")

            if img is not None:
                images.append(img)
                image_names.append(filename)

    return images, image_names

images, image_names = load_images(gram_dir)
intels, intel_names = load_images(intel_dir)

result_folder = newdir

print("파일 로딩 완료")

print("밝기 조절 시작")

average = []
average_intel = []
count = 0
for i in range(len(images)):

    # print(img_gram_name[i] + ": ")
    image = images[i]
    intel = intels[i]

    # print(image_gram.shape)
    # image_seeun = img_seeun[i]
    #
    # l = uniform(0.85, 1.26)
    # l = 1.25

    # w_gram = image_gram.shape[0]
    # h_gram = image_gram.shape[1]

    # w_seeun = image_seeun.shape[0]
    # h_seeun = image_seeun.shape[1]

    # 화소값의 총합
    # gram_sum = image_gram.sum()
    # gram_avg = float(gram_sum / (w_gram * h_gram))

    gram_avg = np.mean(image)
    intel_avg = np.mean(intel)

    # print(gram_avg)

    average.append(gram_avg)
    average_intel.append(intel_avg)
    #
    # seeun_sum = image_seeun.sum()
    # seeun_avg = float(seeun_sum / (w_seeun * h_seeun))

    # key = float(intel_avg / seeun_avg)

    # 밝기 조절
    # image_new = image_seeun * key

    # 255 넘어가는 것 clipping
    # image_new = np.clip(image_new, 0, 255)

    # result = []
    # labels_i = labels[i]

    # print(len(labels_i))

    # count += 1
    # print(count)

    # print(labels_i)

    # for j in range(len(labels[i])):
    #
    #     # print(i, "번째 사진의 ", j, "번째 라벨")
    #
    #     w = images[i].shape[1]
    #     h = images[i].shape[0]
    #
    #     label_i = labels_i[j][0]  # label
    #
    #     x = float(labels_i[j][1])
    #     y = float(labels_i[j][2])
    #     w = float(labels_i[j][3])
    #     h = float(labels_i[j][4])
    #
    #     label = str(label_i) + ' '
    #     x = str(x) + ' '
    #     y = str(y) + ' '
    #     w = str(w) + ' '
    #     h = str(h) + '\n'
    #
    #     result.append(label)
    #     result.append(x)
    #     result.append(y)
    #     result.append(w)
    #     result.append(h)
    #
    #     if label_i in bb_count:
    #         bb_count[label_i] += 1
    #
    #     else:
    #         bb_count[label_i] = 1
    #
    # with open(result_folder + str(l) + "_light_" + label_names[i], mode='w') as file:
    #     file.writelines(result)

    # cv2.imwrite(result_folder + "averaged_" + img_name_seeun[i], image_new)
    #
    # if count % 100 == 0:
    #     print(count)

print("끝")
print(average)
print("===========")
print(average_intel)
# print("밝기: ", l)
