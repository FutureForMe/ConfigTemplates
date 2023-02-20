import os
import torch
import numpy as np
import random
import argparse


def set_seed(args):
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    np.random.seed(args.seed)
    random.seed(args.seed)
    torch.backends.cudnn.deterministic = True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='configTemplates')
    parser.add_argument('-seed', default=2023, type=int, help='set seed for model')