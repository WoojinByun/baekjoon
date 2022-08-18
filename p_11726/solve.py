

def solve(n):
    div_num = 10_007
    prev_num = 0
    cur_num = 1
    next_num = 1
    for i in range(n - 1):
        prev_num = cur_num
        cur_num = next_num
        next_num = prev_num + cur_num
        if next_num >= div_num:
            next_num -= div_num

    return next_num


def get_params():
    n = int(input())
    return n


def main():
    result = solve(get_params())
    print(result)


if __name__ == "__main__":
    main()
