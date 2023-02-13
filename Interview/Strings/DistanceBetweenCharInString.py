def distance(input, char):
    first = -1
    second = -1
    if char not in input:
        print("absent")
        return -1
    else:
        for i, c in enumerate(input):
            if c == char:
                if i == -1:
                    first = i
                    second = i
                else:
                    second = i

    if second == -1:
        return second
    else:
        return second - first - 1


print(distance("a_____a", "a"))
