import logging
import time
from Object.static import get_project_path


class LogConfig:
    """
    logger提供了可以直接使用的接口
    handler将(logger创建的)日志记录发送到合适的目的输出
    filter提供了细度设备来决定输出哪条日志记录
    formatter决定日志记录的最终输出格式
    """
    """
    logging.getLogger([name]):返回一个logger对象，如果没有指定名字将返回root logger
    logging.debug()、logging.info()、logging.warning()、logging.error()、logging.critical()：设定root logger的日志级别
    logging.basicConfig():用默认Formatter为日志系统建立一个StreamHandler，设置基础配置并加到root logger中
    """
    """
    LOG=logging.getLogger(”chat.kernel”)
    Logger.setLevel(lel):指定最低的日志级别，低于lel的级别将被忽略。debug是最低的内置级别，critical为最高
    Logger.addFilter(filt)、Logger.removeFilter(filt):添加或删除指定的filter
    Logger.addHandler(hdlr)、Logger.removeHandler(hdlr)：增加或删除指定的handler
    Logger.debug()、Logger.info()、Logger.warning()、Logger.error()、Logger.critical()：可以设置的日志级别
    设置logger的level， level有以下几个级别：
    """
    def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):
        # 设置创建日志的对象
        self.logger = logging.getLogger(__name__)
        # 设置日志的最低级别低于这个级别将不会在屏幕输出，也不会保存到log文件
        self.logger.setLevel(logging.DEBUG)
        # 给这个handler选择一个格式（）
        fmt = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
        # 设置控制台日志 向终端输出的日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)    # 设置个控制台日志的格式
        sh.setLevel(clevel)     # 设置控制台日志最低等级
        # 设置文件日志 用于向一个文件输出日志信息。不过FileHandler会帮你打开这个文件。
        fh = logging.FileHandler(path, encoding="utf-8")
        fh.setFormatter(fmt)    # 设置个文件日志的格式
        fh.setLevel(Flevel)     # 设置终端日志最低等级
        self.logger.addHandler(sh)  # 增加终端日志Handler
        self.logger.addHandler(fh)  # 增加文件日志Handler

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def exception(self, message):
        self.logger.exception(message)


log = LogConfig(get_project_path() + '/Log/log.log')
