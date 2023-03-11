def solution(s):
    s = s.lower()
    result = ""
    for i in range(len(s)):
        if "a" <= s[i] <= "z":
            if i == 0:
                result += s[i].upper()
            else:
                if s[i-1] == ' ':
                    result += s[i].upper()
                else:
                    result += s[i] 
        else:
            result += s[i]
            
    return result