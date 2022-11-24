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
import pickle
con = psycopg2.connect(host='rajje.db.elephantsql.com',dbname="onjiuvur", user="onjiuvur", password="9MDhITxF84TAukDM1_lqTc9y_Zko7wOx",port=5432)
cur = con.cursor()
#from utils import predict
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
bootstrap_servers = ["172.20.10.2:9092", "172.20.10.2:9093", "172.20.10.2:9094"]
consumer = KafkaConsumer("test_test", bootstrap_servers=bootstrap_servers)
#producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
path = '/Users/jeong-gihun/Desktop/kafka_Python/jeong_2/'



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

    
    



with open("person.pkl","wb") as f:
    pickle.dump(p, f)


    #reate = img_arr
    #cv2.imwrite(path,img_arr)
    #results = predict(img_arr)
    #encoded_results = json.dumps(results).encode('utf-8')

    #producer.send("ResultStream")

#producer.flush()