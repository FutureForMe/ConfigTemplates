# ConfigTemplates

### 1.设置随机种子
为了让模型结果可复现，需要使用随机种子对模型中的参数进行限定，具体代码如下：

    def set_seed(args):
        torch.manual_seed(args.seed)
        torch.cuda.manual_seed_all(args.seed)
        np.random.seed(args.seed)
        random.seed(args.seed)
        torch.backends.cudnn.deterministic = True 


### 2.设置logger，保存结果
在模型运行过程中，需要将中间结果或者最终实验结果保存时，可以定义该文件，将训练过程进行保存。

    def create_logger(logger_file_name):
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
