month = int(input("Enter a moth"))
if month >= 3 and month <= 5:
    print("spring")
elif month >= 6 and month <=8:
    print("summer")
elif month >= 9 and month <=11:
    print("autum")
elif month == 12 or month == 1 or month == 2:
    print("winter")
else:
    print("invaild month")
bool((4==4) == bool("4" == "4"))