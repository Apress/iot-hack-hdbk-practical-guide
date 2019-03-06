#!/usr/bin/python

import os,sys,re, socket, time, select, random, getopt
from Crypto.Cipher import AES

aeskey="fdsl;mewrjope456fds4fbvfnjwaugfo"
wiresharkpacket = "c42cb8276aeb4ef501943c31c207fb1c7e0a546a05e7e7a768f5ae8955bd29a43e661eb16398695176bfb4a5ca8b7b98b921cc52c168326296a155f8cbd8cea5".decode("hex")

aesobj = AES.new(aeskey, AES.MODE_ECB)
print str(aesobj.decrypt(wiresharkpacket))
