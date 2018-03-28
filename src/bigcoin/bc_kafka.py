import sys
import requests
from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError


# Create a KafkaProducer with the given client_id and send to the topic all data given by the generator.
# The generator should send three value each time :
# * message : a string to send to the topic
# * key : bytes (or be serializable to bytes via configured key_serializer) the key of the message (for partitionning)
# * timestamp_ms : int that represent the time for the message in epoch milliseconds (from Jan 1 1970 UTC)
# Exit if kafka timeout timed out
def send_to_topic_from_generator(topic,client_id,generator):
	try:
		kafka_producer = KafkaProducer(client_id=client_id,acks='all',retries=0, linger_ms=100)
		while True:
			message,key,timestamp_ms = generator.next()
			kafka_producer.send(topic=topic,value=message,key=key,timestamp_ms=timestamp_ms)

	except KafkaTimeoutError:
		sys.exit(30) #Kafka timeout
	except StopIteration:
		kafka_producer.close()
