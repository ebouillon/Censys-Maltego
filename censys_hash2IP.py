#############################################
# Censys API Cert Hash to IP
# 
# Author: Emmanuel Bouillon
# Email:  emmanuel.bouillon.sec@gmail.com
# Date: 11/06/2015
#############################################
import sys
import json
import censys.ipv4

from censys_util import *

if __name__ == '__main__':
        cert_hash = sys.argv[1]
        mt = MaltegoTransform()
        mt.addUIMessage('[INFO] ' + cert_hash + ' to IP')
        ipv4 = censys.ipv4.CensysIPv4(UID, SECRET)
        try:
            for c in ipv4.search('parsed.fingerprint_sha1="' + cert_hash + '"'):
                j = json.loads(json.dumps(c))
                me = MaltegoEntity('maltego.IPv4Address',j['ip']);
                mt.addEntityToMessage(me);
        except Exception as e:
            mt.addUIMessage('[Error] ' + str(e))
        mt.returnOutput()


