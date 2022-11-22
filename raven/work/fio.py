def readText(src: str):
    with open(src, 'r+') as file:
        txt = file.read()
    return txt

def writeText(dst: str, txt: str):
    with open(dst, 'w') as file:
        file.write(txt)
    file.close()
