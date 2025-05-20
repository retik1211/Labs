from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'user_actions',
    bootstrap_servers='localhost:9092',
    group_id='user-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

action_count = {}
for message in consumer:
    action = message.value['action']
    action_count[action] = action_count.get(action, 0) + 1
    print(f"Received message: {message.value}")

    if action == "purchase":
        print(f"Purchase action detected: {message.value}")

    print(f"Action count: {action_count}")