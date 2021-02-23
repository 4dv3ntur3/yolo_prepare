import os
os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"

import tensorflow as tf
import numpy as np
import pandas as pd
import operator
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical


data = pd.read_excel('/home/pej/Desktop/sample_data/sample_data.xlsx', engine='openpyxl')

x = data['feature']
y = data['label']


# print(x[0])
dict = {}
for i in range(len(data)):
    # if i == 15:
    #     jj = 0
    list_str = list(data.iloc[i, 0])
    for j in range(len(list_str)):
        if list_str[j] in dict:
            dict[list_str[j]] += 1
        else:
            dict[list_str[j]] = 1

# dict_sorted = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
# print(dict_sorted)
dict_keys = list(dict.keys())
print(dict_keys)
print(len(dict_keys)) # 57

max_len = 0
for i in range(len(x)):
    converted_str = []
    list_str = list(data.iloc[i, 0])
    if len(list_str) > max_len:
        max_len = len(list_str)
    for j in range(len(list_str)):
        converted_str.append(dict_keys.index(list_str[j]))

    # data.iloc[i, ['new_feature']] = converted_str

print(max_len)  # 56
# print(converted_str)

# print(np_data)
dict_len = len(dict_keys)

label = y.unique()
# print(label) #['FTHR' 'EJEC' 'EJEP']

# 분리 후 random shuffle -> index reset -> 이제 개수만큼 분리하면 됨
fthr = data[data['label'] == label[0]].sample(frac=1).reset_index(drop=True)
ejec = data[data['label'] == label[1]].sample(frac=1).reset_index(drop=True)
ejep = data[data['label'] == label[2]].sample(frac=1).reset_index(drop=True)

# print(len(fthr)) # 1791
# print(len(ejec)) # 4463
# print(len(ejep)) # 3751



# print(len(ejec_train))
# print(len(ejec_test))
#
# print(len(ejep_train))
# print(len(ejep_test))
#
# print(len(fthr_train))
# print(len(fthr_test))


ejec_train = ejec[:4000]
ejec_test = ejec[4000:]

ejep_train = ejep[:3300]
ejep_test = ejep[3300:]

fthr_train = fthr[:1400]
fthr_test = fthr[1400:]

# 우선 ejec, ejep만 합친 후 섞음
train = pd.concat([ejec_train, ejep_train, fthr_train]).sample(frac=1).reset_index(drop=True)
test = pd.concat([ejec_test, ejep_test, fthr_test]).sample(frac=1).reset_index(drop=True)

# print(len(train))
# print(len(test))
# print(train.head())
# print(test.head())

x_train = train['feature'].to_numpy()
y_train = train['label'].to_numpy()
x_test = test['feature'].to_numpy()
y_test = test['label'].to_numpy()


x = np.zeros((x_train.shape[0], max_len, dict_len), dtype=np.float32)
x_t = np.zeros((x_test.shape[0], max_len, dict_len), dtype=np.float32)

for i in range(x.shape[0]):
    for j in range(len(x_train[i])):
        x[i, j, dict_keys.index(x_train[i][j])] = 1.0

for i in range(x_t.shape[0]):
    for j in range(len(x_test[i])):
        x_t[i, j, dict_keys.index(x_test[i][j])] = 1.0

# rr=1

encoder = LabelEncoder()

encoder.fit(y_train)
y_train_encoded = encoder.transform(y_train)
y_train_encoded = to_categorical(y_train_encoded)

# X_test데이터에만 존재하는 새로 출현한 데이터를 신규 클래스로 추가
for label in np.unique(y_test):
    if label not in encoder.classes_: # unseen label 데이터인 경우( )
        encoder.classes_ = np.append(encoder.classes_, label) # 미처리 시 ValueError발생

y_test_encoded = encoder.transform(y_test)
y_test_encoded = to_categorical(y_test_encoded)
# print(y_train_encoded.shape) # 7300,


# x_ -> y_train_encoded
# x_t -> y_test_encoded
# print(y_train_encoded)


x__train = x.reshape([x.shape[0], -1])
x__test = x_t.reshape([x_t.shape[0], -1])

print(len(x__test))
print(len(x__train))


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

model = Sequential()
model.add(Dense(500, activation='relu', input_shape=(x__train.shape[1],)))
model.add(Dense(150, activation='relu'))
model.add(Dense(110, activation='relu'))
model.add(Dense(70, activation='relu'))
model.add(Dense(50, activation='relu'))
# model.add(Dense(30, activation='relu'))
model.add(Dense(3, activation='softmax'))


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x__train, y_train_encoded, epochs=300, batch_size=32, validation_split=0.2)

loss, accuracy = model.evaluate(x__test, y_test_encoded, batch_size=32)


print("loss: ", loss)
print("acc: ", accuracy)







