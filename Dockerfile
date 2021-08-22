FROM fedora:34
ENV DIGITALOCEAN_ACCESS_TOKEN=''
ENV DIGITALOCEAN_DOMAIN_NAME=''
ENV DIGITALOCEAN_IDS_EXCLUDE=''

RUN dnf update -y && dnf upgrade -y && dnf install -y python3 python3-digitalocean
ADD main.py /bin/dodns
RUN chmod +x /bin/dodns
CMD dodns