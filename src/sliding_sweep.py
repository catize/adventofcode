def get_data(input):
    with open(input, 'r') as f:
        readdata = f.read().strip().split('\n')
        list_str = []
        for line in readdata:
            list_str.append(line)
        list = [int(i) for i in list_str]
    #print(len(list))
    return list

def calc_height_diff(list):
    height_list = []
    status = ['decreasing', 'increasing', 'no change']
    for number, number2, number3, number4 in zip(list[:-1], list[1:], list[2:], list[3:]):
        if ((number4 + number3 + number2) > (number3 + number2 + number)):
            height_list.append(status[1])
        elif ((number4 + number3 + number2) == (number3 + number2 + number)):
            height_list.append(status[2])
        else:
            height_list.append(status[0])
    print(len(height_list))
    return height_list


input = '/Users/Sina/github/adventofcode/data/sonarsweepdata'
list = get_data(input)
diff = calc_height_diff(list)
diff_count = diff.count('increasing')
print(f'the height is increasing {diff_count} times')



