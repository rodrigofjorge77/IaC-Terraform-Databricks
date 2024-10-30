provider "aws" {
  region = "us-east-2"  # Altere para a região que você preferir
}

# Bucket creation
resource "aws_s3_bucket" "my_s3_bucket"{
    bucket = "rodrigojorge-projeto202410-pispark"

    tags = {
    Name = "My bucket"
    Enviroment ="Dev"
  }
}

# Outputs para facilitar a visualização das informações
output "bucket_name" {
  value = aws_s3_bucket.my_s3_bucket.bucket
}
