def longest_common_subsequence(str1, str2):
    # Write your code below
    long_string = str1 if len(str1) > len(str2) else str2
    short_string = str1 if len(str1) < len(str2) else str2

    l1 = len(long_string)
    l2 = len(short_string)

    subseq = [[""] * (l1 + 1) for _ in range(l2 + 1)]

    for i in range(l2-1, -1, -1):
        for j in range(l1-1, -1, -1):
            if short_string[i] == long_string[j]:
                subseq[i][j] = short_string[i] + subseq[i+1][j+1]
            else:
                subseq[i][j] = subseq[i+1][j] if len(subseq[i+1][j]) > len(subseq[i][j+1]) else subseq[i][j+1]
    return subseq[0][0]

# Test Cases
str1 = input()
str2 = input()

print(longest_common_subsequence(str1, str2))