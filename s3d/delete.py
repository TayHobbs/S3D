from s3d import connect


def delete_bucket_contents(bucket_name, access_key, secret_key, directory, ignore_files):
    ignore_files = ignore_files if not directory else ['{}/{}'.format(directory, f) for f in ignore_files]
    bucket = connect(bucket_name, access_key, secret_key)
    bucketListResultSet = bucket.list(directory)
    bucket.delete_keys([key.name for key in bucketListResultSet if key.name not in ignore_files])
    print 'Bucket contents successfully deleted!'
