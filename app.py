import os
import re
from flask import Flask, request, render_template, send_from_directory, jsonify, session, send_file
from werkzeug.utils import safe_join
from PIL import Image, ImageOps  # Import ImageOps along with Image
import io


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Set your base directory (adjust as needed)
BASE_DIR = '/home/ai-server'

def numerical_sort_key(filename):
    parts = re.split(r'(\d+)', filename)
    parts[1::2] = map(int, parts[1::2])  # Convert numerical parts to integers
    return parts

@app.route('/browse/', defaults={'path': ''})
@app.route('/browse/<path:path>')
def browse(path):
    abs_path = safe_join(BASE_DIR, path)

    if not os.path.exists(abs_path):
        return "Path does not exist", 404

    if os.path.isfile(abs_path) and abs_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        if session.get('histogram_eq_enabled', False):
            return apply_histogram_equalization(abs_path)
        else:
            return send_from_directory(os.path.dirname(abs_path), os.path.basename(abs_path))

    files = [f for f in os.listdir(abs_path) if os.path.isfile(os.path.join(abs_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    directories = [d for d in os.listdir(abs_path) if os.path.isdir(os.path.join(abs_path, d))]
    files.sort(key=numerical_sort_key)
    if 'histogram_eq_enabled' not in session:
        print('here here')
        session['histogram_eq_enabled'] = False
    directories.sort(key=numerical_sort_key)
    histogram_eq_enabled = session.get('histogram_eq_enabled', False)
    return render_template('browse.html', files=files, directories=directories, path=path, histogram_eq_enabled=histogram_eq_enabled)

@app.before_first_request
def clear_session():
    session.clear()

@app.route('/image/<path:filename>')
def get_image(filename):
    # Make sure the path is relative to BASE_DIR
    image_path = safe_join(BASE_DIR, filename)

    # Check if the file exists and serve it
    if os.path.isfile(image_path):
        return send_file(image_path, mimetype='image/png')  # Adjust mimetype if needed
    else:
        return "File not found", 404




@app.route('/toggle_histogram_eq', methods=['POST'])
def toggle_histogram_eq():
    data = request.json
    session['histogram_eq_enabled'] = data.get('enable', False)
    return jsonify({"status": "success", "message": "Histogram equalization updated"})

def apply_histogram_equalization(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    img_gray = img.convert('L')

    # Apply histogram equalization (this is a simplified example)
    img_eq = ImageOps.equalize(img_gray)

    # Save the processed image to a BytesIO object (in-memory file)
    img_io = io.BytesIO()
    img_eq.save(img_io, 'PNG', quality=100)  # Adjust format and quality as needed
    img_io.seek(0)  # Rewind the file-like object to the beginning

    # Return the in-memory file as a response
    return send_file(img_io, mimetype='image/png', as_attachment=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

