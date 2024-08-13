from datetime import datetime, timedelta

def get_current_time(): # Get the current time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d") #格式化时间
    return current_time

def choice_book():
    try_times = 0
    while try_times < 3 :
        choice_book = input("请输入你要编写几月份的账本(请务必输入08, 09):")
        if len(choice_book) != 2 or not choice_book.isdigit() or not ("01" <= choice_book <= "12"):
            print("请输入正确的月份!!!!(范围为01 - 12)")
            try_times += 1
        else:
            open_books = choice_book + "-expenses" + ".bean"
            print("你目前正在编辑的是" + open_books + "账本")
            break #输入正确 跳出循环


def get_previous_dates(current_date, num_days=7):
    dates = [ ]
    for i in range(num_days):
        data = current_date - timedelta(days=i) #时间差
        dates.append(data.strftime("%Y-%m-%d")) #格式化时间
    return dates

def choose_date():
    current_date = datetime.now()
    dates = get_previous_dates(current_date, 9)

    print("以下是过去9天的日期:")
    for i, date in enumerate(dates): #将datas的索引和数据一起打印出来,并赋值给i 和 date
        print(f"{i + 1}. {date}") #打印出来的是索引+1 和 数据
    print("0. 自行输入日期")

    while True:
        choice = input("请选择日期: (回车默认当天日期)")
        if choice == "":
            selected_date = current_date.strftime("%Y-%m-%d")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(dates):
            selected_date = dates[int(choice) - 1]
            break
        elif choice == "0":
            print("上面没有你想要的日期，请自行输入，格式为(2024-08-01)")
        else:
            print("请输入正确的日期")
    print(f"你选择的日期是: {selected_date}")
    return selected_date

def create_Transaction_data():
    Transaction = [ ] #Beancount中的第一行数据
    choice_book() #选择账本
    chosen_date = choose_date() #选择日期
    payee = input("请输入支出的对象: ") 
    Narration = input("请输入支出的描述: ")
    print(chosen_date)
    Transaction = f"{chosen_date} * \"{payee}\" \"{Narration}\" \n" #Beancount中的第一行数据 
    selected_category = Create_Expenses_Entry()
    Transaction += f"    {selected_category} " #Beancount中的第二行数据,开头空4个空格
    amount = input("请输入支出的金额:(格式为12.00, 12.50) ")
    Transaction += f"\t\t {amount} CNY\n" #Beancount中的第二行数据


    print(Transaction)

def Category_Choice(Input_Categories):
    for i, category in enumerate(Input_Categories):
        print(f"{i+1}. {category}")

    choice = input("请选择支出的类别: ")

    try:
        Expenses_Choice = int(choice)
    except ValueError:
        print("请输入正确的数字")
        return None
    

    if 1 <= Expenses_Choice <= len(Input_Categories):
        Selected_Category = Input_Categories[int(Expenses_Choice) - 1]
        #print(f"你选择的支出类别是: {Selected_Category}")
        return Selected_Category
    else:
        print("请输入正确的数字")
        return None

    

