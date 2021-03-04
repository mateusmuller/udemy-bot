#!/usr/bin/python3

from udemy.udemy import UdemyInstructor
import os

if __name__ == '__main__':

  api_key = os.getenv('UDEMY_API_KEY')

  udemy_instructor = UdemyInstructor(api_key)
  udemy_instructor.run()
