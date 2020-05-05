import records
import matplotlib.pyplot as plt


class Opera_Database(object):
    def __init__(self, url):
        self.url = url

    def Connect(self):
        return records.Database(self.url)

    def Query(self, query, operation=1):
        database = self.Connect().get_connection()
        if operation == 1:
            return database.query(query).as_dict()
        if operation == 2:
            return database.query(query)

    def Table_name(self):
        return self.Connect().get_table_names()

    def Check_Table(self, table_name):
        query = 'select * from %s' % table_name
        return self.Query(query, 2).dataset

    def Count_Table(self):
        return len(self.Table_name())


class Data_Analysis(object):
    def __init__(self, dataset):
        self.dataset = dataset

    def Count_Table_Item(self):
        return len(self.dataset)

    def Show_data(self):
        return self.dataset

    def Distribution(self, attr):
        dis = {}
        for row in self.dataset:
            # print(row[attr])
            if row[attr] not in dis:
                dis[row[attr]] = 1
            else:
                dis[row[attr]] += 1
        return dis


class Result_visualization(object):
    def __init__(self, plt_x, plt_label, plt_title):
        self.x = plt_x
        self.label = plt_label
        self.title = plt_title

    def X(self):
        x_axis = []
        for item in self.x:
            x_axis.append(self.x[item])
        return x_axis

    def Pie(self):
        plt.pie(self.X(), labels=self.label, autopct='%1.2f%%')
        plt.title(self.title)
        plt.show()
        return

    def Bar(self):
        plt.bar(range(len(self.X())), self.X(), tick_label=label)
        plt.title(self.title)
        plt.show()
        return


db = Opera_Database('sqlite:///myproject-dev.sqlite3')
result = db.Query('select * from users')
# for i in rows:
#     print(i)
print(db.Table_name())
# print(db.Check_Table('users'))
Tool = Data_Analysis(result)
Tool.Show_data()
# print(Tool.Distribution('role_id'))
# print(list(Tool.Distribution('role_id')))
# dic = {1: 1, 2: 2}
#
# dic.keys()
x = Tool.Distribution('role_id')
label = ['Manager', 'Host', 'Waiter', 'Kitchen', 'Busboy']
title = 'Test'
v = Result_visualization(x, label, title)
v.Pie()
v.Bar()
# x = []
# for item in Tool.Distribution('role_id'):
#     print(Tool.Distribution('role_id')[item])
