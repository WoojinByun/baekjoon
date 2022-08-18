import sys


class Node():

    def __init__(self, id):
        self.id = id
        self.trust_nodes_count = 0

    def __str__(self):
        return f'Node = {self.id}, count = {self.trust_nodes_count}'


def get_params():
    N, _ = map(int, )
    nums = list(map(int, sys.stdin.readline().split()))
    return N, nums


def solve(N, nums):
    from_node, to_node = sys.stdin.readline().split()
    result = 0
    for i in range(N):
        deq.push(i + 1)
    for num in nums:
        dist = deq.find_distance(num)
        deq.roll(dist)
        deq.pop(is_right=False)
        result += abs(dist)
    return result


def main():
    N, nums = get_params()
    result = solve(N, nums)
    print(result)


if __name__ == "__main__":
    main()
