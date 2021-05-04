resource "aws_ecr_repository" "udemy_ecr" {
  name = format("%s-ecr", var.project-name)
}