S3 Bucket Inspector + AI Summary

This Python script scans all S3 buckets in your AWS account and generates a human-readable security summary using OpenAI's GPT 4.0 mini model, although you can change out models. 

Built with some help from ChatGPT for logic and syntax assistance.

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
 
Example of GPT AI Summary response:

=== AI Summary ===

The security posture of the listed S3 buckets can be summarized as follows:

### Summary of Security Posture
1. **Public Access**: All buckets are set to private, which is a positive aspect as it prevents unauthorized public access.
2. **Encryption**: All buckets are encrypted, which is crucial for protecting the data at rest and safeguarding it from unauthorized access.
3. **Versioning**: Only one bucket (myreplicationtarget239834) has versioning enabled. The other buckets do not have versioning, which means that if data is accidentally deleted or overwritten, recovery options are limited.

### Risks Identified
- **Lack of Versioning**: For buckets without versioning, any accidental deletions or overwrites of data cannot be recovered easily. This poses a risk of potential data loss.
- **Public Access Misconfiguration**: While all current settings indicate that buckets are private, there is always a risk of misconfiguration in the future. Continuous monitoring is necessary to ensure that public access settings remain secure.
- **No Lifecycle Policies**: There is no mention of lifecycle policies for managing data retention, which could lead to unnecessary storage costs or compliance issues if data is not appropriately managed.

### Suggested Improvements
1. **Enable Versioning**: Consider enabling versioning on all buckets. This would allow for easy recovery of data in case of accidental deletions or changes, enhancing data protection.
2. **Implement Lifecycle Policies**: Set up lifecycle policies for the buckets to manage data retention effectively. This can help reduce storage costs and ensure compliance with data retention policies.
3. **Regular Security Audits**: Conduct regular audits of bucket settings and access permissions to ensure that they remain secure and compliant with best practices.
4. **Monitor Access Logs**: Enable logging for the S3 buckets to monitor access patterns and detect any unauthorized access attempts. This can help in identifying and responding to potential security incidents promptly.
5. **Educate Users**: If multiple users have access to the buckets, provide training on best practices for managing S3 data, including avoiding accidental deletions and understanding the importance of encryption and versioning.

By implementing these improvements, you can enhance the overall security and management of your S3 buckets, reducing the risk of data loss and ensuring that your data remains secure.

