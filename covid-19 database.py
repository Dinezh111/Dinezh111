
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="050339",
    database="covid_19_database_information"
    )

mycursor=mydb.cursor()
mycursor.execute("create database covid_19_database_information")
print("created college database in my sql")

mycursor=mydb.cursor()
def insert_covid_global_cases():
    sql="insert into covid_global_cases(country,total_cases) values (%s,%s)"
    country=input("enter country name:")
    total_cases=int(input("enter total_cases:"))
    val=(country,total_cases)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data inserted successfully")
def view_covid_global_cases():
    mycursor.execute("SELECT * FROM covid_global_cases")
    result=mycursor.fetchall()
    for i in result:
       print(i)
def insert_vaccination_data():
    sql="insert into vaccination_data (name,age,vaccine) values(%s,%s,%s)"
    name=input("enter your name:")
    age=int(input("enter your age:"))
    vaccine=int(input("enter your vaccine details:"))
    val=(name,age,vaccine)
    mycursor.execute(sql,val)
    mydb.commit()
    print("vaccination data inserted successfully:")
def view_vaccinaton_data():
    mycursor.execute("SELECT * FROM vaccination_data")
    result=mycursor.fetchall()
    for i in result:
       print(i)
def insert_quarantine_members_data():
    sql="insert into quarantine_members_data(name,age,address,quarantine_days) values(%s,%s,%s,%s)"
    name=input("enter your name:")
    age=int(input("enter your age:"))
    address=input("enter your address:")
    quarantine_days=int(input("enter quarantine details:"))
    val=(name,age,address,quarantine_days)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data uploaded succuessfully")
def view_quarantine_members_data():
    mycursor.execute("select * from quarantine_members_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
def insert_non_vaccination_members():
    sql="insert into non_vaccination_members(name,age,address) values(%s,%s,%s)"
    name=input("enter your name:")
    age=int(input("enter your age:"))
    address=input("enter your address:")
    val=(name,age,address)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data uploaded successfully")
def view_non_vaccination_members():
    mycursor.execute("SELECT * FROM non_vaccination_members")
    result=mycursor.fetchall()
    for i in result:
       print(i)
def insert_covid_death_cases():
   sql="insert into covid_death_cases(name,age,monthly_death_list,total_death_list) value(%s,%s,%s,%s)"
   name=input("enter your name:")
   age=int(input("enter your age:"))
   monthly_death_list=int(input("enter monthly death list:"))
   total_death_list=int(input("enter total death list:"))
   val=(name,age,monthly_death_list,total_death_list)
   mycursor.execute(sql,val)
   mydb.commit()
   print("data entered successfully")
def view_covid_death_cases():
   mycursor.execute("SELECT * FROM covid_death_cases")
   result=mycursor.fetchall()
   for i in result:
       print(i)       
print("1->insert_covid_global_cases") 
print("2->view_covid_global_cases")
print("3->insert_vaccination_data")
print("4->view_vaccination_data")
print("5->insert_quarantine_members_data")
print("6->view_quarantine_members_data")
print("7->insert non_vaccination_members")
print("8->view non_vaccinatoin_members")
print("9->enter_covid_death_cases")
print("10->view_covid_death_cases")
try:
   user=int(input("enter the number:"))
   if user==1:
    insert_covid_global_cases()
   elif user==2:
    view_covid_global_cases()
   elif user==3:
    insert_vaccination_data()
   elif user==4:
    view_vaccinaton_data()
   elif user==5:
    insert_quarantine_members_data()
   elif user==6:
    view_quarantine_members_data()
   elif user==7:
    insert_non_vaccination_members()
   elif user==8:
    view_non_vaccination_members()
   elif user==9:
    insert_covid_death_cases()
   elif user==10:
    view_covid_death_cases()
   else:
    print("data not found")
except:
    print("enter numbers only")