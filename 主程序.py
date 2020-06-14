# https://www.bilibili.com/read/cv234716/
数据样本 = [('5M',0.75),('5M',0.75),('5M',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),('500K',0.75),]
深空网功率 = '250G'
dict4数据列表 = {'Moho':6315765981,'Eve':9931011387,'Duna':21783189163,'Dres':46761053692,'Jool':72212238387,'Eeloo':113549713200}

def read读取信息并生成信息字典():
    fo = open("天线数据.csv")
    天线数据 = []
    for line in fo:
        line = line.replace("\n", "")
        天线数据.append(line.strip(","))
    fo.close()
    #print(天线数据)

    dict天线数据 = {}
    for i in 天线数据:
        i = i.split(",")
        #print(i)
        dict天线数据[i[0]] = i[2]
    #print(dict天线数据)
    return dict天线数据

def read2读取配置文件并生成配置字典():
    fo = open("配置文件.csv")
    配置数据 = []
    for line in fo:
        line = line.replace("\n", "")
        line = line.replace("\t", "")
        配置数据.append(line.strip(","))
    fo.close()
    #print(配置数据)

    dict配置数据 = {}
    for i in 配置数据:
        i = i.split(",")
        #print(i)
        dict配置数据[i[0]] = i[1]
    (dict配置数据)
    return dict配置数据

def 生成数据列表(list = 数据样本):
    x=1

def 对应函数(input = str , dict1 = read读取信息并生成信息字典()):
    output = dict1[input]
    return output

def 天线指数对应(atananame = str):
    if atananame == "Communotron 16":
        return 1
    if atananame == "Communotron 16-S":
        return 0
    else:
        return 0.75

def 生成主程序可用列表(dict = read2读取配置文件并生成配置字典()):
    list1 = []
    for i in dict:
        for o in range(eval(dict[i])):
            #print(i,"##",i[0:0])
            名称 = i
            功率 = 对应函数(名称)
            tub = (功率,天线指数对应(名称))
            #rint(tub)
            list1.append(tub)
    #print(list1)
    return list1


#----------------------------------------------------------------------------------------------------------
数据样本 = 生成主程序可用列表()
#print(数据样本)
#----------------------------------------------------------------------------------------------------------


def NumFormart(x=str):
    x = x.upper()
    if x[-1] == 'K':
        output = eval(x[0:-1]+"000")
    if x[-1] == 'M':
        output = eval(x[0:-1]+"000""000")
    if x[-1] == 'G':
        output = eval(x[0:-1]+"000""000""000")
    return output

def T天线功率总和计算(list = 数据样本):                     #输出 天线功率总和
    x = 0
    for i in list:
        x += NumFormart(i[0])
    return x

def Z最高功率天线功率(list= 数据样本):                        #输出 最高功率天线功率
    x = []
    for i in list:
        x.append(NumFormart(i[0]))
    最高功率天线功率 = x[x.index(max(x))]
    return 最高功率天线功率

def formulal2(天线功率总和 = T天线功率总和计算() ,list = 数据样本):               #输出 载具平均加权结合指数
    x = 0
    for i in list:
        x += NumFormart(i[0])*i[1]
    载具平均加权结合指数 = x/天线功率总和
    return 载具平均加权结合指数

def formula1(最高天线功率=Z最高功率天线功率(),天线功率总和=T天线功率总和计算(),载具平均加权结合指数 =formulal2())  :#输出 载具天线总功率
    x = 天线功率总和/最高天线功率
    y = pow(x,载具平均加权结合指数)
    载具天线总功率 = 最高天线功率 * y
    return 载具天线总功率

def formula3(载具天线总功率 , 深空网功率):
    最大传输距离 = pow((载具天线总功率 * 深空网功率),0.5)
    return 最大传输距离

def rel连接点相对距离(距离,最大连接距离):          #连接点相对距离
    x = 距离/最大连接距离
    z = 1 - x
    if z <= 0:
        return 0
    else:
        return z

def 信号强度(相对距离):                           #信号强度
    y = -2*pow(相对距离,3) + 3*pow(相对距离,2)
    return y

#print(T天线功率总和计算(),"T天线功率总和计算")

#print(Z最高功率天线功率(),"Z最高功率天线功率()")

#print(formulal2(T天线功率总和计算()),"载具平均加权结合指数")

#print(T天线功率总和计算()/Z最高功率天线功率())

#print(formula1(),"载具")
载具平均加权结合指数 = formulal2()
探测器总功率 = formula1()
最大连接距离 = formula3(formula1(Z最高功率天线功率(),T天线功率总和计算(),formulal2(T天线功率总和计算())),NumFormart(深空网功率))
print('载具平均加权结合指数{:,.2f}'.format(最大连接距离))
print('探测器总功率{:,.2f}'.format(最大连接距离))
print('最大连接距离为{:,.2f}m'.format(最大连接距离))
#print(rel连接点相对距离(距离=73400000000,最大连接距离=最大连接距离))
#print("信号强度{:,.2f}".format(信号强度(rel连接点相对距离(距离=73400000000,最大连接距离=最大连接距离))))
for i in dict4数据列表:
    far   = dict4数据列表[i] + 13599840256
    close = abs(dict4数据列表[i] - 13599840256)
    per = 信号强度(rel连接点相对距离(距离=close,最大连接距离=最大连接距离))
    print("预计信号强度  {}  MIN{:.2%}  MAX{:.2%}".format(i,信号强度(rel连接点相对距离(距离=far,最大连接距离=最大连接距离)),per))

input("按下Enter键关闭窗口")
