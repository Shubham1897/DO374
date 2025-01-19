#!/usr/bin/env python3

import json

def generate_inventory():
    # Define the dynamic inventory structure
    inventory = {
        "web": {
            "hosts": [
                "serverb.lab.example.com"  # Define the web host
            ]
        },
        "_meta": {
            "hostvars": {
                "serverb.lab.example.com": {
                    "ansible_host": "serverb.lab.example.com",  # Set hostname
                    "ansible_user": "root",        # SSH user
                    # You can add ansible_port, ansible_ssh_private_key_file, etc., if needed
                }
            }
        }
    }

    return inventory

if __name__ == "__main__":
    # Output inventory in JSON format
    print(json.dumps(generate_inventory(), indent=2))

