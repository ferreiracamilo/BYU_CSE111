import math

manufactured_items_qty = int(input("Indicate how many items were manufactured"))
capacity_box_qty = int(input("Indicate how many items fit in a box"))

boxes_needed = math.ceil(manufactured_items_qty/capacity_box_qty)

print(boxes_needed)
#For 8 items, packing 5 items in each box, you will need 2 boxes.