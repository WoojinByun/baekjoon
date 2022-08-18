def solve(n):
    div_num = 10_007
    flag = -1
    cur_num = 1
    for i in range(n - 1):
        flag *= -1
        cur_num = (cur_num * 2 + flag) % div_num

    return cur_num


def get_params():
    n = int(input())
    return n


def main():
    result = solve(get_params())
    print(result)


if __name__ == "__main__":
    main()
