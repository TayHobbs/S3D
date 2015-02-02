from setuptools import setup, find_packages


setup(
    name='s3deploy',
    version='0.0.2',
    author="Taylor Hobbs",
    author_email="hobbstay@gmail.com.com",
    description="boto-egg",
    long_description=open('README.rst').read(),
    url='https://github.com/tayhobbs/',
    packages=find_packages(exclude=['test']),
    install_requires=['boto'],
    entry_points={
        'console_scripts': {
            "s3deploy = s3deploy.script:upload",
        },
    },
)
