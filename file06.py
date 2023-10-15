def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open("data/data06.txt")
    data=f.read()
    l=data.split()
    ls=[]
    for i in range(len(l)):
        ls.append(len(l[i]))
    return ls
print(main("data06.txt"))
# Read data from file