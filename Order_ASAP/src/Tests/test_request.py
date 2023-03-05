import pytest
from src.classes.Request import *
def main():
    request0 = Request(1,"water_bottle")
    request1 = Request(2,"water_bottle")
    print(request0.get_idx)
    #print(request0.get_id)
    #print(request1.get_id)