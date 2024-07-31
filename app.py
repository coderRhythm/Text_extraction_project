
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from src.image_processing import extract_text_from_image
from src.pdf_processing import extract_text_from_pdf
from src.utils import save_text_to_file, setup_logging

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['OUTPUT_FOLDER'] = 'output/'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Extract text
            if filename.lower().endswith('.pdf'):
                text = extract_text_from_pdf(file_path)
            else:
                text = extract_text_from_image(file_path)
            
            # Save text to file
            text_file = os.path.join('static', filename + '.txt')
            save_text_to_file(text, text_file)
            
            # Pass only the necessary information to the template
            return render_template('results.html', 
                                   extracted_text=text, 
                                   text_file=filename + '.txt')

    return render_template('upload.html')

if __name__ == '__main__':
    setup_logging()
    app.run(debug=True)
