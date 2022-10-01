import boto3

def createAccessKey(userName):
    iam=boto3.client('iam')
    response=iam.create_access_key(
        UserName=userName
    )
    print(response)
createAccessKey('new_testuser')

