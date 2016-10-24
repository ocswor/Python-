
#!/usr/bin/env python
# coding=utf-8

__author__ = 'Eric'
import socket
import time
import sys


def myClient():
     host = '192.168.1.40'
     port = 18001
     # bufsize = 1024
     addr = (host,port)
     client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     client.connect(addr)
     while True:
          data = input('Enter:');


          if data=='exit':
               break
          try:
               if not data:
                    print("no data eric")

          except:
               # break
                print("Exception")

          client.send(data.encode("utf8"))



          # while 1:
          




     client.close()

if __name__ == '__main__':
     myClient()
