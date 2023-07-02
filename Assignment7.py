def write_read_data(roll_number, name, class_name, file="data.txt"):
    try:
        f = open(file, "a") 
        f.writelines([roll_number + "\n", name + "\n", class_name + "\n"])

        f = open(file, "r")
        data = f.readlines()
        for line in data:
            print(line)
    except IOError as e:
        print("An error occurred while accessing the file:", e)


write_read_data("25", "Tejas", "Class 12")


