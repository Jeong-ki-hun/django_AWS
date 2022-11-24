from kafka import KafkaConsumer, KafkaProducer
from PIL import Image
import cv2
import numpy as np
import json
import torch
import pandas
import psycopg2
import csv
import datetime
import random
import csv
con = psycopg2.connect(host='rajje.db.elephantsql.com',dbname="onjiuvur", user="onjiuvur", password="9MDhITxF84TAukDM1_lqTc9y_Zko7wOx",port=5432)
cur = con.cursor()
#from utils import predict
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
bootstrap_servers = ["172.20.10.2:9092", "172.20.10.2:9093", "172.20.10.2:9094"]
consumer = KafkaConsumer("test_test", bootstrap_servers=bootstrap_servers)
#producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
path = '/Users/jeong-gihun/Desktop/kafka_Python/jeong_2/'

h = []
for l in range(14,16):
    for i in range(24):
        for j in range(60):
            for k in range(60):
                h.append(f'{l}일_{i}시_{j}분_{k}초')

p = []

for msg_idx, message in enumerate(consumer):
    np_arr = np.frombuffer(message.value, dtype=np.uint8)
    img_arr = cv2.imdecode(np_arr,cv2.IMREAD_COLOR)


    print(img_arr.shape)
    #cv2.imshow('re{msg_idx}',img_arr)
    #
    #result.show()
    img_arr = cv2.rotate(img_arr,cv2.ROTATE_180)
    result = model(img_arr,size=640)
    #result.save(f'/Users/jeong-gihun/Desktop/kafka_Python/jeong_2/jeo{msg_idx}.jpeg')
    #result.pandas().xyxy[0]
    df = result.pandas().xyxy[0]
    person=(df['name']=='person').count()
    p.append(person)
    if len(p)==1000:
        break

    
    
for i in range(len(h)):
    ra=random.choice(p)
    cur.execute("INSERT INTO ob_streettable (address, count,time) VALUES (%s, %s, %s)", ('서울특별시 용산구 원효로89길 13-10',str(ra),'2022년_11월_'+str(h[i])))
    con.commit()


    #reate = img_arr
    #cv2.imwrite(path,img_arr)
    #results = predict(img_arr)
    #encoded_results = json.dumps(results).encode('utf-8')

    #producer.send("ResultStream")

#producer.flush()