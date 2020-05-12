import os

import boto3

from books.use_cases.repositories import BaseS3Repository


AUTHORS_BUCKET_NAME = os.environ['AWS_AUTHORS_BUCKET_NAME']
BOOKS_BUCKET_NAME = os.environ['AWS_BOOKS_BUCKET_NAME']


class S3Repository(BaseS3Repository):
    def save_author_image(self, image: bytes, key: str) -> str:
        client = self._get_client()
        client.put_object(
            Body=image,
            Bucket=AUTHORS_BUCKET_NAME,
            Key=key,
            ContentType=image.mimetype
        )

        return key

    def save_book_image(self, image: bytes, key: str) -> str:
        client = self._get_client()
        client.put_object(
            Body=image,
            Bucket=BOOKS_BUCKET_NAME,
            Key=key,
            ContentType=image.mimetype
        )

        return key

    def _get_client(self):
        endpoint = os.environ.get('AWS_ENDPOINT_URL', None)

        s3 = boto3.resource('s3', endpoint_url=endpoint)
        return boto3.client('s3', endpoint_url=endpoint)
