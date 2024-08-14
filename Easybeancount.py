from datetime import datetime, timedelta

expenses_tran = [ ] #Transaction list for storing expense entries
income_tran = [ ] #Transaction list for storing income entries

def get_current_time(): # Get the current time
    now = datetime.now() 
    current_time = now.strftime("%Y-%m-%d") #格式化时间
    return current_time

def choice_book(): #Chose The Book
    try_times = 0
    while try_times < 3 : #Up to three attempts
        choice_book = input("请输入你要编写几月份的账本(请务必输入08, 09):")
        if len(choice_book) != 2 or not choice_book.isdigit() or not ("01" <= choice_book <= "12"): #判断输入的月份是否正确
            print("请输入正确的月份!!!!(范围为01 - 12)")
            try_times += 1

        #If you have multiple income book, you can cancel the comment of the following code
        # elif legder_selection == 2: 
        else:
            open_books = choice_book + "-expenses" + ".bean"
            print("你目前正在编辑的是" + open_books + "账本")
            return open_books
            break #Exit the loop if the input is correct

        # Because I only hava one income book, so I don't need to choose the income book
        # elif legder_selection == 3:
        #     open_books = choice_book + "-income" + ".bean"
        #     print("你目前正在编辑的是" + open_books + "账本")
        #     return open_books
        #     break #Exit the loop if the input is correct

        # else:
        #     print("请输入正确的数字")
        #     try_times += 1


def get_previous_dates(current_date, num_days): #Get the previous 9 days
    dates = [ ]
    for i in range(num_days):
        data = current_date - timedelta(days=i) #时间差
        dates.append(data.strftime("%Y-%m-%d")) #格式化时间
    return dates

def choose_date(): #Select the bill date
    current_date = datetime.now()
    bill_dates = get_previous_dates(current_date, 9)

    print("以下是过去9天的日期:")
    for i, date in enumerate(bill_dates): #Print the index and data of `bill_dates` together and assign them to `i` and `date`
        print(f"{i + 1}. {date}") #Print the index + 1 and the date
    print("0. 自行输入日期")

    while True:
        date_sel = input("请选择日期: (回车默认当天日期)")
        if date_sel == "": #If the input is empty, the current date is selected
            selected_date = current_date.strftime("%Y-%m-%d")
            break
        elif date_sel.isdigit() and 1 <= int(date_sel) <= len(bill_dates):
            selected_date = bill_dates[int(date_sel) - 1]
            break
        elif date_sel == "0":
            print("上面没有你想要的日期，请自行输入，格式为(2024-08-01)")
        else:
            print("请输入正确的日期")
    print(f"你选择的日期是: {selected_date}")
    return selected_date

def expenses_cate_sel(input_ex_cate):
    for i, category in enumerate(input_ex_cate): #Print the index and data of `input_ex_cate` together and assign them to `i` and `category`
        print(f"{i+1}. {category}")

    choice = input("请选择支出的类别: ")

    try:
        Expenses_Choice = int(choice)
    except ValueError:
        print("请输入正确的数字")
        return None
    

    if 1 <= Expenses_Choice <= len(input_ex_cate):
        Selected_Category = input_ex_cate[int(Expenses_Choice) - 1] #index start from 0
        return Selected_Category
    else:
        print("请输入正确的数字")
        return None

def cate_choices_print(input_ex_cate):
    selected_category = expenses_cate_sel(input_ex_cate) #Get the index number of the selected category
    print(f"你选择的支出类别是: {selected_category}")
    return selected_category
    
