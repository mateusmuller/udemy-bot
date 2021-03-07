resource "aws_lambda_function" "udemy_lambda" {
  function_name = format("%s-function", var.project-name)
  role = aws_iam_role.udemy_role.arn
  image_uri = "${var.ecr_url}:udemy-bot-latest"
  package_type = "Image"
}