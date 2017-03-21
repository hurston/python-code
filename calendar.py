"""
User will be able to do the following:
View the calendar
Add an event to the calendar
Update an existing event
Delete an existing event"""

from time import sleep, strftime

USER_NAME = "Hurston"
calendar = {}


def welcome():
    print "Welcome %s" % USER_NAME
    print "Calendar is opening..."
    #  sleep(1)
    print "Today is: " + strftime("%A %B %d, %Y")
    print "The time is: " + strftime("%H:%M:%S")
    sleep(1)
    print "What would you like to do?"


def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input("A to Add, U to Update, V to View, \
                                D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == 'V':
            if len(calendar.keys()) < 1:
                print "Sorry " + USER_NAME + ", the calendar is empty."
            else:
                print calendar
        elif user_choice == 'U':
            print calendar
            date = raw_input("What date?: ")
            update = raw_input("Enter the Update: ")
            calendar[date] = update
            print "Update was successful"
            print calendar
        elif user_choice == 'A':
            event = raw_input("Enter event: ")
            date = raw_input("Enter date (MM/DD/YYYY): ")
            uyear = user_year(date)
            nowyear = int(strftime("%Y"))
            if (len(date) > 10) or uyear < nowyear:
                print "Invalid date entered"
                try_again = raw_input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == 'Y':
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print calendar
        elif user_choice == 'D':
            if len(calendar.keys()) < 1:
                print "Sorry, Can't delete because the calendar is empty"
            else:
                event = raw_input("What Event?: ")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print "Event %s successfully deleted." % (event)
                        print calendar
                    else:
                        print "An incorrect event was specified"
        elif user_choice == 'X':
            start = False
        else:
            print "You entered an invalid command, so I'm outta here. See ya!"
            start = False


def user_year(adate):
    adate = adate.split("/")
    return int(adate[2])


start_calendar()
