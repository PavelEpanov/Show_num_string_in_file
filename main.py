def main():

    num = int(input("'1' - Создать новый файл, '2' - прочитать файл: "))

    if num == 1:
        create_file()
        read_file()
    else:
        read_file()


def read_file():
    name_of_file = input("Введи название файла без расширения: ")
    name_of_file = name_of_file + ".txt"

    myfile = open(name_of_file, "r")

    track = 1

    string = myfile.readline()

    while string != "":
        info = string
        info = info.strip("\n")
        print(f"{track}:  {info}")
        track += 1
        string = myfile.readline()

    myfile.close()


def create_file():

    name_of_file = input(
        "Введи название файла без расширения, чтобы создать файл: ")
    name_of_file = name_of_file + ".txt"

    myfile = open(name_of_file, "w")

    myfile.write(input("Введи информацию: "))
    myfile.write("\n")

    num = int(
        input("'1' - Ввести ещё информацию, '2' - Перестать вводить информацию: "))

    while num == 1 and num != 2:

        myfile.write(input("Введи информацию: "))
        myfile.write("\n")
        num = int(
            input("'1' - Ввести ещё информацию, '2' - Перестать вводить информацию: "))

    myfile.close()


def check_num(data):
    while data != 1 or data != 2:
        print("Введите либо '1', либо '2'")
        data = int(
            input("'1' - Ввести ещё информацию, '2' - Перестать вводить информацию: "))


main()
