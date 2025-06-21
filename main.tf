provider "aws" {
  region = "us-east-1"
}

# VPC A
resource "aws_vpc" "vpc_a" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "VPC-A"
  }
}

resource "aws_subnet" "subnet_a" {
  vpc_id            = aws_vpc.vpc_a.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "Subnet-A"
  }
}

# VPC B
resource "aws_vpc" "vpc_b" {
  cidr_block = "10.1.0.0/16"
  tags = {
    Name = "VPC-B"
  }
}

resource "aws_subnet" "subnet_b" {
  vpc_id            = aws_vpc.vpc_b.id
  cidr_block        = "10.1.1.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "Subnet-B"
  }
}

# VPC Peering Connection
resource "aws_vpc_peering_connection" "peer" {
  vpc_id      = aws_vpc.vpc_a.id
  peer_vpc_id = aws_vpc.vpc_b.id
  auto_accept = true
  tags = {
    Name = "VPC-A-to-VPC-B"
  }
}

# Route table for VPC A
resource "aws_route_table" "rt_a" {
  vpc_id = aws_vpc.vpc_a.id
}

resource "aws_route" "route_a_to_b" {
  route_table_id            = aws_route_table.rt_a.id
  destination_cidr_block    = aws_vpc.vpc_b.cidr_block
  vpc_peering_connection_id = aws_vpc_peering_connection.peer.id
}

resource "aws_route_table_association" "assoc_a" {
  subnet_id      = aws_subnet.subnet_a.id
  route_table_id = aws_route_table.rt_a.id
}

# Route table for VPC B
resource "aws_route_table" "rt_b" {
  vpc_id = aws_vpc.vpc_b.id
}

resource "aws_route" "route_b_to_a" {
  route_table_id            = aws_route_table.rt_b.id
  destination_cidr_block    = aws_vpc.vpc_a.cidr_block
  vpc_peering_connection_id = aws_vpc_peering_connection.peer.id
}

resource "aws_route_table_association" "assoc_b" {
  subnet_id      = aws_subnet.subnet_b.id
  route_table_id = aws_route_table.rt_b.id
}