def Create_Expenses_Entry():
    Expenses_Categories_Home = [
        "Expenses:Home:Phone",
        "Expenses:Home:SDRQ",
        "Expenses:Home:Washer",
        "Expenses:Home:Haircut",
        "Expenses:Home:Delivery",
        "Expenses:Home:Omission",
        "Expenses:Home:Grocery",
        "Expenses:Home:Other",
        "Expenses:Home:Mortgage:Loan:Interest",
        "Expenses:Home:Insurance:ZJX",
        "Expenses:Home:Insurance:SX:MDW",
        "Expenses:Home:Insurance:YWX:MDW",
        "Expenses:Home:Insurance:YLX:ZFB",
        "Expenses:Home:Insurance:CCX",
        "Expenses:Home:WYF",
    ]

    Expenses_Categories_Relationship = [
        "Expenses:Relationship:Gift",
        "Expenses:Relationship:Relative",
        "Expenses:Relationship:PrePayment",
        "Expenses:Relationship:FilialPiety",
        "Expenses:Relationship:RedEnvelope",
        "Expenses:Relationship:Other",
    ]

    Expenses_Categories_Shopping = [
        "Expenses:Shopping:Clothing",
        "Expenses:Shopping:Digital",
        "Expenses:Shopping:Home",
        "Expenses:Shopping:Book",
        "Expenses:Shopping:Makeup",
        "Expenses:Shopping:Household-Items",
        "Expenses:Shopping:Sports",
        "Expenses:Shopping:Other",
    ]

    Expenses_Categories_Food = [
        "Expenses:Food:Breakfast",
        "Expenses:Food:Lunch",
        "Expenses:Food:Dinner",
        "Expenses:Food:DrinkFruit",
        "Expenses:Food:Vegetables",
        "Expenses:Food:Invite",
        "Expenses:Food:Omission",
        "Expenses:Food:Other",
        "Expenses:Food:Snack",
    ]

    Expenses_Categories_Health = [
        "Expenses:Health:Outpatient",
        "Expenses:Health:Medical",
        "Expenses:Health:Examination",
        "Expenses:Health:Other",
    ]

    Expenses_Categories_Entertainment = [
        "Expenses:Entertainment:Movie",
        "Expenses:Entertainment:Travel",
        "Expenses:Entertainment:Hotel",
        "Expenses:Entertainment:Media",
        "Expenses:Entertainment:Show",
        "Expenses:Entertainment:Games",
        "Expenses:Entertainment:Subscription",
        "Expenses:Entertainment:Other"
    ]

    Expenses_Categories_Transport = [
        "Expenses:Transport:Airline",
        "Expenses:Transport:Railway",
        "Expenses:Transport:TAXI",
        "Expenses:Transport:Mass-transit",
        "Expenses:Transport:Bike-Sharing",
        "Expenses:Transport:Car:Rent",
        "Expenses:Transport:Car:Oil",
        "Expenses:Transport:Car:Tolls",
        "Expenses:Transport:Car:Maintenance",
        "Expenses:Transport:Car:Insurance",
        "Expenses:Transport:Car:Parking",
        "Expenses:Transport:Car:Wash",
        "Expenses:Transport:Other",
    ]

    Expenses_Categories_Government = [  
        "Expenses:Government:Pension",
        "Expenses:Government:Unemployment",
        "Expenses:Government:Medical",
        "Expenses:Government:Injury",
        "Expenses:Government:Maternity",
        "Expenses:Government:IncomeTax",
        "Expenses:Government:Customs",
        "Expenses:Government:Other",
    ]

    Expenses_Categories_Invest = [
        "Expenses:Invest:Dev",
        "Expenses:Invest:Study",
        "Expenses:Invest:Portfolio:Interest",
        "Expenses:Invest:Cost",
        "Expenses:Invest:Other",
    ]    

    Cate_Choice = input("1. 居家\n2. 人际\n3. 购物\n4. 餐饮\n5. 健康\n6. 娱乐\n7. 交通\n8. 税\n9. 投资\n")
    if Cate_Choice == "1":
        # Category_Choice(Expenses_Categories_Home)
        selected_category = Category_Choice(Expenses_Categories_Home)
        print(f"你选择的支出类别是: {selected_category}")
        return selected_category
        

    elif Cate_Choice == "2":
        selected_category = Category_Choice(Expenses_Categories_Relationship)
        print(f"你选择的支出类别是: {selected_category}")
        return selected_category

    elif Cate_Choice == "3":
        selected_category = Category_Choice(Expenses_Categories_Shopping)
        print(f"你选择的支出类别是: {selected_category}")
        return selected_category

    elif Cate_Choice == "4":
        selected_category = Category_Choice(Expenses_Categories_Food)
        print(f"你选择的支出类别是: {selected_category}") 
        return selected_category

    elif Cate_Choice == "5":
        selected_category = Category_Choice(Expenses_Categories_Health)
        print(f"你选择的支出类别是: {selected_category}")
        return selected_category
    
    elif Cate_Choice == "6":
        selected_category = Category_Choice(Expenses_Categories_Entertainment)
        print(f"你选择的支出类别是: {selected_category}") 
        return selected_category

    elif Cate_Choice == "7":
        selected_category = Category_Choice(Expenses_Categories_Transport)
        print(f"你选择的支出类别是: {selected_category}")
        return selected_category

    elif Cate_Choice == "8":
        selected_category = Category_Choice(Expenses_Categories_Government)
        print(f"你选择的支出类别是: {selected_category}")
        return selected_category
    
    elif Cate_Choice == "9":
        selected_category = Category_Choice(Expenses_Categories_Invest)
        print(f"你选择的支出类别是: {selected_category}")
        return selected_category
        
    else:
        print("请输入正确的数字")

def Create_Assets_Entry():
    

# chosen_date = choose_date()
# print(chosen_date)

def create_book(): # Create a new book
    print("功能开发中...")
    # book_name = input("请输入账本名称: ")
    # book = open(book_name + ".bean", "w")

def add_expenses(): # Add expenses
    create_Transaction_data()


print ("\n" + "Welcome To The Easybeancount Program\n" + "现在的时间是: " + get_current_time())
choice_temp = int(input(
    "请输入您的选择:\n 1.创建账本\n 2.添加支出\n 3.添加收入\n 4.查看已编辑好的记录\n 5.将刚刚编写好的记录保存\n 6.退出\n"
    ))

if choice_temp == 1:
    create_book()

if choice_temp == 2:
    add_expenses()

if choice_temp == 3:
    add_income()

if choice_temp == 4:
    view_records()

if choice_temp == 5:
    save_records()

if choice_temp == 6:
    print("感谢您的使用，再见！")
    exit()
if choice_temp == 0:
    Create_Expenses_Entry()