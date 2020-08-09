# def menu():
#     a='*'*38
#     print(a)
#     print(' '*10+'学生管理系统v1.0')
#     print(' '*7+'【1】添加学生信息')
#     print(' '*7+'【2】删除学生信息')
#     print(' '*7+'【3】修改学生信息')
#     print(' '*7+'【4】显示所有学生信息')
#     print(' '*7+'【5】退出系统')
#     print(a)
# menu()
#  sr_name=input('请输入学生姓名：')
#     if sr_name  not in xs.keys():
#
#         xm_age=input('请输入学生年龄：')
#         xm_xb=input('请输入学生性别：')
#         xs[sr_name]=[xm_age,xm_xb]
#         print(xs)
#     else:
#         print('学生信息修改')
#
#         xm_aeg = input('请输入学生年龄：')
#         xm_bx = input('请输入学生性别：')
#         xs[sr_name] = [xm_aeg, xm_bx]
#         print(xs)
# #         删除学生信息：
# def sc():


##################################################################


# xs={'王一航':[20,'男'],'Stella':[20,'男'],'李星':[20,'女'],'王子航':[20,'男'],'夜凌云':[20,'男'],'龙建':[20,'男'],'晓婷':[20,'女'],}
#
# def xt():
#     a = '*' * 38
#     print(a)
#     print(' ' * 10 + '学生管理系统v1.0')
#     print(' ' * 7 + '【1】添加学生信息')
#     print(' '*7+'【2】删除学生信息')
#     print(' '*7+'【3】修改学生信息')
#     print(' '*7+'【4】显示所有学生信息')
#     print(' '*7+'【5】退出系统')
#     print(a)
#
#     sr_name = input('请输入学生姓名：')
#     if  sr_name not in xs.keys():
#         print('学生信息添加')
#
#         xm_age = input('请输入学生年龄：')
#         xm_xb=input('请输入学生性别：')
#         xs[sr_name]=[xm_age,xm_xb]
#         print(xs)
#     #=============学生信息删除===============
#     else:
#         print('学生信息删除')
#         sc_name=input('请输入要删除的学生姓名：')
#         if sc_name in xs:
#             del  xs[sr_name]
#         print(xs)
#
# xt()



#=============================================================
xs={'沸羊羊':[20,'男'],'懒洋洋':[5,'男'],'喜洋洋':[20,'女'],'暖洋洋':[20,'女'],'美洋洋':[20,'女'],'慢羊羊':[60,'男'],'机械羊':[20,'男']}


def meun():
    print('*' * 38)
    print(' ' * 10 + '学生管理系统v1.0')
    print(' ' * 7 + '【1】添加学生信息')
    print(' ' * 7 + '【2】删除学生信息')
    print(' ' * 7 + '【3】修改学生信息')
    print(' ' * 7 + '【4】显示所有学生信息')
    print(' ' * 7 + '【5】退出系统')
    print('*' * 38)




def add_name():
    print('添加学生信息')
    name_id=input('请输入学生姓名')
    if name_id in xs.keys():
        print('该生已存在')
    else:
        name_age=input('请输入学生年龄')
        name_xb=input('请输入学生性别')

        xs[name_id]=[name_age,name_xb]

        print(xs)





def xg_name():

    print('学生信息修改')
    name_id=input('请输入学生姓名')
    if name_id in xs.keys():
        print('该生已存在')
    else:
        id_name= input('请重新输入学生姓名')
        age_name = input('请输入学生年龄')
        xb_name = input('请输入学生性别')
        xs[id_name] = [age_name, xb_name]
        print(xs)


def sc_name():

        print('删除学生信息')
        sc_id=input('请输入学生姓名')
        if sc_id in xs.keys():
            del  xs[sc_id]
            print(xs)
        else:
            print('该学生不在名单')


def ever_name():

        xs.items()
        print(xs)





while True:
    def run():

        meun()
        stella=eval(input('请输入指令：'))
        if stella==1 :
            add_name()


        elif stella==2:
            sc_name()

        elif stella == 3:
            xg_name()

        elif stella==4:

            ever_name()
        elif stella==5:
            print('系统退出')
    run()