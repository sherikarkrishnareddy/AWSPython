import boto3
def addUsertoGroups(userName,userGroups):
    iam=boto3.client('iam')
    response=iam.add_user_to_group(
        UserName=userName,
        GroupName=userGroups
    )
    print(response)
addUsertoGroups('rdsuser','RDSAdmins')
addUsertoGroups('s3user','S3Admins')