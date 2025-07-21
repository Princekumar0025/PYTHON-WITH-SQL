import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",passwd="@prince",database="computer")
if conn.is_connected():
        print('successfully connected')
c1=conn.cursor()
c1.execute('use computer')
c1=conn.cursor()
print('')
print('')
print('         COMPUTER SALES AND SERVICE SYSTEM')
print('')
print('')
print('1.to buy computer parts')
print('2.to ask for computer service')
print('3.problem with our sales or service')
print('4.to see various comments and ratings on our software')
print('5.exit')
print('')
choice=int(input('enter your choice:'))
if choice==1:
        print('')
        print('     COMPUTER SALES')
        print('')
        cust_name=str(input('please enter your name:'))
        phno=int(input('please enter your phone number:'))
        email=str(input('please enter your e-mail id:'))
        address=str(input('please enter your address:'))
        part=str(input('please enter the type of computer part you need:'))
        insert="insert into 1_comp_sales values('"+cust_name+"',"+str(phno)+",'"+email+"','"+address+"','"+part+"')"
        c1.execute(insert)
        conn.commit()
        print('')
        print('   RATING AND COMMENT')
        rating=int(input('please enter the ratings out of 10 for our software :'))
        comment=str(input('please comment on our software :'))
        print('')
        print('')
        print('')
        if rating<5:
                print('sorry for our poor performance next time we will be good')
        else:
                print('thanks for rating us next time we will be even better')
        insert1="insert into rating_comment values("+str(phno)+",'"+address+"','"+email+"',"+str(rating)+",'"+comment+"')"
        c1.execute(insert1)
        conn.commit()
        print('')
        print('             thank you dear customer',cust_name,'your computer part Will be delivered to you shortly and you can pay cash to the delivery boy')

if choice==2:
        print('')
        print('     COMPUTER SERVICE')
        print('')
        name=str(input('please enter your name:'))
        phno=int(input('please enter your phone number:'))
        email=str(input('please enter your e-mail id:'))
        address=str(input('please enter your residential address:'))
        service=str(input('please enter the service you want:'))
        
        insert="insert into 1_comp_service values('"+name+"',"+str(phno)+",'"+email+"','"+address+"','"+service+"')"
        c1.execute(insert)
        conn.commit()
        print('')
        print('')
        print('     RATINGS AND COMMENT')
        rating=int(input('please enter the ratings out of 10 :'))
        comment=str(input('please comment on our software :'))
        print('')
        if rating<5:
                print('sorry for our poor performance next time we will be good enough')
        else:
                print('thanks for rating us next time we will be even better')
        insert1="insert into rating_comment values("+str(phno)+",'"+email+"','"+address+"',"+str(rating)+",'"+comment+"')"
        c1.execute(insert1)
        conn.commit() 
        print('')
        print('')

        print('           thank you dear custmer',name,'the service you asked will be done to your computer parts shortly and cash on delivery')
if choice==3:
        print('')
        print('       PROBLEM WITH SOFTWARE')
        print('')
        print('')
        print('1.problem with sales')
        print('2.problem with service')
        print('3.problem with dor delivary boy or service boy')
        print('')
        a=int(input('please enter your choice:'))
        print('')
        if a==1:
                cus_name=str(input('please enter your name:'))
                phno1=int(input('please enter your phone no:'))
                sa_name=str(input('please enter the name of the sales boy whom you dealed with:'))
                prob=str(input('please enter your problem:'))
                print('')
                print('      sorry for the problem sire/madam we will ensure that this does not happen next time thank you')
                insert2="insert into sales_prob values('"+cus_name+"',"+str(phno1)+",'"+sa_name+"','"+prob+"')"
                c1.execute(insert2)
                conn.commit()
        if a==2:
                cus_name=str(input('please enter your name:'))
                phno1=int(input('please enter your phone no:'))
                se_name=str(input('please enter the name of the service boy you dealed with:'))
                prob=str(input('please enter the problem you face:'))
                print('')
                print('       sorry for the problem sire/madam we will ensure that this does not happen next time . thank you')
                insert2="insert into servive_prob values('"+cus_name+"',"+str(phno1)+",'"+se_name+"','"+prob+"')"
                c1.execute(insert2)
                conn.commit
        if a==3:
                cus_name=str(input('please enter your name:'))
                phno1=int(input('please enter your phone no:'))
                name1=str(input('please enter the boys name:'))
                prob=str(input('please enter the problem you have faced'))
                insert2="insert into sb_prob values('"+cus_name+"',"+str(phno1)+",'"+name1+"','"+prob+"')"
     
                c1.execute(insert2)
                conn.commit()
                print('')
                print('        sorry for the promlem sire/madame we see to it that the boy gets penalized severely.thank you')
if choice==3:
        print('')
        print('       PROBLEM WITH SOFTWARE')
        print('')
        print('')
        print('1.problem with sales')
        print('2.problem with service')
        print('3.problem with dor delivary boy or service boy')
        print('')
        a=int(input('please enter your choice:'))
        print('')
        if a==1:
                cus_name=str(input('please enter your name:'))
                phno1=int(input('please enter your phone no:'))
                sa_name=str(input('please enter the name of the sales boy whom you dealed with:'))
                prob=str(input('please enter your problem:'))
                print('')
                print('sorry for the problem sire/madam we will ensure that this does not happen next time . thank you')
                insert2="insert into servive_prob values('"+cus_name+"',"+str(phno1)+",'"+sa_name+"','"+prob+"')"
                c1.execute(insert2)
                conn.commit
        if a==2:
                cus_name=str(input('please enter your name:'))
                phno1=int(input('please enter your phone no:'))
                se_name=str(input('please enter the name of the service boy you dealed with:'))
                prob=str(input('please enter the problem you face:'))
                print('')
                print('sorry for the problem sire/madam we will ensure that this does not happen next time . thank you')
                insert2="insert into servive_prob values('"+cus_name+"',"+str(phno1)+",'"+se_name+"','"+prob+"')"
                c1.execute(insert2)
                conn.commit
        if a==3:
                cus_name=str(input('please enter your name:'))
                phno1=int(input('please enter your phone no:'))
                name1=str(input('please enter the boys name:'))
                prob=str(input('please enter the problem you have faced'))
                insert2="insert into sb_prob values('"+cus_name+"',"+str(phno1)+",'"+name+"','"+prob+"')"
     
                c1.execute(insert2)
                conn.commit()
                print('')
                print('sorry for the promlem sire/madame we see to it that the boy gets penalized severely.thank you')
if choice==4:
        l="select * from rating_comment"
        c1.execute(l)
        a= c1.fetchone()




             