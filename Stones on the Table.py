def min_stones_to_remove(n, s):
    count = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            count += 1
    return count
n = int(input())
s = input()
print(min_stones_to_remove(n, s))
