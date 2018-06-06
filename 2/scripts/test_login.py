import pytest
from appium import webdriver
# from data.data1 import Data  #我使用这：在命令行就报错  右键就可以使用

# 有时间的话老师帮我看一下issue.py

def data():
    return [("张三", "18503030303", "领导", " "), \
            ("李四", " ", "领导222", "www.itcast.com"), \
            ("王五", " ", " ", "www.itcast.com")]

class TestLogin():

    def setup(self):
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app的信息com.android.contacts/.activities.PeopleActivity
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        #解决中文输入问题
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        #进入保存联系人页面
        self.driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'本地保存')]").click()

    def teardown(self):
            self.driver.keyevent(4)
            self.driver.close_app()

    #参数化   导入data.py中的数据
    @pytest.mark.parametrize(("name", "phone", "remark", "web"),data())
    def test_login(self, name, phone, remark, web):

        #判断数据是否为空， 不为空：搜索定位并输入数据
        if name != ' ':
            while True:
                try:
                    self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]").send_keys(name)
                    break
                except Exception:
                    self.driver.swipe(100, 2000, 100, 1000, 5000)

        if phone != ' ':
            while True:
                try:
                    self.driver.find_element_by_xpath("//*[contains(@text,'电话')]").send_keys(phone)
                    break
                except Exception:
                    self.driver.swipe(100, 2000, 100, 1000, 5000)

        if remark != ' ':
            while True:
                try:
                    self.driver.find_element_by_xpath("//*[contains(@text,'备注')]").send_keys(remark)
                    break
                except Exception:
                    self.driver.swipe(100, 2000, 100, 1000, 5000)

        if web != ' ':
            while True:
                try:
                    self.driver.find_element_by_xpath("//*[contains(@text,'网站')]").send_keys(web)
                    break
                except Exception:
                    self.driver.swipe(100, 2000, 100, 1000, 5000)

if __name__ == '__main__':
    pytest.main(["-s","test_login.py"])