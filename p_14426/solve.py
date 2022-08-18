import sys


def solve(N, S, words):
    result = 0
    S = sorted(S)
    for word in words:
        if is_word_prefix(word, S, N):
            result += 1

    return result


def is_word_prefix(word, str_list, length):
    left_idx = 0
    right_idx = length - 1
    found_idx = 0
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        target_word = str_list[mid_idx]
        if word <= target_word:
            right_idx = mid_idx - 1
            found_idx = mid_idx
        else:
            left_idx = mid_idx + 1

    return str_list[found_idx].startswith(word)


def get_params():
    rl = sys.stdin.readline
    N, M = map(int, rl().strip().split())
    S = [rl().strip() for _ in range(N)]
    words = [rl().strip() for _ in range(M)]
    return N, S, words


def main():
    result = solve(*get_params())
    print(result)


if __name__ == "__main__":
    main()
