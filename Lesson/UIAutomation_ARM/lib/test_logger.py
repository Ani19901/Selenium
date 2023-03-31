import logging

logging.basicConfig(filename="out.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')


def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)


