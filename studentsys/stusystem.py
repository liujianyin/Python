def main():
    while True:
        menu()
        choice = int(input('----请选择-----'))
        if choice==0:
            answer=input('确认需要退出系统吗?(Y/N)')
            if answer=='Y' or answer=='y':
                print('您已经退出系统，欢迎下次使用')
                break
                exit(0)
        elif choice==1:
            insert()
        elif choice==2:
            search()
        elif choice==3:
            delete()
        elif choice==4:
            update()
        elif choice==5:
            sort()
        elif choice==6:
            total()
        elif choice==7:
            show()
        else:
            print('输入合法字符')
def menu():
    print('==========================学生信息管理系统==================')
    print('---------------------------功能菜单-----------------')
    print('\t\t\t\t\t\t1、录入学生信息')
    print('\t\t\t\t\t\t2、查找学生信息')
    print('\t\t\t\t\t\t3、删除学生信息')
    print('\t\t\t\t\t\t4、修改学生信息')
    print('\t\t\t\t\t\t5、排序')
    print('\t\t\t\t\t\t6、统计学生总人数')
    print('\t\t\t\t\t\t7、显示所有学生信息')
    print('\t\t\t\t\t\t0、退出系统')
    print('------------------------')

def insert():
    id=input('请输入id')
    name=input('请输入姓名')
    eglishscore=input('请输入英语成绩')
    pythonscore = input('请输入python成绩')
    phpscore = input('请输入php成绩')
    studet_dic= {'id':id,'name':name,'eglishscore':eglishscore,'pythonscore':pythonscore,'phpscore':phpscore}
    with open("stu.txt", "a") as f:
        f.write(str(studet_dic)+'\n')
    choice=input('是否继续录入（Y/N）')
    if choice == 'Y' or choice == 'y':
       insert()
    else:
        print('学生信息录入完毕')
        menu()

def delete():
    condition=input('请输入要删除的学生id')
    with open('stu.txt', 'r') as f:
        stu_list= f.readlines()
    for i in stu_list:
        stu_dic=eval(i)
        for item in list(stu_dic):
            if(item=='id' and stu_dic.get(item)==condition):
               del stu_dic

    print(stu_list)









main()






