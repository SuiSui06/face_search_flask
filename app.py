from flask import Flask, request, render_template, send_from_directory
import os
from utils import find_similar_faces

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
DATASET_FOLDER = os.path.join('static', 'dataset')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DATASET_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        query_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(query_path)

        results = find_similar_faces(query_path, top_k=5)
        return render_template('results.html', query=file.filename, results=results)
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)