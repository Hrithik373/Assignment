import boto3

# create an instance of the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

# get a reference to the table
table = dynamodb.Table('url-db')

# scan the table and print the result
response = table.scan()
items = response['Items']
print(items)