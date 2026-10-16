output "vpc_id" {
  description = "ID of the provisioned VPC"
  value       = aws_vpc.main.id
}

output "igw_id" {
  description = "ID of the internet gateway"
  value       = aws_internet_gateway.main.id
}
