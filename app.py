#!/usr/bin/env python

from udemy.instructor import UdemyInstructor
import os

if __name__ == '__main__':
  api_key = os.getenv('UDEMY_API_KEY')
  webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

  udemy_instructor = UdemyInstructor(api_key, webhook_url)
  udemy_instructor.run()