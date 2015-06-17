#Console_Check

A python script for checking whether devices can be logged on by ssh.

This script using multithread method to do the check, pretty good for checking a huge amount of devices. I write this as an intern of Alibaba, tests show it works well:)

##Prerequisites
* python 2
* paramiko([http://docs.paramiko.org/](http://docs.paramiko.org/))

##Usage：
Write the host domain or IP address one in a line in `host.txt`, like this:

	www.aaa.com
	www.bbb.com
	111.222.333.444
	...

Then run the script in the same folder：
	
	python Console_Check.py

Then press user name and password, and check begin.

After the check, it well list logon failed devices by reason.