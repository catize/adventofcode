


def get_data(input):
    with open(input, 'r') as f:
        readdata = f.read().strip().split('\n')
        list_str = []
        for line in readdata:
            list_str.append(line.split(' '))
        for pair in list_str:
            pair[1] = int(pair[1])
        #print(list_str)
    return list_str

def forward(horizontal, x):
    horizontal += x
    return horizontal

def up(depth, x):
    depth -= x
    return depth

def down(depth, x):
    depth += x
    return depth

def multiply(horizontal, depth):
    product = horizontal * depth
    return product

def calc_motion(list):
    horizontal = 0
    depth = 0
    for motion in list:
        #print(motion)
        if motion[0] == 'forward':
            horizontal = forward(horizontal, motion[1])
        elif motion[0] == 'down':
            depth = down(depth, motion[1])
        else:
            depth = up(depth, motion[1])
    print(horizontal, depth)
    results = {'horizontal': horizontal, 'depth': depth}
    return results, horizontal, depth


list = get_data('/Users/Sina/github/adventofcode/data/navi_data')
result, horizontal, depth = calc_motion(list)
mult = multiply(horizontal, depth)
print(mult)



