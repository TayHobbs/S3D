import os.path

import boto
import boto.s3

from s3d import connect


def process_files(bucket_name, access_key, secret_key, source_dir):
    bucket = connect(bucket_name, access_key, secret_key)
    for (source, dirname, file_list) in os.walk(source_dir):
        source = '{}{}'.format(source, '/') if '/' not in source else source

        for file_name in file_list:
            source_path = os.path.join(source, file_name)
            print 'Uploading {}'.format(source_path)
            upload_files(bucket, source_dir, source_path)


def upload_files(bucket, source_dir, source_path):
    key = boto.s3.key.Key(bucket)
    key.key = source_path[len(source_dir):] if source_dir in source_path else source_path
    key.set_contents_from_filename(source_path)


def make_bucket_public(bucket_name, access_key, secret_key):
    bucket = connect(bucket_name, access_key, secret_key)
    bucket.set_acl('public-read')
    print 'Bucket made public!'
