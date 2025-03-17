resource "aws_s3_bucket" "s3-input" {
  bucket = "ayomayowa-emr-input-bucket"

  tags = {
    Name        = "Input bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket" "s3-output" {
  bucket = "ayomayowa-emr-output-bucket"

  tags = {
    Name        = "Output bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket" "s3-logs" {
  bucket = "ayomayowa-emr-logs-bucket"

  tags = {
    Name        = "Logs bucket"
    Environment = "Dev"
  }
}