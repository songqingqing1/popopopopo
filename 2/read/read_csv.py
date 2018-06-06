import csv
class Csvdata():
    def data(self):

        with open('../data/text.csv','r',encoding='utf-8') as f:
            lines = csv.reader(f)
            list = []
            for x in lines:
                list.append(x)
            return list[1:]

if __name__ == '__main__':
    print(Csvdata().data()[0])

