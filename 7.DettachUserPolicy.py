import boto3
def detachUserPolicy(username,policy_arn):
    iam=boto3.client('iam')
    response=iam.detach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    print(response)

detachUserPolicy('new_testuser','arn:aws:iam::520654393821610:policy/PythonFullAccess')