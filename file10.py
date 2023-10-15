def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open("data/data10.txt")
    data=f.read()
    l=data.split("\n")
    ls=[]
    for i in range(len(l)):
        ls.append(len(l[i]))
    ma=ls[0]
    for i in range(len(ls)):
        if ma<=ls[i]:
            ma=ls[i]
    return ma 
print(main("data10.py"))
# Read data from file