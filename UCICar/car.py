import csv
import pandas as pd

#这里使用pandas的工具，这是Python统计学分析工具
df = pd.read_csv('car.data.csv',sep=',')
head_name = df.columns.tolist()
print(head_name)
for i in range(len(head_name)):
    print(df[head_name[i]].value_counts())