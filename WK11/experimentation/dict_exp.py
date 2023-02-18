device = {
  "apples": 3,
  "model": 4
}
device.update({"apples" : device.get("apples") + 1})
print(device)
device.update({"apples" : device.get("apples") + 1})
print(device)
device.update({"banana" : device.get("banana") + 1})
print(device)