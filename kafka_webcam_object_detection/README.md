# K-Digital Training Hackathon (코파고)


![스크린샷 2022-11-01 오후 2 25 01](https://user-images.githubusercontent.com/97666832/199164948-06e9b12d-4976-47bf-8e95-d43a44f17621.png)

[Zookeeper]
카프카 브로커들이 한서버에 뜰수있는 역활을 한다

[Kafka]

코드설명

⚫ Producer
  
  ◼ 기기의 카메라를 인식하여 웹캠에 연결후 카프카 프로커 서버로 0.2초당 한장씩 이미지를 만들어 카프카 브로커로 전송한다.

⚫ Consumer
  
  ◼ 카프카 브로커에 연결후 토픽을 지정 ex.)토픽이란 딕셔너리의 키를 의미(?) 하여 들어오는 정보를 받아 yolov5s모델에 결과를 넣는다
  ◼ 그 후 모델의 결과값을 pandas로 풀어내어 인식된 라벨중 사람의 수만 세어 DB에 적재하였다.