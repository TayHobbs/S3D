from boto import connect_s3
from boto.s3.connection import OrdinaryCallingFormat, Location


def connect(bucket_name, access_key, secret_key):
    if '.' in bucket_name:
        connection = connect_s3(access_key, secret_key, calling_format=OrdinaryCallingFormat())
    else:
        connection = connect_s3(access_key, secret_key)
    return connection.create_bucket(bucket_name, location=Location.DEFAULT)
