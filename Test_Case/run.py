# coding=utf-8
import time,os,unittest,shutil
from HTMLTestRunner import HTMLTestRunner


class TestRunner(object):
    ''' Run test '''

    def __init__(self, cases="./",title=u'自动化测试报告',description=u'环境：windows 7'):
        self.cases = cases
        self.title = title
        self.des = description

    #删除log日志里面之前的所有文件
    def clear_logfiles(self):
        delList = []
        delDir = "E:\Project_Auto\Appium_beta3_20191101\Log\\"
        delList = os.listdir(delDir)
        for f in delList:
            filePath = os.path.join( delDir, f )
            if os.path.isfile(filePath):
                os.remove(filePath)
                print filePath + " was removed!"
            elif os.path.isdir(filePath):
                shutil.rmtree(filePath,True)
                print "Directory: " + filePath +" was removed!"

    def run(self):

        for filename in os.listdir(self.cases):
            if filename == "report":
                break
        else:
            os.mkdir(self.cases+'/report')

        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        fp = open("./report/"+ now +"result.html", 'wb')
        case_path = os.getcwd()
        tests = unittest.defaultTestLoader.discover(case_path,pattern='StarDemo_*.py',top_level_dir=None)
        runner = HTMLTestRunner(stream=fp, title=self.title, description=self.des)
        runner.run(tests)
        fp.close()

    def debug(self):
        tests = unittest.defaultTestLoader.discover(self.cases, pattern='*sta.py', top_level_dir=None)
        runner = unittest.TextTestRunner()
        runner.run(tests)


if __name__ == '__main__':
    test = TestRunner()
    test.clear_logfiles()
    test.run()
