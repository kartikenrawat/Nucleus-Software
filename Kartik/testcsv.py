from numpy import fabs
import pandas as pd

# path giving
df = pd.read_csv(r"D:\Kartik\kartik.csv")

# replace NAN
df.fillna("", inplace=True)

# fetch csv
print(df)

name = input("enter your desired name: ")

total_VoIP = (
    df.loc[df["Name"] == name, "Duration"].loc[df["Audio Type"] == "VoIP"].sum()
)
total_not_VoIP = (
    df.loc[df["Name"] == name, "Duration"].loc[df["Audio Type"] != "VoIP"].sum()
)


total_VoIP = total_VoIP.replace("mins", " ")
total_VoIP = total_VoIP.replace("min", " ")

total_not_VoIP = total_not_VoIP.replace("mins", " ")
total_not_VoIP = total_not_VoIP.replace("min", " ")

# copy to array from string
arr = total_VoIP.split()
arr_not_voip = total_not_VoIP.split()
print(arr)

# Array sum
sum = 0
sum_not_voip = 0
for x in arr:
    sum = int(sum) + int(x)

for x in arr_not_voip:
    sum_not_voip = sum_not_voip + int(x)

# filter
print(
    df[["Audio Type", "Name", "Email", "Duration"]]
    .loc[df["Audio Type"] == "VoIP"]
    .loc[df["Name"] == name]
    .assign(Total=sum)
)

print("Total sum of duration for VoIP=", sum)
print("\n")

print(
    df[["Audio Type", "Name", "Email", "Duration"]]
    .loc[df["Audio Type"] != "VoIP"]
    .loc[df["Name"] == name]
    .assign(Total=sum_not_voip)
)

print("Total sum of duration for NOT_VoIP=", sum_not_voip)

result = pd.DataFrame(
    df[["Audio Type", "Name", "Email"]]
    .loc[df["Name"] == name]
    .loc[df["Audio Type"] == "VoIP"]
)
result.to_csv(r"D:\Kartik\result.csv", index=False)
