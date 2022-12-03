#!/bin/bash

# Constants
PHOTO_URL = "http://127.0.0.1:8080/photoaf.jpg"
FILE_NAME_FORMAT = "%Y-%m-%d_%H-%M-%S"

# Generate a filename using the current date and time and the username of the user running the script
file_name = "$(date +"${FILE_NAME_FORMAT}")_$(whoami)"
file_path = "${PWD}/${file_name}.jpg"

# Download the photo from the local server
wget -O "${file_path}" "${PHOTO_URL}" || exit 1

# Upload the photo to Google Drive
gdrive-windows-x64 upload -p xxxxxxxxxxx "${file_name}.jpg"
