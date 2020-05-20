import RootFinder.Utils.constants as constants
import datetime;

class Formatter:

    def __init__(self):
        self.__strings = list()
        self.__start_time =datetime.datetime.now().timestamp()
        pass

    def add_entry(self, *vals):
        line = ""
        for i in vals:
            str_num = str(i)
            while len(str_num) < constants.DEFAULT_DIGITS:
                str_num += " "
            str_num += " | "
            line += str_num
        self.__strings.append(line)

    def display_steps(self):
        with open("../GUI/report.txt", 'w+') as file:
            for line in self.__strings:
                file.write(line)
                file.write("\n")
            file.write("Number of Iterations is "+ str(len(self.__strings) -1 )+ "\n")
            time = datetime.datetime.now().timestamp() - self.__start_time
            file.write("Execution time of the algorithm is "+ "{:0.5f}".format(time) + " seconds "+ "\n" )
            file.write("output precision is "+ str(constants.EPS))

