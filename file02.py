def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open("data/data02.txt")
    data=f.read()
    return len(data)
print(main("data02.txt"))
# Read data from file