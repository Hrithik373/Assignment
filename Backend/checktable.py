import boto3

# create an instance of the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

# get a reference to the table
table_name = 'url-db'
table = dynamodb.Table(table_name)

# scan the table to retrieve all items
response = table.scan()

# print each item in the response
for item in response['Items']:
    print(item)