# Author:   Sean Toman - L00136443
# Date:     07 Oct 017
# Desc:     A Class to hold name, start time, end time, day and stage number of Show


class Show:
    # Class for scheduled Shows

    def __init__(self, name, start_time, end_time, day, stage_no):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.day = day
        self.stage_no = stage_no

    def print_show(self):
        print("Show Name \t\t: {}".format(self.name))
        print("Start Time \t\t: {}".format(self.start_time))
        print("End Time \t\t: {}".format(self.end_time))
        print("Day \t\t\t: {}".format(self.day))
        print("Stage No \t\t: {}".format(self.stage_no))