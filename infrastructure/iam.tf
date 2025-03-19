resource "aws_iam_user" "kestra_instance" {
  name = "kestra"

  tags = {
    Environment = "Dev"
    Owner = "Data Platform Team"
    Service = "Kestra"
  }
}

resource "aws_iam_access_key" "kestra_keys" {
  user = aws_iam_user.kestra_instance.name
}

resource "aws_ssm_parameter" "kestra_access_key" {
  name  = "/dev/kestra/aws_access_key/"
  type  = "String"
  value = aws_iam_access_key.kestra_keys.id
}

resource "aws_ssm_parameter" "kestra_secret_access_key" {
  name  = "/dev/kestra/aws_secret_access_key/"
  type  = "String"
  value = aws_iam_access_key.kestra_keys.secret
}
