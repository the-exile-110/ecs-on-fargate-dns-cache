#!/bin/sh

echo "Starting dnsmasq..."

dnsmasq

echo "dnsmasq started."

echo "Starting app..."

flask run