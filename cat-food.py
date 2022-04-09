year = input('Enter the year')

if (int(year) >1799 and (int(year)< 1900)):
    if(int(year)>1869 and int(year)<1880 ):
        era='Seventies'
    century= 'Nineteenth Century'

else:
 century='Twenteeth Century'
print(century,era)





