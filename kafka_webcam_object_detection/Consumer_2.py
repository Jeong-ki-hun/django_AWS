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


p = []

for msg_idx, message in enumerate(consumer):
    np_arr = np.frombuffer(message.value, dtype=np.uint8)
    img_arr = cv2.imdecode(np_arr,cv2.IMREAD_COLOR)



    img_arr = cv2.rotate(img_arr,cv2.ROTATE_180)
    result = model(img_arr,size=640) # 모델에 카프카로 받아온 실시간 영상의 사진을 넣어

    df = result.pandas().xyxy[0] # 디텍션된 결과값을 따로 저장한후
    person=(df['name']=='person').count() # 사람으로 인식된 검출결과만을 따로 카운트하여 모아 DB에 적재한다
    cur.execute("INSERT INTO ob_streettable (address, count,time) VALUES (%s, %s, )", ('서울특별시 용산구 원효로89길 13-10',str(person)))
    # 주소값은 임의로 설정하였다.
    con.commit()
