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
        "alembic==0.8.2",
        "dataset==0.6.1",
        "httplib2==0.9.2",
        "Mako==1.0.2",
        "MarkupSafe==0.23",
        "normality==0.2.4",
        "python-editor==0.4",
        "pytz==2015.6",
        "PyYAML==3.11",
        "six==1.10.0",
        "SQLAlchemy==1.0.8",
        "twilio==4.6.0",
        "wheel==0.24.0"
    ]
)