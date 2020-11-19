import logging



def info(filename,log):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename=filename, level=logging.DEBUG, format=LOG_FORMAT)
    logging.info(log)


def debug(filename,log):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename=filename, level=logging.DEBUG, format=LOG_FORMAT)
    logging.debug(log)


def warning(filename,log):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename=filename, level=logging.DEBUG, format=LOG_FORMAT)
    logging.warning(log)


def error(filename,log):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename=filename, level=logging.DEBUG, format=LOG_FORMAT)
    logging.error(log)


def critical(filename,log):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename=filename, level=logging.DEBUG, format=LOG_FORMAT)
    logging.critical(log)
