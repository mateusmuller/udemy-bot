resource "null_resource" "udemy_image" {

  provisioner "local-exec" {
    command = "aws ecr get-login-password --region sa-east-1 | docker login --username AWS --password-stdin ${aws_ecr_repository.udemy_ecr.repository_url}"
  }

  provisioner "local-exec" {
    command = "docker build --build-arg=DISCORD_WEBHOOK_URL=$DISCORD_WEBHOOK_URL --build-arg=UDEMY_API_KEY=$UDEMY_API_KEY -t udemy-bot:0.1 ../"
  }

  provisioner "local-exec" {
    command = "docker tag udemy-bot:0.1 ${aws_ecr_repository.udemy_ecr.repository_url}:udemy-bot-latest"
  }

  provisioner "local-exec" {
    command = "docker push ${aws_ecr_repository.udemy_ecr.repository_url}:udemy-bot-latest"
  }

  triggers = {
    always_run = "${timestamp()}"
  }
}
