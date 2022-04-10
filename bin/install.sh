#!/bin/bash
git clone https://github.com/macuyler/gitbin.git /tmp/gitbin_install && \
	/tmp/gitbin_install/gb install https://github.com/macuyler/gitbin.git && \
	rm -rf /tmp/gitbin_install && \
	echo ' * Successfully installed Git Bin!'
