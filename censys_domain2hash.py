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
import censys.certificates

from censys_util import *

if __name__ == '__main__':
        dom = sys.argv[1]
        mt = MaltegoTransform()
        mt.addUIMessage('[INFO] ' + dom + ' to IP')
        cert = censys.certificates.CensysCertificates(UID, SECRET)
        try:
            for c in cert.search(dom):
                j = json.loads(json.dumps(c))
                if j.has_key('parsed.fingerprint_sha256'):
                    for i in j['parsed.fingerprint_sha256']:
                        me = MaltegoEntity('maltego.Hash', i)
                        mt.addEntityToMessage(me);         
                if j.has_key('parsed.fingerprint_sha1'):
                    for i in j['parsed.fingerprint_sha1']:
                        me = MaltegoEntity('maltego.Hash', i)
                        mt.addEntityToMessage(me);         
                if j.has_key('parsed.fingerprint_md5'):
                    for i in j['parsed.fingerprint_md5']:
                        me = MaltegoEntity('maltego.Hash', i)
                        mt.addEntityToMessage(me);         
                me.addAdditionalFields('notes#', 'notes', False, j['parsed.subject_dn'][0])

        except Exception as e:
            mt.addUIMessage('[Error] ' + str(e))
        mt.returnOutput()


