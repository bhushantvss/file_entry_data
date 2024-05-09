name = input("Enter  name ")

if name:

    with open(r"record.txt", "a") as e:

        e.write(name  + "\n")

show_info = input("Do you want to see all the user Y/N : ")

if show_info == 'y':

    try:
        with open(r"record.txt", 'r') as file:
            content = file.readlines()
    
    except Exception as e:
        print(e, type(e))
    
    else:

        for line in content:
            print(line)

else:
    print("thank You")