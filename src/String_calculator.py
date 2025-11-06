def Add(string: str) -> int:
    if string == "":
        return 0
    if "," in string:
        parts = string.split(",")
        return int(parts[0]) + int(parts[1])
    return int(string)
#