import requests


def lambda_handler(event, context):
    response =  requests.get('https://www.yahoo.com')
    return str(response)

