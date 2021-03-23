# r:읽기, a: 생성 혹은 덧붙이기, w: 기존 파일 대체
# ..: 상대경로, .: 절대경로


f = open('./resource/review.txt', 'r')
content=f.read()
print(content)
f.close


