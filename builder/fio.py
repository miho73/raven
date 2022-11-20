def readText(src):
    with open(src, 'r+') as file:
        txt = file.read()
    return txt

def writeText(dst, txt):
    with open(dst, 'w') as file:
        file.write(txt)
    file.close()
