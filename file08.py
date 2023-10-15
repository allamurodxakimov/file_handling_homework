def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open("data/data08.txt")
    data=f.read()
    ls=[]
    for i in range(len(data)):
        if data[i].isdigit():
            ls.append(int(data[i]))
    ma=ls[0]
    for i in range(len(ls)):
        if ma<=ls[i]:
            ma=ls[i]
    return ma
print(main("data08.txt"))