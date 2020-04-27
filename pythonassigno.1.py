import pandas as pd
import numpy as np
import random as rd
'''
#1. How to import pandas and check the version?
import pandas as pd
print(pd.__version__)

#2. How to create a series from a list, numpy array and dict?
l=[1,2,3,7,5,8,9,9,6,5,6]
print(pd.Series(l))

dict1={
    "Name":["nikhil","Tejas","diya"],
    "Gender":["male","Male","Female"]
    }
print(pd.Series(dict1))
a=pd.Series(np.ramdom.rand(5))
print(a)

#3.How to convert the index of a series into a column of a dataframe?
dict1={
    "Name":["nikhil","Tejas","diya"],
    "Gender":["male","Male","Female"],
    "city":["Mumbai","Pune","USA"]
    }
df=pd.DataFrame(dict1)
print(df)
print(df.reset_index())
#5.How to assign name to the series’ index?
df.index.name="Index"
print(df)

#4.How to combine many series to form a dataframe?
l=[3,2,5,15,5,65,"nikhil"]
n=[3,5,45,52,5,6,"tejas"]
l=pd.Series(l)
n=pd.Series(n)
ln=pd.concat([l,n],axis=1)
print(ln)

#6. How to get the items of series A not present in series B?
l = pd.Series([5,3,6,41,2])
n = pd.Series([3,5,2,1,3])
ser1[~n.isin(sn)]

#7.How to get the items not common to both series A and series B?
l=[3,2,5,15,5,65,"nikhil"]
n=[3,5,45,52,5,6,"tejas"]
l=pd.Series(l)
n=pd.Series(n)
ln=pd.DataFrame(list(set(l).symmetric_difference(set(n))))
print(ln)

#8.How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
df=pd.read_csv("D:\\python codes\\Automobile_data.csv")
q=df.describe()
print(q)


#9.How to get frequency counts of unique items of a series?
l=[3,2,5,15,5,65,"nikhil"]
l=pd.Series(l)
print(l.value_counts())

#10.How to keep only top 2 most frequent values as it is and replace everything else as‘Other’?

l=[3,2,3,5,3,5,15,5,65,"nikhil"]
l=pd.Series(l)
n=l.value_counts()
print(n)
print("top 2 most frequent values",n.head(2))
#(l.value_counts().index[2:])="Others"
#print(l)

#11.How to bin a numeric series to 10 groups of equal size?
l=[*range(21)]
l=pd.Series(l)
print(pd.cut(l,10))


#12. How to convert a numpy array to a dataframe of given shape? (L1)

a=np.array([[10,20],[30,40]])
print(a)
a2=pd.DataFrame(a)
a2=pd.DataFrame(a,columns=["One","Two"])
print(a2)


#13.How to find the positions of numbers that are multiples of 3 from a series?
#Error
l=[*range(21)]
l=pd.Series(l)
print(1)
r=np.argwhere(l % 3==0)
print(r)


#14. How to extract items at given positions from a series?
l=[rd.randint(1,50) for i in range(10)]
n=pd.Series(l)
pos=[0,2,4,6,8]
print(n)
r=n.take(pos)
print("Positions values are\n",r)



#15. How to stack two series vertically and horizontally ?
#Not understood the question

#16. How to get the positions of items of series A in another series B?

l=[rd.randint(1,21) for i in range(20)]
A=pd.Series(l)
B=pd.Series([1,6,5,18,4,12,3])
print(A)
r=A.take(B)
print("Positions values are\n",r)


#17. How to compute the mean squared error on a truth and predicted series?
#Not undershood


#18.How to convert the first character of each element in a series to uppercase?
rand=["nikhil","tejas","ramgiri","goa","mumbai"]
a=pd.Series(rand).str.title()
print(a)



#19.How to calculate the number of characters in each word in a series?

rand=["nikhil","tejas","ramgiri","goa","mumbai"]
a=pd.Series(rand)
print(a)
print(a.str.len())

#20.How to compute difference of differences between consequtive numbers of a series?
l=[rd.randint(1,21) for i in range(10)]
n=pd.Series(l)
print(n)
n2=np.diff(n)
print(n2)


#21.How to convert a series of date-strings to a timeseries?

l=['04/23/20', '1/04/20', '2/04/20', '3/04/20', '13/04/20',]
l=pd.Series(l)
n= pd.to_datetime(l)
print(n)


#22.How to get the day of month, week number, day of year and day of week from a series ofdate strings?
l=['04/23/20', '1/04/20', '2/04/20', '3/04/20', '13/04/20',]
l=pd.Series(l)
l= pd.to_datetime(l)
print(l.dt.day.tolist())
print("Day of year:")
print(l.dt.dayofyear.tolist())
print("Week number:")
print(l.dt.weekofyear.tolist())
print("Day of week:")
print(l.dt.weekday_name.tolist())


#23.How to convert year-month string to dates corresponding to the 4th day of the month
#Not understood

#24.How to filter words that contain atleast 2 vowels from a series
#import re
#ss=("one", "two", "three", "hundred", "thousand")
#ss[len(re.findall("[aeiou]",ss))]
#25.How to filter valid emails from a series?
e=["nkhilramgiri@gmail.con","cjbhdsajbc","njdshngmail.com","tej@yahoo.com"]
e=pd.Series(e)
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]'
print(e.str.findall(pattern))


#26. How to get the mean of a series grouped by another series?
name=pd.Series(np.random.choice(["Nikhil","Tejas","Vidhya","Gopi"],12))
ages=pd.Series(rd.randint(1,60) for i in range(12))
print(ages.groupby(name).mean())


#27. How to compute the euclidean distance between two series?
l=pd.Series(rd.randint(0,100) for i in range(10))
n=pd.Series(rd.randint(0,100) for i in range(10))
print(sum((l-n)**2)**0.5)

#28. How to find all the local maxima (or peaks) in a numeric series?
#Not Understood
#29. How to replace missing spaces in a string with the least frequent character?
'''
#l=['nas ca cscc jhksak']
n=pd.Series(list('nas ca cscc jhksak'))
print(n)
count=n.value_counts()
last= count.index[-1]
#least_freq = freq.dropna().index[-1]
print("".join(n.replace(" ",last)))



















































