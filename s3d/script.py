import argparse
from s3d.deploy import process_files
from s3d.delete import delete_bucket_contents


parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bucket', type=str, required=True, help='Name of Bucket')
parser.add_argument('-a', '--access-key', type=str, required=True, help='AWS Access Key')
parser.add_argument('-s', '--secret-key', type=str, required=True, help='AWS Secret Key')
parser.add_argument('-i', '--ignore-files', nargs='*', required=False, help='List of files to ignore')
parser.add_argument('-d', '--directory', type=str, required=False, help='''
    Directory of the files you want to upload or the prefix of the directory in the bucket to delete''')


def upload():
    args = parser.parse_args()
    if args.directory:
        process_files(args.bucket, args.access_key, args.secret_key, args.directory)
    else:
        print('You must supply a source directory')


def delete():
    args = parser.parse_args()
    delete_bucket_contents(args.bucket, args.access_key, args.secret_key, args.directory, args.ignore_files)
