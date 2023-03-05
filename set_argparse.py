"""
    Description: set parser for model
    Author: WangHaotian
    Date: 2023/3/4 16:28
"""
import argparse  # 第一步：引入argparse库


def set_parser():
    parser = argparse.ArgumentParser(description='The parser for text classification')  # 第二步：创建解析对象

    parser.add_argument('-model_name', type=str, default='CNN',
                        choices=['CNN', 'RNN', 'Transformer'])  # 第三步：添加命令行参数和选项
    parser.add_argument('-filter', type=str, default='3,4,5', help='kernel size for CNN')

    # ...可以添加其他模型需要的参数

    args = parser.parse_args()  # 第四步：对参数进行解析

    return args


if __name__ == '__main__':
    args = set_parser()
    print(args.model_name)