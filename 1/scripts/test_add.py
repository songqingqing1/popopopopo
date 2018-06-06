import time
from appium import webdriver
import pytest
#首先是前置代码
class Test_address:
    """前置代码木有问题"""
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 点击增加联系人按钮
    #参数化
    #第一次张三的信息添加备注有时会定位错误
    @pytest.mark.parametrize(("name", "phone", "remark","webok")
        ,[("田馥甄","18810731890", "小姐姐",""),("金高银","","大姐姐","ithema"),("","","","itcast")])
    def test_add_linkman(self,name,phone,remark,webok):
        driver = self.driver
        start_location = driver.get_window_size()["width"]
        print(driver.get_window_size())
        start_location2 = driver.get_window_size()["height"]
        start_x = start_location * 0.5
        end_x = start_x
        start_y = start_location2 * 0.75
        end_y = start_location2 * 0.25
        driver.find_element_by_id('com.android.contacts:id/floating_action_button').click()
        driver.find_element_by_xpath('//*[contains(@text,"本地保存")]').click()
        #不能用is not None
        while True:
            try:
                if name != '':
                    driver.find_element_by_xpath('//*[contains(@text,"姓名")]').send_keys(name)
                else:
                    break
                break
            except Exception:
                driver.swipe(start_x,start_y,end_x,end_y,5000)
        while True:
            try:
                if phone != '':
                    driver.find_element_by_xpath('//*[contains(@text,"电话")]').send_keys(phone)
                else:
                    break
                break
            except Exception:
                driver.swipe(start_x,start_y,end_x,end_y,5000)
        while True:
            try:
                if remark != '':
                    driver.find_element_by_xpath('//*[contains(@text,"备注")]').send_keys(remark)
                else:
                    break
                break
            except Exception:
                driver.swipe(start_x,start_y,end_x,end_y,7000)
        while True:
            try:
                if webok != '':
                    driver.find_element_by_xpath('//*[contains(@text,"网站")]').send_keys(webok)
                else:
                    break
                break
            except Exception:
                driver.swipe(start_x,start_y,end_x,end_y,5000)
    def teardown(self):
        """不能自动保存，需要加关闭"""
        # self.driver.find_element_by_class_name('android.widget.ImageButton').click()
        self.driver.keyevent(4)

        #1
        #2
        #3

