import mysql.connector
import random
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE hotel22")
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel22")
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE hotel1 (name VARCHAR(255), phoneno VARCHAR(255), adharno VARCHAR(255), roomno VARCHAR(255), roomtype VARCHAR(255))")
#mycursor.execute("CREATE TABLE ORDER1 (name VARCHAR(255), food VARCHAR(255))")
#mycursor.execute("CREATE TABLE RESTURANTBILL (name VARCHAR(255), Dishname VARCHAR(255), quantity VARCHAR(255), foodbill VARCHAR(255))")
#mycursor.execute("CREATE TABLE laundarybill (name VARCHAR(255), quantity VARCHAR(255), discount VARCHAR(255), billcharged VARCHAR(255))")
def room():
    c="y"
    while c=="y":
        print("1.BOOK ROOM")
        print("2.CANCEL ROOM")
        print("3.CHECK YOUR ROOM NUMBER AND DETAILS")
        print("4.Exit")
        p=int(input("enter your choice"))
        if p==1:
            print("1.SINGLE(ROOM FOR ONE PERSON)")
            print("2.DOUBLE(ROOM FOR TWO PERSON)")
            print("3.TRIPLE(ROOM FOR THREE PERSON)")
            print("4.QUAD(ROOM FOR FOUR PERSON)")
            print("5.QUEEN(ROOM WITH QUEEN SIZED BED)")
            print("6.KING(ROOM WITH KING SIZED BED)")
            f=int(input("enter your choice which room you want"))
            if f==1:
                R="SINGLE"
            if f==2:
                R="DOUBLE"
            if f==3:
                R="TRIPLE"
            if f==4:
                R="QUAD"
            if f==5:
                R="QUEEN"
            if f==6:
                R="KING"
            N=input("enter your name")
            D=input("enter the phone number")
            S=input("enter you adhar number")
            P=str(random.randrange(200,500))
            sql = "INSERT INTO hotel1 (name, phoneno, adharno, roomno, roomtype) VALUES (%s, %s, %s, %s, %s)"
            val = (N,D,S,P,R)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Your room has been Booked")
        elif p==2:
            print("CANCEL THE BOOKING")
            g=input("enter your adhar number")
            sql = "DELETE FROM hotel1 WHERE adharno =%s"
            a=(g,)
            mycursor.execute(sql,a)
            mydb.commit()
            print("your room has been cancel")
        elif p==3:
            print("your room number and details")
            g=input("enter your adhar number")
            f="SELECT * FROM hotel1 WHERE adharno =%s"
            a=(g,)
            mycursor.execute(f,a)
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
        elif p==4:
                exit()
        else:
                print("you enter the wrong choice")
        c=input("do you want to continue")
