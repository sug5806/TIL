# pip install django-storages
# pip install boto3

from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    # location = 'media'
    bucket_name = 'board-media.economy-info.site'
    custom_domain = '%s' % bucket_name
    file_overwrite = False
