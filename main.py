import pandas as pd

data = {"성명" : ["이겨례", "조약돌"],
       "나이" : [25, 19], "성별" : ["남", "여"],
       "키" : [185, 163], "체중" : [89, 53]}

df = pd.DataFrame(data)

print(df)
print("\n")

df["BMI"] = 0
print(df)
print("\n")

df.loc[2] = 0

print(df)
print("\n")

df.loc[3] = ["강산애",27,"남",177,63,0]

print(df)
print("\n")

# df.loc[x] // x 데이터를 추가 행에 넣음
df.loc["추가"] = df.loc[3]

print(df)
print("\n")