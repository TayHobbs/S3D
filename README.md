#s3deploy

Deploy static sites or upload files to s3.

Simply pass your aws access key, aws secret key, the name of the bucket you want to upload to, and the directory the files are stored in.

Current possible command line arguements are:

    --access-key, -a, 'AWS Access Key'
    --secret-key, -s, 'AWS Secret Key'
    --bucket, -b, 'Name of the bucket to upload to'
    --directory, -d, 'Name of the directory where the files or folders you want to upload are stored'`

##Upload

s3deploy will upload everything contained in that folder, including more folders. It will also keep the structure. So,

    .
    ├── parent/
      ├── file
      └── child/
        └── file

will look like this inside your bucket:

    .
    ├── /
      ├── file
      └── child/
        └── file

Currently, files and folders will be uploaded to the base directory of the bucket.

Example usage of upload:

    s3deploy -b bucket-name -a aws-access-key -s aws-secret-key -d parent/


##Delete

s3deploy also contains a delete command, s3delete.

Currently this deletes the entire contents of your S3 bucket.
It takes your aws access key, aws secret key, and the name of the bucket to delete from.

Example usage of s3delete:

    s3delete -b bucket-name -a aws-access-key -s aws-secret-key
