import boto3

# Specify the service
s3 = boto3.resource('s3')


def to_bucket(f, bucket):
    data = open(f, 'rb')
    s3.Bucket(my_bucket).put_object(Key=f, Body=data)
    print('Success! {} added to {} bucket'.format(f, bucket))


if __name__ == '__main__':
    # Specify the bucket to write to
    my_bucket = 'quora-bwl'
    # File to move
    f = 'test_cleaned.csv'
    # Open file and put it in the bucket
    to_bucket(f, my_bucket)
