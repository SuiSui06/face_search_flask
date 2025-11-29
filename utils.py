import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image

# モデル（クエリ画像用のみ）
model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

# 保存済み特徴量をロード
features = np.load("features.npy")
filenames = np.load("filenames.npy")

def extract_features(img_path):
    """クエリ画像から特徴ベクトルを抽出"""
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = preprocess_input(np.expand_dims(x, axis=0))
    feat = model.predict(x)
    return feat.flatten()

def find_similar_faces(query_path, top_k=5):
    """クエリ画像と保存済み特徴量を比較"""
    query_feat = extract_features(query_path)
    sims = cosine_similarity([query_feat], features)[0]
    idxs = sims.argsort()[::-1][:top_k]
    results = [(filenames[i], sims[i]) for i in idxs]
    return results