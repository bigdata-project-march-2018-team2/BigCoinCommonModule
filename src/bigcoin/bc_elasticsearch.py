import sys
import os
from elasticsearch import Elasticsearch,ConnectionTimeout
from elasticsearch import helpers



class BCElasticsearch:

	_es = None

	def __init__(self):

		#Try to get actual value from environment vars
		user = os.environ["ES_ADMIN_USER"] if ("ES_ADMIN_USER" in os.environ) else None
		password = os.environ["ES_ADMIN_PASS"] if "ES_ADMIN_PASS" in os.environ else None
		host = os.environ["ES_HOST"] if "ES_HOST" in os.environ else "locahost"
		port = os.environ["ES_PORT"] if "ES_PORT" in os.environ else 9200
		http_auth = (user,password) if (user is not None and password is not None) else None
		try:
			self._es = Elasticsearch([host], http_auth=http_auth, port=port, scheme='http')
		except ConnectionTimeout:
			sys.exit(50)

	# Try to get records from kafka, return a list of message
	def send_messages(self,generator):
		try:
			helpers.bulk(self._es, generator)
		except ConnectionTimeout:
			sys.exit(50)
