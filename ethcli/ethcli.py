import requests
import json
import sys
import time
import os


def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def json_req (command, args = []):
	payload = {
		"method": command,
		"params": args,
		"jsonrpc": "2.0",
		"id": 0,
	}
	r = requests.post('http://localhost:8545/', data=json.dumps(payload), headers={'content-type': 'application/json'}).json()

	return r['result']


if len (sys.argv) > 1:
	print (json_req (sys.argv[1], sys.argv[2:]))
else:
	while True:
		cls ()
		print ('Ethereum cli')

		print ('Current block:', int (json_req ('eth_blockNumber'),16))

		print ('Mining hashrate:',int (json_req ('eth_hashrate'),16),'h/s')

		print ('\nAccounts:')
		for x in json_req ('eth_accounts'):
			print ('\t',x,'\t->\t',float (int (int (json_req ('eth_getBalance', [x, 'latest']), 16) / 1000000000000000) / 1000),' eth')

		time.sleep (10)
