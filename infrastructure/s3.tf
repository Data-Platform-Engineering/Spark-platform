resource "aws_s3_bucket" "s3-input" {
  bucket = "ayomayowa-emr-input-bucket"

  tags = {
    Service     = "EMR"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket" "s3-output" {
  bucket = "ayomayowa-emr-output-bucket"

  tags = {
    Service     = "EMR"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket" "s3-logs" {
  bucket = "ayomayowa-emr-logs-bucket"

  tags = {
    Service     = "EMR"
    Environment = "Dev"
  }
}