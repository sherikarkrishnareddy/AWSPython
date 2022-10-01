import boto3
def setAccesskeyState(userName,accessKeyID):
    iam=boto3.client('iam')
    response=iam.update_access_key(
        AccessKeyId=accessKeyID,
        Status='Inactive',
        UserName=userName
    )
    print(response)
setAccesskeyState('new_testuser','HA***KIhsgdt')