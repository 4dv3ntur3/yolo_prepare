import cv2
import numpy as np
import sys, os, re
from random import uniform
from sklearn.metrics import mean_squared_error
from skimage import measure

# # 기본 이미지 사이즈
# w = 1024
# h = 768

gram_dir='/home/pej/Desktop/1920*1080/seeun_right'
intel_dir='/home/pej/Desktop/1920*1080/intel_right'


print("디렉토리 생성")
newdir = gram_dir + "_compared_rmse_640360/"
os.makedirs(newdir)


def RMSE(y0, y1):
    return np.sqrt(mean_squared_error(y0, y1))


def load_images(folder):
    images = []
    image_names = []

    filenames = os.listdir(folder)
    filenames.sort()

    for filename in filenames:
         if ".jpg" in filename:
            img = cv2.imread(os.path.join(folder, filename))

            if img is not None:
                images.append(img)
                image_names.append(filename)

    return images, image_names


def load_binary(folder):
    images = []
    image_names = []

    filenames = os.listdir(folder)
    filenames.sort()

    for filename in filenames:
         if ".bin" in filename:
            img = np.fromfile(os.path.join(folder, filename), dtype=np.uint8)
            # img = np.reshape(img, (480, 640, 3))

            if img is not None:
                images.append(img)
                image_names.append(filename)

    return images, image_names


images, image_names = load_images(gram_dir)
intels, intel_names = load_images(intel_dir)


result_folder = newdir

print("파일 로딩 완료")

print("resize 시작: 1024 * 168 -> 640 * 480")

bb_count = {}
for i in range(len(images)):
    #
    # print(intel_names[i])
    # print(image_names[i])

    intel = intels[i]
    image = images[i]


    # resize
    resize_i = cv2.resize(intel, dsize=(640, 360), interpolation=cv2.INTER_LINEAR)
    resize_s = cv2.resize(image, dsize=(640, 360), interpolation=cv2.INTER_LINEAR)



    image_1 = np.reshape(resize_s, (640*360*3))
    intel_1 = np.reshape(resize_i, (640*360*3))

    # # 밝기 조절
    # image = image * l
    # image = np.clip(image, 0, 255)

    # w = image.shape[1]
    # h = image.shape[0]

    # resize
    # resize = cv2.resize(image, dsize=(640, 480), interpolation=cv2.INTER_LANCZOS4)

    # zero_zero_g = resize[0][0][0]
    # zero_zero_i = intel[0][0][0]

    # resize_1 = np.reshape(resize, (640*480*3))

    # # # resize된 이미지 크기
    # w_new = resize.shape[1]
    # h_new = resize.shape[0]

    # for k in range(resize.shape[0]):
    #     for h in range(resize.shape[1]):
    #         for l in range(3):
    #             a = RMSE(resize[k][h][l], intel[sk][h][l])

    a = RMSE(image_1, intel_1)
    print(a)

    # print(mean_squared_error(resize[0][0][0], intel[0][0][0]))
    #
    # print(RMSE(zero_zero_i, zero_zero_g))

    # image_c = resize.copy()
    # tempDiff = cv2.subtract(resize, intel)

    #
    # grayA = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # grayB = cv2.cvtColor(intel, cv2.COLOR_BGR2GRAY)
    #
    # (score, diff) = measure.compare_ssim(grayA, grayB, full=Truew)
    # diff = (diff * 255).astype("uint8")
    # print(f"Similarity: {score:.5f}")
    #
    # assert score, "다른 점 찾을 수 없음"

    cv2.imwrite(result_folder + "_640360_" + image_names[i], resize_s)
    cv2.imwrite(result_folder + "_640360_" + intel_names[i], resize_i)


    # if i % 100 == 0:
    #     print(i)

print("끝")
# print(bb_count)
# print("배율: ", p)