def food():
    k="y"
    while k=="y":
        print("1.INDIAN FOOD")
        print("2.CHINESE FOOD")
        print("3.ITALIAN")
        print("4.MEXCICAN")
        q=int(input("enter the value"))
        if q==1:
                 print("1.BUTTER CHICKEN(rupess 300 per plate)")
                 print("2.MATTAR PANEER(rupess 200 per plate)")
                 print("3.CHOLE BHATURE(rupess 200 per plate)")
                 print("4.FISH(rupess 250 per plate)")
                 print("5.see your order")
                 Q=int(input("enter what do want to eat from the given choice"))
                 if Q==1:
                        u=input("enter your name")
                        sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                        val = (u,'Butter chicken')
                        mycursor.execute(sql, val)
                        mydb.commit()
                        print("your order has been taken")
                 elif Q==2:
                        u=input("enter your name")
                        sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                        val = (u,'MATTAR PANEER')
                        mycursor.execute(sql, val)
                        mydb.commit()
                 elif Q==3:
                        u=input("enter your name")
                        sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                        val = (u,'CHOLE BHATURE')
                        mycursor.execute(sql, val)
                        mydb.commit()
                 elif Q==4:
                        u=input("enter your name")
                        sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                        val = (u,'FISH')
                        mycursor.execute(sql, val)
                        mydb.commit()
                 elif Q==5:
                     g=input("enter your name")
                     f="SELECT * FROM ORDER1 WHERE name =%s"
                     a=(g,)
                     mycursor.execute(f,a)
                     myresult = mycursor.fetchall()
                     for x in myresult:
                         print(x)
                        
                 else:
                        print("wrong choice")
        if q==2:
                print("1.KUNG PAO CHICKEN(rupess 300 per plate)")
                print("2.SPRING ROLL(rupess 200 per plate)")
                print("3.DUMPLING(rupess 200 per plate)")
                print("4.CHOW MEIN(rupess 100 per plate)")
                print("5.see your order")
                Q=int(input("enter what do want to eat"))
                u=input("enter your name")
                if Q==1:
                        sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                        val = (u,'KUNG PAO CHICKEN')
                        mycursor.execute(sql, val)
                        mydb.commit()
                        print("your order has been taken")
                elif Q==2:
                        sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                        val = (u,'SPRING ROLL')
                        mycursor.execute(sql, val)
                        mydb.commit()
                elif Q==3:
                        sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                        val = (u,'DUMPLING')
                        mycursor.execute(sql, val)
                        mydb.commit()
                elif Q==4:
                        sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                        val = (u,'CHOW MEIN')
                        mycursor.execute(sql, val)
                        mydb.commit()
                elif Q==5:
                        g=input("enter your name")
                        f="SELECT * FROM ORDER1 WHERE name =%s"
                        a=(g,)
                        mycursor.execute(f,a)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            print(x)
                else:
                        print("wrong choice")
        if q==3:
                print("1.PIZZA(rupess 300 per pizza)")
                print("2.CARBONARA(rupess 200 per plate)")
                print("3.FOCACCIA(rupess 200 per plate)")
                print("4.ARANCINI(rupess 100 per plate)")
                print("5.see your order")
                Q=int(input("enter what do want to eat"))
                u=input("enter your name")
                if Q==1:
                        sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                        val = (u,'PIZZA')
                        mycursor.execute(sql, val)
                        mydb.commit()
                        print("your order has been taken")
                elif Q==2:
                        sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                        val = (u,'CARBONARA')
                        mycursor.execute(sql, val)
                        mydb.commit()
                elif Q==3:
                        sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                        val = (u,'FOCACCIA')
                        mycursor.execute(sql, val)
                        mydb.commit()
                elif Q==4:
                        sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                        val = (u,'ARANCINI')
                        mycursor.execute(sql, val)
                        mydb.commit()
                elif Q==5:
                        g=input("enter your name")
                        f="SELECT * FROM ORDER1 WHERE name =%s"
                        a=(g,)
                        mycursor.execute(f,a)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            print(x)
                else:
                        print("wrong choice")
        if q==4:
            print("1.BURRITO(rupess 300 per pizza)")
            print("2.TACO(rupess 250 per plate)")
            print("3.BIRRIA(rupess 250 per plate)")
            print("4.TOSTADA(rupess 100 per plate)")
            print("5.see your order")
            Q=int(input("enter what do want to eat"))
            u=input("enter your name")
            if Q==1:
                sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                val = (u,'KUNG PAO CHICKEN')
                mycursor.execute(sql, val)
                mydb.commit()
                print("your order has been taken")
            elif Q==2:
                sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                val = (u,'SPRING ROLL')
                mycursor.execute(sql, val)
                mydb.commit()
            elif Q==3:
                sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                val = (u,'DUMPLING')
                mycursor.execute(sql, val)
                mydb.commit()
            elif Q==4:
                sql = "INSERT INTO ORDER1 (name, food) VALUES (%s, %s)"
                val = (u,'CHOW MEIN')
                mycursor.execute(sql, val)
                mydb.commit()
            elif Q==5:
                g=input("enter your name")
                f="SELECT * FROM ORDER1 WHERE name =%s"
                a=(g,)
                mycursor.execute(f,a)
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
            else:
                print("wrong choice")
        k=input("if you want to continue then press y or not to continue press any key")
    else:
        exit()
def restbill():
    c="y"
    while c=="y":
            print("Butter chicken,MATTAR PANEER,CHOLE BHATURE,FISH,KUNG PAO CHICKEN,SPRING ROLL,DUMPLING,CHOW MEIN,PIZZA,CARBONARA,FOCACCIA,ARANCINI,BURRITO,TACO,BIRRIA,TOSTADA")
            print("press r for check your order details OR history details")
            print("enter your dish name in capital letters")
            v=input("enter your order or press r to check order details")
            if v=="BUTTER CHICKEN" or v=="BURRITO" or v=="KUNG PAO"or v=="PIZZA":
                  I=input("enter you name")
                  e=int(input("How many plate you buy:"))
                  m=300*e
                  j=str(e)
                  z=str(m)
                  sql = "INSERT INTO RESTURANTBILL (name, Dishname, quantity , foodbill) VALUES (%s, %s, %s, %s)"
                  val = (I,v,j,z)
                  mycursor.execute(sql,val)
                  mydb.commit()
                  print("Sir your bill amount is ",m,"rupess")
            elif v=="MATTAR PANEER" or v=="CHOLE"or v=="BHATURE"or v=="SPRING ROLL"or v=="DUMPLING"or v=="CARBONARA"or v=="FOCACCIA":
                  I=input("enter you name")
                  e=int(input("How many plate you buy:"))
                  m=200*e
                  j=str(e)
                  z=str(m)
                  sql = "INSERT INTO RESTURANTBILL (name, Dishname, quantity , foodbill) VALUES (%s, %s, %s, %s)"
                  val = (I,v,j,z)
                  mycursor.execute(sql,val)
                  mydb.commit()
                  print("Sir your bill amount is ",m,"rupess")
            elif v=="FISH"or v=="TACO"or v=="BIRRIA":
                  I=input("enter you name")
                  e=int(input("How many plate you buy:"))
                  m=250*e
                  j=str(e)
                  z=str(m)
                  sql = "INSERT INTO RESTURANTBILL (name, Dishname, quantity , foodbill) VALUES (%s, %s, %s, %s)"
                  val = (I,v,j,z)
                  mycursor.execute(sql,val)
                  mydb.commit()
                  print("Sir your bill amount is ",m,"rupess")
            elif v=="CHOW MEIN"or v=="ARANCINI"or v=="TOSTADA":
                  I=input("enter you name")
                  e=int(input("How many plate you buy:"))
                  m=100*e
                  j=str(e)
                  z=str(m)
                  sql = "INSERT INTO RESTURANTBILL (name, Dishname, quantity , foodbill) VALUES (%s, %s, %s, %s)"
                  val = (I,v,j,z)
                  mycursor.execute(sql,val)
                  mydb.commit()
                  print("Sir your bill amount is ",m,"rupess")
            elif v=="r":
                  I=input("enter you name")
                  f="SELECT * FROM RESTURANTBILL WHERE name =%s"
                  a=(I,)
                  mycursor.execute(f,a)
                  myrecord5=mycursor.fetchall()
                  for z in myrecord5:
                      print(z)
            else:
                print("YOU ENTER THE WRONG CHOICE")
            c=input("if you want to continue then press y or press any key for exit")
    else:
        exit()
