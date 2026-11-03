import os


try:
    with open ('DOB.txt', 'r') as file:
        lines = file.readlines()

    names = []
    birthdates = []

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        parts = line.split()

        name = " ".join(parts[0:2])
        dob = " ".join(parts[2:])

        names.append(name)
        birthdates.append(dob)

    print("Names :")
    for name in names:
        print(name)

    print("\nBirthdates :")
    for dob in birthdates:
        print(dob)

except FileNotFoundError:
    print("The file does not exist. Please check the file path and try again.")
