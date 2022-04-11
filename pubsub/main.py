import base64
import json
from flask_cors import CORS, cross_origin
import functions_framework

from google.cloud import pubsub_v1

# Instantiates a Pub/Sub client
publisher = pubsub_v1.PublisherClient()
PROJECT_ID = 'cloud-computing-sandbox-346022'

# Publishes a message to a Cloud Pub/Sub topic.
@cross_origin()
@functions_framework.http
def publish_result(request):
    
    message = request.get_json(silent=True).get("message")

    topic_name = 'food-order-topic'

    if not topic_name or not message:
        return ('Missing "topic" and/or "message" parameter.', 400)

    print(f'Publishing message to topic {topic_name}')

    # References an existing topic
    topic_path = publisher.topic_path(PROJECT_ID, topic_name)

    message_json = json.dumps({
        'data': {'message': message},
    })
    message_bytes = message_json.encode('utf-8')

    # Publishes a message
    try:
        publish_future = publisher.publish(topic_path, data=message_bytes)
        publish_future.result()  # Verify the publish succeeded
        return 'Request published.'
    except Exception as e:
        print(e)
        return (e, 500)
