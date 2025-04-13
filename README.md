S3 Bucket Inspector + AI Summary

This Python script scans all S3 buckets in your AWS account and generates a human-readable security summary using OpenAI's GPT 4.0 mini model, although you can change out models. 

+ Requirements

- Python 3.7+
- Boto3
- OpenAI SDK (v1.0+) and $$ credits to use for OpenAI's API tokens 
**even if you have a paid subsubscription, you still must purchase credits for token usage**

Setup
1. Install dependencies
2. Set up AWS credentials
3. Add your OpenAI API key
4. Run the inspector script
5. Run the AI summary script
 
 You'll get a summary of your security posture of your S3 buckets - this was more of an excersize for me in wading into AI land while also addressig practical need.
 
 MIT License