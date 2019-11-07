import pandas as pd

path = "Year_2_Data.xlsx"
p = 3 #Excel Sheet Number - 1
df = pd.read_excel(path, p,None)
start = 0 #Constant
end = 456 # ~N Vector size for number of rows of raw data, simultaneous update for each post
out = ""
jackass_c1 = ["हर्षित धेतरवाल","Dhananjay Kaushal","Deepanshu Rao","Srijan Rai"] #Reacting Haha, throwing off the data
jackass_c2 = [] #No outliers, Data is consistent
jackass_c3 = ["Aman Malik For Hindu College's Prime Minister","Community · Political Candidate","Vishnu Prathap","Divyansh Agrawal","Raju Biswas","Hari Kanojia"] #The page liking its own post, reacting haha, throwing the data off
for i in range(start,end):
    keyx = df.iloc[i] #Row Vector
    key = str(keyx[0])#Column Vector
    f = str(key).find("mutual") #Not a name
    g = str(key).find("Message")#Not a name
    h = str(key).find("Follow") #Not a name
    if f < 0 and g<0 and h<0 and key not in jackass_c3:
        out += str(key) + "\n" #Value accepted as a name
print (out)