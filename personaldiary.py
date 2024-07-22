def write_diary():
    with open("diary.txt", "a") as file:
        entry = input("Write your diary entry: ")
        file.write(entry + "\n")

def read_diary():
    with open("diary.txt", "r") as file:
        entries = file.readlines()
        for entry in entries:
            print(entry)

if __name__ == "__main__":
    while True:
        choice = input("Do you want to (1) write or (2) read your diary? ")
        if choice == '1':
            write_diary()
        elif choice == '2':
            read_diary()
        else:
            break
