# Author:   Sean Toman - L00136443
# Date:     07 Oct 2017
# Desc:     A program that allows the user to search for Shows and display their timetable.
#           Users can edit all shows, add a new show, delete a show or display a show/s.
#           All shows are wrote out to a text file when the program is launched and after every edit.

from Show import Show


# function to find the show in the list and return its index
def find_show(name_in):
    #shows_file = open("shows.txt").readlines()
    #for line in shows_file:
    #    if (name in line):
    #        title, start, end, day, stage = line.split(",")
    #        return "Show Name:\t\t{0}\nStart Time:\t\t{1}\nEnd Time:\t\t{2}\nDay:\t\t\t{3}\nStage:\t\t\t{4}".format(
    #            name, start, end, day, stage)
    i = 0
    for show in show_list:
        if (name_in == show.__getattribute__('name')):
            return "{}".format(i)
        i += 1
    #shows_file = open("shows.txt", "r")
    #for line in shows_file:
    #    if (name in line):
    #        return line


# function to get show name from user and convert it to title case
# to ensure names input from user are always title case
def get_show():
    print("Please enter show name: ")
    name = input()
    name = name.title()
    return name


# function to check if time is valid and return True or False
def is_time_valid(hour, minute):
    if(hour < 0 or hour > 23 or minute < 0 or minute > 59):
        return False
    else:
        return True


# function to check if day is valid against a tuple containing days of week
def is_day_valid(day_in):
    for i in day_list:
        if(i == day_in):
            return True

    return False


# function to display menu to user and returns user option
def display_menu():
    top_bar = "*" * 4
    print(top_bar + "Please select an option" + top_bar)
    print("{:>5d} Search for a Show".format(1))
    print("{:>5d} Edit a Show Name".format(2))
    print("{:>5d} Edit a Show Time".format(3))
    print("{:>5d} Edit a Show Day".format(4))
    print("{:>5d} Edit a Show Stage Number".format(5))
    print("{:>5d} Add a show".format(6))
    print("{:>5d} Delete a show".format(7))
    print("{:>5d} Display all shows".format(8))
    print("{:>5d} End".format(0))
    user_option = input()

    return user_option


# function to write show details to a text file
def write_to_file(shows_list):
    shows_file = open("shows.txt", "w")
    for shows in shows_list:
        shows_file.write("{0},{1},{2},{3},{4}\n".format(shows.__getattribute__('name'), shows.__getattribute__('start_time'),
                                                        shows.__getattribute__('end_time'), shows.__getattribute__('day'),
                                                        shows.__getattribute__('stage_no')))

    shows_file.close()


# Creates empty show list to store show objects
# Opens text file and reads each line
show_list = []
shows_file_lines = open("shows.txt", 'r').readlines()

# Splits each line and creates show abject from data
# Adds show object to shows list
for line in shows_file_lines:
    # Ignores line if line is blank and moves on to next one.
    # In case there is a white space between lines in the text file
    if (not line.isspace()):
        name, start, end, day, stage = line.split(',')
        show_list.append(Show(name, start, end, day, stage))

# tuple to hold days of the week
day_list = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# ORIGINALLY THE PROGRAM WAS CREATING DEFAULT OBJECTS AND WRITING OUT TO FILE
# WITHOUT READING THE DATA IN FROM A FILE
# THIS IS THE CODE THAT WAS USED

# creating default show objects
# show1 = Show("Vertigo", 1800, 2000, "Wednesday", 2)
# show2 = Show("Die Fiedermaus", 1700, 1900, "Saturday", 4)
# show3 = Show("Under The Influence", 1930, 2130, "Friday", 1)

# list holding Show objects
# show_list = [show1, show2, show3]

# writes show details to a text file
# write_to_file(show_list)

