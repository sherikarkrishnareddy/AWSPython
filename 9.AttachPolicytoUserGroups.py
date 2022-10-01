import boto3
def attachPolicytoUserGroups(userGroup,policy_arn):
    iam=boto3.client('iam')
    response=iam.attach_group_policy(
        GroupName=userGroup,
        PolicyArn=policy_arn
    )
    print(response)
attachPolicytoUserGroups('RDSAdmins','arn:aws:iam::aws:policy/AmazonRDSFullAccess')
attachPolicytoUserGroups('S3Admins','arn:aws:iam::aws:policy/AmazonS3FullAccess')