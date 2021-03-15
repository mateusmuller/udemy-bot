# What is Udemy bot?

A small script to grab some data from the [Udemy Instructor API](https://www.udemy.com/developers/instructor/), build a sort of report and send on a Discord channel.

# Why does it exist?

I built this bot purely to combinate some keys technologies I was studying like Python, AWS, Terraform, Docker, GitHub Actions and Git.

# How can I test it out?

Obviously, you must be an Udemy Instructor, or at least have an Udemy Instructor API key. Otherwise, it won't even authenticate.

```
$ git clone https://github.com/mateusmuller/udemy-bot.git
$ cd udemy-bot/
```

### AWS

The first step is to build the AWS infrastructure to run the code. I worked on some Terraform modules to make it work, it creates an S3 bucket, ECR, Docker image, Lambda Function, CloudWatch events and IAM policies.

```
$ cd terraform/
$ terraform apply -var 'project-name=<some-random-name>'
```

This `project-name` variable is used to define the resources names on aws.

If it fails, it might be because Lambda needs the Docker image URI and for timeout reasons it won't be able to gather. Run it again and it should work.

### GitHub Actions

There is a simple CI/CD pipeline setup to run `pytest`, build the docker image, push do ECR and update the Lambda Function.

### Docker

This script relies on `UDEMY_API_KEY` and `DISCORD_WEBHOOK_URL` environment variables, so you have to build the image with them.

Also, this image is prepared to run on AWS Lambda, se here is how you test it:

```
$ export UDEMY_API_KEY=<your-api-key>
$ export DISCORD_WEBHOOK_URL=<webhook-url>
$ docker build --build-arg=DISCORD_WEBHOOK_URL=$DISCORD_WEBHOOK_URL --build-arg=UDEMY_API_KEY=$UDEMY_API_KEY -t udemy-bot:0.1 .
$ docker run -v $HOME/.aws:/root/.aws -p 9000:8080 udemy-bot:0.1
```

I am volume binding the AWS credentials as the script needs to upload to S3.

To test the lambda function on Docker:

```
$ curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

If it works, then you are probably good to go.

### Quick note

You might have to adjust the S3 bucket name and other stuff to the proper name.