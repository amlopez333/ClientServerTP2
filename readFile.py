def readLine(i):
    with open("fortunes.txt") as fortunes:
        for x, line in enumerate(fortunes):
            if i == x:
                return line


