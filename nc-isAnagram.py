# First Solution

def isAnagram(s: str, t: str) -> bool:
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    return True

if __name__ == '__main__':
    s = 'bbcc'
    t = 'ccbc'
    print(isAnagram(s, t))

# Second Soltuion:

def isAnagram(s: str, t:str) -> bool:
    countT, countS = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[s[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
