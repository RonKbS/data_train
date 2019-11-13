import numpy as np
import pandas as pd

'''
# convert series to df with index as other column
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

df = ser.to_frame().reset_index()
print(df.head())
'''

'''
# combine many series to form df
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df = pd.DataFrame({'col1': ser1, 'col2': ser2})
print(df.head())
# using concat is deemed to be less efficient in docs
'''

'''
# gives name to series
ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))

ser.name = 'alphabets'
print(ser.head())
'''

'''
# get item of series A not present in series B
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

print(ser1[~ser1.isin(ser2)])
# removing tilde prints items in A that are in B
'''

'''
# items not common to both series A and B
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ser_u = pd.Series(np.union1d(ser1, ser2))  # union
ser_i = pd.Series(np.intersect1d(ser1, ser2))  # intersect
print(ser_u[~ser_u.isin(ser_i)])
'''

'''
# compute min, 25th, median, 75th and max of series
state = np.random.RandomState(100)
# https://stackoverflow.com/questions/22994423/difference-between-np-random-seed-and-np-random-randomstate
ser = pd.Series(state.normal(10, 5, 25))

# using np.random.normal generates random numbers everytime
# file is run

# print(ser)
print(
    np.percentile(ser, q=[0, 25, 50, 75, 100])
)
'''


# frequency counts of unique items in series
ser = pd.Series(
    np.take(list('abcdefgh'), np.random.randint(8, size=30))
)
print(ser.value_counts())