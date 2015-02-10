import boto
import boto.s3


def connect(bucket_name, access_key, secret_key):
    connection = boto.connect_s3(access_key, secret_key)
    return connection.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)
