import mysql.connector as mysql
import getpass as gp
p=gp.getpass("\n Your MySQL Password::")
con =mysql.connect(host="127.0.0.1",user="root",passwd=p)
cur = con.cursor()

def makeTables():
   cur.execute("create database ATM_management;")
   cur.execute("use ATM_management")
   cur.execute("create table if not exists atm(SNo int(10) primary key auto_increment,Card_Num char(16) unique,pin char(6),Holder_Name varchar(55),Balance double(10,2),Valid_From date,Valid_Till date);")
   cur.execute("create table if not exists transaction1(SNo int(10) primary key auto_increment,TranType varchar(10), TranAmount double(10,2), FinalAmt double(10,2),TranDate date);")
   cur.execute("create table if not exists transaction2(SNo int(10) primary key auto_increment,TranType varchar(10), TranAmount double(10,2), FinalAmt double(10,2),TranDate date);")
   cur.execute("create table if not exists transaction3(SNo int(10) primary key auto_increment,TranType varchar(10), TranAmount double(10,2), FinalAmt double(10,2),TranDate date);")

   cur.execute("Insert into atm(card_num,pin,holder_name,balance,valid_from,valid_till) values('1234123412341234','888888','Tanmay Suhanne',50000.00,'20041116','20340419');")
   con.commit()
   cur.execute("Insert into atm(card_num,pin,holder_name,balance,valid_from,valid_till) values('1111222233334444','123456','Baishali Roy',50000.00,'20041116','20340419');")
   con.commit()
   cur.execute("Insert into atm(card_num,pin,holder_name,balance,valid_from,valid_till) values('5555666677778888','000999','Arijit',50000.00,'20041116','20340419');")
   con.commit()

try:
   cur.execute("use ATM_management")
except:
   makeTables()

def menu():
    while (True):
        print("\n\nWelcome to the ATM system of the State Bank of India")
        print("\n1. To proceed to the log-in interface")
        print("0. To quit")

        ch=input("Enter your choice::")

        if ch=='1':
          print("\nTo proceed further please enter your ATM number and pin")
          atm_num=input("\nATM Number::")
          pin=gp.getpass("Pin::")
          if checkPin(atm_num,pin):
              while(True):
                print("\n1. For Balance Enquiry")#baisu
                print("2. To Withdraw Money")#ari
                print("3. To Deposit Money")#ari
                print("4. To Change your Pin")#ari
                print("5. To Transfer Money")#baishali
                print("6. To Print the Mini Statement")#baishali
                print("0. To return back to the log-in menu")#baishali

                choice = input("\nEnter your choice::")

                if choice=='1':
                   balanceEnquiry(atm_num)
                   continue

                if choice=='2':
                   wthdrwMoney(atm_num)
                   continue

                if choice=="3":
                   dpstMoney(atm_num)
                   continue

                if choice =='4':
                   changePin(atm_num)
                   continue

                if choice=='5':
                   trnsfrMoney(atm_num)
                   continue

                if choice=='6':
                   miniStmnt(atm_num)
                   continue

                if choice == '0':
                    break
             
                else:
                    print('Wrong input! Please try again.')
                    continue
          
          else:
              print("The details that you entered seem to be incorrect! Please try again.")
              continue

        if choice=='0':
            print("\n\nGoodbye!")
            exit()
        else:
            print("Wrong input! Please Try Again.")
            continue


def checkPin(atm_num,pin):
   cur.execute("select pin from ATM where card_num='%s';"%(atm_num))
   data=cur.fetchall()
   pin2=''

   for row in data:
      for i in row:
         pin2=i
   
   if pin2=="":
      print("ATM Number not in database! Please try again with a different ATM Number.")
      return False

   if pin==pin2:
      return True

   else:
      print("Wrong Pin, please try again!")
      return False

def balanceEnquiry(atm_num):
   cur.execute("select balance from atm where card_num='%s';"%(atm_num))
   data=cur.fetchall()
   bal=0

   for i in data:
      for j in i:
         bal=j

   print("\nThe available balance is",bal)
   return

