def add_chunks(chunks):
    cals: list = []
    calcount: int = 0
    y: int = 0
    for x in chunks:
        if x == "":
            cals.append(calcount)
            calcount = 0
        else:
            x = int(x)
            calcount += x
    cals.append(calcount)
    cals = sorted(cals)
    print(cals)
    cals = cals[::-1]
    cals = cals[:3]
    print(cals)
    for x in cals:
        y += x
    return y
    



def main(data):
    chunks = data.splitlines()
    print(add_chunks(chunks))

if __name__ == "__main__":
    main('**kwargs')

