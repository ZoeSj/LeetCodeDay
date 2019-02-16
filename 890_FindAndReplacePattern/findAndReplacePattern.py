# @File    : findAndReplacePattern.py
# @Date    : 2019-02-15
# @Author  : shengjia

# words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
words = ["badc", "abab", "dddd", "dede", "yyxx"]

# words = ["bab"]
pattern = "baba"


def numForPattern(pattern, words):
    p = []

    def F(word):
        m = {}
        return [m.setdefault(c, len(m)) for c in word]

    for w in words:
        if F(w) == F(pattern):
            p.append(w)

    return p


print (numForPattern(pattern, words))
