# my solution
n = int(input())
words = []
for _ in range(n):
    words.append(input())

words.sort(key = lambda x: (len(x), x))

uni = []
for w in words:
    if w not in uni:
        uni.append(w)
        
for i in uni:
    print(i)
    
    
# more simple solution
n = int(input())

words = set() # set 선언
for _ in range(n):
    words.add(input())
    
words = list(words) # unique한 값만 남겨놓기
words.sort() # 1차 정렬: 알파벳순
words.sort(key = lambda x: len(x)) # 2차 정렬: 길이순

print('\n'.join(words))
