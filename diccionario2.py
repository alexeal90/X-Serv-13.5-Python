#!/usr/bin/python
# -*- coding: utf-8 -*-

fich=open("/etc/passwd","r")
user_num=fich.readlines()
print "El numero de usuarios de este ordenador es: " + str(len(user_num))
fich.close()

# Primera parte hecha

diccionario = {}

fich=open("/etc/passwd","r")

for user in user_num:
    
	conf = user.split(":");
	username = conf[0]
	shell = conf[-1]
	print "El usuario: *" + username + "* utiliza la shell: " + shell
	diccionario[username] = shell

print "root", diccionario["root"]

try:
	print "imaginario", diccionario["imaginario"]
except KeyError:
	print ("no es una clave correcta")

fich.close()

