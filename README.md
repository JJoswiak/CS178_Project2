# CS178 Project 2: Automated "Stat of the Day" Email with AWS

# This project is a serverless application that automatically sends a random "Stat of the Day" email every morning at 7:00 AM using AWS services. 
It integrates AWS Lambda, DynamoDB, SES (Simple Email Service), EventBridge, and IAM roles to deliver a personalized, scheduled email system.

---

## Project Summary

# - Stores a list of Brody Peebles basketball stats in a DynamoDB table (Project2Stats)
# - AWS Lambda function selects a random stat and sends it via SES
# - Daily automation at 7:00 AM using EventBridge rules
# - Python files are built and tested in VS Code, then deployed to Lambda
# - IAM roles are carefully configured to allow secure service integration

---

## Technologies Used

# - Python 3 – Programming language
# - AWS Lambda – Serverless function execution
# - AWS DynamoDB – NoSQL database storing stats
# - Amazon SES – Sending emails
# - Amazon EventBridge – Scheduled daily trigger
# - IAM Roles – Secure access between services
# - boto3 – Python AWS SDK for interacting with services

---
