import boto3
def detachPolicytoUserGroups(userGroup,policy_arn):
    iam=boto3.client('iam')
    response=iam.detach_group_policy(
        GroupName=userGroup,
        PolicyArn=policy_arn
    )
    print(response)
detachPolicytoUserGroups('RDSAdmins','arn:aws:iam::aws:policy/AmazonRDSFullAccess')
detachPolicytoUserGroups('S3Admins','arn:aws:iam::aws:policy/AmazonS3FullAccess')