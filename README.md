# PyAppiumUI
基于python+Appium的UI自动化框架

1、	框架介绍
框架目录结构分为：Config_File、Get_Device_Info、Log、public_method、Test_Case
Config_File主要是配置文件，提供原参数，为各个方法调用提供数据配置。
Get_Device_Info主要是获取链接设备的驱动信息，然后return返回值给调用对象。
Log主要是记录当前执行每一个脚本的日志，方便debug信息。
public_method主要是实现脚本执行过程中需要调用相关公共类方法，从而获取UI元素获取、执行、响应等功能。
Test_Case主要是脚本集+批量执行方法，达到一次执行，所有脚本按序依次执行完。
该框架使用的unittest单元测试架构，相对来说该框架简单易用、可塑性强、稳定。


2、	方法介绍
2.1、Config_File中CommPath有1个方法：
Conf_Path:
configPath = os.path.join(proDir, "SdkInfo.ini")
path = os.path.abspath(configPath)
config.read(path)
return config
返回配置数据获取方法，方便后面调用。

2.2  Config_File中EmailConfig：
	里面主要是配置了邮件使用参数（Smtp_Server、Smtp_Sender
	、Smtp_Sender_Password、Smtp_Receiver）
	
2.3  Config_File中SdkInfo.ini：
	里面主要配置app软件参数、登录用户名密码、脚本文件路径。

2.4  Get_Device_Info中DeviceInfo
主要检查当前测试设备是否连接成功。
2.5  Log文件
有多少个测试脚本Log里就有多少个文件夹，每一个文件夹里的log文件都是每一个脚本测试日志。
2.6  public_method中Color_Change
主要是对每一条测试用例进行记录，在excel中对异常用例进行标记。
2.7  public_method中Email_Method（已开发，方法主流网上的都有）
主要是实现邮件发送相关人员接受测试所有数据，同步测试结果给相关人，这里面会调用配置参数、压缩文件方法。
zip_pathname = zip_ya()
part = MIMEApplication(open(zip_pathname, 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename=zip_pathname)
msg.attach(part)
# 发送附件
# Header()用于定义邮件主题，主题加上时间，是为了防止主题重复，主题重复，发送太过频繁，邮件会发送不出去。
msg['Subject'] = Header('[执行结果：' + 'XXXXUI自动化测试报告' + now, 'utf-8')
# 定义发件人，如果不写，发件人为空
msg['From'] = sender
# 定义收件人，如果不写，收件人为空
msg['To'] = ",".join(receiver)
tmp = smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

2.8  public_method中Log_Method
该方法主要实现了所有脚本、方法引用Log公共类方法，可以设置为info、error、debug等级别进行处理。
# 创建一个logger
self.logger = logging.getLogger(logger)
self.logger.setLevel(logging.DEBUG)

log_path_excel = os.path.dirname(os.getcwd()) + '\\Log\\'
print("log_path_excel:", log_path_excel)
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# 创建一个handler，用于写入日志文件
file_case_name = log_path_excel + path
print("file_case_name:", file_case_name)
os.mkdir(file_case_name, 0777)
self.log_path = file_case_name
log_path = self.log_path
self.log_name = log_path + '/' + rq + path + '.log'
log_name = self.log_name
fh = logging.FileHandler(log_name)

#调高log等级
fh.setLevel(logging.INFO)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
2.9  public_method中Read_Excel（如果用htmlrunner python自带的这个方法，就不用这么麻烦了，目前已上传的code就是支持htmlrunner方法使用，这块可以了解一下就行）
该方法的功能是在指定路径新建一个excel，用来记录存储测试结果数据。首先是初始化excel，配置上用例名、测试结果、失败原因、失败log路径、失败数、成功数、成功率。然后再引用该对对象，在每次执行脚本的时候写入测试结果、保存。
book = xlrd.open_workbook(excel_Name, formatting_info=True)  # 得到Excel文件的book对象，实例化对象
wb = copy(book)
wt = wb.get_sheet(0)
return book, wb, wt

2.10  public_method中Result_Excel
主要是用来遍历Test_Case路径下是测试用例的脚本名，保存为上一方法（Read_Excel）中的用例名。
def readFilename(path):
    for root, dirs, files in os.walk(path):
        return root, dirs, files

def startfind_count(root, dirs, files):
    j = 0
    count = []
    for ii in files:
        if ii.startswith('news_') and ii.endswith('.py'):
            j = j + 1
            count.append(j)
        else:
            continue
    return count

def startfind(root, dirs, files):
    book, wb, wt = read_excel()
    i = 0
    for ii in files:
        if ii.startswith('news_') and ii.endswith('.py'):
            case_Name = ii.split('.py')[0]
            i = i + 1
            wt.write(i, 0, case_Name)
        else:
            continue

    wb.save(excel_Name)

2.11  public_method中UI_Method
主要是所有元素获取函数话，每次修改只需要修改函数的入参即可，UI元素有调整也只需要去函数里修改就行，减少脚本的维护度。
driver, wait = get_driver()

class PySelenuim(object):

    #presence_of_element_located((By.ID))用法
    def by_element(self, css, value):
        if css == "id":
            css_ele = wait.until(EC.presence_of_element_located((By.ID, value)))
            return css_ele
        elif  css == "name":
            css_ele = wait.until(EC.presence_of_element_located((By.NAME, value)))
            return css_ele
        elif  css == "class":
            css_ele = wait.until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            return css_ele
        elif  css == "link_text":
            css_ele = wait.until(EC.presence_of_element_located((By.LINK_TEXT, value)))
            return css_ele
        elif  css == "xpath":
            css_ele = wait.until(EC.presence_of_element_located((By.XPATH, value)))
            return css_ele
        elif  css == "css":
            css_ele = wait.until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            return css_ele
        else:
            return False
            #raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
2.12  public_method中Zip_Log（已开发、未调试）
主要是用来压缩Log下的所有日志文件，为发送邮件提供。
startdir = "E:\F\Project_Auto\Appium_beta1\Log\\"  #要压缩的文件夹路径
nowdate = time.strftime("%Y-%m-%d-%H_%M_%S")
file_news = startdir + nowdate + '.zip' # 压缩后文件夹的名字
z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED) #参数一：文件夹名
zip_pathname = z.filename

