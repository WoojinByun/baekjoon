import sys


class DequeWoojin():

    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def push(self, value, is_right=True):
        if is_right:
            self._list.append(value)
        else:
            self._list.insert(0, value)

    def pop(self, is_right=True):
        if is_right:
            return self._list.pop()
        else:
            return self._list.pop(0)

    def peek(self, is_right=True):
        if is_right:
            return self._list[-1]
        else:
            return self._list[0]

    def roll(self, amount):
        for _ in range(abs(amount)):
            self.push(self.pop(amount < 0), amount > 0)

    def find_distance(self, value):
        if self.peek(0) == value:
            return 0

        target_idx = 1
        flag = 1

        while True:
            if self._list[target_idx * flag] == value:
                break
            flag *= -1
            if flag == 1:
                target_idx += 1
        return target_idx * flag

    def __str__(self):
        return ' '.join(map(str, self._list))


def get_params():
    N, _ = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    return N, nums


def solve(N, nums):
    result = 0
    deq = DequeWoojin()
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
