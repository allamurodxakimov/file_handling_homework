def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open("data/data01.txt")
    data=f.read().split(",")
    ls=[]
    for i in data:
        ls.append(int(i))
    return ls
print(main("data01.txt"))

# Read data from file