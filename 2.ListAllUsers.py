import boto3
def all_users():
    iam=boto3.client('iam')
    paginator=iam.get_paginator('list_users')
    for response in paginator.paginate():
        for user in response['Users']:
            #print("Name",user['UserName'])
            #print("ARN",user['Arn'])
            print("Name: {} ARN: {}".format(user['UserName'],user['Arn']))


all_users()

