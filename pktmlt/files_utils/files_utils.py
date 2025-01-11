import csv
import json
import logging


def load_csv(path:str, delimiter:str)->list:
    """ loads the content of a csv file
    args:
        path(str) : path to file
        delimiter(str) : columns delimiter

    returns:
        rows(list) """

    try:
        with open(path, "r") as f:
            content = csv.reader(f, delimiter=delimiter)
            logging.info("csv file loaded")
            return list(content)
    except FileNotFoundError:
        logging.critical("Could not find csv file to load")


def save_csv(path:str, content:list, delimiter:str):
    """ saves content to csv file
    args:
        path(str) : path to file
        content(list) : content to store
        delimiter(str) : columns delimiter """

    try:
        with open(path, "w") as f:
            writer = csv.writer(f, delimiter=delimiter, quotechar="|", quoting=csv.QUOTE_MINIMAL)
            for row in content:
                writer.writerow(row)
            logging.info("csv file written")
    except FileNotFoundError:
        logging.critical("Could not find csv file to write")


def save_json(path:str, content:dict):
    """ save content to json file
    args:
        path(str) : path to file
        content(dict) : content to save """

    try:
        with open(path, "w") as f:
            json.dump(content, f)
            logging.info("json file written")
    except FileNotFoundError:
        logging.critical("Could not find json file to write")


def load_json(path):
    """ loads the content of a json file
    args:
        path(str) : path to file """

    try:
        with open(path, "r") as f:
            logging.info("json file loaded")
            return json.load(f)
    except FileNotFoundError:
        logging.critical("Could not find json file to load")
