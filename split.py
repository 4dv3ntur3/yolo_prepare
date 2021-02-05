import random

# txt = open('/home/pej/platform_yolo/image/train.txt', 'r')
# f = open('/home/pej/platform_yolo/image/train_shuffle.txt', 'w')
#
# tmp = []
#
# while True:
#     line = txt.readline()
#     if not line:
#         break
#     tmp.append(line)
#
# random.shuffle(tmp)
#
# for i in tmp:
#     f.write(i)
#
# txt.close()
# f.close()

#
count = 0
length = 19693

txt = open('/home/pej/platform_yolo/image/train_shuffle.txt', 'r')

i = 0

f = open('/home/pej/platform_yolo/image/train_data.txt', 'w')
f2 = open('/home/pej/platform_yolo/image/validation_data.txt', 'w')

while True:
    if i == 0:
        line = txt.readline()
        if not line:
            break
        count += 1
        if count < int(length/10) * 2:
            f2.write(line)
        else:
            f.write(line)
txt.close()
f.close()
f2.close()