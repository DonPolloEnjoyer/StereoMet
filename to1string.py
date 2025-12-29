
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

# https://t4.bcbits.com/stream/9d08612d623926f7886c9330ccc4b143/mp3-128/1742058719?p=0&ts=1767044503&t=00ade78aa4ebbb7dcf74eb52a62b21a6c9d33d10&token=1767044503_bd5645e3d0a01c8487a45f850b4c1ea425801edf
