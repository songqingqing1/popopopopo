#要保存联系人的数据
class Data():
    def data(self):
        return [("张三", "18503030303", "领导", " "),\
               ("李四", " ", "领导222","www.itcast.com"),\
               ("王五", " ", " ", "www.itcast.com")]

if __name__ == '__main__':
    print(Data().data())