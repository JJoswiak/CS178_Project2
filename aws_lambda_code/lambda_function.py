import boto3
import random
from botocore.exceptions import ClientError

def lambda_handler(event, context):
# DynamoDB setup
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Project2Stats')

# Pull random stat
    response = table.scan()
    stat = random.choice(response['Items'])['stat']

# SES setup
    ses = boto3.client('ses', region_name='us-east-1')

    SENDER = "joseph.joswiak@drake.edu"
    RECIPIENT = "joseph.joswiak@drake.edu"

    try:
        ses.send_email(
            Source=SENDER,
            Destination={'ToAddresses': [RECIPIENT]},
            Message={
                'Subject': {'Data': 'Stat of the Day'},
                'Body': {'Text': {'Data': stat}}
            }
        )
        print("Email sent!")
    except ClientError as e:
        print("Error:", e.response['Error']['Message'])