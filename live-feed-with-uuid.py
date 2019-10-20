# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:20:40 2019

@author: yohann
"""

import uuid
import requests
import socket
import struct

def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask

URL = "https://endpoints.office.com/endpoints/worldwide?clientrequestid="+str(uuid.uuid4())
PARAMS = {'N/A':'N/A'}
r = requests.get(url = URL, params = PARAMS)
livefeed = r.json() 

ips = []
tmp_urls = []
for x in range(len(livefeed)):
    try:
        for y in livefeed[x]["ips"]:
            ips.append(y)
        for z in livefeed[x]["urls"]:
            tmp_urls.append(z)
    except KeyError:
        pass
        #print "Line "+str(x)+" has an issue"

ipv4_ips = []
ipv6_ips = []

for x in set(ips):
    if ":" not in x:
        ipv4_ips.append(x)
    else:
        ipv6_ips.append(x)
        
urls = set(tmp_urls)

# Write IPv4 IPs in Radware Alteon Format
"""
/c/slb/nwclss O365-IPs
	name "O365-IPs"
	type "address"
	ipver v4
/c/slb/nwclss O365-IPs/network 13.106.4.128_25
	net subnet 13.106.4.128 255.255.255.128 include
"""

file1 = open("ipv4.txt","w")
file1.write("/c/slb/nwclss O365-IPs\n")
file1.write("name \"O365-IPs\"\n")
file1.write("type \"address\"\n")
file1.write("ipver v4\n")
for x in ipv4_ips:
    ip,mask = cidr_to_netmask(x)
    file1.write("/c/slb/nwclss O365-IPs/network "+ip+"_"+mask+"\n")
    file1.write("net subnet "+ip+" "+mask+" include\n")
file1.close() 

# Write IPv4 IPs in Radware Alteon Format
"""
/c/slb/nwclss O365-IPv6s
	name "O365-IPv6s"
	type "address"
	ipver v6
/c/slb/nwclss O365-IPv6s/network 1
	net subnet 2a01:111:f100:3002:0:0:8987:320c 128 include
"""

file1 = open("ipv6.txt","w")
file1.write("/c/slb/nwclss O365-IPv6s\n")
file1.write("name \"O365-IPv6s\"\n")
file1.write("type \"address\"\n")
file1.write("ipver v6\n")
for x in ipv6_ips:
    [ip,mask] = x.split("/")
    file1.write("/c/slb/nwclss O365-IPv6s/network "+str(ipv6_ips.index(x)+1)+"\n")
    file1.write("net subnet "+ip+" "+mask+" include\n")
file1.close() 

# Write URLs in Radware Alteon Format
"""
/c/slb/layer7/slb/cntclss O365-SSL-URLs ssl
/c/slb/layer7/slb/cntclss O365-SSL-URLs ssl/hostname _.office.com
	hostname "*.office.com"
"""

file1 = open("urls.txt","w")
file1.write("/c/slb/layer7/slb/cntclss O365-SSL-URLs ssl\n")
for x in urls:
    file1.write("/c/slb/layer7/slb/cntclss O365-SSL-URLs ssl/hostname "+x.replace("*","_")+"\n")
    file1.write("hostname \""+x+"\"\n")
file1.close() 