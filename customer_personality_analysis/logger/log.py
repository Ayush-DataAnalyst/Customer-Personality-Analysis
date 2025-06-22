import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

def log(message):
    logging.info(message)