for dirpath, dirnames, filenames in os.walk(startdir):
    fpath = dirpath.replace(startdir, '') #这一句很重要，不replace的话，就从根目录开始复制
    fpath = fpath and fpath + os.sep or ''#这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
    for filename in filenames:
        z.write(os.path.join(dirpath, filename), fpath+filename)
z.close()
return zip_pathname

2.12  Test_Case中脚本
脚本主要是对元素进行一系列用例步骤操作，保存测试数据，脚本名的格式需要“news”开头，“.Py”结尾。
2.13  Test_Case中的Run
主要实现对所有脚本一次性加载、依次执行，且在每一次执行的时候都会清除上一次Log下所有的文件日志，最后计算测试通过率，记录到excel中。
#删除log日志里面之前的所有文件
def clear_logfiles():
    delList = []
    delDir = "E:\F\Project_Auto\Appium_beta1\Log\\"
    delList = os.listdir(delDir)
    for f in delList:
        filePath = os.path.join( delDir, f )
        if os.path.isfile(filePath):
            os.remove(filePath)
            print filePath + " was removed!"
        elif os.path.isdir(filePath):
            shutil.rmtree(filePath,True)
            print "Directory: " + filePath +" was removed!"


# 报告存放路径，也是所有脚本的执行的地方
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





三、	操作使用
1、操作使用前，需要安装好app；手机连接电脑（最好手动检查是否连接获取驱动成功）；然后启动Appium服务
 
2、直接默认配置启动
 

3、	需要安装python环境（selenium包安装）；
4、	执行Run脚本；

