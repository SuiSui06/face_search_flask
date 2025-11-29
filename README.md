# 類似顔検索AIアプリ（Flask版 + CelebA）

顔画像をアップロードすると、学習済みCNN（MobileNetV2）を使って類似する顔画像を検索・表示するAIアプリです。FlaskでWeb化し、CelebAデータセットを利用しています。

## 使用技術
- Python 3.10
- TensorFlow / Keras
- OpenCV
- scikit-learn
- Flask

## 実行方法（ローカル）
```bash
pip install -r requirements.txt
python prepare_celeba.py   # CelebAデータセットを準備
python prepare_features.py # 特徴量を事前計算
python app.py