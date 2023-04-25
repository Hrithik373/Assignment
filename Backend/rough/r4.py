import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# List all tables in the region
response = dynamodb.list_tables()

# Check if the table exists
if 'url-db' in response['TableNames']:
    print('Table found')
else:
    print('Table not found')