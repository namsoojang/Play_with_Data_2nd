from PIL import Image
import os, glob
import numpy as np
import random, math
# 분류 대상 카테고리
root_dir = "./image/"
categories = ["normal", "beni", "negi", "cheese"]
nb_classes = len(categories)
image_size = 50
# 이미지 데이터 읽어 들이기 --- (※1)
X = [] # 이미지 데이터
Y = [] # 레이블 데이터
def add_sample(cat, fname, is_train):
    img = Image.open(fname)
    img = img.convert("RGB") # 색상 모드 변경하기
    img = img.resize((image_size, image_size)) # 이미지 크기 변경하기
    data = np.asarray(img)
    X.append(data)
    Y.append(cat)
    if not is_train: return
    # 각도를 조금 변경한 파일 추가하기
    # 회전하기
    for ang in range(-20, 20, 5):
        img2 = img.rotate(ang)
        data = np.asarray(img2)
        X.append(data)
        Y.append(cat)
        # img2.save("gyudon-"+str(ang)+".PNG")
        # 반전하기
        img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
        data = np.asarray(img2)
        X.append(data)
        Y.append(cat)
def make_sample(files, is_train):
    global X, Y
    X = []; Y = []
    for cat, fname in files:
        add_sample(cat, fname, is_train)
    return np.array(X), np.array(Y)
# 각 폴더에 들어있는 파일 수집하기 --- (※2)
allfiles = []
for idx, cat in enumerate(categories):
    image_dir = root_dir + "/" + cat
    files = glob.glob(image_dir + "/*.PG")
    for f in files:
        allfiles.append((idx, f))
# 섞은 뒤에 학습 전용 데이터와 테스트 전용 데이터 구분하기 --- (※3)
random.shuffle(allfiles)
th = math.floor(len(allfiles) * 0.6)
train = allfiles[0:th]
test  = allfiles[th:]
X_train, y_train = make_sample(train, True)
X_test, y_test = make_sample(test, False)
xy = (X_train, X_test, y_train, y_test)
np.save("./image/gyudon2.npy", xy)
print("ok,", len(y_train))