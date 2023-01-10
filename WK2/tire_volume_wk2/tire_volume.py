from datetime import datetime
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

    return final_path
#Function end

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))
current_date_and_time = datetime.now()

v = math.pi * w**2 * a * (w * a + 2540 * d) / 10000000000
print(f"{current_date_and_time:%Y-%m-%d}, {w:.2f}, {a:.2f}, {d:.2f}, {v:.2f}")
print(f"The approximate volume is {v:.2f} liters")

with open(buildPath("volumes.txt"), "at") as volumes_file:
    #Note that absolute path is built dinamycally with the function I created
    print(f"{current_date_and_time:%Y-%m-%d}, {w:.2f}, {a:.2f}, {d:.2f}, {v:.2f}", file=volumes_file)