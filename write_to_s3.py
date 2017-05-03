import boto3

# Specify the service
s3 = boto3.resource('s3')


def to_bucket(f, bucket, write_path):
    '''
    Write files to s3 bucket.

    INPUT: f - file to write
           bucket - bucket to write to
           write_path - path in bucket to write file 
    '''
    data = open(f, 'rb')
    s3.Bucket(my_bucket).put_object(Key='{}/{}'.format(write_path, f), Body=data)
    print('Success! {} added to {} bucket @ {}'.format(f, bucket, write_path))
