import pytest
import json
from udemy.instructor import UdemyReview

class TestFiles():
  
  @pytest.fixture
  def dummy_json (self):
    yield '{"count":1522,"next":"https://www.udemy.com/instructor-api/v1/taught-courses/reviews/?page=2","previous":null,"results":[{"_class":"course_review","id":"x01CAFhSD_6wPM321pON6waQQ==","content":"","rating":5,"created":"2020-09-21T18:54:51Z","user_modified":"2021-03-09T14:17:37Z","user":{"_class":"user","id":"x01jhjU5dSsDWVMP5XhyEXKvw==","title":"Angelica Ribeiro Silva","name":"Angelica Ribeiro"}},{"_class":"course_review","id":"x01-6Dwu9Ab3Zy7KPL-DFS5KQ==","content":"","rating":3,"created":"2021-01-04T16:21:48Z","user_modified":"2021-03-08T17:55:17Z","user":{"_class":"user","id":"x01tKuvwpw_ZyQHQ6Ba6T1Gkw==","title":"Bruno Nunes Rocha","name":"Bruno Nunes"}},{"_class":"course_review","id":"x01XLu2rUpjCGn8hu52N1Qfxg==","content":"","rating":5,"created":"2021-03-08T14:07:10Z","user_modified":"2021-03-08T14:07:10Z","user":{"_class":"user","id":"x01Ed8F8ZbNzN8J-nBOxJw4Rw==","title":"Thiago Martins de Melo","name":"Thiago Martins"}},{"_class":"course_review","id":"x01us7y2AAvXwjqcQJ9Oj62jA==","content":"","rating":5,"created":"2021-03-01T12:08:01Z","user_modified":"2021-03-07T18:46:38Z","user":{"_class":"user","id":"x01SFEu3AkbWtmyzlnzoAUVtw==","title":"Igor Dias szot","name":"Igor Dias"}},{"_class":"course_review","id":"x01PcDCc9I2rGNT0L3MyG5oVA==","content":"","rating":5,"created":"2021-03-06T22:27:22Z","user_modified":"2021-03-06T22:27:23Z","user":{"_class":"user","id":"x0193hXnbUAzm6SZusiu1E3bA==","title":"Diego Henrique Rezek Silveira","name":"Diego Henrique"}},{"_class":"course_review","id":"x01sS4Nga9DID94ytCMkG_t-Q==","content":"","rating":4,"created":"2021-03-05T20:21:52Z","user_modified":"2021-03-05T20:21:54Z","user":{"_class":"user","id":"x01ZkCYY0iRQ8zpGOMa7TP-yg==","title":"Nicolas Eduardo Pasqual Duarte","name":"Nicolas Eduardo Pasqual"}},{"_class":"course_review","id":"x01qo4eHjoqprlKmwvK-KMvWg==","content":"","rating":5,"created":"2021-03-05T18:24:20Z","user_modified":"2021-03-05T18:24:21Z","user":{"_class":"user","id":"x01aMrw3WEu0FYarG8SmdRdqA==","title":"Pedro Lobo","name":"Pedro"}},{"_class":"course_review","id":"x01UnpG74zUwAnR4qFQLW7tYw==","content":"","rating":3.5,"created":"2021-03-05T15:18:40Z","user_modified":"2021-03-05T15:18:44Z","user":{"_class":"user","id":"x01VW26lhNDlnvJmjppp3xaJA==","title":"Clayton Queiroga","name":"Clayton"}},{"_class":"course_review","id":"x01h7ZcKt0sNh9k3fyOkCeE3g==","content":"","rating":3.5,"created":"2021-03-05T06:57:44Z","user_modified":"2021-03-05T06:57:45Z","user":{"_class":"user","id":"x01KKN8kdBQUcRMlUyqDra63g==","title":"Diego Alves da Silva","name":"Diego Alves"}},{"_class":"course_review","id":"x011qZ7SsQ0DQvzCStRO_gFSQ==","content":"","rating":5,"created":"2021-03-05T00:30:43Z","user_modified":"2021-03-05T00:30:44Z","user":{"_class":"user","id":"x01SldRtZmr2_rKkWK3rQ5Z-Q==","title":"Pedro Victor Silva de Souza","name":"Pedro Victor Silva"}},{"_class":"course_review","id":"x01WdNcrfvrPog7WKQTErurIg==","content":"Excelente curso, se rolar uma promo no curso de Linux  Completo eu consigo me inscrever. Obrigado!","rating":5,"created":"2021-03-04T18:46:30Z","user_modified":"2021-03-04T18:54:02Z","user":{"_class":"user","id":"x01MhFU8QlLU0lNH7GLr2_r2A==","title":"Adilson Gonçalves Ximenes","name":"Adilson Gonçalves"}},{"_class":"course_review","id":"x01M0VxXW_3gRQUQh-rMiUYqQ==","content":"","rating":5,"created":"2019-11-14T00:31:52Z","user_modified":"2021-03-04T15:33:16Z","user":{"_class":"user","id":"x01CxIOkY1nMAf5e0muSIOxhw==","title":"Veronica Arone","name":"Veronica"}}]}'

  @pytest.fixture
  def dummy_course_ids(self):
    yield """
x01CAFhSD_6wPM321pON6waQQ==
x01-6Dwu9Ab3Zy7KPL-DFS5KQ==
x01XLu2rUpjCGn8hu52N1Qfxg==
x01us7y2AAvXwjqcQJ9Oj62jA==
x01PcDCc9I2rGNT0L3MyG5oVA==
x01sS4Nga9DID94ytCMkG_t-Q==
x01qo4eHjoqprlKmwvK-KMvWg==
x01UnpG74zUwAnR4qFQLW7tYw==
x01h7ZcKt0sNh9k3fyOkCeE3g==
x011qZ7SsQ0DQvzCStRO_gFSQ==
x01WdNcrfvrPog7WKQTErurIg==
x01M0VxXW_3gRQUQh-rMiUYqQ==
"""
  @pytest.fixture
  def dummy_new_course_ids(self):
    yield """
x01CAFhSD_6wPM321pON6waQQ==
x01-6Dwu9Ab3Zy7KPL-DFS5KQ==
x01XLu2rUpjCGn8hu52N1Qfxg==
x01us7y2AAvXwjqcQJ9Oj62jA==
x01PcDCc9I2rGNT0L3MyG5oVA==
x01sS4Nga9DID94ytCMkG_t-Q==
x01qo4eHjoqprlKmwvK-KMvWg==
x01UnpG74zUwAnR4qFQLW7tYw==
h39281h9832c981jksxnkaskl==
x011qZ7SsQ0DQvzCStRO_gFSQ==
x01WdNcrfvrPog7WKQTErurIg==
x01M0VxXW_3gRQUQh-rMiUYqQ==
"""

  def test_set_json_db(self, dummy_json, tmpdir):
    a_file = tmpdir.join('db.json')
    udemy_review = UdemyReview("","")
    udemy_review.set_json_db(dummy_json, str(a_file))

    assert a_file.read() == json.dumps(dummy_json)

  def test_get_course_id_from_json (self, dummy_json):
    udemy_review = UdemyReview("","")

    assert udemy_review.get_course_id_from_json(dummy_json).count("\n") == 11

  def test_set_new_reviews(self, tmpdir, dummy_course_ids):
    a_file = tmpdir.join('new_reviews.txt')
    udemy_review = UdemyReview("","")
    udemy_review.set_new_reviews(dummy_course_ids, str(a_file))

    assert dummy_course_ids == a_file.read()

  def test_get_diff_reviews(self, tmpdir, dummy_course_ids, dummy_new_course_ids):
    udemy_review = UdemyReview("","")
    old = tmpdir.join('old_reviews.txt')
    new = tmpdir.join('news_reviews.txt')
    old.write(dummy_course_ids)
    new.write(dummy_new_course_ids)
    
    assert udemy_review.get_diff_reviews(str(old), str(new)) == "h39281h9832c981jksxnkaskl==".split()