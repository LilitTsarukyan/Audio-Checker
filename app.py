import json
import os


from playsound import playsound

output_data = {}


def process_next_file(file_name, file_path):
    print(f"Playing file: {file_name}")
    playsound(file_path)

    result = None
    while result not in ["c", "n"]:
        result = input(f"File: {file_name}, clear or noisy? c/n: ")

    output_data[file_name] = result


input("Press any key to start audio checker...")
file_paths = [(fl, "data/" + fl) for fl in os.listdir("data")]
for name, path in file_paths:
    process_next_file(name, path)

with open("results.json", "w+") as results_file:
    json.dump(output_data, results_file)
