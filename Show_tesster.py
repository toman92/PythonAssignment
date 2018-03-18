# Author:   Sean Toman
# Date:     07/10/2017
# Desc:     A program to test the Show class


from Show import Show

show1 = Show("vertigo", 1830, 2100, "wednesday", 2)
show2 = Show("die fiedermaus", 1800, 2030, "friday", 1)
show3 = Show("under the influence", 1830, 2100, "wednesday", 4)

show_list = [show1, show2, show3]

show_list.append(Show("New Show", 1830, 2100, "wednesday", 3))

bar = "*" * 5

for i in show_list:
    num = 0
    print("Show {}".format(num + 1))
    print("Show name: {}".format(i.name))
    print("Start time: {}".format(i.start_time))
    print("End Time: {}".format(i.end_time))
    print("Day: {}".format(i.day))
    print("Stage: {}".format(i.stage_no))

