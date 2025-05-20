from kafka import KafkaProducer
import json
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    user_id = input("Enter user_id: ")
    action = input("Enter action: ")
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    message = {"user_id": user_id, "action": action, "timestamp": timestamp}
    producer.send('user_actions', message)
    print(f"Sent message: {message}")