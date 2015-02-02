import argparse
from s3deploy import process_files


parser = argparse.ArgumentParser()
parser.add_argument("-b", "--bucket", type=str, required=True, help="Name of Bucket")
parser.add_argument("-d", "--directory", type=str, required=True, help="Directory of the files you want to upload")
parser.add_argument("-a", "--access-key", type=str, required=True, help="AWS Access Key")
parser.add_argument("-s", "--secret-key", type=str, required=True, help="AWS Secret Key")


def upload():
    args = parser.parse_args()
    process_files(args.bucket, args.access_key, args.secret_key, args.directory)
