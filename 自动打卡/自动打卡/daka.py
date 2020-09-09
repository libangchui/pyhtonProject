
from selenium import webdriver
from time import sleep
import random
import datetime
import smtplib
from email.mime.text import MIMEText
from selenium.webdriver.chrome.options import Options


# 收件人列表
mail_namelist = ["2098957758@qq.com"]
# 发送方信息
mail_user = "2230871059@qq.com"
# 口令,注意这里是腾讯的授权码，可不是什么 QQ密码或者独立密码！
# http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256
mail_pass = "epdsoejrewuedhgg"#epdsoejrewuedhgg    wppkacinbycldebj
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
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
    # driver = webdriver.PhantomJS()
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.PhantomJS('/phantomjs-2.1.1-linux-i686/bin/hantomjs')
    driver = webdriver.Chrome()
    # 用get打开百度页面
    driver.get("https://cas.gfxy.com/lyuapServer/login")
    print(driver.page_source)
    input_first = driver.find_element_by_id('username')
    input_two = driver.find_element_by_id('password')
    
    input_first.send_keys('35318618')
    input_two.send_keys('09393X')

    driver.find_element_by_name('login').click()
    sleep(5)
    print(driver.current_url)
    driver.save_screenshot('jjj.png')
    driver.find_element_by_xpath('.//div[@class="el-scrollbar__view"]/li[4]/a').click()
    sleep(5)
    driver.switch_to.window(driver.window_handles[1])

    sleep(5)
    driver.get(driver.current_url)
    print(driver.current_url)
    wendu = driver.find_element_by_id('DQTW')
    wendu.clear()
    sleep(5)
    wendu_list = ['36.5', '36.3', '36.4', '36.6']
    tem = random.choices(wendu_list)
    wendu.send_keys(tem)
    sleep(8)
    banli = driver.find_element_by_xpath('//a[@class="submitbtn"]')
    banli.click()
    sleep(0.5)
    send_qq_email("打卡成功咯！", '<div>肖乐已打卡温度为：%s，请打开手机app查看<img src="https://api.pingping6.com/tools/acg3/index.php"></div>'%tem)
    # 关闭浏览器
    driver.quit()

#auto_dk()
#send_qq_email("打卡成功咯！", "肖乐已打卡，请打开手机app查看")
def time_data():
    nowTime = datetime.datetime.now().strftime('%H:%M:%S')
    hour=eval(nowTime.split(':')[0])
    if 1<hour<12:
        time_data = '12:03:24'
    elif 12<hour<20:
        time_data='19:03:30'
    else:
        time_data='00:03:12'
    return time_data


def main(time_date):

    while True:
        sleep(1)
        nowTime = datetime.datetime.now().strftime('%H:%M:%S')  # 现在
        # 早上打卡

        if nowTime == time_date:
            auto_dk()
            time_date='12:03:24'
        # 中午打卡
        elif nowTime == time_date:
            auto_dk()
            time_date='19:03:30'
        # 晚上打卡
        elif nowTime == time_date:
            auto_dk()
            time_date='00:03:30'
        else:
            print('\r当前时间'+nowTime+',打卡程序休眠状态',end='')

auto_dk()

# try:
#     time_date = time_data()
#     print(time_date + '\n')
#     main(time_date)
# except Exception as f:
#     print(f)
#     send_qq_email("打卡失败！!!", '<div>服务器崩溃<video poster="https://api.pingping6.com/tools/acg3/index.php"/></div>')
#     nowTime = datetime.datetime.now().strftime('%H:%M:%S').split(':')
#     if '0' in nowTime[1]:
#         num1=nowTime[1].replace('0','')
#     else:
#         num1=nowTime[1]
#
#     num=eval(num1)+10
#     nowTime[1]=str(num)
#     print(nowTime)
#     t=':'.join(nowTime)
#     main(t)
#
