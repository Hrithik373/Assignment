import boto3
import pyshorteners

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('url-db')
s = pyshorteners.Shortener()

# Retrieve the URL based on its url_id attribute
response = table.get_item(
    Key={
        'url_id': 1
    }
)
long_url = response['Item']['url']

# Shorten the URL using pyshorteners
short_url = s.tinyurl.short(long_url)

print(f"Long URL: {long_url}")
print(f"Short URL: {short_url}")