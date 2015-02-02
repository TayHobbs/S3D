from setuptools import setup, find_packages


setup(
    name='s3deploy',
    version='1.0.0',
    author="Taylor Hobbs",
    author_email="hobbstay@gmail.com.com",
    description="boto-egg",
    long_description=open('README.md').read(),
    url='https://github.com/tayhobbs/',
    packages=find_packages(exclude=['test']),
    install_requires=['boto'],
    entry_points={
        'console_scripts': {
            "s3deploy = s3deploy.script:upload",
            "s3delete = s3deploy.script:delete",
        },
    },
)
