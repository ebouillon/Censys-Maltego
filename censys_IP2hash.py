#############################################
# Censys API Cert IP to Hash
# 
# Author: Emmanuel Bouillon
# Email:  emmanuel.bouillon.sec@gmail.com
# Date: 11/06/2015
#############################################
import sys
import json
import censys.ipv4
import censys.certificates
import requests

from censys_util import *

if __name__ == '__main__':
        ip = sys.argv[1]
        mt = MaltegoTransform()
        mt.addUIMessage('[INFO] ' + ip + ' to Hash')
        res = requests.get(API_URL + "/view/ipv4/" + ip, auth=(UID, SECRET))
        mt.addUIMessage('[INFO] query ' +  API_URL + '/view/ipv4/' + ip)
        if res.status_code != 200:
            mt.addUIMessage('[Error] ' + res.json()["error"])
            mt.returnOutput()
        j = res.json()
        if j.has_key('443') and j['443'].has_key('https') and  j['443']['https'].has_key('tls'):
            cert_hash = j['443']['https']['tls']['certificate']['parsed']['fingerprint_sha1'] 
            me = MaltegoEntity('maltego.Hash', cert_hash);
            cert_hash = j['443']['https']['tls']['certificate']['parsed']['fingerprint_sha256'] 
            me = MaltegoEntity('maltego.Hash', cert_hash);
            cert_hash = j['443']['https']['tls']['certificate']['parsed']['fingerprint_md5'] 
            me = MaltegoEntity('maltego.Hash', cert_hash);
            me.addAdditionalFields('notes#', 'notes', False, j['443']['https']['tls']['certificate']['parsed']['subject_dn'] )
            mt.addEntityToMessage(me);
        mt.returnOutput()


