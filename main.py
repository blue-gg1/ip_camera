import os
import sys

import requests
import wget
from datetime import datetime

# Constants
PHOTO_URL = "http://192.168.1.25:8080/photo.jpg"
PHOTO_DIRECTORY = "/Users/bluepill/Documents/proj/ipcamrea/photos"
FILE_NAME_FORMAT = "%Y-%m-%d_%H-%M-%S"

# Download the photo repeatedly at a specified interval
try:
    wget.download(
        PHOTO_URL,
        out=PHOTO_DIRECTORY,
        retry_delay=10,
        wait=10,
        min_size=100,
        timestamping=True,
    )
except requests.exceptions.RequestException as error:
    print(f"Error downloading photo: {error}")
    sys.exit(1)

# Generate a filename using the current date and time
file_name = datetime.now().strftime(FILE_NAME_FORMAT)
file_path = os.path.join(PHOTO_DIRECTORY, file_name + ".jpg")

# Add the timestamp to the photo
try:
    with open(file_path, "rb") as f:
        image = Image.open(f)
        draw = ImageDraw.Draw(image)
