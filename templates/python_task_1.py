import pandas as pd
import numpy as np
from datetime import datetime as dt
from itertools import product
import warnings
warnings.filterwarnings('ignore')
path=r'C:\Users\lalitha\OneDrive\Documents\GitHub\MapUp-Data-Assessment-F\datasets'
file1=r'\dataset-1.csv'
file2=r'\dataset-2.csv'


#Q1 Car Generation matrix
def generate_car-matrix(dataset):
     df = pd.read_csv(dataset)
     #pivot the data frame to create a matrix
    car_matrix=df.pivot(index='id=1',columns='id_2',values='car').fillna(0)
    #set diagonal values to 0
    for col in car_matrix.columns.tolist():
        car_matrix.at[col,col]=0
    return car_matrix    

#Q2 Car Type Count Calculation

def get_type_count(dataset):
df=pd.read_csv(dataset)
#create the column car_type
df['car_type']=df['car'].apply(lambda x:'low' if x<=15 else('medium' if 15<x<=25 else 'high'))
#create a dictionary of value counts of each car type and sort it by alphabetical order
final_dict=pd.DataFrame(df['car_type'].value_counts()).sort_index(axis=0).to_dict()['count']
return final_dict
     
#Q3 Bus Count Interval Index

def get_bus_indexes(dataset):
     df=pd.read_csv(dataset)
     #returning the list of indexes where bus value > 2* mean of the ccolumn
     final_list=df]df['bus']>(df['bus'].mean()*2)].sort_index(axis=0).index.tolist()
     return final_list

#Q4 Route Filtering

def filter_routes(dataset):
     df=pd.read_csv(dataset)
     df1=df.groupby('route').agg({'truck':'mean'}).sort_index(axis=0)
     final_list=df1[df1['truck']>7].index.tolist()
     return final_list


#Q5 Matrix Value Modification
def multiply_matrix(result):
     result1=result.applymap(lambda x: x*0.75 if x>20 else x*1.25)
     return result1

#Q6 Time Check



def time_check(dataset):
     df=pd.read_csv(dataset)
     df['startTime']=pd.to_datetime(df['startTime'],format=%H:%M:%S')
     df['endTime']=pd.to_datetime(df['endTime'],format='%H:%M:%S')
     df['incorrect_start_flag']=np.where(
          (df['startTime'].dt.hour !=0) |
          (df['startTime'].dt.minute !=0) |
          (df['startTime'].dt.second!=0) |
          ~df['saturday'].isin(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']),1,0
     )
     df['incorrect_combined']=df[['incorrect_start_flag','incorrect_end_flag']].apply(lambda x:max(x[0],x[1],axis=1)
     df['incorrect_combined']=df['incorrect_commbined'].apply(lambda x:True if x==1 else False)
     final=df.groupby(['id','id_2'])['incorrect_combined'].any()
     return final

def _main_(path,file1,file2):
     result1=generate_car_matrix(path+file1)
     result2=get_type_count(path+file1)
     result3=get_bus_indexes(path+file1)
     result4=filter_routes(path+file1)
     result5=multiply_matrix(result1)
     result6=time_check(path+file2)
     return result1,result2,result3,result4,result5,result6

result1,result2,result3,result4,result5,result6=_main_(path,file1,file2)
