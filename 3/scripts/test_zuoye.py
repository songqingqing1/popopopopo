from appium import webdriver
import pytest
class Testtask:
    def setup(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'# 系统名
        desired_caps['platformVersion'] = '5.1'# 版本名
        desired_caps['deviceName'] = '192.168.56.101:5555'# 设备名
        # app信息
        desired_caps['appPackage'] = 'com.android.contacts'# 包名
        desired_caps['appActivity'] = '.activities.PeopleActivity'# 启动名
        # 下两条是获取中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # 数据参数化
    @pytest.mark.parametrize(('name','phone','remark','website'),[('曹焱兵','188888888','领导',''),                                    ('刘羽禅','','领导222','www.aa.com'),                               ('孙斩天','','','www.aa.com')])
    def test_task(self,name,phone,remark,website):
        # 点击新建联系人
        self.driver.find_element_by_id('com.android.contacts:id/floating_action_button').click()
        self.driver.find_element_by_xpath('//*[contains(@text,"本地保存")]').click()
        # 获取屏幕大小
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        start_x = width * 0.5
        start_y = height * 0.75
        end_x = width * 0.5
        end_y = height * 0.25
        while True:
            try:
                # 判断
                if name != '':
                    # 传入参数，姓名
                    self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]").send_keys(name)
                    break
                else:
                    break
            except Exception:
                self.driver.swipe(start_x, start_y, end_x, end_y, 5000)


        while True:
            try:
                if phone != '':
                    self.driver.find_element_by_xpath("//*[contains(@text,'电话')]").send_keys(phone)
                    break
                else:
                    break
            except Exception:
                self.driver.swipe(start_x, start_y, end_x, end_y, 5000)


        while True:
            try:
                if remark != '':
                    self.driver.find_element_by_xpath("//*[contains(@text,'备注')]").send_keys(remark)
                    break
                else:
                    break
            except Exception:
                self.driver.swipe(start_x, start_y, end_x, end_y, 5000)


        while True:
            try:
                if website != '':
                    self.driver.find_element_by_xpath("//*[contains(@text,'网站')]").send_keys(website)
                    break
                else:
                    break
            except Exception:
                self.driver.swipe(start_x, start_y, end_x, end_y, 5000)

    def teardown(self):
        # 点击返回保存联系人
        self.driver.find_element_by_class_name('android.widget.ImageButton').click()






