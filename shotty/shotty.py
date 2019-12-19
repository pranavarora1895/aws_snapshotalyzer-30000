import boto3
import click



session = boto3.Session(
aws_access_key_id = '*youraccesskey*',
aws_secret_access_key = '*yoursecretaccesskey*')
ec2 = session.resource('ec2','us-east-1')

@click.command()
def list_instances():
    "List EC2 instances"
    for i in ec2.instances.all():
        print(','.join((i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))
    return

if __name__=='__main__':

    list_instances()
