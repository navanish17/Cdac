try:
    with open("name.txt") as f:
        for line in f:
            try:
                num = int(line)
                print("Number:", num)
            except ValueError:
                print(f"this is the string: {line}")
except FileNotFoundError:
    print("File does not exist")