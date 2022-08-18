import sys


def get_params():
    N = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().split()))
    return N, nums


def solve(N, nums):
    sum_from_left = 0
    max_sum_from_left = 0
    max_idx_from_left = 0
    sum_from_right = 0
    max_sum_from_right = 0
    max_idx_from_right = -1
    for i in range(N):
        sum_from_left += nums[i]
        if max_sum_from_left < sum_from_left:
            print(max_sum_from_left, sum_from_left, 'aaa', i)
            max_sum_from_left = sum_from_left
            max_idx_from_left = i
        rev_i = (i * -1) - 1
        sum_from_right += nums[rev_i]
        if max_sum_from_right < sum_from_right:
            print(max_sum_from_right, sum_from_right, 'bbb', rev_i)
            max_sum_from_right = sum_from_right
            max_idx_from_right = rev_i
    print('a')
    print(max_sum_from_left)
    print(max_sum_from_right)

    return max_idx_from_left, max_idx_from_right, nums[max_idx_from_left:max_idx_from_right]


def main():
    result = solve(*get_params())
    print(result)


if __name__ == "__main__":
    main()
