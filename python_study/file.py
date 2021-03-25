# r:읽기, a: 생성 혹은 덧붙이기, w: 기존 파일 대체
# ..: 상대경로, .: 절대경로


# f = open('./python_study/resource/review.txt', 'r')
# content=f.read()
# print(content)
# f.close

import csv
import pandas as pd
# w=[[1,2],[3,4],[5]]

# with open('./python_study/resource/sample3.csv','w',newline='')as f:
#     wt= csv.writer(f)
#     for v in w:
#         wt.writerow(v)


# with open('./python_study/resource/sample1.csv','r') as f:
#     reader=csv.DictReader(f)
#     for c in reader:
#         print(c)

# with open('./python_study/resource/sample2.csv','r') as f:
#     reader=csv.reader(f,delimiter='|')
#     for v in reader:
#         print(v)

# xlsx=pd.read_excel('./python_study/resource/sample.xlsx')
# print(xlsx)
# xlsx.to_excel('./python_study/resource/result.xlsx', index=False)
# xlsx.to_csv('./python_study/resource/result.csv', index=False)
