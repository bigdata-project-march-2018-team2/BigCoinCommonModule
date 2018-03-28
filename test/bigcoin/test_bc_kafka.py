
try:
    # Python 3
    from unittest import mock
except ImportError:
    # Python 2, install from pip first
    import mock
import unittest
from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError
from bigcoin import bc_kafka

#Generator used to send values to the tested method
def generator_kafka_data(obj):
    for value in obj:
        yield value['message'],value['key'],value['timestamp_ms']



class TestBCKafka(unittest.TestCase):

    @mock.patch.object(KafkaProducer,'__init__') #Need to test if constructor called once, no init problem since the instance is created in __new__
    @mock.patch.object(KafkaProducer,'send')
    def test_send_to_topic_from_generator(self, mock_send, mock_init):
        #Necessary as constructor don't return anything and mock return the mock by default
        mock_init.return_value = None

        #Test normal behavior
        topic = "mock_topic"
        client_id = "mock_client_id"
        json = [
            {"message":"mess","key":"key","timestamp_ms":"1000000"},
            {"message":"mess2","key":None,"timestamp_ms":"1000000"},
            {"message":"mess3","key":"key","timestamp_ms":None},
            {"message":None,"key":None,"timestamp_ms":None},
        ]
        bc_kafka.send_to_topic_from_generator(topic,client_id,generator_kafka_data(json))

        calls = [mock.call(value=x['message'],key=x['key'],timestamp_ms=x['timestamp_ms'],topic=topic) for x in json]

        mock_init.assert_called_once()
        mock_send.assert_has_calls(calls)

        #Test when kafka timeout
        mock_send.side_effect = KafkaTimeoutError()
        passed_timeout = False
        try:
            bc_kafka.send_to_topic_from_generator(topic,client_id,generator_kafka_data(json))
        except SystemExit as e:
            if e.code == 30:
                passed_timeout = True
        assert passed_timeout

if __name__ == "__main__":
    unittest.main()
