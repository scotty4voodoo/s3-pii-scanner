import boto3
import os
from scan import write_scan_results_to_file

def send_results_via_sns(topic_arn,output_file):
    """
    Send scan results via Amazon SNS
    """
    # Initialize SNS client
    sns_client = boto3.client('sns',region_name='ap-northeast-2')

    # Read scan results
    try:
        with open(output_file, 'r') as f:
            scan_results = f.read()

        # Send message via SNS
        response = sns_client.publish(
            TopicArn=topic_arn,
            Subject='S3 Scan Results',
            Message=scan_results
        )
        print(f"Results sent successfully via SNS: {response['MessageId']}")

    except Exception as e:
        print(f"Error sending results via SNS: {str(e)}")