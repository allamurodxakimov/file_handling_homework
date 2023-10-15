def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open("data/data03.txt")
    data=f.read()
    ls=[]
    for i in range(len(data)):
        if data[i].isdigit():
            ls.append(data[i])
    return ls
print(main("data03.txt"))
# Read data from file
