"""
    Description: 设置log文件信息，保存模型中间输出和最终结果
    Author: WangHaotian
    Date: 2023/2/20 12:53
"""
import logging
import argparse


def create_logger(logger_file_name):
    """
    :param logger_file_name:
    :return:
    """
    logger = logging.getLogger()         # 设定日志对象
    logger.setLevel(logging.INFO)        # 设定日志等级

    file_handler = logging.FileHandler(logger_file_name)
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s: %(message)s "
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='configTemplates')
    parser.add_argument('-log_path', default='./results/test.log', type=str, help='log file path to save result')

    args = parser.parse_args()

    logger = create_logger(args.log_path)

    logger.info('Begin Training Model...')