def create_expenses_transaction():
    #temp_tran is Temporary Transaction data

    choice_book() #Choose the bill
    chosen_date = choose_date() #Select the bill date
    payee = input("请输入支出的对象: ") 
    Narration = input("请输入支出的描述: ")
    print(chosen_date)

    selected_category = create_expenses_entry() #Selected the Expenses Categorys
    amount = input("请输入支出的金额:(格式为12.00, 12.50) ")
    selected_assets = create_assets_entry()

    temp_tran = f"{chosen_date} * \"{payee}\" \"{Narration}\" \n" #Beancoune Payee and Narration data 
    temp_tran += f"    {selected_category} " #Beancount Expenses Entry datas
    temp_tran += f"\t\t {amount} CNY\n" # Expenses Entry Amount
    temp_tran += f"    {selected_assets} \t\t -{amount} CNY\n" #Beancount中的第三行数据

    expenses_tran.append(temp_tran)
    print("交易记录已经添加成功!!!")
    print(temp_tran)
    return expenses_tran

def create_income_transaction():
    open_books = "income.bean"
    print(f"你目前正在编辑的是{open_books}账本")
    chosen_date = choose_date()
    payee = input("请输入收入的对象: ")
    Narration = input("请输入收入的描述: ")
    print(chosen_date)

    selected_category = create_income_entry()
    amount = input("请输入收入的金额:(格式为12.00, 12.50) ")
    selected_assets = create_assets_entry()

    temp_tran = f"{chosen_date} * \"{payee}\" \"{Narration}\" \n"
    temp_tran += f"    {selected_category} "
    temp_tran += f"\t\t -{amount} CNY\n"
    temp_tran += f"    {selected_assets} \t\t {amount} CNY\n"

    income_tran.append(temp_tran)
    print("交易记录已经添加成功!!!")
    print(temp_tran)
    return income_tran




