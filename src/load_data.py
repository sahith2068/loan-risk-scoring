import gdown
import os

# Make sure the data/raw directory exists
os.makedirs("data/raw", exist_ok=True)

# Google Drive file links
accepted_url = "https://drive.google.com/uc?id=1m9KbR6L6kjg6tBFZjZhZEds82zUp4Nyy"
rejected_url = "https://drive.google.com/uc?id=1sbt_iSVaCHHA1QIUCpqo6QmXA33nUpX6"

# Paths to save downloaded files
accepted_path = "data/raw/accepted_2007_to_2018Q4.csv"
rejected_path = "data/raw/rejected_2007_to_2018Q4.csv"

# Download files
gdown.download(accepted_url, accepted_path, quiet=False)
gdown.download(rejected_url, rejected_path, quiet=False)

