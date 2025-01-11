import os
import logging

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
