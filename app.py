#!/usr/bin/python3

from udemy.udemy import UdemyInstructor
import os

if __name__ == '__main__':

  api_key = os.getenv('UDEMY_API_KEY')

  udemy_instructor = UdemyInstructor(api_key)
  # udemy_instructor.get_courses_id()
  # print(udemy_instructor.get_courses_json())
  # print(udemy_instructor.get_reviews_json())
udemy_instructor.get_last_reviews()