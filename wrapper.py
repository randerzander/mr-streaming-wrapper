#!/usr/bin/python
from subprocess import call
import sys

for line in sys.stdin:
  path = line.strip()
  filename = path.split('/')[-1]
  command = 'gzip ' + filename

  # Get the input file from HDFS
  sys.stderr.write('getting ' + path + ' from hdfs\n')
  call(['hadoop', 'fs', '-get', path])
  sys.stderr.write('got ' + filename + ' from hdfs, running ' + command + '\n')

  # Execute command
  call(command.split(' '))
  sys.stderr.write('writing ' + filename + '.gz to hdfs\n')

  # Put the result into HDFS
  call(['hadoop', 'fs', '-put', filename + '.gz', '/user/dev/converted/'])
