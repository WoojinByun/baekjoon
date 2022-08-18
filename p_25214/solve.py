def get_params():
    N = int(input())
    nums = list(map(int, input().split()))
    return N, nums


def solve(N, nums):
    min_val = nums[0]
    max_val = nums[0]
    cur_max_val = 0
    for i in range(N):
        n = nums[i]
        if max_val < n or cur_max_val < n - min_val:
            if max_val < n:
                max_val = n
            cur_max_val = n - min_val
        if min_val > n:
            min_val = n
        print(cur_max_val, end=' ' if i < N - 1 else '\n')


def main():
    solve(*get_params())


if __name__ == "__main__":
    main()
