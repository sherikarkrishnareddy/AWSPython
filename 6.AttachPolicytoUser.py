import boto3
def attachPolicytoUser(username,policy_arn):
    iam=boto3.client('iam')
    response=iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    print(response)

attachPolicytoUser('new_testuser','arn:aws:iam::5203948821610:policy/PythonFullAccess')