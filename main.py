#!/usr/bin/env python3
import os

import digitalocean
from requests import get

DO_TOKEN = os.getenv('DIGITALOCEAN_ACCESS_TOKEN')
DO_DOMAIN = os.getenv('DIGITALOCEAN_DOMAIN_NAME')
DO_IDS_EXCLUDE = os.getenv('DIGITALOCEAN_IDS_EXCLUDE')


def get_public_ip():
    ip_ipfify = get('https://api.ipify.org').text
    ip_ifconfig = get('https://ifconfig.me/').text

    if ip_ipfify != ip_ifconfig:
        return False
    return ip_ipfify


def set_public_ip(ip: str, exclude_ids: ()):
    records = domain.get_records()

    for record in records:
        if record.id not in exclude_ids:
            print("Updating {} - {} to {} ...".format(record.id, record.name, ip))
            record.data = ip
            record.save()

domain = digitalocean.Domain(token=DO_TOKEN, name=DO_DOMAIN)
ids_exclude = list(map(int, DO_IDS_EXCLUDE.split(',')))


public_ip = get_public_ip()

if public_ip is False:
    print("Could not retrieve public IP address.")
    exit(-1)

set_public_ip(public_ip, ids_exclude)
