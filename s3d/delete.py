from s3d import connect


def delete_bucket_contents(bucket_name, access_key, secret_key):
    bucket = connect(bucket_name, access_key, secret_key)
    bucketListResultSet = bucket.list()
    bucket.delete_keys([key.name for key in bucketListResultSet])
    print 'Bucket contents successfully deleted!'
