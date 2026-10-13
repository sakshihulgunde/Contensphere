data "aws_ami" "amazon_linux_2023" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-*-x86_64"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "web" {
  ami                    = data.aws_ami.amazon_linux_2023.id
  instance_type          = var.instance_type
  subnet_id              = var.subnet_id
  vpc_security_group_ids = [var.security_group_id]

  user_data = <<-EOF_SCRIPT
    #!/bin/bash
    dnf install -y httpd
    systemctl enable --now httpd

    cat > /var/www/html/index.html <<'HTML'
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>ContentSphere - Terraform Project</title>
      <style>
        body { font-family: Arial; background: #f1f5f9; color: #172554; padding: 40px; }
        main { max-width: 700px; margin: auto; background: white; padding: 32px; border-radius: 14px; }
        h1 { color: #2563eb; }
        .status { padding: 14px; background: #dcfce7; color: #166534; }
      </style>
    </head>
    <body>
      <main>
        <h1>ContentSphere</h1>
        <p>Infrastructure as Code Deployment and Automation using Terraform</p>
        <p><strong>Student Name:</strong> Sakshi Hulgunde</p>
        <p><strong>Batch Code:</strong> DRA-501</p>
        <p><strong>AWS Region:</strong> ap-south-1</p>
        <p><strong>Environment:</strong> Development</p>
        <p class="status">Infrastructure Provisioned using Terraform</p>
      </main>
    </body>
    </html>
    HTML
  EOF_SCRIPT

  user_data_replace_on_change = true

  metadata_options {
    http_tokens   = "required"
    http_endpoint = "enabled"
  }

  tags = {
    Name = "${var.project_name}-web-server"
  }
}
