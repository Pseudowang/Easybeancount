from datetime import datetime, timedelta

Transaction = [ ] #Transaction list for storing income and expense entries

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
        else:
            open_books = choice_book + "-expenses" + ".bean"
            print("你目前正在编辑的是" + open_books + "账本")
            return open_books
            break #Exit the loop if the input is correct


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
    
def create_Transaction_data():
    #temp_tran is Temporary Transaction data

    choice_book() #Choose the bill
    chosen_date = choose_date() #Select the bill date
    payee = input("请输入支出的对象: ") 
    Narration = input("请输入支出的描述: ")
    print(chosen_date)

    selected_category = Create_Expenses_Entry() #Selected the Expenses Categorys
    amount = input("请输入支出的金额:(格式为12.00, 12.50) ")
    selected_assets = Create_Assets_Entry()

    temp_tran = f"{chosen_date} * \"{payee}\" \"{Narration}\" \n" #Beancoune Payee and Narration data 
    temp_tran += f"    {selected_category} " #Beancount Expenses Entry datas
    temp_tran += f"\t\t {amount} CNY\n" # Expenses Entry Amount
    temp_tran += f"    {selected_assets} \t\t -{amount} CNY\n" #Beancount中的第三行数据

    Transaction.append(temp_tran)
    print("交易记录已经添加成功!!!")
    print(temp_tran)
    return Transaction


    

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
        return cate_choices_print(Expenses_Categories_Home)
        
    elif Cate_Choice == "2":
        return cate_choices_print(Expenses_Categories_Relationship)

    elif Cate_Choice == "3":
        return cate_choices_print(Expenses_Categories_Shopping)

    elif Cate_Choice == "4":
        return cate_choices_print(Expenses_Categories_Food)

    elif Cate_Choice == "5":
        return cate_choices_print(Expenses_Categories_Health)
    
    elif Cate_Choice == "6":
        return cate_choices_print(Expenses_Categories_Entertainment)

    elif Cate_Choice == "7":
        return cate_choices_print(Expenses_Categories_Transport)

    elif Cate_Choice == "8":
        return cate_choices_print(Expenses_Categories_Government)
    
    elif Cate_Choice == "9":
        return cate_choices_print(Expenses_Categories_Invest)
        
    else:
        print("请输入正确的数字")

def Create_Assets_Entry():
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


# chosen_date = choose_date()
# print(chosen_date)

def create_book(): # Create a new book
    print("功能开发中...")
    # book_name = input("请输入账本名称: ")
    # book = open(book_name + ".bean", "w")

def add_expenses(): # Add expenses
    create_Transaction_data()

def view_records(): # View records
    print("所有记录")
    for record in Transaction:
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
        add_expenses()

    if choice_temp == 3:
        add_income()

    if choice_temp == 4:
        view_records()

    if choice_temp == 5:
        # bookfilename = choice_book()
        filename = input("请输入文件名: ")
        save_records(Transaction, filename)
        print(f"记录已保存到 {filename}")

    if choice_temp == 6:
        print("感谢您的使用，再见！")
        exit()

    if choice_temp == 0:
        Create_Assets_Entry() 
