def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open("data/data09.txt")
    data=f.read()
    ls=[]
    for i in range(len(data)):
        if data[i].isdigit():
            ls.append(int(data[i]))
    mi=ls[0]
    for i in range(len(ls)):
        if ls[i]<=mi:
            mi=ls[i]
    return mi
print(main("data09.txt"))
# Read data from file