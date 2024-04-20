def add_chunks(chunks):
    cals: list = []
    calcount: int = 0
    for x in chunks:
        if x == "":
            cals.append(calcount)
            calcount = 0
        else:
            x = int(x)
            calcount += x
    print(max(cals))

def main(data):
    chunks = data.splitlines()
    add_chunks(chunks)

if __name__ == "__main__":
    main('**kwargs')
