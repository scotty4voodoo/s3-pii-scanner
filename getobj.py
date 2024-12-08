import boto3
import os

def is_text_file(key):
    # List of common text file extensions
    text_extensions = ['.doc','docx','.ppt','.pptx','.xls','.xlsx','.txt', '.csv', '.json', '.xml', '.log', '.html','.pdf']
    return any(key.lower().endswith(ext) for ext in text_extensions)

def download_s3_objects():

    # Initialize S3 client
    s3_client = boto3.client('s3')

    # Get list of all bucket names
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    # Create local directory to store downloaded files
    if not os.path.exists('temp_scan_files'):
        os.makedirs('temp_scan_files')

    # Iterate through each bucket
    for bucket in buckets:
        print(f"Processing bucket: {bucket}")

        # Get list of all objects in bucket
        objects = s3_client.list_objects_v2(Bucket=bucket)

        # Download each object
        if 'Contents' in objects:
            for obj in objects['Contents']:
                # Get object key (file path/name)
                key = obj['Key']

                # Only download text files
                if is_text_file(key):
                    # Create local directory structure if needed
                    local_path = os.path.join('temp_scan_files', bucket, key)
                    os.makedirs(os.path.dirname(local_path), exist_ok=True)

                    # Download file
                    print(f"Downloading text file: {key}")
                    s3_client.download_file(bucket, key, local_path)

    print("Download complete!")