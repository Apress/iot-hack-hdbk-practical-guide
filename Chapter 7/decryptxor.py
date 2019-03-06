import os
import sys

key = "8844a2d168b45a2d".decode("hex")
data = sys.stdin.read()

r = ""
for i in range(len(data)):
	c = chr(ord(data[i]) ^ ord(key[i % len(key)]))
	r += c

sys.stdout.write(r)

