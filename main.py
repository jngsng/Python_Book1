import pandas as pd

a = pd.DataFrame([[23,"남","서울특별시"],
                  [53,"여","제주특별자치도"]],
                  index = ["A00301","D00809"],
                  columns = ["연령","성별","거주지"])

print(a)
print("\n")

a.rename(index={"A00301":"환자1","D00809":"환자2"}, inplace=True)

a.rename(columns={"연령":"AGE","성별":"GENDER","거주지":"ADDRESS"}, inplace=True)

print(a)
