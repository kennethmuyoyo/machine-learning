#classifyImage
    
import json
import boto3
import base64

# The name of your deployed model
ENDPOINT = "image-classification-2024-10-11-13-08-35-720"

runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])

    # Make a prediction:
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT,
                                       ContentType='image/png',
                                       Body=image)
    
    inferences = response['Body'].read().decode('utf-8')
    
    # We return the data back to the Step Function    
    event['body']["inferences"] = json.loads(inferences)
    return {
        'statusCode': 200,
        'body': json.dumps(event['body'])
    }

#filterInferences
import json

THRESHOLD = 0.93

def lambda_handler(event, context):
    
    # Grab the inferences from the event
    inferences = json.loads(event['body'])['inferences']
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(float(x) > THRESHOLD for x in inferences)
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        return {
            'statusCode': 200,
            'body': event['body']
        }
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")
        
        
#serializeImageData
import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input
    key = event['s3_key']
    bucket = event['s3_bucket']
    
    # Download the data from s3 to /tmp/image.png
    s3.download_file(bucket, key, '/tmp/image.png')
    
    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }
