output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.app_server.id
}

output "public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.app_server.public_ip
}

output "website_url" {
  description = "URL of the web server"
  value       = "http://${aws_instance.app_server.public_ip}"
}