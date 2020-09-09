from selenium import webdriver
from time import sleep
import random
import datetime
import smtplib
from email.mime.text import MIMEText


# 收件人列表
mail_namelist = ["2877175097@qq.com"]
# 发送方信息
mail_user = "2098957758@qq.com"
# 口令,注意这里是腾讯的授权码，可不是什么 QQ密码或者独立密码！
# http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256
mail_pass = "wppkacinbycldebj"
def send_qq_email(title, conen):
    try:
        msg = MIMEText(str(conen))
        # 设置标题
        msg["Subject"] = title
        # 发件邮箱
        msg["From"] = mail_user
        # 收件邮箱
        msg["To"] = ";".join(mail_namelist)
        # 设置服务器、端口
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 登录邮箱
        s.login(mail_user, mail_pass)
        # 发送邮件
        s.sendmail(mail_user, mail_namelist, msg.as_string())
        s.quit()
        print("邮件发送成功!")
        return True
    except smtplib.SMTPException as err:
        print("邮件发送失败！"+str(err))
        return False


def auto_dk():
    # 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
    # driver = webdriver.Chrome('C:\\Users\\fugui\\PycharmProjects\\自动打卡\\自动打卡\\chromedriver.exe')
    driver = webdriver.PhantomJS('C:\\Users\\fugui\\PycharmProjects\\自动打卡\\自动打卡\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    # 通过抓包获取到学校打卡系统app有登录后台找到这个登陆链接直接模拟登陆
    driver.get("https://cas.gfxy.com/lyuapServer/login")
    input_first = driver.find_element_by_id('username')
    input_two = driver.find_element_by_id('password')
    input_first.send_keys('35318618') # 六位学号
    input_two.send_keys('09393X') # 默认密码省份证后六位
    driver.find_element_by_name('login').click()
    sleep(3)
    # 登录按钮
    driver.find_element_by_xpath('.//div[@class="el-scrollbar__view"]/li[4]/a').click()
    sleep(5)
    # 切换当前页面url
    driver.switch_to.window(driver.window_handles[1])
    driver.get(driver.current_url)

    print(driver.current_url)
    # 获取温度输入框
    wendu = driver.find_element_by_id('DQTW')
    # 清空上一次温度
    wendu.clear()
    # 温度 list
    wendu_list = ['36.5', '36.3', '36.4', '36.6', '36.7', '36.2']
    # 随机获取一个温度
    tem = random.choices(wendu_list)
    wendu.send_keys(tem)
    sleep(3)
    driver.find_element_by_xpath('.//div[@id="bar_v4"]/div/div[2]/span/a')
    sleep(0.5)
    # 关闭浏览器
    driver.quit()

while True:
    sleep(1)
    nowTime = datetime.datetime.now().strftime('%H:%M:%S')  # 现在时间
    print(nowTime)
    # 早上打卡
    try:
        if nowTime == '07:30:30':
            auto_dk()
        # 中午打卡
        elif nowTime == '12:05:30':
            auto_dk()
        # 晚上打卡
        elif nowTime == '19:05:10':
            auto_dk()
        else:
            print('休眠')
    except Exception as e:
        print(e)