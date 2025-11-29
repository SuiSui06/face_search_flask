import os
import shutil
import zipfile

# ダウンロード済みのCelebA zipファイルの場所
celeba_zip = "img_align_celeba.zip"   # プロジェクト直下に配置
extract_dir = "celeba_images"
dataset_dir = os.path.join("static", "dataset")

# 展開先フォルダを作成
os.makedirs(extract_dir, exist_ok=True)
os.makedirs(dataset_dir, exist_ok=True)

# ZIPを展開
with zipfile.ZipFile(celeba_zip, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# CelebAの画像を一部コピー（例：最初の500枚）
files = os.listdir(extract_dir)
sample_size = 500   # ←ここを100〜1000に調整可能
for i, fname in enumerate(files[:sample_size]):
    src = os.path.join(extract_dir, fname)
    dst = os.path.join(dataset_dir, fname)
    shutil.copy(src, dst)

print(f"CelebAの画像 {sample_size} 枚を dataset/ にコピーしました。")