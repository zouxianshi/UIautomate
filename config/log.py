# -*-coding:UTF-8 -*-
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S', filename=r'/log.log', filemode='w')
# 创建一个handler，输出到控制台
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(ch)


def info(INFO):
    logger.info(INFO)


def error(ERROR):
    logger.info(ERROR)


def critical(CRITICAL):
    logger.critical(CRITICAL)


def warning(WARNING):
    logger.warning(WARNING)


def debug(DEBUG):
    logger.debug(DEBUG)
