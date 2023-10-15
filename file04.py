def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open("data/data04.txt")
    data=f.read()
    ls=[]
    for i in range(len(data)):
        if data[i].isdigit():
            continue
        else:
            ls.append(data[i])
# Read data from file
    return ls
print(main("data04.txt"))