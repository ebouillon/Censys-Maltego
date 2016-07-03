# Censys-Maltego
Some Maltego transforms for Censys.io

# Prerequisites:
- Censys Python Library (see https://censys.io/api)

# INSTALL:
- Edit censys_util.py and set API credentials (UID and SECRET).

- Import transforms in Maltego:
. censys_IP2hash.py: [CENSYS] IP to SSL/TLS Hash / Returns SSL/TLS Hash seen on IP
. censys_domain2hash.py: [CENSYS] Domain to SSL/TLS Hash / Returns SSL/TLS Hash corresponding to Domain
. censys_hash2IP.py: [CENSYS] SSL/TLS Hash to IP / Returns IP seen with SSL/TLS Hash
