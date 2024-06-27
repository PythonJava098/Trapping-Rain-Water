def elevation(list1):
    elevation = []
    max_alt = max(list1)

    for base in range(1, max_alt+1):
        data = []

        for num in list1:
            if num >= base:
                data.append(1)
            else:
                data.append(0)
        elevation.append(data)

    return elevation

def water_space(elevation):
    stack = []
    water = []

    for data in elevation:
        for num in data:
            if num == 0:
                if len(stack) > 0:
                    if stack[-1] >= 0:
                       stack.append(0)
                '''else:
                    continue'''
            elif num == 1:
                if len(stack) == 0:
                    stack.append(1)
                elif stack[-1] == 0:
                    total = stack.count(0)
                    water.append(total)
                    stack = [1]
        stack= []

    return sum(water)

def main():
    data = [4,2,0,3,2,5]

    list1 = elevation(data)
    for row in list1[-1::-1]:
        print(row)
    result = water_space(list1)
    print("Total spaces are: ",result)

main()
