from  spy_details import Spy,spy_name
from steganography.steganography import Steganography
from datetime import datetime
from colors import blue,red



class ChatMessage:

#ChatMessage class

    def __init__(self, message ,send_by_me):

        self.message=message
        self.time=datetime.now()
        self.send_by_me=send_by_me



spy = Spy('bond', 'Mr.', 24, 4.7)

#instances of Spy class

friend_one = Spy('Ironman', 'Mr', 5.3, 27)
friend_two = Spy('Thor', 'Mr', 5.39, 21)
friend_three = Spy('WonderWomen', 'Ms', 4.95, 37)

#friends list will contain a list of friends
friends = [friend_one, friend_two, friend_three]




STATUS_MESSAGE=['my name is bod,james bond','shaken,not stirred.','keeping the british end up,sir']

print "Hello! Let\'s get started"

question = "Do you want to continue as "+ spy_name + " (Y/N)?  "
existing = raw_input(question)





def add_status(current_status_message):

#add_status function will add a status.status could be choosed from old status message or could be created a new one.

    update_status_message=None

    if current_status_message!=None:
        print "  your current status message is %s"%(current_status_message)
    else:
        print "  you dont have any status message currently "


    default= raw_input("Do you want to select from older status(y/n)?")

    if default.upper()=="N":
        new_status_message=raw_input("what status message do you want to set?")


        if len(new_status_message)>0:
            STATUS_MESSAGE.append(new_status_message)
            update_status_message=new_status_message

    elif default.upper()=="Y":
        item_position=1
        for message in STATUS_MESSAGE:
            print '%d.%s'%(item_position,message)
            item_position=item_position+1
        message_selection=int(raw_input("\n choose from the above messages"))


        if len(STATUS_MESSAGE)>=message_selection:
            update_status_message=STATUS_MESSAGE[message_selection-1]
    else:
        print "the option you choose is not valid !.press either y or n ."
    if update_status_message:

        print 'your updated status message is:- %s'%(update_status_message)

    else:
        print 'you did not update your status message.'


    return update_status_message


def add_friend():

#add_friend function will add a new friend to the friends list.

    new_friend=Spy('','',0,0.0)

    new_friend.name=raw_input("please add your friends name: ")
    new_friend.salutation=raw_input("Are they Mr or Ms?: ")

    new_friend.name=new_friend.salutation+" "+new_friend.name

    new_friend.age=raw_input('Age?')
    new_friend.age=int(new_friend.age)

    new_friend.rating=raw_input('rating?')
    new_friend.rating=float(new_friend.rating)



    if len(new_friend.name)>0 and new_friend.age>12 and new_friend.rating>=spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
        print friends


    else:


        print 'sorry!Invalid entry.We cant add spy with the detail you provided'


    return len(friends)






def select_a_friend():
    item_number = 0

#select friend function will help in choosing a friend from a list of friends.


    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend.name,friend.age,friend.age)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends :-")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

def send_message():

    friend_choice=select_a_friend()

#send message function will send a secret message through an image to the chosen friend.

    original_image=raw_input('What is the name of the image? ')

    if len(original_image)==0:
        print 'Invalid Image Path'
    else:
        output_path='D:\python\output.jpg'
        text=raw_input('What do you want to say? ')

        Steganography.encode(original_image,output_path,text)

        new_chat = ChatMessage(text,True)



        friends[friend_choice].chats.append(new_chat)


        print 'Your secret message image is ready !'
        print friends



def read_message():


    sender = select_a_friend()
    output_path = raw_input('What is the name of the file? ')
    secret_text=Steganography.decode(output_path)

#read message function will read the secret message from a chosen friend through output image.

    new_chat=ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)


    if len(secret_text)==0:

        print 'Sorry! No secret message to be Displayed '
    elif secret_text.upper()=='SOS':
        print 'Emergency'
    elif secret_text.upper()=='SAVE ME' or secret_text.upper()=='SAVEME':
        print 'Hold On'
    elif len(secret_text)>100:
        friends.remove(friends[sender])
        print 'Spy is removed!!'

    else:
        print secret_text






def read_chat_history():


    read_for = select_a_friend()
#chat history function will give a history of chat messages and the time.


    for chat in friends[read_for].chats:

        if chat.send_by_me:


            print '[%s] %s: %s'%(chat.time.strftime(blue('%d %Y %B')),red('you_said'),chat.message)

        else:
            print '[%s] %s: %s' %(chat.time.strftime(blue('%d %Y %B')),red(friends[read_for].name),chat.message)




def start_chat(spy):

#start chat will authenticate the user and give a menu things that a spy can do.
    current_status_message=None

    if  spy.age>12 and  spy.age<50:
        print "authentication complete.welcome "+spy.name+" age:"+str(spy.age)+" and rating of: "+str(spy.rating)+" proud to have you on board."
        show_menu=True
        while show_menu:
            menu_choices="What you want to do?\n 1.Add a status update\n 2.Add a friend\n 3.send a secret message\n 4.read a secret message\n 5.read chats from a user\n 6.close application\n"
            menu_choice=raw_input(menu_choices)

            if len(menu_choice)>0:
                menu_choice=int(menu_choice)
                if menu_choice==1:
                    current_status_message = add_status(current_status_message)
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()


                else:
                    show_menu=False
                    print 'Invalid Selection'
    else:
         print 'sorry you not of the correct sage to be spy'


if existing=="Y":


    start_chat(Spy)

else:
    spy=Spy('','',0,0.0)

    spy.name=raw_input("welcome to spy chat,you must tell your name first: ")
    if len(spy.name)>0:
        spy.salutation=raw_input("what should i call you Mr or Ms? ")

        spy.age=raw_input("Whats your Age? ")
        spy.age=int(spy.age)

        spy.rating=raw_input("What is your spy rating? ")
        spy.rating=float(spy.rating)


        spy.spy_is_online=True

        start_chat(spy)