def wthdrwMoney(atm_num):
   amt=float(input("\nEnter the amount you want to withdraw : "))
   cur.execute("select balance from atm where card_num='%s';"%(atm_num))
   data=cur.fetchall()
   bal=0

   for i in data:
      for j in i:
         bal=j

   if amt%50!=0:
      print("\nThe amount entered must be expressed by at least using RS50 currency notes.")
      return

   if amt>bal:
      print("\nYour ATM balance is less than the amount you want to withdraw!")
      return

   bal-=amt
   cur.execute("update atm set balance=balance-%f where card_num='%s';"%(amt,atm_num))
   con.commit()
   if atm_num=='1111222233334444':
      cur.execute("insert into transaction2(TranType,TranAmount,FinalAmt,TranDate) values('withdrawl',%f,%f,curdate());"%(amt,bal))
      con.commit()
      print("\n\nTransaction Successful!")
      return
   
   if atm_num=='1234123412341234':
      cur.execute("insert into transaction1(TranType,TranAmount,FinalAmt,TranDate) values('withdrawl',%f,%f,curdate());"%(amt,bal))
      con.commit()
      print("\n\nTransaction Successful!")
      return

   if atm_num=='5555666677778888':
      cur.execute("insert into transaction3(TranType,TranAmount,FinalAmt,TranDate) values('withdrawl',%f,%f,curdate());"%(amt,bal))
      con.commit()
      print("\n\nTransaction Successful!")
      return

   
def dpstMoney(atm_num):
   amt=float(input("\nEnter the amount you want to deposit : "))
   cur.execute("select balance from atm where card_num='%s';"%(atm_num))
   data=cur.fetchall()
   bal=0

   for i in data:
      for j in i:
         bal=j

   bal+=amt
   cur.execute("update atm set balance=balance+%f where card_num='%s';"%(amt,atm_num))
   con.commit()
   if atm_num=='1111222233334444':
      cur.execute("insert into transaction2(TranType,TranAmount,FinalAmt,TranDate) values('deposit',%f,%f,curdate());"%(amt,bal))
      con.commit()
      print("\n\nTransaction Successful!")
      return
   
   if atm_num=='1234123412341234':
      cur.execute("insert into transaction1(TranType,TranAmount,FinalAmt,TranDate) values('deposit',%f,%f,curdate());"%(amt,bal))
      con.commit()
      print("\n\nTransaction Successful!")
      return

   if atm_num=='5555666677778888':
      cur.execute("insert into transaction3(TranType,TranAmount,FinalAmt,TranDate) values('deposit',%f,%f,curdate());"%(amt,bal))
      con.commit()
      print("\n\nTransaction Successful!")
      return

   
def changePin(atm_num):
   print("\nEnter new pin(6 digits).")
   pin=gp.getpass("New Pin: ")
   cur.execute("update atm set pin='%s' where atm_num='%s"%(pin,atm_num))
   cur.commit()
   return

def trnsfrMoney(atm_num):
   tran_card=input("Enter the card number to which you want to transfer money")
   amt=float(input("\nEnter the amount you want to transfer : "))

   if amt<0:
      print("Please enter a positive value for transfer amount!")
      return

   cur.execute("select balance from atm where card_num='%s';"%(tran_card))
   data=cur.fetchall()
   bal=0

   for i in data:
      for j in i:
         bal=j

   cur.execute("select balance from atm where card_num='%s';"%(atm_num))
   data=cur.fetchall()
   bal2=0

   for i in data:
      for j in i:
         bal=j

   if amt>bal:
      print("\nYour ATM balance is less than the amount you want to transfer!")
      return

   bal+=amt
   bal2-=amt
   cur.execute("update atm set balance=balance+%f where card_num='%s';"%(amt,tran_card))
   con.commit()
   cur.execute("update atm set balance=balance-%f where card_num='%s';"%(amt,atm_num))
   con.commit()
   if tran_card=='1111222233334444':
      cur.execute("insert into transaction2(TranType,TranAmount,FinalAmt,TranDate) values('deposit',%f,%f,curdate());"%(amt,bal))
      con.commit()
   
   if tran_card=='1234123412341234':
      cur.execute("insert into transaction1(TranType,TranAmount,FinalAmt,TranDate) values('deposit',%f,%f,curdate());"%(amt,bal))
      con.commit()

   if tran_card=='5555666677778888':
      cur.execute("insert into transaction3(TranType,TranAmount,FinalAmt,TranDate) values('deposit',%f,%f,curdate());"%(amt,bal))
      con.commit()

   
   if atm_num=='1111222233334444':
      cur.execute("insert into transaction2(TranType,TranAmount,FinalAmt,TranDate) values('transfer',%f,%f,curdate());"%(amt,bal2))
      con.commit()
      print("\n\nTransaction Successful!")
      return
   
   if atm_num=='1234123412341234':
      cur.execute("insert into transaction1(TranType,TranAmount,FinalAmt,TranDate) values('transfer',%f,%f,curdate());"%(amt,bal2))
      con.commit()
      print("\n\nTransaction Successful!")
      return

   if atm_num=='5555666677778888':
      cur.execute("insert into transaction3(TranType,TranAmount,FinalAmt,TranDate) values('transfer',%f,%f,curdate());"%(amt,bal2))
      con.commit()
      print("\n\nTransaction Successful!")
      return

   
#def miniStmnt():

menu()
