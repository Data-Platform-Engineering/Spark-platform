
# Provisioning the VPC where EMR will be deployed

resource "aws_vpc" "emr-vpc" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"
  enable_dns_hostnames = true

  tags = {
    Name = "production-emr"
    environment = "production"
    owner = "data_platform_team"
    managed_by = "terraform"
  }
}

# Creating private subnet
resource "aws_subnet" "private-subnet" {
  vpc_id     = aws_vpc.emr-vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "eu-central-1a"

  tags = {
    Name = "private-subnet"
  }
}


# Creating public subnet
resource "aws_subnet" "public-subnet" {
  vpc_id     = aws_vpc.emr-vpc.id
  cidr_block = "10.0.2.0/24"
  availability_zone = "eu-central-1b"
  map_public_ip_on_launch = true

  tags = {
    Name = "public-subnet"
  }
}

# Creating internet gateway and attaching to VPC
resource "aws_internet_gateway" "emr-igw" {
  vpc_id = aws_vpc.emr-vpc.id

  tags = {
    Name = "emr-igw"
  }
}

# Creating route table
resource "aws_route_table" "public-rt" {
  vpc_id = aws_vpc.emr-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.emr-igw.id
  }

  tags = {
    Name = "public-rt"
  }
}


# Making explicit association of public subnet to route table
resource "aws_route_table_association" "public-subnet-association" {
  subnet_id      = aws_subnet.public-subnet.id
  route_table_id = aws_route_table.public-rt.id
}

