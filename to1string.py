
def to1str1(filename):
    f  = open(filename, "r", encoding="UTF-8")
    sol = ""
    for s in f.readlines():
        sol += s[:-1] + '\\n'
    return sol

if __name__ == "__main__":
    fr = input("from: ")
    # print(to1str1(fn))
    to = input("to: ")
    tow = to1str1(fr)
    print(tow)
    t = open(to, "w")
    t.write(tow)
    t.close()


