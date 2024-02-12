
# Flask Image Browser

## Introduction
This Flask application provides a web interface for browsing through images stored in a specific directory on the server. It also features an option to apply histogram equalization to any image, enhancing its contrast for better visibility. This functionality is particularly useful for viewing images in environments where lighting conditions may not be ideal, or for images that are naturally low in contrast.

## Features
- **Image Browsing:** Navigate through directories and view images (.png, .jpg, .jpeg, .gif) stored on the server.
- **Histogram Equalization:** Dynamically apply histogram equalization to images to improve their contrast directly from the web interface.
- **Safe Navigation:** Access files and directories safely without exposing the server to security risks.
- **Session Management:** User session management to remember preferences like histogram equalization toggle across browsing sessions.

## Setup
### Prerequisites
- Python 3.6+
- Flask
- Pillow

### Installation
1. Clone the repository to your local machine or server.
2. Install the required Python packages using pip:
    ```bash
    pip install Flask Pillow
    ```
3. Set the `BASE_DIR` variable in the script to point to the directory you want to browse.

### Running the Application
Execute the following command from the directory containing the application:
```bash
python app.py
```
The application will start running on `http://0.0.0.0:5001/`. You can access it from your web browser.

## Usage
- Navigate to `http://<server-ip>:5001/browse/` to start browsing through the images stored under the `BASE_DIR`.
- Click on any image to view it. If histogram equalization is enabled, the image will be displayed with the applied effect.
- Toggle the histogram equalization feature by sending a POST request to `/toggle_histogram_eq` with JSON data `{"enable": true}` or `{"enable": false}`.

## Customization
- **Change Port:** Modify the `port` parameter in `app.run()` to use a different port.
- **Secret Key:** Change the `app.secret_key` to something unique and secure for session management.

## License
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
