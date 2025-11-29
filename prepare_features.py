import os
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image

model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = preprocess_input(np.expand_dims(x, axis=0))
    feat = model.predict(x)
    return feat.flatten()

dataset_dir = "static/dataset"
features = []
filenames = []

for fname in os.listdir(dataset_dir):
    path = os.path.join(dataset_dir, fname)
    feat = extract_features(path)
    features.append(feat)
    filenames.append(fname)

features = np.array(features)
np.save("features.npy", features)
np.save("filenames.npy", filenames)

print(f"特徴量 {features.shape} を保存しました。")