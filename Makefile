# Makefile to send this site to Zam
SHELL=/usr/bin/env /bin/bash

all:	send

send:	send_zamok
send_zamok:
	CP --cvs-exclude --exclude=./.git ./ ${Szam}cuisine/
