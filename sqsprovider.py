import boto3
import json
from types import SimpleNamespace


class SqsProvider: 
    def __init__(self, queuename: str, region: str = 'ap-southeast-2') -> None:
        sqs = boto3.resource('sqs', region_name=region)
        self.queue = sqs.get_queue_by_name(QueueName=queuename)

    def send(self, target: any) -> int:
        response = self.queue.send_message(MessageBody=target)
        return response.get('MessageId'), response.get('MD5OfMessageBody')

    def receive(self, messaageContext: str) -> None:
        for message in self.queue.receive_messages(MessageAttributeNames=[messaageContext]):
            if message.message_attributes is not None:
                # get message
                data = message.message_attributes.get('Author').get('StringValue')
                x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
                print(x)
                message.delete()
