from setuptools import setup, find_packages


setup(
    name='boto-egg',
    version='0.0.1',
    author="Taylor Hobbs",
    author_email="hobbstay@gmail.com.com",
    description="boto-egg",
    long_description=open('README.rst').read(),
    url='https://github.com/tayhobbs/',
    packages=find_packages(exclude=['test']),
    install_requires=['boto'],
    entry_points={
        'console_scripts': {
            "upload = boto_egg.script:boto_egg",
        },
    },
)
