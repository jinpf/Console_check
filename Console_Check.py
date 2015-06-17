#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: qinan.jpf
# @Date:   2015-06-16 14:20:51
# @Last Modified by:   qinan.jpf
# @Last Modified time: 2015-06-16 17:40:45

import getpass
import paramiko
from multiprocessing.dummy import Pool as ThreadPool

def get_host(fname):
	with open(fname, 'r') as f:
		hosts = f.readlines()
		return [host.strip('\n') for host in hosts]

def print_process():
	global Total_number
	global Now_count
	Now_count += 1
	p = 100 * Now_count / Total_number
	print '='*(p/10*3) + '> ' + str(p) + '%'

def ssh_test(host):
	global Port
	global User
	global Password
	
	try:
		ssh = paramiko.Transport((host, Port))
	except :
		print_process()
		print host + ' : Unable to connect to the host or port!'
		return (host,1)
	try:
		ssh.connect(username = User, password = Password)
	except paramiko.ssh_exception.AuthenticationException:
		print_process()
		print host + ' : Authentication failed!'
		return (host,2)
	except paramiko.ssh_exception.SSHException:
		print_process()
		print host + ' : Port not SSH service!'
		return (host,3)
	if ssh.is_authenticated():
		print_process()
		print host + ' : Login OK!'
	ssh.close()
	return (host,0)

def ssh_test_using_multithread(hosts):
	# Thread number by default depends on cpu core number
	# or use pool = ThreadPool(4) to specify
	pool = ThreadPool()
	results = pool.map(ssh_test, hosts)
	pool.close()
	pool.join()
	return results

def show_result(results):
	login_ok = []
	connection_error = []
	authentication_error = []
	port_error = []

	for i in results:
		if i[1] == 0:
			login_ok.append(i[0])
		elif i[1] == 1:
			connection_error.append(i[0])
		elif i[1] ==2:
			authentication_error.append(i[0])
		elif i[1] ==3:
			port_error.append(i[0])

	n = len(login_ok)
	if n:
		print "Login OK total " + str(n)
		print

	n = len(connection_error)
	if n:
		connection_error.sort()
		print "Connection Error total " + str(n) + ":"
		for h in connection_error:
			print h
		print

	n = len(authentication_error)
	if n:
		authentication_error.sort()
		print "Authentication Error total " + str(n) + ":"
		for h in authentication_error:
			print h
		print

	n = len(port_error)
	if n:
		port_error.sort()
		print  "Port Error total " + str(n) + ":"
		for h in port_error:
			print h
		print

if __name__ == '__main__':
	User = raw_input('user name:')
	Password = getpass.getpass('password:')
	Port = 22
	hosts = get_host('host.txt')
	Total_number = len(hosts)
	Now_count = 0
	print '*' * 30
	print
	results = ssh_test_using_multithread(hosts)
	print '*' * 30
	print
	show_result(results)
	raw_input('Press enter to exit.')