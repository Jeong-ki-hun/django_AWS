import cv2
import time
import sys
from kafka import KafkaProducer

topic = 'test_test'
def publish_camera():
    """
    Publish camera video stream to specified Kafka topic.
    Kafka Server is expected to be running on the localhost. Not partitioned.
    """

    # Start up producer
    producer = KafkaProducer(bootstrap_servers=["172.20.10.2:9092", "172.20.10.2:9093", "172.20.10.2:9094"])

    camera = cv2.VideoCapture(0)
    try:
        while(True):
            success, frame = camera.read()
        
            ret, buffer = cv2.imencode('.jpg', frame)
            producer.send(topic, buffer.tobytes())
            
            # Choppier stream, reduced load on processor
            time.sleep(0.2)

    except:
        print("\nExiting.")
        sys.exit(1)

    
    camera.release()


publish_camera()

