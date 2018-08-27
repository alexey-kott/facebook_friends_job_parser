if __name__ == "__main__":
    s = set()
    with open("users_backup.txt") as file:
        for line in file.readlines():
            link = line.split(';')[0].strip(' \n')
            if link in s:
                print(link)
            s.add(link)

    print(len(s))