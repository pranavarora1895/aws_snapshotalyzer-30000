import boto3

if __name__=='__main__':
    session = boto3.Session(
    aws_access_key_id = 'AKIAVCU5LPAZKRLU57UC',
    aws_secret_access_key = '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')


    ec2 = session.resource('ec2','us-east-1')
    for i in ec2.instances.all():
        print(i)
