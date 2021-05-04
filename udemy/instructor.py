from udemy.reviews import UdemyReview
from udemy.questions import UdemyQuestion
import requests

class UdemyInstructor:

  def __init__(self, api_key, webhook_url):
    self.api_key = api_key
    self.webhook_url = webhook_url
    self.review = UdemyReview(api_key, webhook_url)
    self.question = UdemyQuestion(api_key, webhook_url)

  def run(self):
    report = self.question.report() + self.review.report()
    payload = {"content": "\n".join(report)}
    requests.post(self.webhook_url, data=payload)