import requests
import json
import boto3
from os import path
from udemy.decorators import Decorators

class UdemyInstructor:

  def __init__(self, api_key, webhook_url):
    self.api_key = api_key
    self.authorization = {
        'Authorization': 'bearer %s' % self.api_key 
    }
    self.webhook_url = webhook_url

  @Decorators.pretty_json
  def get_reviews_json(self):
    return "https://www.udemy.com/instructor-api/v1/taught-courses/reviews/"

  @Decorators.pretty_json
  def get_courses_json(self):
    return "https://www.udemy.com/instructor-api/v1/taught-courses/courses/"

  def pull_new_reviews(self):
    response = requests.get (
      'https://www.udemy.com/instructor-api/v1/taught-courses/reviews/',
      headers=self.authorization
    )

    with open ("db/db.json", "w") as db:
      json.dump(response.json(), db, indent=2)

    reviews = json.loads(response.content)
    course_ids = '\n'.join(reviews["id"] for reviews in reviews["results"])

    with open("db/new_reviews.txt", "w") as file:
          file.write(course_ids)

  def get_diff_reviews(self):
    with open("db/old_reviews.txt") as old_reviews:
      with open("db/new_reviews.txt") as new_reviews:
        strip_diff = [diff.strip() for diff in set(new_reviews).difference(old_reviews)]
    return strip_diff

  @staticmethod
  def set_old_db(self):
    with open ("db/new_reviews.txt", "r") as new_reviews:
      with open ("db/old_reviews.txt", "w") as old_reviews:
        old_reviews.write(new_reviews.read())

  def show_new_reviews(self):
    with open ("db/db.json", "r") as file:

      messages = []
      reviews = json.load(file)
      diff_reviews = self.get_diff_reviews()

      for reviews in reviews["results"]:
        if reviews["id"] in diff_reviews:
          user = reviews["user"]["name"]
          rating = reviews["rating"]
          comment = reviews["content"]

          messages.append("O usuário **%s** avaliou com o score **%s**!" % (user, rating))
      
      payload = {"content": '\n'.join(messages)}
      requests.post(self.webhook_url, data=payload)

    self.set_old_db()

  def run(self):
    self.create_db_file()
    # self.pull_new_reviews()
    # self.show_new_reviews()