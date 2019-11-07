import pandas as pd

path = "Final_Admissions.xlsx"

df = pd.read_excel(path, 0,None)
start = 2
end = 73375
filex = open("Script1.txt","r+")
clg = "Hindu College"
out = ""
for i in range(start,end-1):
    print (str((i/end)*100))
    keyx = df.iloc[i]
    key = str(keyx[7])
    if key == clg:
        out += str(keyx[1]) + "\t" + str(keyx[6]) + "\t" + str(keyx[3]) + "\t" + str(keyx[10]) + "\n"

resultString = filex.read()
filex.write(out)
filex.close()