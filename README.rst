S3D
========

Deploy static sites or upload files to s3.

Simply pass your aws access key, aws secret key, the name of the bucket
you want to upload to, and the directory the files are stored in.

Current possible command line arguements are:

::

    --access-key, -a, 'AWS Access Key'
    --secret-key, -s, 'AWS Secret Key'
    --bucket, -b, 'Name of the bucket to upload to'
    --directory, -d, 'Name of the directory where the files or folders you want to upload are stored'`

Installable from pip:
::

   pip install S3D

Upload
------

s3deploy will upload everything contained in that folder, including more
folders. It will also keep the structure. So,

::

    .
    ├── parent/
      ├── file
      └── child/
        └── file

will look like this inside your bucket:

::

    .
    ├── /
      ├── file
      └── child/
        └── file

Currently, files and folders will be uploaded to the base directory of
the bucket.

Example usage of upload:

::

    s3deploy -b bucket-name -a aws-access-key -s aws-secret-key -d parent/

Delete
------

s3deploy also contains a delete command, s3delete.

This deletes the entire contents of your S3 bucket, unless you pass
it a prefix or a list of files to ignore. It takes your aws access key,
aws secret key, the name of the bucket to delete from, the prefix of
the directory to delete from, and a list of files to ignore.

if you pass both a list of files to ignore and a prefix, the prefix will
be appended to all the files to ignore, otherwise these files will not be
ignored and deleted anyway.  So if you want to ignore :code:`important_file.txt`
in the :code:`stuff/` prefix but wish to delete everything else in the :code:`stuff/` prefix,
simply pass :code:`-d stuff -i important_file.txt` to the command. The file to ignore will
become :code:`stuff/important_file.txt`.

Example usage of s3delete:

::

    s3delete -b bucket-name -a aws-access-key -s aws-secret-key