def create_expenses_entry():
    expenses_categories_home = [
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

    expenses_categories_relationship = [
        "Expenses:Relationship:Gift",
        "Expenses:Relationship:Relative",
        "Expenses:Relationship:PrePayment",
        "Expenses:Relationship:FilialPiety",
        "Expenses:Relationship:RedEnvelope",
        "Expenses:Relationship:Other",
    ]

    expenses_categories_shopping = [
        "Expenses:Shopping:Clothing",
        "Expenses:Shopping:Digital",
        "Expenses:Shopping:Home",
        "Expenses:Shopping:Book",
        "Expenses:Shopping:Makeup",
        "Expenses:Shopping:Household-Items",
        "Expenses:Shopping:Sports",
        "Expenses:Shopping:Other",
    ]

    expenses_categories_food = [
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

    expenses_categories_health = [
        "Expenses:Health:Outpatient",
        "Expenses:Health:Medical",
        "Expenses:Health:Examination",
        "Expenses:Health:Other",
    ]

    expenses_categories_entertainment = [
        "Expenses:Entertainment:Movie",
        "Expenses:Entertainment:Travel",
        "Expenses:Entertainment:Hotel",
        "Expenses:Entertainment:Media",
        "Expenses:Entertainment:Show",
        "Expenses:Entertainment:Games",
        "Expenses:Entertainment:Subscription",
        "Expenses:Entertainment:Other"
    ]

    expenses_categories_transport = [
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

    expenses_categories_government = [  
        "Expenses:Government:Pension",
        "Expenses:Government:Unemployment",
        "Expenses:Government:Medical",
        "Expenses:Government:Injury",
        "Expenses:Government:Maternity",
        "Expenses:Government:IncomeTax",
        "Expenses:Government:Customs",
        "Expenses:Government:Other",
    ]

    expenses_categories_invest = [
        "Expenses:Invest:Dev",
        "Expenses:Invest:Study",
        "Expenses:Invest:Portfolio:Interest",
        "Expenses:Invest:Cost",
        "Expenses:Invest:Other",
    ]    

    Cate_Choice = input("1. 居家\n2. 人际\n3. 购物\n4. 餐饮\n5. 健康\n6. 娱乐\n7. 交通\n8. 税\n9. 投资\n")
    if Cate_Choice == "1":
        return cate_choices_print(expenses_categories_home)
        
    elif Cate_Choice == "2":
        return cate_choices_print(expenses_categories_relationship)

    elif Cate_Choice == "3":
        return cate_choices_print(expenses_categories_shopping)

    elif Cate_Choice == "4":
        return cate_choices_print(expenses_categories_food)

    elif Cate_Choice == "5":
        return cate_choices_print(expenses_categories_health)
    
    elif Cate_Choice == "6":
        return cate_choices_print(expenses_categories_entertainment)

    elif Cate_Choice == "7":
        return cate_choices_print(expenses_categories_transport)

    elif Cate_Choice == "8":
        return cate_choices_print(expenses_categories_government)
    
    elif Cate_Choice == "9":
        return cate_choices_print(expenses_categories_invest)
        
    else:
        print("请输入正确的数字")

def create_income_entry():
    income_categories = [
        "Income:CN:Salary:XYZ",
        "Income:CN:Salary:MUJI",
        "Income:CN:RedEnvelope",
        "Income:CN:Allowance",
        "Income:CN:School",
        "Income:CN:Tip",
        "Income:PassiveIncome:Project",
        "Income:PassiveIncome:Invest",
        "Income:PassiveIncome:Other",
        "Income:CN:Extra",
        "Income:CN:Rebate",
        "Income:CN:Invest",
        "Income:CN:Compensation",
        "Income:CN:Sales",
        "Income:CN:Other",
    ]
    selected_income = expenses_cate_sel(income_categories)
    print(f"你选择的收入类别是: {selected_income}")
    return selected_income

def create_assets_entry():
    Assets_Categories = [
        "Assets:DebitCard:CN:PINGAN-6479",
        "Assets:DebitCard:CN:ICBC-6641",
        "Assets:DebitCard:CN:ABC-1273",
        "Assets:Alipay:Balance",
        "Assets:Cash:CN",
        "Assets:Alipay:JA",
        "Assets:Alipay:ETF",
        "Assets:WeChat:Balance",
        "Assets:WeChat:ETF",
        "Assets:School:CampusCard",
        "Assets:AliCloud",
        "Assets:TencentCloud",
    ]
    selected_assets = expenses_cate_sel(Assets_Categories)
    print(f"你选择的资产类别是: {selected_assets}")
    return selected_assets



def create_book(): # Create a new book
    print("功能开发中...")
    # book_name = input("请输入账本名称: ")
    # book = open(book_name + ".bean", "w")

def add_expenses(): # Add expenses
    create_expenses_transaction()

def add_income(): # Add income
    create_income_transaction()

def view_records(): # View records
    print("所有的支出记录")
    for record in expenses_tran:
        print(record)

    print("所有的收入记录")
    for record in income_tran:
        print(record)

def save_records(records, filename):
    with open(filename, "a", encoding='utf-8') as file:
        for record in records:
            file.write(record + '\n')

while True:

    print ( "Welcome To The Easybeancount Program\n" + "现在的时间是: " + get_current_time())
    choice_temp = int(input(
        "请输入您的选择:\n 1.创建账本\n 2.添加支出\n 3.添加收入\n 4.查看已编辑好的记录\n 5.将刚刚编写好的记录保存\n 6.退出\n"
        ))

    if choice_temp == 1:
        create_book()

    if choice_temp == 2:
        legder_selection = 2
        add_expenses()

    if choice_temp == 3:
        legder_selection = 3
        add_income()

    if choice_temp == 4:
        view_records()

    if choice_temp == 5:
        type_selection = int(input("请选择要保存的类型(1.支出 2.收入): "))
        if type_selection == 1:
            filename = choice_book()
            save_records(expenses_tran, filename)
            print(f"记录已保存到 {filename}")

        elif type_selection == 2:
            filename = "income.bean"
            save_records(income_tran, filename)
            print(f"记录已保存到 {filename}")

        else:
            print("请输入正确的数字")
        # filename = input("请输入文件名: ")
        # save_records(expenses_tran, filename)
        # print(f"记录已保存到 {filename}")

    if choice_temp == 6:
        print("感谢您的使用，再见！")
        exit()

    if choice_temp == 0:
        create_assets_entry() 
