import boto3
import random

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Project2Stats')

response = table.scan()
stat = random.choice(response['Items'])['stat']
print(stat)