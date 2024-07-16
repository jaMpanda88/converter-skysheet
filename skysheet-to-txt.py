import os
import json

# Define the base directory and the filename
base_dir = 'song-sheet'
filename = ''

# Construct the full file path
file_path = os.path.join(base_dir, filename)

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Load the SKYSHEET content as JSON
skysheet_data = json.loads(content)

# Define output filenames based on the original filename
base_filename = os.path.splitext(filename)[0]
txt_output_path = os.path.join(base_dir, f'{base_filename}.txt')

# Save the content to a TXT file in a readable format
with open(txt_output_path, 'w') as txt_file:
    txt_file.write(json.dumps(skysheet_data, indent=4))

# Delete the original SKYSHEET file
os.remove(file_path)

print(f'Converted TXT file saved to {txt_output_path}')
print(f'Original file {file_path} has been deleted.')