resource "aws_cloudwatch_log_group" "udemy_log" {
  name              = format("/aws/lambda/%s-function", var.project-name)
  retention_in_days = 14
}