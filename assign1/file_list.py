# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

import boto3
from flask import Flask
from botocore.config import Config
from flask import redirect, render_template

  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def bucket_list():
    
    buckets=[]
    file_names=dict()
    s3 = boto3.client(
    's3',
    aws_access_key_id='zzzz',
    aws_secret_access_key='xxx')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        buckets.append(bucket["Name"])
    print(buckets)
    for i in buckets:
        response = s3.list_objects(Bucket=i)
        bucketfiles=[]
        for content in response.get('Contents', []):
            bucketfiles.append(content.get('Key'))
            print("File found: {key}".format(key=content.get('Key')))
        file_names[i]=bucketfiles
    print(file_names)

    


    
    return render_template('home.html',file_names=file_names)



# main driver function
if __name__ == '__main__':
    my_config = Config(
    region_name = 'ap-south-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    })


    client = boto3.client('kinesis', config=my_config)
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()