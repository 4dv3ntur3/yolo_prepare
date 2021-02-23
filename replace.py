import glob

# train_data와 train_labels_dat 를 만든 후 validation 도 해 줘야 함
files = glob.glob("/home/pej/Desktop/alcohol_1407/images/validation_data.txt")
labels = open('/home/pej/Desktop/alcohol_1407/images/validation_labels_data.txt', 'w')
count = 0

for file in files:
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            labels.write(line.replace("jpg", "txt"))
        else:
            pass