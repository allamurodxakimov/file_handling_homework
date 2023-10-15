def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open("data/data07.txt")
    data=f.read()
    sum=0
    for i in range(len(data)):
        if data[i].isdigit():
            sum+=int(data[i])
    return sum
print(main("data07.txt"))