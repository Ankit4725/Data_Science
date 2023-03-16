key_location = "chair"
location = ["garbage" , "living room" , "chair" , "closet"]
for key in range(len(location)):
    if key_location == location[key]:
        print("Key found in ",location[key])
        break 
    else:
        print("Key not found in ",location[key])
