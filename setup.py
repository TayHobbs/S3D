from setuptools import setup, find_packages


setup(
    name='S3D',
    version='1.2.0',
    author='Taylor Hobbs',
    author_email='hobbstay@gmail.com.com',
    description='s3deploy',
    long_description=open('README.rst').read(),
    url='https://github.com/tayhobbs/s3deploy',
    packages=find_packages(exclude=['test']),
    install_requires=['boto==2.49.0'],
    entry_points={
        'console_scripts': {
            's3deploy = s3d.script:upload',
            's3delete = s3d.script:delete',
        },
    },
)
