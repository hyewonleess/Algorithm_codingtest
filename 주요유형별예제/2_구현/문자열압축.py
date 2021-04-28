# 책 solution (나중에 다시 풀어보기)
def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2+1):
        compress = ""
        start = s[:step]
        count = 1
        
        for j in range(step, len(s), step):
            if start == s[j:j+step]:
                count += 1
            else:
                compress += str(count)+start if count>=2 else start
                start = s[j:j+step]
                count = 1
        compress += str(count)+start if count>=2 else start
        answer = min(answer, len(compress))
    return answer
