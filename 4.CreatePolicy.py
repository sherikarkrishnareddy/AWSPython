import boto3
import json
def CreatePolicy():
    iam=boto3.client('iam')
    user_policy={
        "Version":"2012-10-17",
        "Statement":[
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }
    response=iam.create_policy(
        PolicyName='PythonFullAccess',
        PolicyDocument=json.dumps(user_policy)
    )
    print(response)
CreatePolicy()