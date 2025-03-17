# # VPC Stacks

# # VPC
# resource "aws_vpc" "main" {
#   cidr_block = "10.0.0.0/16"
# }

# # Subnet

# resource "aws_subnet" "main" {
#   vpc_id     = aws_vpc.main.id
#   cidr_block = "10.0.1.0/24"

#   tags = {
#     Name = "Public Subnet"
#   }
# }



# Provisioning the VPC

resource "aws_vpc" "emr-vpc" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"
  enable_dns_hostnames = true

  tags = {
    Name = "emr-vpc"
  }
}

# Creating private subnet
resource "aws_subnet" "private-subnet" {
  vpc_id     = aws_vpc.custom-vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "eu-central-1a"

  tags = {
    Name = "private-subnet"
  }
}


# Creating public subnet
resource "aws_subnet" "public-subnet" {
  vpc_id     = aws_vpc.custom-vpc.id
  cidr_block = "10.0.2.0/24"
  availability_zone = "eu-central-1b"
  map_public_ip_on_launch = true

  tags = {
    Name = "public-subnet"
  }
}

