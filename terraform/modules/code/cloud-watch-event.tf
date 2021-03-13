resource "aws_cloudwatch_event_rule" "udemy_event" {
  name = format("%s-trigger", var.project-name)
  schedule_expression = "cron(00 12,00 ? * * *)"
  role_arn = aws_iam_role.udemy_role_cloudwatch.arn
}

resource "aws_cloudwatch_event_target" "udemy_event_target" {  
  rule = aws_cloudwatch_event_rule.udemy_event.id
  arn = aws_lambda_function.udemy_lambda.arn
}