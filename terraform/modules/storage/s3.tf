resource "aws_s3_bucket" "udemy_s3" {
  bucket = format("%s-s3", var.project-name)
  acl    = "private"
}

resource "aws_s3_bucket_public_access_block" "udemy_s3_policy" {
  bucket = aws_s3_bucket.udemy_s3.id

  block_public_acls   = true
  block_public_policy = true
}