import pytest
import os
import boto3
from udemy.reviews import UdemyReview
from moto import mock_s3

class TestS3():

  @pytest.fixture
  def s3_client(self, aws_credentials):
    with mock_s3():
      yield boto3.client('s3', region_name='us-east-1')

  @pytest.fixture
  def bucket_name(self):
    return "my-test-bucket"

  @pytest.fixture
  def s3_test(self, s3_client, bucket_name):
    s3_client.create_bucket(Bucket=bucket_name)
    yield

  def test_download_files(self, s3_client, s3_test, tmpdir):
    a_file = tmpdir.join('dummy.txt')
    a_file.write("test")

    s3_client.upload_file(str(a_file), "my-test-bucket", "old_reviews.txt")
    s3_client.upload_file(str(a_file), "my-test-bucket", "new_reviews.txt")
    s3_client.upload_file(str(a_file), "my-test-bucket", "db.json")

    udemy_review = UdemyReview("","")
    udemy_review.download_files(bucket="my-test-bucket")

    downloaded_files = {
      "/tmp/old_reviews.txt",
      "/tmp/new_reviews.txt",
      "/tmp/db.json"
    }

    for file in downloaded_files:
      assert os.path.exists(file)
      os.remove(file)

  def test_upload_files(self, s3_client, s3_test, tmpdir):
    udemy_review = UdemyReview("","")

    a_file = tmpdir.join('dummy.txt')
    a_file.write("test")
      
    udemy_review.upload_files(str(a_file), "my-test-bucket")

    uploaded_files = {
      "old_reviews.txt",
      "new_reviews.txt",
      "db.json"
    }

    for file in uploaded_files:
      assert s3_client.get_object(Bucket="my-test-bucket", Key=file)["Body"].read().decode("utf-8") == "test"
