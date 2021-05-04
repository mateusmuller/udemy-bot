resource "aws_lambda_function" "udemy_lambda" {
  function_name = format("%s-function", var.project-name)
  role = aws_iam_role.udemy_role.arn
  image_uri = "${var.ecr_url}:udemy-bot-latest"
  package_type = "Image"
  timeout = 60
}

resource "aws_lambda_permission" "udemy_allow_cloud_watch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.udemy_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.udemy_event.arn
}