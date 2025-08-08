def filereader(filename):
    with open(filename) as f:
        for i in f:
            print(i.strip())

def main():
    filereader("file.txt")


if __name__ == "__main__":
    main()