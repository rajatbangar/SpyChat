#spy detail file
print 'hello!\nLet\'s get started!'


class Spy:
#Spy class will create a spy.

    def __init__(self , name , salutation , age , rating):


        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.chats=[]
        self.is_online=True
        self.current_status_message=None



spy_name=raw_input("What is your spy name? ")

if len(spy_name)>0:



    spy_salutation = raw_input('What should i call you Mr or Ms?  ')
    while spy_salutation!='Mr' and spy_salutation!='Ms':
        print 'Wrong'
        spy_salutation = raw_input('What should i call you Mr or Ms?  ')
    spy_name=spy_salutation+' '+spy_name


    print 'Alright! I would like to know a little more about you before we proceed..'

    spy_age=raw_input("What is your spy age? ")
    spy_age=int(spy_age)
    if spy_age>12 and spy_age<50:


        spy_rating=raw_input('What is your spy rating? ')
        spy_rating=float(spy_rating)

        if spy_rating>=4.5:

            print 'Great Ace!'

        elif spy_rating>3.5 and spy_rating<4.5:

            print 'You are a Good one!'

        elif spy_rating>2.5 and spy_rating<3.5:

            print 'You can always do Better '

        spy_is_online=True

        print 'Authentication Completed! Welcome %s Your age is %d and Your Spy Rating is %.1f'%(spy_name,spy_age,spy_rating)




    else:
        print 'Sorry! You are not of correct Age to be a Spy :-('


else:
    print 'Please type a valid Name'
