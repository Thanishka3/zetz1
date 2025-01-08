import pandas as pd
screen_time=[2,1,3,4,]
sleep_hours=[3,7,8,9,]
student_name=["Anudeep","Thanu","shivani","shiva",]
dict1={
    "screen_time":screen_time,
    "sleep_hours":sleep_hours,
    "student_name":student_name
}
print(dict1)
df=pd.DataFrame(dict1)
print(df)
