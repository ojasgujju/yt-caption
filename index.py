from flask import Flask, jsonify, request
from app import app as flask_app

def handler(event, context):
    if event['httpMethod'] == 'GET':
        # Extract query parameters from the event
        query_parameters = event['queryStringParameters'] if 'queryStringParameters' in event else {}
        
        # Set up Flask request with query parameters
        with flask_app.request_context(event['path'], method=event['httpMethod'], query_string=query_parameters):
            response = flask_app.full_dispatch_request()
        
        # Convert Flask response to dictionary
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data(as_text=True)
        }
    else:
        return {
            'statusCode': 405,
            'body': 'Method Not Allowed'
        }
