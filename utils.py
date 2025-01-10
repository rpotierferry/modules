import csv
import json

def load_csv(path, delimiter):
    try:
        with open(path, "r") as f:
            content = csv.reader(f, delimiter=delimiter)
            return list(content)
    except FileNotFoundError:
        print("Could not find csv file to load")

def save_csv(path, content, delimiter):
    try:
        with open(path, "w") as f:
            writer = csv.writer(f, delimiter=delimiter, quotechar="|", quoting=csv.QUOTE_MINIMAL)
            for row in content:
                writer.writerow(row)
    except FileNotFoundError:
        print("Could not find csv file to write")

def save_json(path, content):
    try:
        with open(path, "w") as f:
            json.dump(content, f)
    except FileNotFoundError:
        print("Could not find json file to write")

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Could not find json file to load")
