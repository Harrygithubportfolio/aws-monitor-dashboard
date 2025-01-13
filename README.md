# AWS Monitoring Dashboard


## Overview
The **AWS Monitoring Dashboard** is a Flask-based web application that provides real-time monitoring of your AWS resources. This project showcases how to interact with various AWS services programmatically and present the data in a user-friendly web interface.

It supports the following AWS services:
- **EC2**: Monitor instance states, types, and regions.
- **S3**: List and display bucket details.
- **RDS**: Track the status of database instances.
- **Lambda**: View functions and their runtime configurations.
- **Lightsail**: Display instance states and metrics.

---

## Features
- **Dynamic Region Selection**: Monitor AWS resources in any region specified by the user.
- **Real-Time Data**: Refresh resource statuses periodically.
- **User-Friendly Dashboard**: Clean, responsive UI built with Flask and Bootstrap.
- **Extensibility**: Add more AWS services and metrics easily.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- AWS account with programmatic access enabled
- IAM role or user with the following permissions:
  - `ec2:DescribeInstances`
  - `s3:ListAllMyBuckets`
  - `rds:DescribeDBInstances`
  - `lambda:ListFunctions`
  - `lightsail:GetInstances`
  - `cloudwatch:GetMetricData`
- AWS CLI configured locally

### Step 1: Clone the Repository
```bash
git clone https://github.com/Harrygithubportfolio/aws-monitor-dashboard.git
cd aws-monitor-dashboard
Step 2: Set Up Environment
Create a Virtual Environment:

#### bash

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

#### bash

pip install -r requirements.txt
Step 3: Run the Application
Start the Flask application:

#### bash

python monitor-policies.py
Open your browser and visit:

http://127.0.0.1:5000/

Usage

Select a Region: When prompted, enter the AWS region you want to monitor (e.g., us-east-1, eu-west-2).

View Resource Details: The dashboard will display data for EC2, S3, RDS, Lambda, and Lightsail services.

Monitor Changes: Refresh the page or modify the region to fetch updated data.





Roadmap

 Add Cost Monitoring using the AWS Cost Explorer API.

 Integrate AWS SNS for alerts and notifications.

 Enable dynamic filters for resource types and states.

 Deploy the application on AWS Elastic Beanstalk or Lightsail.



License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or feedback, please reach out:

GitHub: Harrygithubportfolio
Email: [cloudtechhorizon@gmail.com] 

Acknowledgments
Built with Flask.
Powered by AWS Boto3 SDK.
UI styled with Bootstrap.
yaml


---

