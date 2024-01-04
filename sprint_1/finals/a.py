# https://contest.yandex.ru/contest/22450/run-report/102605198/
import sys
from typing import Generator


def read(delimiter: str = ' ', chunk_size: int = 16384) -> Generator[str, None, None]:
    while True:
        result = sys.stdin.readline(chunk_size)
        len_result = len(result)
        if len_result == chunk_size:
            c = sys.stdin.read(1)
            while c != delimiter and c != '\n':
                result += c
                c = sys.stdin.read(1)
        yield result.rstrip()
        if len_result < chunk_size:
            break


def get_zero_positions_and_count() -> tuple:
    zeros_positions = []
    zeroes_number = 0
    current_index = 0

    for chunk in read():
        nums = chunk.split()
        for a in nums:
            if a == '0':
                zeros_positions.append(current_index)
                zeroes_number += 1
            current_index += 1

    return zeros_positions, zeroes_number


def print_distances(zeros_positions: list, zeroes_number: int, n: int) -> None:
    for i in range(zeros_positions[0] + 1):
        print(zeros_positions[0] - i, end=' ')

    if zeroes_number > 1:
        closest_right = zeros_positions[0]
        closest_left = zeros_positions[1]
        closest_left_position = 1

        for i in range(zeros_positions[0] + 1, zeros_positions[-1] + 1):
            if i != closest_left:
                print(min(i - closest_right, closest_left - i), end=' ')
            else:
                print(0, end=' ')
                if i == zeros_positions[-1]:
                    break
                closest_left_position += 1
                closest_right = closest_left
                closest_left = zeros_positions[closest_left_position]

    for i in range(zeros_positions[-1] + 1, n):
        print(i - zeros_positions[-1], end=' ')


n = int(input())
zeros_positions, zeroes_number = get_zero_positions_and_count()
print_distances(zeros_positions, zeroes_number, n)
