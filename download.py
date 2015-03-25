import subprocess
import tangelo
import json
import os
import tempfile

def run(output_format="",data=""):
	filename = '/tmp/svg_input.%s.txt' % os.getpid()
	temp = open(filename, 'w+b')
	try:
		temp.write(data)
	finally:
		temp.close()
	output_file = '/tmp/svg_output.%s.txt' % os.getpid()
	if output_format=='png':
		zoom = 10
	else:
		zoom = 1

	subprocess.call(["rsvg-convert","-o",output_file, "-z",str(zoom),"-f", output_format,filename])
	tmp=open(output_file,'r')
	try:
		test=tmp.read()
	finally:
		tmp.close()
		#os.remove(output_file)
		#os.remove(filename)

	tangelo.content_type('application/x-pdf')
	return test