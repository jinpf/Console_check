#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jinpf
# @Date:   2015-05-27 20:34:43
# @Last Modified by:   qinan.jpf
# @Last Modified time: 2015-05-29 09:48:08

import getpass
import telnetlib

def telnet_test(Host, Port, User, Password, error_hint):
	tn = telnetlib.Telnet()
	try:
		tn.open(Host, Port)
	except:
		print "Connect error!"
		return
	info = tn.read_until("login:")
	print info.replace("login:",'',-1)
	tn.write(User + '\n')
	tn.read_until("Password:")
	tn.write(Password + '\n')
	info = tn.read_until("login:")
	if error_hint in info:
		print 'user name or password error!'
	else:
		print 'login ok !'
	tn.close()

if __name__ == '__main__':
	Host = '159.226.251.134'
	Port = 23
	User = raw_input('user name:')
	Password = getpass.getpass()
	telnet_test(Host, Port, User, Password, 'incorrect')
	raw_input('请按回车键退出脚本程序'.decode('utf-8').encode('gbk'))
