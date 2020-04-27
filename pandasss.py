df.head(5)#1

df.tail(5)

df.replace("?","N.A")#2

df.replace('n.a',"N.A")


df[["company","price"]].sort_values("price",ascending=False).head(1)#3


df1=df.groupby("company")#4
>>> df1.get_group("toyota")


df.company.value_counts()#5

 df.groupby("company")[["company","price"]].max()#6

 df.groupby("company")[["company","average-mileage"]].mean()#7

 df.sort_values(by="price",ascending=False).head(5)#8

#9
 GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price':
[23845, 171995, 135925 , 71400]}
>>> df1=pd.DataFrame(GermanCars)
>>> df1

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '],
'Price': [29995, 23600, 61500 , 58900]}
>>> df2=pd.DataFrame(japaneseCars)
>>> df2

df3=pd.concat([df1,df2],keys=["GermanCar","Japanesecars"])
>>> df3



#10
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price':
[23845, 17995, 135925 , 71400]}
>>> c=pd.DataFrame(Car_Price)
>>> c


car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
'horsepower': [141, 80, 182 , 160]}
>>> d=pd.DataFrame(car_Horsepower)
>>> d

e=pd.merge(c,d)
>>> e











