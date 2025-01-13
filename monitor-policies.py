import boto3
from flask import Flask, render_template

app = Flask(__name__)

# Prompt user for region at startup
print("Welcome to the AWS Monitoring Dashboard!")
aws_region = input("Enter the AWS region you want to monitor (e.g., us-east-1, eu-west-2): ")

# Validate region input
valid_regions = boto3.Session().get_available_regions('ec2')
if aws_region not in valid_regions:
    print(f"Invalid region: {aws_region}. Please choose from: {', '.join(valid_regions)}")
    exit(1)

# Initialize AWS clients with the selected region
ec2_client = boto3.client('ec2', region_name=aws_region)
s3_client = boto3.client('s3', region_name=aws_region)
rds_client = boto3.client('rds', region_name=aws_region)
lambda_client = boto3.client('lambda', region_name=aws_region)
lightsail_client = boto3.client('lightsail', region_name=aws_region)
cloudwatch_client = boto3.client('cloudwatch', region_name=aws_region)

# Fetch data from AWS services
def fetch_aws_data():
    data = {}

    # EC2 instances
    ec2_instances = ec2_client.describe_instances()
    ec2_data = []
    for reservation in ec2_instances['Reservations']:
        for instance in reservation['Instances']:
            ec2_data.append({
                'InstanceId': instance['InstanceId'],
                'State': instance['State']['Name'],
                'Type': instance['InstanceType'],
                'Region': instance['Placement']['AvailabilityZone']
            })
    data['ec2'] = ec2_data

    # S3 buckets
    s3_buckets = s3_client.list_buckets()
    s3_data = [{'Name': bucket['Name']} for bucket in s3_buckets['Buckets']]
    data['s3'] = s3_data

    # RDS databases
    rds_instances = rds_client.describe_db_instances()
    rds_data = [{'DBInstanceIdentifier': db['DBInstanceIdentifier'], 'Status': db['DBInstanceStatus']} for db in rds_instances['DBInstances']]
    data['rds'] = rds_data

    # Lambda functions
    lambda_functions = lambda_client.list_functions()
    lambda_data = [{'FunctionName': func['FunctionName'], 'Runtime': func['Runtime']} for func in lambda_functions['Functions']]
    data['lambda'] = lambda_data

    # Lightsail instances
    lightsail_instances = lightsail_client.get_instances()
    lightsail_data = [{'Name': instance['name'], 'State': instance['state']['name']} for instance in lightsail_instances['instances']]
    data['lightsail'] = lightsail_data

    return data

@app.route('/')

def dashboard():
    aws_data = fetch_aws_data()
    return render_template('index.html', data=aws_data)

if __name__ == '__main__':
    app.run(debug=True)
