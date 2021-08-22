# DigitalOceanDNS
Update DigitalOcean DNS entry to match your public ip address.

## Requirements
* python3-digitalocean

## Usage
Define following environment variables:

```shell
# Your DO access token
export DIGITALOCEAN_ACCESS_TOKEN=""
# Domain name to update
export DIGITALOCEAN_DOMAIN_NAME=""
# ID of the records to ignore
export DIGITALOCEAN_IDS_EXCLUDE=""
```

Then you are ble to run it either directly:

```shell
python3 main.py
```

Or build a container and run it like this:
```shell
docker build . -t memoryleak/dodns:latest
docker run \
    --env DIGITALOCEAN_ACCESS_TOKEN="ABC" \
    --env DIGITALOCEAN_DOMAIN_NAME="example.com" \
    --env DIGITALOCEAN_IDS_EXCLUDE=1,2,3,4 \
    --rm memoryleak/dodns:latest 

```