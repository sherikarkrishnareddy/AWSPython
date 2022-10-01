import boto3

def createUserGroups(group_name):
    iam=boto3.client('iam')
    response=iam.create_group(GroupName=group_name)
    print(response)

createUserGroups('RDSAdmins')
createUserGroups('S3Admins')