# Vis-Zon-Shopping-Platform

Server-Client Architecture for Detecting the duration of hand wash along with using AWS Facial Recognition to determine the identity of the person washing hands. This is to monitor Hand wash compliance.

## Repository Metadata ##

* Version: 1.1.0

## config.py Format ##

Add the following `config.py` file to the project folder and Fill the empty credentials before running the code

```python
# AWS S3 Credentials
AWS_REGION=''
AWS_ACCESS_ID=''
AWS_SECRET_KEY=''
AWS_BUCKET_NAME=''

```

## Steps to run the program ##

* Do Git Clone to clone the Repository.
* Add a `config.py` file in the project folder (Format Given Above)
* Install the dependencies by doing `pip install -r requirements.txt`
* run the `app_webpage.py` file and keep it running in one terminal. 
* Once the server is running without issues, open the link localhost:3000/

## Who do I talk to? ##

* [Vinay Kumar Verma, Developer and Creator](mailto:vermavinay982@gmail.com ) - For Facial Recognition using AWS, Pipeline, Webpage Part
