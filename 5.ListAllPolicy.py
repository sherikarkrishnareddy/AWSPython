import boto3
def list_policies():
    iam=boto3.client('iam')
    paginator=iam.get_paginator('list_policies')
    #to get AWS policies
    for response in paginator.paginate(Scope='AWS'):
    #to get custom policies
    #for response in paginator.paginate(Scope='Local'):
        for policy in response['Policies']:
            print('PolicyName: {}, ARN: {}'.format(policy['PolicyName'],policy['Arn']))
list_policies()