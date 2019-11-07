import pandas as pd

path = "Year_2_Data.xlsx"

df = pd.read_excel(path, "Sheet9",None)
start = 0
end = 1613

out = ""
name = []
times = []
for i in range(start,end):
    keyx = df.iloc[i]
    key = str(keyx[0])
    if key in name:
        m = name.index(key)
        p = times[m]
        times[m] = p+1
    else:
        name.append(key)
        times.append(1)
out = ""
for q in range(len(name)):
    out += name[q] + "\t" + str(times[q]) + "\n"
print(out)