# continues to user presses 0 on menu to break
while 1:
    # displays menu to user
    option = display_menu()

    # Search for and dislpay a show
    if (option == "1"):
        # gets show name from user and converts to title case
        show_name = get_show()

        # finds show index in show list
        show = find_show(show_name)

        # displays show if it was found
        if (show is None):
            print("Sorry, show was not found")

        else:
            show = int(show)
            show_list[show].print_show()

    # Edit a show name
    elif (option == "2"):
        # gets show name from user and converts to title case
        show_name = get_show()

        # finds show index in show list
        show = find_show(show_name)

        # continues only if show was found in show list
        if (show is None):
            print("Sorry, " + show_name + " was not found")

        else:
            # asks user for new show name
            print("Please enter new show name: ")
            new_shw_name = input()
            new_shw_name = new_shw_name.title()

            show = int(show)

            # changes attribute in class then writes changes to file
            print("{0} name was successfully changed to {1}".format(show_name, new_shw_name))
            show_list[show].__setattr__('name', new_shw_name)
            write_to_file(show_list)

    # Edit a time for a show
    elif (option == "3"):
        # gets show user wishes to edit
        show_name = get_show()

        # finds show in show list
        show = find_show(show_name)

        # continues only if show was found in show list
        if (show is None):
            print("Sorry, " + show_name + " was not found")
        else:
            show = int(show)

            # Tries to execute block of code
            # catches error and displays message if user tries to enter a non integer number
            try:
                # Gets start time hour from user
                print("Please enter new start time hour: ")
                new_start_hr = input()
                new_start_hr = int(new_start_hr)

                # Gets start time min from user
                print("Please enter new start time min: ")
                new_start_min = input()
                new_start_min = int(new_start_min)

                # Gets end time hour from user
                print("Please enter new end time hour: ")
                new_end_hr = input()
                new_end_hr = int(new_end_hr)

                # Gets end time minute from user
                print("Please enter new end time minute: ")
                new_end_min = input()
                new_end_min = int(new_end_min)

            # catches value error if user enters non integer number
            except ValueError as error:
                print("Sorry, times must be integer format \n{}".format(error))

            else:
                # checks if time is a valid time
                if (is_time_valid(new_start_hr, new_start_min) and is_time_valid(new_end_hr, new_end_min)):
                    # Formats time to 4 characters long (24 hour format)
                    new_start = "{0:02d}{1:02d}".format(new_start_hr, new_start_min)
                    new_end = "{0:02d}{1:02d}".format(new_end_hr, new_end_min)

                    # Changes time to user desired time and writes to file
                    print("{} time was successfully changed".format(show_name))
                    show_list[show].__setattr__('start_time', new_start)
                    show_list[show].__setattr__('end_time', new_end)
                    write_to_file(show_list)

                # Displays error message to user if time is not valid
                else:
                    print("ERROR!! Please enter valid times in 24 hour format")

    # Edit a Shows day
    elif (option == "4"):
        # gets show user wishes to edit
        show_name = get_show()

        # finds show in show list
        show = find_show(show_name)

        # continues only if show is found in show list
        if (show is None):
            print("Sorry, " + show_name + " was not found")

        else:
            print("Please enter new day: ")
            new_day = input()
            new_day = new_day.title()

            # checks if day is valid and continues to change name if day is valid
            if (is_day_valid(new_day)):
                show = int(show)
                print("Day has been successfully changed from {0} to {1}".format(show_list[show].__getattribute__('day'), new_day))
                show_list[show].__setattr__('day', new_day)
                write_to_file(show_list)

            # Displays error message to user if day is not valid
            else:
                print("Error!! Please enter a valid day")

    # Edit a Shows stage number
    elif (option == "5"):
        # Gets show whose stage number the user wishes to edit
        show_name = get_show()

        # finds show in show list
        show = find_show(show_name)

        # continues only if show is found in show list
        if (show is None):
            print("Sorry, " + show_name + " was not found")

        else:
            show = int(show)

            # Tries to execute block of code
            # catches error and displays message if user tries to enter a non integer number
            try:
                print("Please enter new stage number: ")
                new_stage = input()
                new_stage = int(new_stage)

            except ValueError as error:
                print("ERROR! stage number must be in integer format \n{}".format(error))

            # continues to change stage number if there is no error
            else:
                print("Stage number has successfully been changed from {0} to {1}".format(show_list[show].__getattribute__('stage_no'), new_stage))
                show_list[show].__setattr__('stage_no', new_stage)
                write_to_file(show_list)

    # Add a new show
    elif (option == "6"):
        # gets show name from user and converts to title case
        new_shw_name = get_show()

        # Tries to execute block of code
        # catches error and displays message if user tries to enter a non integer number
        try:
            print("Please enter start time hour: ")
            new_start_hr = input()
            new_start_hr = int(new_start_hr)

            print("Please enter start time min: ")
            new_start_min = input()
            new_start_min = int(new_start_min)

            print("Pleas enter end time hour: ")
            new_end_hr = input()
            new_end_hr = int(new_end_hr)

            print("Please enter end time minutes: ")
            new_end_min = input()
            new_end_min = int(new_end_min)

            # Gets day from user and coverts to title case
            print("Please enter day: ")
            new_day = input()
            new_day = new_day.title()

            print("Pleass enter stage Number: ")
            new_stage = input()
            new_stage = int(new_stage)

        except ValueError as error:
            print("ERROR! Start and end times and stage number must be in integer format \n{}".format(error))

        else:
            # Checks if time is valid
            if(is_time_valid(new_start_hr, new_start_min) and is_time_valid(new_end_hr, new_end_min) and is_day_valid(new_day)):
                # Formats time to 4 characters long (24 hour format)
                new_start_tme = "{0:02d}{1:02d}".format(new_start_hr, new_start_min)
                new_end_tme = "{0:02d}{1:02d}".format(new_end_hr, new_end_min)

                # Creates and adds new show to show list and writes out to file
                print(new_shw_name + " was successfully added to timetable")
                show_list.append(Show(new_shw_name, new_start_tme, new_end_tme, new_day, new_stage))
                write_to_file(show_list)

            # Displays error message to user if day is not valid
            else:
                print("ERROR!! Please enter valid times in 24 hour format and a valid day")

    # Delete a Show
    elif (option == "7"):
        # gets show user wishes to delete and converts to title case
        show_name = get_show()

        # Finds show in show list
        show = find_show(show_name)

        # Continues only if show was found in list
        if (show is None):
            print("Sorry, {} was not found".format(show_name))

        else:
            # Makes sure user wants to carry through with deletion
            print("Are you sure you want to delete " + show_name + "? (yes or no)")
            sure = input()
            sure = sure.title()
            if (sure == 'Yes'):
                # Deletes show from list and writes new list to file
                show = int(show)
                print("{} was successfully deleted".format(show_name))
                show_list.remove(show_list[show])
                write_to_file(show_list)

    # Display all shows
    elif (option == "8"):
        # loop to display all shows in list
        for show in show_list:
            print("*" * 30)
            show.print_show()
            print("*" * 30)

    # End program
    elif (option == "0"):
        print("Thank you, goodbye!")
        break

    # Dislpays error message to user if option is not valid
    else:
        print("Error, Please select an option from the menu (0-8)")
