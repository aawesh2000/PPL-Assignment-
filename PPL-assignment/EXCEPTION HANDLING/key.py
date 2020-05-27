d = {"a":1,"b":2,"c":3}
try:
    print(d["c"])                  #trying to fetch value for key which does not exist
except LookupError:                  #looking for key which is not present which raises exception
    print("key does not exist")
