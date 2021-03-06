# pip install django-storages
# pip install boto3

from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    bucket_name = 'm-dsta'

    file_overwrite = False
    region_name = 'ap-northeast-2'
    custom_domain = '%s.s3.%s.amazonaws.com' % (bucket_name, region_name)
