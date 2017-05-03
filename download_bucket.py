import boto3


def download_files(f_list, bucket, write_path):
    '''
    This function reads specified files from a bucket and downloads them to a
    specified path.

    INPUT: f_list - list of files to download in bucket
           bucket - s3 bucket to download from
           write_path - file path to write to on local machine or ec2 instance
    '''
    # specify s3 as the resource
    s3 = boto3.resource('s3')
    # iteratively download files in the specified file list (f_list)
    for f in f_list:
        s3.meta.client.download_file(bucket, f, '{}/{}'.format(write_path, f))
    print('Complete...')
