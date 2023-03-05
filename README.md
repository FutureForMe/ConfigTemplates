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
在模型运行过程中，需要将中间结果或者最终实验结果保存时，可以定义该文件，将训练过程进行保存。具体详解参见[知乎链接](https://zhuanlan.zhihu.com/p/610766031) 。

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

### 3.设置argparse
设置argparse可分为四大步骤：  
- 第一步：引入argparse库  
- 第二步：创建解析对象
- 第三步：添加命令行参数和选项
- 第四步：对参数进行解析。将参数字符串转换为对象并将其设为命名空间的属性。 返回带有成员的命名空间。  

常用参数解析模板如下所示：

    import argparse   # 第一步：引入argparse库

    def set_parser():
        parser = argparse.ArgumentParser(description='The parser for text classification')     # 第二步：创建解析对象
    
        parser.add_argument('-model_name', type=str, default='CNN', choices=['CNN', 'RNN', 'Transformer'])   # 第三步：添加命令行参数和选项
        parser.add_argument('-filter', type=str, default='3,4,5', help='kernel size for CNN')
    
        # ...可以添加其他模型需要的参数
    
        args = parser.parse_args()    # 第四步：对参数进行解析
    
        return args

    if __name__ == '__main__':
        args = set_parser()
        print(args.model_name)

调用方式也基本分为两种，一种是在模型内部代码中调用，另一种是可以命令行运行是进行赋值调用。

    python set_argparse -model RNN

具体细节见 [知乎链接](https://zhuanlan.zhihu.com/p/611448111) 。