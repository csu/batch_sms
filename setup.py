try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='batch_sms',
    version='0.1.0',
    description='Library to send large numbers of text messages.',
    long_description=long_description,
    author='Christopher Su',
    author_email='chris+py@christopher.su',
    url='https://github.com/csu/batch_sms',
    packages=['batch_sms'],
    install_requires=[
        "dataset==0.6.1",
        "twilio==4.6.0"
    ]
)