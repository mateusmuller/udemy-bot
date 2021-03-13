resource "aws_iam_policy" "udemy_policy_invoke_lambda" {

  name = format("%s-policy-invoke-lambda", var.project-name)
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "lambda:InvokeFunction"
        ]
        Effect = "Allow"
        Resource = aws_lambda_function.udemy_lambda.arn
      },
    ]
  })

}

resource "aws_iam_role" "udemy_role_cloudwatch" {

  name = format("%s-role-cloudwatch", var.project-name)

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [ "sts:AssumeRole" ]
        Effect = "Allow"
        Principal = {
          "Service": "events.amazonaws.com"
        }
        Sid = ""
      },
    ]
  })

  managed_policy_arns = [
    aws_iam_policy.udemy_policy_invoke_lambda.arn
  ]

}