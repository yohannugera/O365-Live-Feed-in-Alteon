# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:07:17 2019

@author: yohann
"""

import socket
import struct

def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask

livefeed = [
  {
    "id": 1,
    "serviceArea": "Exchange",
    "serviceAreaDisplayName": "Exchange Online",
    "urls": [
      "outlook.office.com",
      "outlook.office365.com"
    ],
    "ips": [
      "13.107.6.152/31",
      "13.107.18.10/31",
      "13.107.128.0/22",
      "23.103.160.0/20",
      "40.96.0.0/13",
      "40.104.0.0/15",
      "52.96.0.0/14",
      "131.253.33.215/32",
      "132.245.0.0/16",
      "150.171.32.0/22",
      "191.234.140.0/22",
      "204.79.197.215/32",
      "2603:1006::/40",
      "2603:1016::/40",
      "2603:1026::/40",
      "2603:1026:200::/39",
      "2603:1026:400::/39",
      "2603:1026:600::/44",
      "2603:1026:620::/44",
      "2603:1026:800::/44",
      "2603:1026:820::/45",
      "2603:1036::/39",
      "2603:1036:200::/40",
      "2603:1036:400::/40",
      "2603:1036:600::/40",
      "2603:1036:800::/38",
      "2603:1036:c00::/40",
      "2603:1046::/37",
      "2603:1046:900::/40",
      "2603:1056::/40",
      "2603:1056:400::/40",
      "2603:1056:600::/40",
      "2603:1096::/38",
      "2603:1096:400::/40",
      "2603:1096:600::/40",
      "2603:1096:a00::/39",
      "2603:1096:c00::/40",
      "2603:10a6:200::/40",
      "2603:10a6:400::/40",
      "2603:10a6:600::/40",
      "2603:10a6:800::/40",
      "2603:10d6:200::/40",
      "2620:1ec:4::152/128",
      "2620:1ec:4::153/128",
      "2620:1ec:c::10/128",
      "2620:1ec:c::11/128",
      "2620:1ec:d::10/128",
      "2620:1ec:d::11/128",
      "2620:1ec:8f0::/46",
      "2620:1ec:900::/46",
      "2620:1ec:a92::152/128",
      "2620:1ec:a92::153/128",
      "2a01:111:f400::/48"
    ],
    "tcpPorts": "80,443",
    "expressRoute": True,
    "category": "Optimize",
    "required": True
  },
  {
    "id": 2,
    "serviceArea": "Exchange",
    "serviceAreaDisplayName": "Exchange Online",
    "urls": [
      "smtp.office365.com"
    ],
    "ips": [
      "13.107.6.152/31",
      "13.107.18.10/31",
      "13.107.128.0/22",
      "23.103.160.0/20",
      "40.96.0.0/13",
      "40.104.0.0/15",
      "52.96.0.0/14",
      "131.253.33.215/32",
      "132.245.0.0/16",
      "150.171.32.0/22",
      "191.234.140.0/22",
      "204.79.197.215/32",
      "2603:1006::/40",
      "2603:1016::/40",
      "2603:1026::/40",
      "2603:1026:200::/39",
      "2603:1026:400::/39",
      "2603:1026:600::/44",
      "2603:1026:620::/44",
      "2603:1026:800::/44",
      "2603:1026:820::/45",
      "2603:1036::/39",
      "2603:1036:200::/40",
      "2603:1036:400::/40",
      "2603:1036:600::/40",
      "2603:1036:800::/38",
      "2603:1036:c00::/40",
      "2603:1046::/37",
      "2603:1046:900::/40",
      "2603:1056::/40",
      "2603:1056:400::/40",
      "2603:1056:600::/40",
      "2603:1096::/38",
      "2603:1096:400::/40",
      "2603:1096:600::/40",
      "2603:1096:a00::/39",
      "2603:1096:c00::/40",
      "2603:10a6:200::/40",
      "2603:10a6:400::/40",
      "2603:10a6:600::/40",
      "2603:10a6:800::/40",
      "2603:10d6:200::/40",
      "2620:1ec:4::152/128",
      "2620:1ec:4::153/128",
      "2620:1ec:c::10/128",
      "2620:1ec:c::11/128",
      "2620:1ec:d::10/128",
      "2620:1ec:d::11/128",
      "2620:1ec:8f0::/46",
      "2620:1ec:900::/46",
      "2620:1ec:a92::152/128",
      "2620:1ec:a92::153/128",
      "2a01:111:f400::/48"
    ],
    "tcpPorts": "587",
    "expressRoute": True,
    "category": "Allow",
    "required": True
  },
  {
    "id": 3,
    "serviceArea": "Exchange",
    "serviceAreaDisplayName": "Exchange Online",
    "urls": [
      "r1.res.office365.com",
      "r3.res.office365.com",
      "r4.res.office365.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 5,
    "serviceArea": "Exchange",
    "serviceAreaDisplayName": "Exchange Online",
    "urls": [
      "*.outlook.office.com",
      "outlook.office365.com"
    ],
    "ips": [
      "13.107.6.152/31",
      "13.107.18.10/31",
      "13.107.128.0/22",
      "23.103.160.0/20",
      "40.96.0.0/13",
      "40.104.0.0/15",
      "52.96.0.0/14",
      "131.253.33.215/32",
      "132.245.0.0/16",
      "150.171.32.0/22",
      "191.234.140.0/22",
      "204.79.197.215/32",
      "2603:1006::/40",
      "2603:1016::/40",
      "2603:1026::/40",
      "2603:1026:200::/39",
      "2603:1026:400::/39",
      "2603:1026:600::/44",
      "2603:1026:620::/44",
      "2603:1026:800::/44",
      "2603:1026:820::/45",
      "2603:1036::/39",
      "2603:1036:200::/40",
      "2603:1036:400::/40",
      "2603:1036:600::/40",
      "2603:1036:800::/38",
      "2603:1036:c00::/40",
      "2603:1046::/37",
      "2603:1046:900::/40",
      "2603:1056::/40",
      "2603:1056:400::/40",
      "2603:1056:600::/40",
      "2603:1096::/38",
      "2603:1096:400::/40",
      "2603:1096:600::/40",
      "2603:1096:a00::/39",
      "2603:1096:c00::/40",
      "2603:10a6:200::/40",
      "2603:10a6:400::/40",
      "2603:10a6:600::/40",
      "2603:10a6:800::/40",
      "2603:10d6:200::/40",
      "2620:1ec:4::152/128",
      "2620:1ec:4::153/128",
      "2620:1ec:c::10/128",
      "2620:1ec:c::11/128",
      "2620:1ec:d::10/128",
      "2620:1ec:d::11/128",
      "2620:1ec:8f0::/46",
      "2620:1ec:900::/46",
      "2620:1ec:a92::152/128",
      "2620:1ec:a92::153/128",
      "2a01:111:f400::/48"
    ],
    "tcpPorts": "143,993",
    "expressRoute": True,
    "category": "Allow",
    "required": False,
    "notes": "Exchange Online IMAP4 migration"
  },
  {
    "id": 6,
    "serviceArea": "Exchange",
    "serviceAreaDisplayName": "Exchange Online",
    "urls": [
      "*.outlook.office.com",
      "outlook.office365.com"
    ],
    "ips": [
      "13.107.6.152/31",
      "13.107.18.10/31",
      "13.107.128.0/22",
      "23.103.160.0/20",
      "40.96.0.0/13",
      "40.104.0.0/15",
      "52.96.0.0/14",
      "131.253.33.215/32",
      "132.245.0.0/16",
      "150.171.32.0/22",
      "191.234.140.0/22",
      "204.79.197.215/32",
      "2603:1006::/40",
      "2603:1016::/40",
      "2603:1026::/40",
      "2603:1026:200::/39",
      "2603:1026:400::/39",
      "2603:1026:600::/44",
      "2603:1026:620::/44",
      "2603:1026:800::/44",
      "2603:1026:820::/45",
      "2603:1036::/39",
      "2603:1036:200::/40",
      "2603:1036:400::/40",
      "2603:1036:600::/40",
      "2603:1036:800::/38",
      "2603:1036:c00::/40",
      "2603:1046::/37",
      "2603:1046:900::/40",
      "2603:1056::/40",
      "2603:1056:400::/40",
      "2603:1056:600::/40",
      "2603:1096::/38",
      "2603:1096:400::/40",
      "2603:1096:600::/40",
      "2603:1096:a00::/39",
      "2603:1096:c00::/40",
      "2603:10a6:200::/40",
      "2603:10a6:400::/40",
      "2603:10a6:600::/40",
      "2603:10a6:800::/40",
      "2603:10d6:200::/40",
      "2620:1ec:4::152/128",
      "2620:1ec:4::153/128",
      "2620:1ec:c::10/128",
      "2620:1ec:c::11/128",
      "2620:1ec:d::10/128",
      "2620:1ec:d::11/128",
      "2620:1ec:8f0::/46",
      "2620:1ec:900::/46",
      "2620:1ec:a92::152/128",
      "2620:1ec:a92::153/128",
      "2a01:111:f400::/48"
    ],
    "tcpPorts": "995",
    "expressRoute": True,
    "category": "Allow",
    "required": False,
    "notes": "Exchange Online POP3 migration"
  },
  {
    "id": 8,
    "serviceArea": "Exchange",
    "serviceAreaDisplayName": "Exchange Online",
    "urls": [
      "*.outlook.com",
      "*.outlook.office.com",
      "attachments.office.net"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 9,
    "serviceArea": "Exchange",
    "serviceAreaDisplayName": "Exchange Online",
    "urls": [
      "*.protection.outlook.com"
    ],
    "ips": [
      "40.92.0.0/15",
      "40.107.0.0/16",
      "52.100.0.0/14",
      "52.238.78.88/32",
      "104.47.0.0/17",
      "2a01:111:f403::/48"
    ],
    "tcpPorts": "443",
    "expressRoute": True,
    "category": "Allow",
    "required": True
  },
  {
    "id": 10,
    "serviceArea": "Exchange",
    "serviceAreaDisplayName": "Exchange Online",
    "urls": [
      "*.mail.protection.outlook.com"
    ],
    "ips": [
      "40.92.0.0/15",
      "40.107.0.0/16",
      "52.100.0.0/14",
      "104.47.0.0/17",
      "2a01:111:f400::/48",
      "2a01:111:f403::/48"
    ],
    "tcpPorts": "25",
    "expressRoute": True,
    "category": "Allow",
    "required": True
  },
  {
    "id": 11,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "ips": [
      "13.107.64.0/18",
      "52.112.0.0/14"
    ],
    "udpPorts": "3478,3479,3480,3481",
    "expressRoute": True,
    "category": "Optimize",
    "required": True
  },
  {
    "id": 12,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "*.lync.com",
      "*.teams.microsoft.com",
      "teams.microsoft.com"
    ],
    "ips": [
      "13.70.151.216/32",
      "13.71.127.197/32",
      "13.72.245.115/32",
      "13.73.1.120/32",
      "13.75.126.169/32",
      "13.89.240.113/32",
      "13.107.3.0/24",
      "13.107.64.0/18",
      "51.140.155.234/32",
      "51.140.203.190/32",
      "51.141.51.76/32",
      "52.112.0.0/14",
      "52.163.126.215/32",
      "52.170.21.67/32",
      "52.172.185.18/32",
      "52.178.94.2/32",
      "52.178.161.139/32",
      "52.228.25.96/32",
      "52.238.119.141/32",
      "52.242.23.189/32",
      "52.244.160.207/32",
      "104.215.11.144/32",
      "104.215.62.195/32",
      "138.91.237.237/32",
      "2603:1027::/48",
      "2603:1037::/48",
      "2603:1047::/48",
      "2603:1057::/48",
      "2620:1ec:6::/48",
      "2620:1ec:40::/42"
    ],
    "tcpPorts": "80,443",
    "expressRoute": True,
    "category": "Allow",
    "required": True
  },
  {
    "id": 13,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "*.broadcast.skype.com",
      "broadcast.skype.com"
    ],
    "ips": [
      "13.70.151.216/32",
      "13.71.127.197/32",
      "13.72.245.115/32",
      "13.73.1.120/32",
      "13.75.126.169/32",
      "13.89.240.113/32",
      "13.107.3.0/24",
      "13.107.64.0/18",
      "51.140.155.234/32",
      "51.140.203.190/32",
      "51.141.51.76/32",
      "52.112.0.0/14",
      "52.163.126.215/32",
      "52.170.21.67/32",
      "52.172.185.18/32",
      "52.178.94.2/32",
      "52.178.161.139/32",
      "52.228.25.96/32",
      "52.238.119.141/32",
      "52.242.23.189/32",
      "52.244.160.207/32",
      "104.215.11.144/32",
      "104.215.62.195/32",
      "138.91.237.237/32",
      "2603:1027::/48",
      "2603:1037::/48",
      "2603:1047::/48",
      "2603:1057::/48",
      "2620:1ec:6::/48",
      "2620:1ec:40::/42"
    ],
    "tcpPorts": "443",
    "expressRoute": True,
    "category": "Allow",
    "required": True
  },
  {
    "id": 14,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "quicktips.skypeforbusiness.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 15,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "*.sfbassets.com",
      "*.urlp.sfbassets.com",
      "skypemaprdsitus.trafficmanager.net"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 16,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "*.keydelivery.mediaservices.windows.net",
      "*.msecnd.net",
      "*.streaming.mediaservices.windows.net",
      "ajax.aspnetcdn.com",
      "mlccdn.blob.core.windows.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 17,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "aka.ms",
      "amp.azure.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 18,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "*.users.storage.live.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Federation with Skype and public IM connectivity: Contact picture retrieval"
  },
  {
    "id": 19,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "*.adl.windows.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Applies only to those who deploy the Conference Room Systems"
  },
  {
    "id": 22,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "*.skypeforbusiness.com"
    ],
    "ips": [
      "13.70.151.216/32",
      "13.71.127.197/32",
      "13.72.245.115/32",
      "13.73.1.120/32",
      "13.75.126.169/32",
      "13.89.240.113/32",
      "13.107.3.0/24",
      "13.107.64.0/18",
      "51.140.155.234/32",
      "51.140.203.190/32",
      "51.141.51.76/32",
      "52.112.0.0/14",
      "52.163.126.215/32",
      "52.170.21.67/32",
      "52.172.185.18/32",
      "52.178.94.2/32",
      "52.178.161.139/32",
      "52.228.25.96/32",
      "52.238.119.141/32",
      "52.242.23.189/32",
      "52.244.160.207/32",
      "104.215.11.144/32",
      "104.215.62.195/32",
      "138.91.237.237/32",
      "2603:1027::/48",
      "2603:1037::/48",
      "2603:1047::/48",
      "2603:1057::/48",
      "2620:1ec:6::/48",
      "2620:1ec:40::/42"
    ],
    "tcpPorts": "443",
    "expressRoute": True,
    "category": "Allow",
    "required": False,
    "notes": "Teams: Messaging interop with Skype for Business"
  },
  {
    "id": 26,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "*.msedge.net",
      "compass-ssl.microsoft.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 27,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "*.mstea.ms",
      "*.secure.skypeassets.com",
      "mlccdnprod.azureedge.net",
      "videoplayercdn.osi.office.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 29,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "*.tenor.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Yammer third-party integration"
  },
  {
    "id": 31,
    "serviceArea": "SharePoint",
    "serviceAreaDisplayName": "SharePoint Online and OneDrive for Business",
    "urls": [
      "*.sharepoint.com"
    ],
    "ips": [
      "13.107.136.0/22",
      "40.108.128.0/17",
      "52.104.0.0/14",
      "104.146.128.0/17",
      "150.171.40.0/22",
      "2620:1ec:8f8::/46",
      "2620:1ec:908::/46",
      "2a01:111:f402::/48"
    ],
    "tcpPorts": "80,443",
    "expressRoute": True,
    "category": "Optimize",
    "required": True
  },
  {
    "id": 32,
    "serviceArea": "SharePoint",
    "serviceAreaDisplayName": "SharePoint Online and OneDrive for Business",
    "urls": [
      "*.log.optimizely.com",
      "click.email.microsoftonline.com",
      "ssw.live.com",
      "storage.live.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "OneDrive for Business: supportability, telemetry, APIs, and embedded email links"
  },
  {
    "id": 33,
    "serviceArea": "SharePoint",
    "serviceAreaDisplayName": "SharePoint Online and OneDrive for Business",
    "urls": [
      "*.search.production.apac.trafficmanager.net",
      "*.search.production.emea.trafficmanager.net",
      "*.search.production.us.trafficmanager.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "SharePoint Hybrid Search - Endpoint to SearchContentService where the hybrid crawler feeds documents"
  },
  {
    "id": 35,
    "serviceArea": "SharePoint",
    "serviceAreaDisplayName": "SharePoint Online and OneDrive for Business",
    "urls": [
      "admin.onedrive.com",
      "officeclient.microsoft.com",
      "skydrive.wns.windows.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 36,
    "serviceArea": "SharePoint",
    "serviceAreaDisplayName": "SharePoint Online and OneDrive for Business",
    "urls": [
      "g.live.com",
      "oneclient.sfx.ms"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 37,
    "serviceArea": "SharePoint",
    "serviceAreaDisplayName": "SharePoint Online and OneDrive for Business",
    "urls": [
      "*.sharepointonline.com",
      "cdn.sharepointonline.com",
      "privatecdn.sharepointonline.com",
      "publiccdn.sharepointonline.com",
      "spoprod-a.akamaihd.net",
      "static.sharepointonline.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 38,
    "serviceArea": "SharePoint",
    "serviceAreaDisplayName": "SharePoint Online and OneDrive for Business",
    "urls": [
      "prod.msocdn.com",
      "watson.telemetry.microsoft.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "SharePoint Online: auxiliary URLs"
  },
  {
    "id": 39,
    "serviceArea": "SharePoint",
    "serviceAreaDisplayName": "SharePoint Online and OneDrive for Business",
    "urls": [
      "*.svc.ms",
      "*-files.sharepoint.com",
      "*-myfiles.sharepoint.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 40,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "ajax.aspnetcdn.com",
      "r3.res.outlook.com",
      "spoprod-a.akamaihd.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Office 365 Video CDNs"
  },
  {
    "id": 41,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.api.microsoftstream.com",
      "*.notification.api.microsoftstream.com",
      "amp.azure.net",
      "api.microsoftstream.com",
      "az416426.vo.msecnd.net",
      "s0.assets-yammer.com",
      "vortex.data.microsoft.com",
      "web.microsoftstream.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Microsoft Stream"
  },
  {
    "id": 42,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "amsglob0cdnstream11.azureedge.net",
      "amsglob0cdnstream12.azureedge.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Microsoft Stream CDN"
  },
  {
    "id": 43,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "nps.onyx.azure.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Microsoft Stream 3rd party integration (including CDNs)"
  },
  {
    "id": 44,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.azureedge.net",
      "*.media.azure.net",
      "*.streaming.mediaservices.windows.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Microsoft Stream - unauthenticated"
  },
  {
    "id": 45,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.keydelivery.mediaservices.windows.net",
      "*.streaming.mediaservices.windows.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Office 365 Video"
  },
  {
    "id": 46,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*broadcast.officeapps.live.com",
      "*excel.officeapps.live.com",
      "*onenote.officeapps.live.com",
      "*powerpoint.officeapps.live.com",
      "*rtc.officeapps.live.com",
      "*shared.officeapps.live.com",
      "*view.officeapps.live.com",
      "*visio.officeapps.live.com",
      "*word-edit.officeapps.live.com",
      "*word-view.officeapps.live.com",
      "office.live.com"
    ],
    "ips": [
      "13.107.6.171/32",
      "13.107.140.6/32",
      "52.108.0.0/14",
      "52.238.106.116/32",
      "52.247.150.191/32",
      "2603:1010:2::cb/128",
      "2603:1010:200::c7/128",
      "2603:1020:200::682f:a0fd/128",
      "2603:1020:201:9::c6/128",
      "2603:1020:600::a1/128",
      "2603:1020:700::a2/128",
      "2603:1020:800:2::6/128",
      "2603:1020:900::8/128",
      "2603:1030:7::749/128",
      "2603:1030:800:5::bfee:ad3c/128",
      "2603:1030:f00::17/128",
      "2603:1030:1000::21a/128",
      "2603:1040:200::4f3/128",
      "2603:1040:401::762/128",
      "2603:1040:601::60f/128",
      "2603:1040:a01::1e/128",
      "2603:1040:c01::28/128",
      "2603:1040:e00:1::2f/128",
      "2603:1040:f00::1f/128",
      "2603:1050:1::cd/128",
      "2620:1ec:8fc::6/128",
      "2620:1ec:a92::171/128",
      "2a01:111:f100:2000::a83e:3019/128",
      "2a01:111:f100:2002::8975:2d79/128",
      "2a01:111:f100:2002::8975:2da8/128",
      "2a01:111:f100:7000::6fdd:6cd5/128",
      "2a01:111:f100:a004::bfeb:88cf/128"
    ],
    "tcpPorts": "443",
    "expressRoute": True,
    "category": "Allow",
    "required": True
  },
  {
    "id": 47,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.cdn.office.net",
      "contentstorage.osi.office.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 49,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.onenote.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 50,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.microsoft.com",
      "*.msecnd.net",
      "*.office.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "OneNote notebooks (wildcards)"
  },
  {
    "id": 51,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*cdn.onenote.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 52,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "ad.atdmt.com",
      "s.ytimg.com",
      "www.youtube.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "OneNote 3rd party supporting services and CDNs"
  },
  {
    "id": 53,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "ajax.aspnetcdn.com",
      "apis.live.net",
      "cdn.optimizely.com",
      "officeapps.live.com",
      "www.onedrive.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 54,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "ccs.login.microsoftonline.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 56,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.msappproxy.net",
      "*.msftidentity.com",
      "*.msidentity.com",
      "account.activedirectory.windowsazure.com",
      "accounts.accesscontrol.windows.net",
      "adminwebservice.microsoftonline.com",
      "api.passwordreset.microsoftonline.com",
      "autologon.microsoftazuread-sso.com",
      "becws.microsoftonline.com",
      "clientconfig.microsoftonline-p.net",
      "companymanager.microsoftonline.com",
      "device.login.microsoftonline.com",
      "graph.microsoft.com",
      "graph.windows.net",
      "login.microsoft.com",
      "login.microsoftonline.com",
      "login.microsoftonline-p.com",
      "login.windows.net",
      "logincert.microsoftonline.com",
      "loginex.microsoftonline.com",
      "login-us.microsoftonline.com",
      "nexus.microsoftonline-p.com",
      "passwordreset.microsoftonline.com",
      "provisioningapi.microsoftonline.com"
    ],
    "ips": [
      "13.106.4.128/25",
      "13.106.56.0/25",
      "20.190.128.0/18",
      "40.126.0.0/18",
      "65.54.170.128/25",
      "104.44.218.128/25",
      "104.44.254.128/25",
      "104.44.255.0/25",
      "134.170.67.0/25",
      "134.170.172.128/25",
      "157.55.45.128/25",
      "157.55.130.0/25",
      "157.55.145.0/25",
      "157.55.155.0/25",
      "157.55.227.192/26",
      "191.232.2.128/25",
      "2001:df0:d9:200::/64",
      "2603:1006:2000::/48",
      "2603:1007:200::/48",
      "2603:1016:1400::/48",
      "2603:1017::/48",
      "2603:1020:201:2::/64",
      "2603:1020:201:3::/64",
      "2603:1026:3000::/48",
      "2603:1027:1::/48",
      "2603:1036:3000::/48",
      "2603:1037:1::/48",
      "2603:1046:2000::/48",
      "2603:1047:1::/48",
      "2603:1047:100::/64",
      "2603:1056:2000::/48",
      "2603:1057:2::/48",
      "2a01:111:2005:6::/64",
      "2a01:111:200a:a::/64",
      "2a01:111:2035:8::/64",
      "2a01:111:f406:1::/64",
      "2a01:111:f406:2::/64",
      "2a01:111:f406:c00::/64",
      "2a01:111:f406:1004::/64",
      "2a01:111:f406:1805::/64",
      "2a01:111:f406:3404::/64",
      "2a01:111:f406:8000::/64",
      "2a01:111:f406:8801::/64",
      "2a01:111:f406:a003::/64"
    ],
    "tcpPorts": "80,443",
    "expressRoute": True,
    "category": "Allow",
    "required": True
  },
  {
    "id": 59,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.microsoftonline.com",
      "*.microsoftonline-p.com",
      "*.msauth.net",
      "*.msauthimages.net",
      "*.msecnd.net",
      "*.msftauth.net",
      "*.msftauthimages.net",
      "*.phonefactor.net",
      "enterpriseregistration.windows.net",
      "management.azure.com",
      "policykeyservice.dc.ad.msft.net",
      "secure.aadcdn.microsoftonline-p.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 64,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.manage.office.com",
      "*.protection.office.com",
      "manage.office.com",
      "protection.office.com"
    ],
    "ips": [
      "13.80.125.22/32",
      "13.91.91.243/32",
      "13.107.6.156/31",
      "13.107.7.190/31",
      "13.107.9.156/31",
      "40.81.156.154/32",
      "40.90.218.198/32",
      "52.108.0.0/14",
      "52.174.56.180/32",
      "52.183.75.62/32",
      "52.184.165.82/32",
      "104.42.230.91/32",
      "157.55.145.0/25",
      "157.55.155.0/25",
      "157.55.227.192/26",
      "2603:1006:1400::/40",
      "2603:1016:2400::/40",
      "2603:1026:2400::/40",
      "2603:1036:2400::/40",
      "2603:1046:1400::/40",
      "2603:1056:1400::/40",
      "2a01:111:200a:a::/64",
      "2a01:111:2035:8::/64",
      "2a01:111:f406:1::/64",
      "2a01:111:f406:c00::/64",
      "2a01:111:f406:1004::/64",
      "2a01:111:f406:1805::/64",
      "2a01:111:f406:3404::/64",
      "2a01:111:f406:8000::/64",
      "2a01:111:f406:8801::/64",
      "2a01:111:f406:a003::/64"
    ],
    "tcpPorts": "443",
    "expressRoute": True,
    "category": "Allow",
    "required": True
  },
  {
    "id": 65,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.portal.cloudappsecurity.com",
      "account.office.net",
      "admin.microsoft.com",
      "home.office.com",
      "portal.office.com",
      "www.office.com"
    ],
    "ips": [
      "13.80.125.22/32",
      "13.91.91.243/32",
      "13.107.6.156/31",
      "13.107.7.190/31",
      "13.107.9.156/31",
      "40.81.156.154/32",
      "40.90.218.198/32",
      "52.108.0.0/14",
      "52.174.56.180/32",
      "52.183.75.62/32",
      "52.184.165.82/32",
      "104.42.230.91/32",
      "157.55.145.0/25",
      "157.55.155.0/25",
      "157.55.227.192/26",
      "2603:1006:1400::/40",
      "2603:1016:2400::/40",
      "2603:1026:2400::/40",
      "2603:1036:2400::/40",
      "2603:1046:1400::/40",
      "2603:1056:1400::/40",
      "2a01:111:200a:a::/64",
      "2a01:111:2035:8::/64",
      "2a01:111:f406:1::/64",
      "2a01:111:f406:c00::/64",
      "2a01:111:f406:1004::/64",
      "2a01:111:f406:1805::/64",
      "2a01:111:f406:3404::/64",
      "2a01:111:f406:8000::/64",
      "2a01:111:f406:8801::/64",
      "2a01:111:f406:a003::/64"
    ],
    "tcpPorts": "80,443",
    "expressRoute": True,
    "category": "Allow",
    "required": True
  },
  {
    "id": 66,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "apc.delve.office.com",
      "aus.delve.office.com",
      "can.delve.office.com",
      "delve.office.com",
      "delve-gcc.office.com",
      "eur.delve.office.com",
      "gbr.delve.office.com",
      "ind.delve.office.com",
      "jpn.delve.office.com",
      "kor.delve.office.com",
      "lam.delve.office.com",
      "nam.delve.office.com",
      "suite.office.net",
      "webshell.suite.office.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 67,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.blob.core.windows.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Security and Compliance Center eDiscovery export"
  },
  {
    "id": 68,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.helpshift.com",
      "*.localytics.com",
      "analytics.localytics.com",
      "api.localytics.com",
      "connect.facebook.net",
      "firstpartyapps.oaspapps.com",
      "outlook.uservoice.com",
      "prod.firstpartyapps.oaspapps.com.akadns.net",
      "rink.hockeyapp.net",
      "sdk.hockeyapp.net",
      "telemetryservice.firstpartyapps.oaspapps.com",
      "web.localytics.com",
      "webanalytics.localytics.com",
      "wus-firstpartyapps.oaspapps.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Portal and shared: 3rd party office integration. (including CDNs)"
  },
  {
    "id": 69,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.aria.microsoft.com",
      "*.events.data.microsoft.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 70,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.o365weve.com",
      "amp.azure.net",
      "appsforoffice.microsoft.com",
      "assets.onestore.ms",
      "auth.gfx.ms",
      "az826701.vo.msecnd.net",
      "c1.microsoft.com",
      "client.hip.live.com",
      "contentstorage.osi.office.net",
      "dgps.support.microsoft.com",
      "docs.microsoft.com",
      "msdn.microsoft.com",
      "platform.linkedin.com",
      "prod.msocdn.com",
      "products.office.com",
      "r1.res.office365.com",
      "r4.res.office365.com",
      "res.delve.office.com",
      "shellprod.msocdn.com",
      "support.content.office.net",
      "support.microsoft.com",
      "support.office.com",
      "technet.microsoft.com",
      "templates.office.com",
      "videocontent.osi.office.net",
      "videoplayercdn.osi.office.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 71,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.office365.com"
    ],
    "ips": [
      "2603:1020:0:7::19c/128",
      "2603:1020:0:7::4e1/128",
      "2603:1020:200::682f:a1d8/128",
      "2603:1020:201::3c4/128",
      "2603:1020:201::5f2/128",
      "2603:1020:201:a::2b1/128",
      "2603:1020:300::33/128",
      "2603:1020:400::26/128",
      "2603:1020:600::1d3/128",
      "2603:1020:600::1f0/128",
      "2603:1020:600::21f/128",
      "2603:1020:700::1cb/128",
      "2603:1020:700::215/128",
      "2603:1030:603::6a/128",
      "2603:1030:603::72/128",
      "2603:1030:603::3c9/128",
      "2603:1030:a02::118/128",
      "2603:1030:a02::367/128",
      "2603:1040:200::111/128",
      "2603:1040:200::325/128",
      "2603:1040:400::5d/128",
      "2603:1040:400::5e/128",
      "2603:1040:400::7b/128",
      "2603:1040:400::2f4/128",
      "2603:1040:401::c/128",
      "2603:1040:401::57/128",
      "2603:1040:401::597/128",
      "2603:1040:601::2f/128",
      "2603:1040:601::4e/128",
      "2603:1040:601::1e7/128",
      "2603:1040:601::26f/128",
      "2603:1040:601::36c/128",
      "2801:80:1d0:1c00::/64",
      "2a01:111:2003::/48",
      "2a01:111:202c::/48",
      "2a01:111:202d::/48",
      "2a01:111:202e::/48",
      "2a01:111:202e::156/128",
      "2a01:111:202e::190/128",
      "2a01:111:202e::191/128",
      "2a01:111:f100:1002::4134:c0cb/128",
      "2a01:111:f100:1002::4134:c440/128",
      "2a01:111:f100:1002::4134:d93c/128",
      "2a01:111:f100:1002::4134:d9ee/128",
      "2a01:111:f100:1003::4134:3644/128",
      "2a01:111:f100:1003::4134:36d5/128",
      "2a01:111:f100:1004::4134:f0c8/128",
      "2a01:111:f100:2000::a83e:3349/128",
      "2a01:111:f100:2002::8975:2c33/128",
      "2a01:111:f100:2002::8975:2cbc/128",
      "2a01:111:f100:2002::8975:2d11/128",
      "2a01:111:f100:2002::8975:2d43/128",
      "2a01:111:f100:2002::8975:2d92/128",
      "2a01:111:f100:2002::8975:2d98/128",
      "2a01:111:f100:3000::a83e:1a8c/128",
      "2a01:111:f100:3002::8987:320c/128",
      "2a01:111:f100:3002::8987:342a/128",
      "2a01:111:f100:3002::8987:3552/128",
      "2a01:111:f100:3002::8987:358e/128",
      "2a01:111:f100:4001::4625:609b/128",
      "2a01:111:f100:4001::4625:61ea/128",
      "2a01:111:f100:4001::4625:a065/128",
      "2a01:111:f100:4001::4625:a1e3/128",
      "2a01:111:f100:4001::4625:a248/128",
      "2a01:111:f100:4001::4625:a4b4/128",
      "2a01:111:f100:4002::9d37:c021/128",
      "2a01:111:f100:4002::9d37:c08f/128",
      "2a01:111:f100:4002::9d37:c11a/128",
      "2a01:111:f100:6000::4134:a2af/128",
      "2a01:111:f100:6000::4134:a591/128",
      "2a01:111:f100:6000::4134:b0ba/128",
      "2a01:111:f100:6000::4134:b84b/128",
      "2a01:111:f100:7000::6fdd:50bb/128",
      "2a01:111:f100:7000::6fdd:568a/128",
      "2a01:111:f100:7000::6fdd:6095/128",
      "2a01:111:f100:7000::6fdd:682b/128",
      "2a01:111:f100:7000::6fdd:699d/128",
      "2a01:111:f100:7000::6fdd:6b20/128",
      "2a01:111:f100:7000::6fdd:6b76/128",
      "2a01:111:f100:7000::6fdd:6cac/128",
      "2a01:111:f100:7000::6fdd:6fc4/128",
      "2a01:111:f100:8000::4134:902e/128",
      "2a01:111:f100:8000::4134:941b/128",
      "2a01:111:f100:8001::d5c7:8077/128",
      "2a01:111:f100:9001::1761:91cb/128",
      "2a01:111:f100:9001::1761:9642/128",
      "2a01:111:f100:a000::5ef5:581c/128",
      "2a01:111:f100:a000::5ef5:6c55/128",
      "2a01:111:f100:a001::a83f:5c85/128",
      "2a01:111:f100:a004::bfeb:8aa2/128",
      "2a01:111:f100:a004::bfeb:8c89/128",
      "2a01:111:f100:a004::bfeb:8cb8/128",
      "2a01:111:f100:a004::bfeb:8deb/128",
      "2a01:111:f102:8001::1761:4237/128",
      "2a01:111:f102:8001::1761:4daf/128",
      "2a01:111:f102:8001::1761:4f8a/128",
      "2a01:111:f406:1000::/64",
      "2a01:111:f406:1801::/64"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 72,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.cloudapp.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Azure Rights Management (RMS) with Office 2010 clients"
  },
  {
    "id": 73,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.aadrm.com",
      "*.azurerms.com",
      "*.informationprotection.azure.com",
      "ecn.dev.virtualearth.net",
      "informationprotection.hosting.portal.azure.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 74,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "testconnectivity.microsoft.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Remote Connectivity Analyzer - Initiate connectivity tests."
  },
  {
    "id": 75,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.hockeyapp.net",
      "*.sharepointonline.com",
      "*.staffhub.office.com",
      "api.office.com",
      "dc.applicationinsights.microsoft.com",
      "dc.services.visualstudio.com",
      "ea-000.forms.osi.office.net",
      "eus2-000.forms.osi.office.net",
      "forms.microsoft.com",
      "forms.office.com",
      "mem.gfx.ms",
      "neu-000.forms.osi.office.net",
      "office365servicehealthcommunications.cloudapp.net",
      "securescore.office.com",
      "signup.microsoft.com",
      "staffhub.ms",
      "staffhub.office.com",
      "staffhub.uservoice.com",
      "staffhubweb.azureedge.net",
      "watson.telemetry.microsoft.com",
      "weu-000.forms.osi.office.net",
      "wus-000.forms.osi.office.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Graph.windows.net, Office 365 Management Pack for Operations Manager, SecureScore, Azure AD Device Registration, Forms, StaffHub, Application Insights, captcha services"
  },
  {
    "id": 76,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "vortex.data.microsoft.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Microsoft Azure RemoteApp"
  },
  {
    "id": 77,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "nexus.officeapps.live.com",
      "nexusrules.officeapps.live.com",
      "portal.microsoftonline.com"
    ],
    "ips": [
      "13.107.6.171/32",
      "13.107.140.6/32",
      "52.108.0.0/14",
      "52.238.106.116/32",
      "52.247.150.191/32",
      "2603:1010:2::cb/128",
      "2603:1010:200::c7/128",
      "2603:1020:200::682f:a0fd/128",
      "2603:1020:201:9::c6/128",
      "2603:1020:600::a1/128",
      "2603:1020:700::a2/128",
      "2603:1020:800:2::6/128",
      "2603:1020:900::8/128",
      "2603:1030:7::749/128",
      "2603:1030:800:5::bfee:ad3c/128",
      "2603:1030:f00::17/128",
      "2603:1030:1000::21a/128",
      "2603:1040:200::4f3/128",
      "2603:1040:401::762/128",
      "2603:1040:601::60f/128",
      "2603:1040:a01::1e/128",
      "2603:1040:c01::28/128",
      "2603:1040:e00:1::2f/128",
      "2603:1040:f00::1f/128",
      "2603:1050:1::cd/128",
      "2620:1ec:8fc::6/128",
      "2620:1ec:a92::171/128",
      "2a01:111:f100:2000::a83e:3019/128",
      "2a01:111:f100:2002::8975:2d79/128",
      "2a01:111:f100:2002::8975:2da8/128",
      "2a01:111:f100:7000::6fdd:6cd5/128",
      "2a01:111:f100:a004::bfeb:88cf/128"
    ],
    "tcpPorts": "443",
    "expressRoute": True,
    "category": "Allow",
    "required": True
  },
  {
    "id": 78,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.microsoft.com",
      "*.msocdn.com",
      "*.office.com",
      "*.office.net",
      "*.onmicrosoft.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Some Office 365 features require endpoints within these domains (including CDNs). Many specific FQDNs within these wildcards have been published recently as we work to either remove or better explain our guidance relating to these wildcards."
  },
  {
    "id": 79,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "o15.officeredir.microsoft.com",
      "ocsredir.officeapps.live.com",
      "officepreviewredir.microsoft.com",
      "officeredir.microsoft.com",
      "r.office.microsoft.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 80,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "ocws.officeapps.live.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 81,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "odc.officeapps.live.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 82,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "roaming.officeapps.live.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 83,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "activation.sls.microsoft.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 84,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "crl.microsoft.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 85,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "ols.officeapps.live.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 86,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "office15client.microsoft.com",
      "officeclient.microsoft.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 87,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "ocsa.officeapps.live.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 88,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "insertmedia.bing.office.net"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 89,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "go.microsoft.com",
      "support.office.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 90,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "mrodevicemgr.officeapps.live.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 91,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "ajax.aspnetcdn.com",
      "cdn.odc.officeapps.live.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 92,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "officecdn.microsoft.com",
      "officecdn.microsoft.com.edgesuite.net"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 93,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "ajax.microsoft.com",
      "c.bing.net",
      "excelbingmap.firstpartyapps.oaspapps.com",
      "excelcs.officeapps.live.com",
      "ocos-office365-s2s.msedge.net",
      "omextemplates.content.office.net",
      "peoplegraph.firstpartyapps.oaspapps.com",
      "pptcs.officeapps.live.com",
      "store.office.com",
      "templateservice.office.com",
      "tse1.mm.bing.net",
      "uci.officeapps.live.com",
      "watson.microsoft.com",
      "wikipedia.firstpartyapps.oaspapps.com",
      "wordcs.officeapps.live.com",
      "www.bing.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "ProPlus: auxiliary URLs"
  },
  {
    "id": 95,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.acompli.net",
      "*.outlookmobile.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS"
  },
  {
    "id": 96,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.manage.microsoft.com",
      "api.office.com",
      "go.microsoft.com",
      "login.windows-ppe.net",
      "secure.aadcdn.microsoftonline-p.com",
      "vortex.data.microsoft.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Authentication"
  },
  {
    "id": 97,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "account.live.com",
      "apis.live.net",
      "auth.gfx.ms",
      "login.live.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Consumer Outlook.com and OneDrive integration"
  },
  {
    "id": 98,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "accounts.google.com",
      "mail.google.com",
      "www.googleapis.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Google integration"
  },
  {
    "id": 99,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "api.login.yahoo.com",
      "social.yahooapis.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Yahoo integration"
  },
  {
    "id": 100,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "api.dropboxapi.com",
      "www.dropbox.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: DropBox integration"
  },
  {
    "id": 101,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "app.box.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Box integration"
  },
  {
    "id": 102,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "graph.facebook.com",
      "m.facebook.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Facebook integration"
  },
  {
    "id": 103,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "www.evernote.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Evernote integration"
  },
  {
    "id": 104,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "a.wunderlist.com",
      "www.wunderlist.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: WunderList integration"
  },
  {
    "id": 105,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "bit.ly",
      "www.acompli.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Outlook Privacy"
  },
  {
    "id": 106,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "by.uservoice.com",
      "outlook.uservoice.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: User voice integration"
  },
  {
    "id": 107,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "api.diagnostics.office.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Log upload integration"
  },
  {
    "id": 109,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "data.flurry.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Flurry log integration"
  },
  {
    "id": 110,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "app.adjust.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Adjust integration"
  },
  {
    "id": 111,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "rink.hockeyapp.net",
      "sdk.hockeyapp.net"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Hockey log integration"
  },
  {
    "id": 112,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "acompli.helpshift.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Helpshift integration"
  },
  {
    "id": 113,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "play.google.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Play Store integration (Android only)"
  },
  {
    "id": 114,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.appex.bing.com",
      "*.appex-rf.msn.com",
      "*.itunes.apple.com",
      "c.bing.com",
      "c.live.com",
      "cl2.apple.com",
      "client.hip.live.com",
      "d.docs.live.net",
      "directory.services.live.com",
      "docs.live.net",
      "en-us.appex-rf.msn.com",
      "foodanddrink.services.appex.bing.com",
      "ms.tific.com",
      "odcsm.officeapps.live.com",
      "office.microsoft.com",
      "officeimg.vo.msecnd.net",
      "partnerservices.getmicrosoftkey.com",
      "roaming.officeapps.live.com",
      "sas.office.microsoft.com",
      "signup.live.com",
      "view.atdmt.com",
      "watson.telemetry.microsoft.com",
      "weather.tile.appex.bing.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Office Mobile URLs"
  },
  {
    "id": 115,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "api.meetup.com",
      "secure.meetup.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Outlook for Android and iOS: Meetup integration"
  },
  {
    "id": 116,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "account.live.com",
      "auth.gfx.ms",
      "c.bing.com",
      "c.live.com",
      "cl2.apple.com",
      "client.hip.live.com",
      "directory.services.live.com",
      "docs.live.net",
      "en-us.appex-rf.msn.com",
      "foodanddrink.services.appex.bing.com",
      "go.microsoft.com",
      "login.live.com",
      "ms.tific.com",
      "office.microsoft.com",
      "officeimg.vo.msecnd.net",
      "p100-sandbox.itunes.apple.com",
      "partnerservices.getmicrosoftkey.com",
      "roaming.officeapps.live.com",
      "sas.office.microsoft.com",
      "signup.live.com",
      "view.atdmt.com",
      "watson.telemetry.microsoft.com",
      "weather.tile.appex.bing.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Office for iPad URLs"
  },
  {
    "id": 117,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.yammer.com",
      "*.yammerusercontent.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Yammer"
  },
  {
    "id": 118,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.assets-yammer.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Yammer CDN"
  },
  {
    "id": 119,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "tasks.office.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Planner"
  },
  {
    "id": 120,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "ajax.aspnetcdn.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Planner CDNs"
  },
  {
    "id": 121,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "www.outlook.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Planner: auxiliary URLs"
  },
  {
    "id": 122,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "eus-www.sway-cdn.com",
      "eus-www.sway-extensions.com",
      "wus-www.sway-cdn.com",
      "wus-www.sway-extensions.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Sway CDNs"
  },
  {
    "id": 123,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "www.google-analytics.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Sway website analytics"
  },
  {
    "id": 124,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "sway.com",
      "sway.office.com",
      "www.sway.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Sway"
  },
  {
    "id": 125,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.entrust.net",
      "*.geotrust.com",
      "*.omniroot.com",
      "*.public-trust.com",
      "*.symcb.com",
      "*.symcd.com",
      "*.verisign.com",
      "*.verisign.net",
      "aia.entrust.net",
      "apps.identrust.com",
      "cacert.a.omniroot.com",
      "cacert.omniroot.com",
      "cacerts.digicert.com",
      "cdp1.public-trust.com",
      "cert.int-x3.letsencrypt.org",
      "crl.entrust.net",
      "crl.globalsign.com",
      "crl.globalsign.net",
      "crl.identrust.com",
      "crl.microsoft.com",
      "crl3.digicert.com",
      "crl4.digicert.com",
      "evintl-aia.verisign.com",
      "evintl-crl.verisign.com",
      "evintl-ocsp.verisign.com",
      "evsecure-aia.verisign.com",
      "evsecure-crl.verisign.com",
      "evsecure-ocsp.verisign.com",
      "isrg.trustid.ocsp.identrust.com",
      "mscrl.microsoft.com",
      "ocsp.digicert.com",
      "ocsp.entrust.net",
      "ocsp.globalsign.com",
      "ocsp.int-x3.letsencrypt.org",
      "ocsp.msocsp.com",
      "ocsp.omniroot.com",
      "ocsp2.globalsign.com",
      "ocspx.digicert.com",
      "s1.symcb.com",
      "s2.symcb.com",
      "sa.symcb.com",
      "sd.symcb.com",
      "secure.globalsign.com",
      "sr.symcb.com",
      "sr.symcd.com",
      "su.symcb.com",
      "su.symcd.com",
      "vassg142.crl.omniroot.com",
      "vassg142.ocsp.omniroot.com",
      "www.digicert.com",
      "www.microsoft.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 126,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "officespeech.platform.bing.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Connection to the speech service is required for Office Dictation features. If connectivity is not allowed, Dictation will be disabled."
  },
  {
    "id": 127,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "*.skype.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 128,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.manage.microsoft.com",
      "*.officeconfig.msocdn.com",
      "config.office.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "Blocking this endpoint will affect Office 365 ProPlus and other Click-to-Run deployment features in including deployment via Configuration Manager and Intune as well as Office policy management."
  },
  {
    "id": 130,
    "serviceArea": "Common",
    "serviceAreaDisplayName": "Microsoft 365 Common and Office Online",
    "urls": [
      "*.loki.delve.office.com",
      "loki.delve.office.com",
      "loki.delve-gcc.office.com",
      "lpcres.delve.office.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  },
  {
    "id": 145,
    "serviceArea": "Exchange",
    "serviceAreaDisplayName": "Exchange Online",
    "urls": [
      "*.measure.office.com"
    ],
    "tcpPorts": "80,443",
    "expressRoute": False,
    "category": "Default",
    "required": False,
    "notes": "This Endpoint is used for Telemetry Purposes."
  },
  {
    "id": 146,
    "serviceArea": "Skype",
    "serviceAreaDisplayName": "Skype for Business Online and Microsoft Teams",
    "urls": [
      "statics.teams.microsoft.com"
    ],
    "tcpPorts": "443",
    "expressRoute": False,
    "category": "Default",
    "required": True
  }
]
  
ips = []
for x in range(len(livefeed)):
    try:
        for y in livefeed[x]["ips"]:
            ips.append(y)
    except KeyError:
        pass
        #print "Line "+str(x)+" has an issue"

"""
/c/slb/nwclss O365-IPs
	name "O365-IPs"
	type "address"
	ipver v4
/c/slb/nwclss O365-IPs/network 13.106.4.128_25
	net subnet 13.106.4.128 255.255.255.128 include
"""

ipv4_ips = []
ipv6_ips = []

for x in set(ips):
    if ":" not in x:
        ipv4_ips.append(x)
    else:
        ipv6_ips.append(x)

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