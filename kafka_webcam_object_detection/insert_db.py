import csv
import psycopg2
import pandas as pd
import pandas as pd
import random
import datetime
import pickle

con = psycopg2.connect(host='rajje.db.elephantsql.com',dbname="onjiuvur", user="onjiuvur", password="9MDhITxF84TAukDM1_lqTc9y_Zko7wOx",port=5432)

cur = con.cursor()

# df_c = pd.read_csv('/Users/jeong-gihun/Desktop/Hackathon-copago/object/csv/음식점.csv',encoding='cp949')
# df_e = pd.read_excel('/Users/jeong-gihun/Desktop/Hackathon-copago/object/csv/cctv.xlsx',)
# df_c['소재지'] = ((df_c['소재지'].str.split(',',expand=True)[0]).str.split('(',expand=True))[0]
# df_c = df_c[['업태명','업소명','소재지']]
# df_e=df_e[['소재지지번주소']]


with open("per.pkl","rb") as f:
    person = pickle.load(f)
h = []
for l in range(14,16):
    for i in range(24):
        for j in range(60):
            h.append(f'{l}일_{i}시_{j}분')

#for j in range()
#    person.append()

for i in range(len(h)):
    cur.execute("INSERT INTO ob_streettable (address, count,time) VALUES (%s, %s, %s)", ('서울특별시 용산구 원효로89길 13-10',str(person[i]),'2022년_11월_'+str(h[i])))
    con.commit()

# for i in range(100):
#     a = random.randrange(15, 401)
#     d = datetime.datetime.now()
#     t =(f"{d.year}년_{d.month}월_{d.day}일_{d.hour}시_{d.minute}분")
#     cur.execute("INSERT INTO ob_streettable (address, count,time) VALUES (%s, %s, %s)", ('서울특별시 용산구 원효로89길 13-10',str(a),str(t)))
# for idx,row in df_c.iterrows():
#     cur.execute("INSERT INTO ob_resttable (label, food_name, name, address, count) VALUES (%s, %s, %s, %s, %s)", ('음식점',row['업태명'],row['업소명'],row['소재지'],'7'))
# for idx,row in df_e.iterrows():
#      cur.execute("INSERT INTO ob_cctvtable (label, address, count) VALUES (%s, %s, %s)", ('CCTV',row['소재지지번주소'],'30'))


cur.close()
con.close()



