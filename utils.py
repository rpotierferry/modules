import csv
import json
import logging
import os


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


def create_file_logger(name, logs_path="logs"):
    """ returns a custome logger that writes to a file using logger name at INFO level
    will create a folder containing the logs
    args:
        name(str) : name of the logger, will be used to name the file
        logs_path(str) : name of the logs folder (defaults to "logs") """

    if not os.path.exists(logs_path):
        os.mkdir(logs_path)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    log_file_path = os.path.join(logs_path, name)
    file_handler = logging.FileHandler(f"{log_file_path}.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger
