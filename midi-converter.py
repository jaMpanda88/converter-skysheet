import mido

# Load the MIDI file
mid = mido.MidiFile('example.mid')

# Extract data
midi_data = []
for i, track in enumerate(mid.tracks):
    track_data = {"name": track.name, "messages": []}
    for msg in track:
        track_data["messages"].append(str(msg))
    midi_data.append(track_data)

# Convert to TXT
with open('output.txt', 'w') as txt_file:
    for track in midi_data:
        txt_file.write(f"Track: {track['name']}\n")
        for msg in track["messages"]:
            txt_file.write(f"  {msg}\n")

# Convert to JSON
import json
with open('output.json', 'w') as json_file:
    json.dump(midi_data, json_file, indent=2)