def lbill():
    c="y"
    while c=="y": 
        print("press 1 for check details")
        print("press 2 for bill ")
        print("press any key for exit")
        choice=int(input("enter your choice"))
        if choice==1:
            l=input("enter your name")
            f="SELECT * FROM laundarybill WHERE name =%s"
            a=(l,)
            mycursor.execute(f,a)
            myrecord6=mycursor.fetchall()
            for z in myrecord6:
                print(z)
        if choice==2:
            l=input("enter your name")
            a=int(input("enter the quantity of clothes"))
            print("washing of 1 cloth is 10 ruppess")
            print("1.If the clothes less than 10 then no discount")
            print("2.If the clothes 10 to 15 then 5 % discount")
            print("3.If the clothes 16 to 22 then 10 % discount")
            print("4.If the clothes 23 to 30 then 15 % discount")
            print("5.If the clothes more than 30 then 20 % discount")
            if a>0 and a<10:
                h=str(a)
                x=a*10
                s=str(x)
                print("your bill of ",a,"clothes is",x,"ruppess")
                sql = "INSERT INTO laundarybill (name, quantity, discount, billcharged) VALUES (%s, %s, %s, %s)"
                val = (l,h,'0%',s)
                mycursor.execute(sql,val)
                mydb.commit()
            elif a>9 and a<16:
                h=str(a)
                x=a*10
                y=(5/100)*x
                s=str(x-y)
                print("your bill of ",a,"clothes is",s,"ruppess")
                sql = "INSERT INTO laundarybill (name, quantity, discount, billcharged) VALUES (%s, %s, %s, %s)"
                val = (l,h,'5%',s)
                mycursor.execute(sql,val)
                mydb.commit()

            elif a>15 and a<23:
                h=str(a)
                x=a*10
                y=(10/100)*x
                s=str(x-y)
                print("your bill of ",a,"clothes is",s,"ruppess")
                sql = "INSERT INTO laundarybill (name, quantity, discount, billcharged) VALUES (%s, %s, %s, %s)"
                val = (l,h,'10%',s)
                mycursor.execute(sql,val)
                mydb.commit()

            elif a>22 and a<31:
                h=str(a)
                x=a*10
                y=(15/100)*x
                s=str(x-y)
                print("your bill of ",a,"clothes is",s,"ruppess")
                sql = "INSERT INTO laundarybill (name, quantity, discount, billcharged) VALUES (%s, %s, %s, %s)"
                val = (l,h,'15%',s)
                mycursor.execute(sql,val)
                mydb.commit()

            else:
                h=str(a)
                x=a*10
                y=(20/100)*x
                s=str(x-y)
                print("your bill of ",a,"clothes is",s,"ruppess")
                sql = "INSERT INTO laundarybill (name, quantity, discount, billcharged) VALUES (%s, %s, %s, %s)"
                val = (l,h,'20%',s)
                mycursor.execute(sql,val)
                mydb.commit()
        c=input("if you want to continue then press y or press any key for exit")
    else:
        exit()
print("   ------------------------------------------------------------------------")
print("   ------------------------------------------------------------------------")
print("   ------------------------------------------------------------------------")
print("   -----------------------------HOTEL RJ-----------------------------")
print("   ------------------------------------------------------------------------")
print("   ------------------------------------------------------------------------")
print("   ------------------------------------------------------------------------")

print("1.Check room")
print("2.Order food")
print("3.Restaurant bill")
print("4.LAUNDARY BILL")
print("PRESS ANY number FOR EXIT ")
b=int(input("Enter your choice"))
def main():
    if b==1:
        room()
    elif b==2:
        food()
    elif b==3:
        restbill()
    elif b==4:
        lbill()
    else:
        exit()
main()      
