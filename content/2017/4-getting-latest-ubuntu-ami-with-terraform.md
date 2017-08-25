Title: Getting latest Ubuntu AMI with Terraform
Date: 2017-08-25 11:00
Author: Andrea Grandi
Category: Development
Tags: AWS, Terraform, Ubuntu, devops
Slug: getting-latest-ubuntu-ami-with-terraform
Status: published

When we need to create an EC2 resource on AWS using Terraform, we need to specify the AMI id to get the correct image.
The id is not easy to memorise and it changes depending on the zone we are working one. On every new release the id changes again.
So, how can we be sure to get the correct ID for our region, of the latest image available for a given Linux distribution?

### Getting latest Ubuntu AMI id

In this example I will show how to get the ID for the latest version of Ubuntu 16.04 server, for the London region and create an EC2 instance using that ID.

    :::terraform
    variable "aws_region" { default = "eu-west-2" } # London

    provider "aws" {
        region = "${var.aws_region}"
        access_key = "youraccesskey"
        secret_key = "yoursecretkey"
    }

    data "aws_ami" "ubuntu" {
        most_recent = true

        filter {
            name   = "name"
            values = ["ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-*"]
        }

        filter {
            name   = "virtualization-type"
            values = ["hvm"]
        }

        owners = ["099720109477"] # Canonical
    }

    resource "aws_instance" "web" {
        ami           = "${data.aws_ami.ubuntu.id}"
        instance_type = "t2.micro"

        tags {
            Name = "HelloUbuntu"
        }
    }

    output "image_id" {
        value = "${data.aws_ami.ubuntu.id}"
    }

After we have initialised our script using **terraform init** if we run it, we will get the AMI id and the instance will be created:

    :::
    ➜  example1$: terraform apply
    data.aws_ami.ubuntu: Refreshing state...
    aws_instance.web: Creating...
        ami:                          "" => "ami-03998867"
        associate_public_ip_address:  "" => "<computed>"
        availability_zone:            "" => "<computed>"
        ebs_block_device.#:           "" => "<computed>"
        ephemeral_block_device.#:     "" => "<computed>"
        instance_state:               "" => "<computed>"
        instance_type:                "" => "t2.micro"
        ipv6_address_count:           "" => "<computed>"
        ipv6_addresses.#:             "" => "<computed>"
        key_name:                     "" => "<computed>"
        network_interface.#:          "" => "<computed>"
        network_interface_id:         "" => "<computed>"
        placement_group:              "" => "<computed>"
        primary_network_interface_id: "" => "<computed>"
        private_dns:                  "" => "<computed>"
        private_ip:                   "" => "<computed>"
        public_dns:                   "" => "<computed>"
        public_ip:                    "" => "<computed>"
        root_block_device.#:          "" => "<computed>"
        security_groups.#:            "" => "<computed>"
        source_dest_check:            "" => "true"
        subnet_id:                    "" => "<computed>"
        tags.%:                       "" => "1"
        tags.Name:                    "" => "HelloUbuntu"
        tenancy:                      "" => "<computed>"
        volume_tags.%:                "" => "<computed>"
        vpc_security_group_ids.#:     "" => "<computed>"
    aws_instance.web: Still creating... (10s elapsed)
    aws_instance.web: Still creating... (20s elapsed)
    aws_instance.web: Still creating... (30s elapsed)
    aws_instance.web: Creation complete (ID: i-0f58f8bd55b3a7e38)

    Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

    Outputs:

    image_id = ami-03998867

That's all we need to spin up an EC2 instance on AWS using latest Ubuntu image available.
