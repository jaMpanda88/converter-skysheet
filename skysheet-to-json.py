import os
import json

# Define the base directory and the filename
base_dir = 'song-sheet'
filename = 'Kaine(Salvation).skysheet'

# Construct the full file path
file_path = os.path.join(base_dir, filename)

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Load the SKYSHEET content as JSON
skysheet_data = json.loads(content)

# Define paths for the output files
base_filename = os.path.splitext(filename)[0]
json_output_path = os.path.join(base_dir, f'{base_filename}.json')

# Save the content to a JSON file
with open(json_output_path, 'w') as json_file:
    json.dump(skysheet_data, json_file, indent=4)

os.remove(file_path)

print(f'Converted JSON file saved to {json_output_path}')
print(f'Original file {file_path} has been deleted.')