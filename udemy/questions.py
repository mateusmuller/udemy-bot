import requests
import json
from markdownify import markdownify
from udemy.decorators import Decorators

class UdemyQuestion:

  def __init__(self, api_key, webhook_url):
    self.api_key = api_key
    self.webhook_url = webhook_url
    self.authorization = {
      "Authorization": "bearer %s" % self.api_key 
    }
    self.messages = ["Oi Mateus,\n"]

  @Decorators.pretty_json
  def get_questions_json(self):
    return "https://www.udemy.com/instructor-api/v1/taught-courses/questions/?status=unread"

  """Pull unread questions and call parse_json"""
  def pull_new_questions(self):
    response = requests.get (
      "https://www.udemy.com/instructor-api/v1/taught-courses/questions/?status=unread",
      headers=self.authorization
    )
    self.parse_response(response.content)

  """Parse the response and extract title, body and course to pass to format_message"""
  def parse_response(self, response):
    dump = json.loads(response)
    self.messages.append("Você tem **%s** perguntas não lidas.\n" % dump["count"])
    for unread_questions in dump["results"]:
      title = unread_questions["title"]
      body = markdownify(unread_questions["body"]).strip("\n")
      course = unread_questions["course"]["title"]

      self.format_message(title, body, course)

  """Format using markdown tricks to send to discord and append to self.messages"""
  def format_message(self, title, body, course):
    self.messages.append("Curso: **```diff\n+%s```**" \
                         "Título: **```diff\n+%s```**" \
                         "Pergunta: **```diff\n%s```**" % (course, title, body))

  """Return the self.messages """
  def report(self):
    self.pull_new_questions()
    return self.messages
