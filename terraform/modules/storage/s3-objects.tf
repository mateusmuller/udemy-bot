resource "aws_s3_bucket_object" "udemy_s3_object" {
  for_each = toset([ "db.json", "new_reviews.txt", "old_reviews.txt" ])
  
  bucket = aws_s3_bucket.udemy_s3.id
  key    = each.key
  source = "modules/storage/files/${each.key}"
}