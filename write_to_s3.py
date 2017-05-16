'''
This script takes 3 additional arguments and runs like so:
    python write_to_s3.py file_name bucket_name path_to_write
'''
from sys import argv

import boto3

def to_bucket(f, bucket, write_path):
    '''
    Write files to s3 bucket.

    INPUT: f - file to write
           bucket - bucket to write to
           write_path - path in bucket to write file
    '''
    # Specify the service
    s3 = boto3.resource('s3')
    data = open(f, 'rb')
    s3.Bucket(my_bucket).put_object(Key='{}/{}'.format(write_path, f), Body=data)
    print('Success! {} added to {} bucket @ {}'.format(f, bucket, write_path))


if __name__ == '__main__':
    _, f, bucket_name, write_path = argv
    to_bucket(f, bucket_name, write_path)
