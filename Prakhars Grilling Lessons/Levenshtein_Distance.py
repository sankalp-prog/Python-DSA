# function LevenshteinDistance(char s[1..m], char t[1..n]):
def LevenshteinDistance(s, t):
    m = len(s)
    n = len(t)
#   // for all i and j, d[i,j] will hold the Levenshtein distance between
#   // the first i characters of s and the first j characters of t
#   declare int d[0..m, 0..n]
#   set each element in d to zero
    d = [[0] * (n + 1) for _ in range(m + 1)]
 
#   // source prefixes can be transformed into empty string by
#   // dropping all characters
#   for i from 1 to m:
#     d[i, 0] := i
    for i in range(1, m + 1):
      d[i][0] = i
 
#   // target prefixes can be reached from empty source prefix
#   // by inserting every character
#   for j from 1 to n:
#     d[0, j] := j
    for j in range(1, n + 1):
      d[j][0] = j
 
#   for j from 1 to n:
#     for i from 1 to m:
    for j in range(1, n + 1):
        for i in range(1, m + 1):

    #   if s[i] = t[j]:
    #     substitutionCost := 0
    #   else:
    #     substitutionCost := 1
            if s[i - 1] == t[j - 1]:
                substitutionCost = 0
            else:
               substitutionCost = 1

    #   d[i, j] := minimum(d[i-1, j] + 1,                   // deletion
    #                      d[i, j-1] + 1,                   // insertion
    #                      d[i-1, j-1] + substitutionCost)  // substitution
            d[i][j] = min(d[i-1][j] + 1,
                          d[i][j-1] + 1,
                          d[i-1][j-1] + substitutionCost)
 
#   return d[m, n]
    return d[m][n]

print(LevenshteinDistance("acd", "abd"))

# NEETCODE VIDEO SOLUTION:
def levenshtein_distance(word1, word2):
    cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

    for j in range(len(word2) + 1):
        cache[len(word1)][j] = len(word2) - j
    for i in range(len(word1) + 1):
        cache[i][len(word2)] = len(word1) - i

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                cache[i][j] = cache[i + 1][j + 1]
            else: 
                cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])

    return cache[0][0]

print(levenshtein_distance("abd", "acd"))