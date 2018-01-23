import numpy as np


def deletion_distance(str1, str2):
    distances = np.zeros([len(str1) + 1, len(str2) + 1])

    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if i == 0:
                distances[i][j] = j
            elif j == 0:
                distances[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                # str1[i] != str2[j]
                distances[i][j] = 1 + min(
                    distances[i][j - 1],
                    distances[i - 1][j]
                )

    return distances[len(str1)][len(str2)]

str1 = 'frog'
str2 = 'dog'
# expected 'og' => 3
print(deletion_distance(str1, str2))
