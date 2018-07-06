import socket
import json
import os,binascii

def sending(message):
	ip = '127.0.0.1'
	port = 6613
	BUFFER_SIZE = 65536
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(message)
	data = s.recv(BUFFER_SIZE)
	s.close()
	return data

def rsa(data_js, bits):
	req=json.loads(data_js)
	req["length"]=bits
	print "Send gen parameters : \n " + json.dumps(req) +"\n"
	data_js_n=sending(json.dumps(req))
	answ=json.loads(data_js_n)	
	print "Recived  rsa gen: \n"+(json.dumps(answ)) +"\n\n\n"
	req["algorithm"]="RSA"
	req["type"]="string"
	req["hex"]=0
	req["plaintext"]="Hello world"
	req["privkey"]=answ["privkey"]
	req["operation"]="sign"
	print "Send sign : \n " + json.dumps(req) +"\n"
	data_js_n=sending(json.dumps(req))
	answ_1=json.loads(data_js_n)	
	print "Recived  sign done: \n"+(json.dumps(answ_1)) +"\n\n\n"
	json_v='{ "version": 1 , "algorithm":"RSA", "type":"string","plaintext": "Hello world", "hex":0,"pubkey": "" ,"sign":""}'
	req=json.loads(json_v)
	req["pubkey"]=answ["pubkey"]
	req["sign"]=answ_1["sign"]
	req["operation"]="verify"
	print "Send verify : \n " + json.dumps(req) +"\n"
	data_js_n=sending(json.dumps(req))
	answ_2=json.loads(data_js_n)
	print "Recived  verify done: \n"+(json.dumps(answ_2)) +"\n\n\n"
	json_enc='{ "version": 1 , "algorithm":"RSA", "type":"string","pubkey": "" ,"operation":"enc", "plaintext":"hello world!!!" }'
	req=json.loads(json_enc)
	req["pubkey"]=answ["pubkey"]
	print "Send enc : \n " + json.dumps(req) +"\n"
	data_js_n=sending(json.dumps(req))
	answ_3=json.loads(data_js_n)
	print "Recived  enc done: \n"+(json.dumps(answ_3)) +"\n\n\n"
	req["privkey"]=answ["privkey"]
	req["plaintext"]=answ_3["result"]
	req["pubkey"]=""
	req["operation"]="dec"
	print "Send dec : \n " + json.dumps(req) +"\n"
	data_js_n=sending(json.dumps(req))
	answ_3=json.loads(data_js_n)
	print "Recived  enc done: \n"+(json.dumps(answ_3)) +"\n\n\n"	



rsa_gen='{ "version": 1 , "algorithm":"RSA", "operation":"gen" , "length": 2048 }'
rsa(rsa_gen,1024)

