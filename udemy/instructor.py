#!/usr/bin/python3

import requests
import json
from os import path

class UdemyInstructor:

  class Decorators(object):
    @classmethod
    def pretty_json(cls, func):    
        def formatter(self):
          load_json = json.loads(func(self))
          return json.dumps(load_json, indent=4, sort_keys=True)
        return formatter

  def __init__(self, api_key):
    self.api_key = api_key
    self.authorization = {
        'Authorization': 'bearer %s' % self.api_key 
    }

  @Decorators.pretty_json
  def get_reviews_json(self):
    response = requests.get (
      'https://www.udemy.com/instructor-api/v1/taught-courses/reviews/',
      headers=self.authorization
    )
    return response.content

  @Decorators.pretty_json
  def get_courses_json(self):
    response = requests.get (
      'https://www.udemy.com/instructor-api/v1/taught-courses/courses/',
      headers=self.authorization
    )
    return response.content

  # def get_courses_id(self):
  #   response = requests.get (
  #     'https://www.udemy.com/instructor-api/v1/taught-courses/courses/',
  #     headers=self.authorization
  #   )

  #   courses = json.loads(response.content)

  #   for courses in courses["results"]:
  #     course_id = courses["id"]
  #     course_title = courses["title"]
  #     print (f"{course_id} - {course_title}")

  @staticmethod
  def create_db_file():
    if not path.exists("old_reviews.txt"):
      with open("old_reviews.txt", "w") as file:
        file.write("")
    if not path.exists("new_reviews.txt"):
      with open("new_reviews.txt", "w") as file:
        file.write("")

  def pull_new_reviews(self):
    response = requests.get (
      'https://www.udemy.com/instructor-api/v1/taught-courses/reviews/',
      headers=self.authorization
    )

    with open ("db.json", "w") as db:
      json.dump(response.json(), db, indent=2)

    reviews = json.loads(response.content)
    course_ids = '\n'.join(reviews["id"] for reviews in reviews["results"])

    with open("new_reviews.txt", "w") as file:
          file.write(course_ids)

  def get_diff_reviews(self):
    with open("old_reviews.txt") as old_reviews:
      with open("new_reviews.txt") as new_reviews:
        strip_diff = [diff.strip() for diff in set(new_reviews).difference(old_reviews)]
    return strip_diff

  def set_old_db(self):
    with open ("new_reviews.txt", "r") as new_reviews:
      with open ("old_reviews.txt", "w") as old_reviews:
        old_reviews.write(new_reviews.read())

  def show_new_reviews(self):
    with open ("db.json", "r") as file:

      reviews = json.load(file)
      diff_reviews = self.get_diff_reviews()

      for reviews in reviews["results"]:
        if reviews["id"] in diff_reviews:
          user = reviews["user"]["name"]
          rating = reviews["rating"]
          comment = reviews["content"]

          print(f"O usuário {user} deixou a avaliação com nota {rating}. Veja o comentário:")
          print(f"{comment}")

    self.set_old_db()