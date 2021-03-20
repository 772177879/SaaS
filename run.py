import unittest
import HTMLTestRunner
import time
from Object import static


case_path = static.get_project_path() + '/Test'
now = time.strftime('%Y-%m-%d %H-%M-%S')

if __name__ == "__main__":
    fp = open(static.get_project_path() + '/ResultReport/' + now + '.html', 'wb')
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="Test*.py",
                                                   top_level_dir=None)
    run = HTMLTestRunner.HTMLTestRunner(
        title="优云企业版测试报告", description="测试结果", verbosity=2, stream=fp)
    run.run(discover)
    fp.close()
