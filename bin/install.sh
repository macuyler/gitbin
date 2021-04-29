#!/bin/bash
git clone https://github.com/macuyler/mac.git /tmp/mac_install && \
	/tmp/mac_install/mac install https://github.com/macuyler/mac.git && \
	rm -rf /tmp/mac_install && \
	echo $'\n\n * Successfully installed Macuyler\'s Automation Cli!'
