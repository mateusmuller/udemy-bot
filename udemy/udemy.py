#!/usr/bin/python3

import requests
import json

class UdemyInstructor:

  def __init__(self, api_key):
    self.api_key = api_key
    self.authorization = {
        'Authorization': 'bearer %s' % self.api_key 
    }

  def pretty_json(func):
    
    def formatter(self):
      load_json = json.loads(func(self))
      return json.dumps(load_json, indent=4, sort_keys=True)

    return formatter

  @pretty_json
  def get_reviews_json(self):
    payload = {
        # 'status': 'commented'
    }

    response = requests.get (
      'https://www.udemy.com/instructor-api/v1/taught-courses/reviews/',
      headers=self.authorization,
      params=payload
    )

    return response.content

  @pretty_json
  def get_courses_json(self):
    payload = {
    
    }

    response = requests.get (
      'https://www.udemy.com/instructor-api/v1/taught-courses/courses/',
      headers=self.authorization,
      params=payload
    )

    return response.content

  def get_courses_id(self):
    payload = {
    
    }

    response = requests.get (
      'https://www.udemy.com/instructor-api/v1/taught-courses/courses/',
      headers=self.authorization,
      params=payload
    )

    courses = json.loads(response.content)

    for courses in courses["results"]:
      course_id = courses["id"]
      course_title = courses["title"]
      print (f"{course_id} - {course_title}")

  def get_last_reviews(self):
    payload = {
        # 'status': 'commented'
    }

    response = requests.get (
      'https://www.udemy.com/instructor-api/v1/taught-courses/reviews/',
      headers=self.authorization,
      params=payload
    )

    reviews = json.loads(response.content)
    course_ids = '\n'.join(reviews["id"] for reviews in reviews["results"])
    return course_ids

  def populate_new_reviews(self):
    f = open("review_db.txt", "w")
    f.write(self.get_last_reviews())
    f.close()

  def compare_reviews(self):
    f = open("review_db.txt", "r")
    if f.read() == self.get_last_reviews():
      f.close()
      return True
    f.close()
    return False

  