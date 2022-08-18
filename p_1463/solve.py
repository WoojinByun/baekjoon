
min_val_dict = {1: 0, 2: 1, 3: 1}


def get_min_val(num):
    if num in min_val_dict:
        return min_val_dict[num]
    min_vals = [
        get_min_val(num // 3) + num % 3,
        get_min_val(num // 2) + num % 2
    ]
    min_val = min(min_vals) + 1
    min_val_dict[num] = min_val
    return min_val


def solve(n):
    return get_min_val(n)


def get_params():
    n = int(input())
    return n


def main():
    result = solve(get_params())
    print(result)


if __name__ == "__main__":
    main()
