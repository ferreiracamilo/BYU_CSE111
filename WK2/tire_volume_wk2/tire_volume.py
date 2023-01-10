import math
import os

#Function start
def buildPath(file_name):
    #I am utilizing a github repo to save my assignment and I jump from time to time from Windows to Mac OS. The path will not be exactly the same, that is why I built this function
    dir_path = os.path.dirname(os.path.realpath(__file__)) #retrieve root folder for py file
    final_path = ""

    #Review if how to proceed for next node based on previous slash or backslash presence
    if dir_path.find("/") != -1:
        final_path = dir_path + "/" + file_name
    elif dir_path.find("//") != -1:
        final_path = dir_path + "//" + file_name
    elif dir_path.find("\\") != -1:
        final_path = dir_path + "\\" + file_name
#Function end

pai = math.pi
w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = pai * w**2 * a * (w * a + 2540 * d) / 10000000000
print(f"Volume is {v:.2f}")