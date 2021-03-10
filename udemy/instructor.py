import requests
import json
import boto3
from udemy.decorators import Decorators

class UdemyInstructor:

  files_directory = "/tmp"

  def __init__(self, api_key, webhook_url):
    self.api_key = api_key
    self.webhook_url = webhook_url
    self.authorization = {
      "Authorization": "bearer %s" % self.api_key 
    }
    self.persistent_files = {
      "db": "db.json",
      "new": "new_reviews.txt",
      "old": "old_reviews.txt"
    }

  @Decorators.pretty_json
  def get_reviews_json(self):
    return "https://www.udemy.com/instructor-api/v1/taught-courses/reviews/"

  @Decorators.pretty_json
  def get_courses_json(self):
    return "https://www.udemy.com/instructor-api/v1/taught-courses/courses/"

  def download_files(self, bucket="udemy-mateusmuller-s3"):
    s3 = boto3.resource("s3")
    for _, value in self.persistent_files.items():
      s3.meta.client.download_file(bucket, value, "/tmp/%s" % value)

  def upload_files(self, file=None, bucket="udemy-mateusmuller-s3"):
    s3 = boto3.resource("s3")
    for _, value in self.persistent_files.items():
      if file is None:
        s3.meta.client.upload_file("/tmp/%s" % value, bucket, value)
      else:
        s3.meta.client.upload_file(file, bucket, value)

  def set_json_db(self, response, file=None):
    if file is None:
      with open ("/tmp/%s" % self.persistent_files["db"], "w") as db:
        json.dump(response, db, indent=2)
    else:
      with open (file, "w") as db:
        json.dump(response, db, indent=2)

  def get_course_id_from_json(self, response):
    reviews = json.loads(response)
    course_ids = "\n".join(reviews["id"] for reviews in reviews["results"])
    return course_ids

  def set_new_reviews(self, ids, file=None):
    if file is None:
      with open("/tmp/%s" % self.persistent_files["new"], "w") as new:
        new.write(ids)
    else:
      with open(file, "w") as new:
        new.write(ids)

  def pull_new_reviews(self):
    response = requests.get (
      "https://www.udemy.com/instructor-api/v1/taught-courses/reviews/",
      headers=self.authorization
    )

    self.download_files()
    self.set_json_db(response.json())
    self.set_new_reviews(self.get_course_id_from_json(response.content))

  def get_diff_reviews(self, old=None, new=None):
    if old is None or new is None:
      with open("/tmp/%s" % self.persistent_files["old"]) as old_reviews:
        with open("/tmp/%s" % self.persistent_files["new"]) as new_reviews:
          strip_diff = [diff.strip() for diff in set(new_reviews).difference(old_reviews)]
    else:
      with open(old) as old_reviews:
        with open(new) as new_reviews:
          strip_diff = [diff.strip() for diff in set(new_reviews).difference(old_reviews)]
    return strip_diff

  def move_new_to_old(self):
    with open ("%s/new_reviews.txt" % (self.files_directory), "r") as new_reviews:
      with open ("%s/old_reviews.txt" % (self.files_directory), "w") as old_reviews:
        old_reviews.write(new_reviews.read())
    self.upload_files()

  def get_new_reviews(self):
    with open ("%s/db.json" % (self.files_directory), "r") as file:

      messages = []
      reviews = json.load(file)
      diff_reviews = self.get_diff_reviews()

      for reviews in reviews["results"]:
        if reviews["id"] in diff_reviews:
          user = reviews["user"]["name"]
          rating = reviews["rating"]
          comment = reviews["content"]
          messages.append("O usuário **%s** avaliou com o score **%s**!" % (user, rating))

    self.send_webook(messages)
    self.move_new_to_old()

  def send_webook(self, messages):
    payload = {"content": "\n".join(messages)}
    requests.post(self.webhook_url, data=payload)

  def run(self):
    self.pull_new_reviews()
    self.get_new_reviews()