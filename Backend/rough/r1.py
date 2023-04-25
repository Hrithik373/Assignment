import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('url-db')

# Retrieve the URL based on its url_id attribute
response = table.get_item(
    Key={
        'url_id': 1
    }
)
url = response['Item']['url']

# Print the URL
print(f"URL: {url}")