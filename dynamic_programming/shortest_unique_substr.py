"""Smallest Substring of All Characters.

Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:
input:  arr = ['x','y','z'], str = "xyyzyzyx"
output: "zyx"
"""


class ShortestUniqueSubstring(object):
    def __init__(self):
        self.memory = {}

    def valid_string(self, arr, string):
        t = set(arr)
        for s in string:
            try:
                t.remove(s)
            except KeyError:
                continue
            if len(t) == 0:
                return True
        return False

    def getShortestUniqueSubstring(self, arr, string):
        if len(arr) == 0:
            return ''

        if len(string) < len(arr):
            return ''

        if self.valid_string(arr, string) is False:
            return ''

        s1 = string[1:]
        s2 = string[:-1]
        if s1 in self.memory:
            r1 = self.memory[s1]
        else:
            r1 = self.memory[s1] = self.getShortestUniqueSubstring(arr, s1)

        if s2 in self.memory:
            r2 = self.memory[s2]
        else:
            r2 = self.memory[s2] = self.getShortestUniqueSubstring(arr, s2)

        if r1 is '' and r2 is '':
            return string
        elif r1 is not '' and r2 is '':
            return r1
        elif r1 is '' and r2 is not '':
            return r2
        elif len(r1) < len(r2):
            return r1
        else:
            return r2

# arr = ['x','y','z']
# string = "xyyzyzyx"

arr = ['x', 'y', 'z']
string = "xypyzaxxxazzzzyaxxxxsssnawyzyyx"

su = ShortestUniqueSubstring()
print(su.getShortestUniqueSubstring(arr, string))
