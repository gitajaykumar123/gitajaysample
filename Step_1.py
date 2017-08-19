# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:40:24 2017

@author: ajaykumar
"""

import pandas as pd
import time
from geopy.geocoders import Nominatim 
nm = Nominatim()
df =pd.read_csv('train.csv')
#df =pd.read_csv('dummy.csv')
start_c=time.time()
df["coordinates"]=df["pickup_latitude"].astype(str)+','+df["pickup_longitude"].astype(str)
end_c= time.time()
start_r=time.time()
df["Address"]= df["coordinates"].apply(nm.reverse)
end_r=time.time()
print("The time for  creating  coordinates is ",end_c - start_c)
print("The time for  reverse Geocoding is ",end_r - start_r)
print("The time for  overall execution is ",end_r - start_c)
df.to_csv('train_refined.csv')
  