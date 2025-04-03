namelist = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

name = input("Enter the name you are searching for. (Case Sensitive): ")

if name in namelist:
    print(f"{name} was in the list.")
else:
    print(f"{name} was not in the list.")