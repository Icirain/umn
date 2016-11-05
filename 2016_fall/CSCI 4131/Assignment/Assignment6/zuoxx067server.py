#!/usr/bin/env python3
# See https://docs.python.org/3.2/library/socket.html
# for a decscription of python socket and its parameters
import socket
import os
import sys
from threading import Thread
from argparse import ArgumentParser

# for the server you may find the following python libraries useful:
#import os - check to see if a file exists in python -
# e.g., os.path.isfile, os.path.exists

#import stat
#check if a file has others permissions set, os.stat

#import sys - enables you to get the argument vector (argv) from command line and use
# values passed in from the command line


#other defintions that will come in handy for getting data and
#constructing a response
BUFSIZE = 4096
CRLF = '\r\n'
#You might find it useful to define variables similiar to the one above
#for each kind of response message

#Outline for processing a request - indicated by the call to processreq below
#the outline below is for a GET request, though the others should be similar (but not the same)
#remember, you have an HTTP Message that you are parsing
#so, you want to parse the message to get the first word on the first line
#of the message (the HTTP command GET, HEAD, ????) if the HTTP command is not known you should respond with an error
#then get the  resource (file path and name) - python strip and split should help
#Next,  does the resource have a legal name (no % character) 
#			if false  - construct an error message for the response and return
#           if true - check to see if the resource exists
#				if false - construct an error message for the response and return
#				if true - check to see if the permissions on the resource for others are ok
#					if false - construct an error message for the response and resturn
#					if true - Success!!! 
#                              open the resource (file)
#                              read the resource into a buffer
#                              create a response message by concatenating the OK message above with
#                              the string you read in from the file
#                              return the response
#

def  processreq(req):
  line=req.split(CRLF)[0]
  req_part=line.split(' ')
  req_method=req_part[0]
  req_protocol=req_part[-1]
  req_url=' '.join(req_part[1:-1])
  
  response_200='{} 200 OK {}{}{}'.format(req_protocol,CRLF,CRLF,CRLF)
  response_301='{} 301 Move Permanently {}{}{}{}'.format(req_protocol,"http://www.cs.umn.edu",CRLF,CRLF,CRLF)
  response_301_head='{} 301 Move Permanently {}{}{}'.format(req_protocol,CRLF,CRLF,CRLF)
  response_403='{} 403 Forbidden {}{}{}'.format(req_protocol,CRLF,CRLF,CRLF)
  response_404='{} 404 Not Found {}{}{}'.format(req_protocol,CRLF,CRLF,CRLF)
  response_405='{} 405 Method Not Allowed {}{}{}'.format(req_protocol,CRLF,CRLF,CRLF)
  response_406='{} Not Acceptable Response{}{}{}'.format(req_protocol,CRLF,CRLF,CRLF)
  response_505='{} Protocol Version Not Supported{}{}{}'.format(req_protocol,CRLF,CRLF,CRLF)
  extend_set=['html','jpeg','gif','pdf','doc','pptx','mod']

  if req_protocol not in ['HTTP/1.0','HTTP/1.1']:
    return response_505
  if req_method not in ['GET','HEAD']:
    return response_405
  location=req_url.lstrip('/')
  if location=='csumn':
    if req_method=='GET':
      return response_301
    else:
      return response_301_head
  if os.path.isfile(location)==False:
    if req_method=='GET':
      return response_404+addFile('404.html')
    else:
      return response_404
  permissions=bin(os.stat(location).st_mode)
  extend=location.split('.')[-1]
  print(extend)
  print(permissions)
  if permissions[-3]=='1':
    if extend not in extend_set:
      if req_method=='GET':
        return response_406+addFile('406.html')
      else:
        return response_406
    else:
      if req_method=='GET':
        return response_200+addFile(location)
      else:
        return response_200
  else:
    if req_method=='GET':
      return response_403+addFile('403.html')
    else:
      return response_403


def addFile(path):
  extend=path.split('.')[-1]

  if extend=='html':
   try:
     stream=open(path,'r')
     content=stream.read()
     stream.close()
   except:
     content=''
  else:
    content='a {} file called {} '.format(extend,path)
  return content
def client_talk(client_sock, client_addr):
    print('talking to {}'.format(client_addr))
    data = client_sock.recv(BUFSIZE)
	# note, here is where you decode the data and process the request
    req = data.decode('utf-8')
	# then, you'll need a routine to process the data, and formulate a response
    # response = processreq(req) 
    #once have the response, you send it
    response=processreq(req)
    print(response)
    client_sock.send(bytes(response, 'utf-8'))

    client_sock.shutdown(1)
    client_sock.close()
    print('connection closed.')

class EchoServer:
  def __init__(self, host, port):
    print('listening on port {}'.format(port))
    self.host = host
    self.port = port

    self.setup_socket()

    self.accept()

    self.sock.shutdown()
    self.sock.close()

  def setup_socket(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.bind((self.host, self.port))
    self.sock.listen(128)

  def accept(self):
    while True:
      (client, address) = self.sock.accept()
      th = Thread(target=client_talk, args=(client, address))
      th.start()

def parse_args():
  parser = ArgumentParser()
  parser.add_argument('--host', type=str, default='localhost',
                      help='specify a host to operate on (default: localhost)')
  parser.add_argument('-p', '--port', type=int, default=9001,
                      help='specify a port to operate on (default: 9001)')
  args = parser.parse_args()
  return (args.host, args.port)


if __name__ == '__main__':
  (host, port) = parse_args()
  EchoServer(host, port)

