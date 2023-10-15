def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open("data/data05.txt")
    data=f.read()
    s=0
    c=0
    for i in range(len(data)):
        if data[i].isdigit():
            s+=1
        else:
            c+=1
    return [s,c]
print(main("data05.txt"))
# Read data from file