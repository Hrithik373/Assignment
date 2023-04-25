import boto3
import pyshorteners

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('url-db')
s = pyshorteners.Shortener()

# Retrieve the URL based on its url_id attribute
response = table.get_item(
    Key={
        'url_id': 1
    }
)
long_url = response['Item']['url']

# Shorten the URL
short_url = s.tinyurl.short(long_url)

# Update the short_url attribute in the item
table.update_item(
    Key={
        'url_id': 1
    },
    UpdateExpression='SET short_url = :val',
    ExpressionAttributeValues={
        ':val': short_url
    }
)