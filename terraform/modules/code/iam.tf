resource "aws_iam_policy" "udemy_policy" {

  name = format("%s-policy", var.project-name)
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:GetObject",
          "s3:PutObject"
        ]
        Effect = "Allow"
        Resource = var.s3_arn
      },
    ]
  })

}

resource "aws_iam_role" "udemy_role" {

  name = format("%s-role", var.project-name)

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [ "sts:AssumeRole" ]
        Effect = "Allow"
        Principal = {
          "Service": "lambda.amazonaws.com"
        }
        Sid = ""
      },
    ]
  })

  managed_policy_arns = [aws_iam_policy.udemy_policy.arn]

}
