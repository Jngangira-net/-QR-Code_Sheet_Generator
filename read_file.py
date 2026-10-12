import csv
import os
import requests
from io import StringIO

# Use local CSV mode since students.csv is right there in your folder
USE_OFFLINE_MODE = True 
local_csv_filename = "students.csv"

# 1. Ensure the destination folder exists
os.makedirs("qr_codes", exist_ok=True)

# 2. Read the local CSV file
print("Reading from local CSV file...")
with open(local_csv_filename, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    students = [row for row in reader]

print(f"Loaded {len(students)} student records successfully!")

# 3. Loop through each student and download/save their QR code
for student in students:
    name = student.get("Name")
    admission = student.get("Admission Number")
    qr_url = student.get("Qr Code")

    if not qr_url or not name or not admission:
        print("Skipping incomplete row:", student)
        continue

    # Build the target filename inside the qr_codes folder
    filename = os.path.join("qr_codes", f"{name}_{admission}.png")

    # If the file already exists, skip it
    if os.path.exists(filename):
        print("Already exists locally:", filename)
        continue

    # Download the QR code image bytes from the URL
    try:
        print(f"Downloading QR for {name}...")
        qr_response = requests.get(qr_url)
        
        if qr_response.status_code == 200:
            with open(filename, "wb") as img_file:
                img_file.write(qr_response.content)
            print("Successfully Saved:", filename)
        else:
            print(f"Failed to download. Status code: {qr_response.status_code}")
            
    except Exception as e:
        print(f"Error downloading {name}: {e}")