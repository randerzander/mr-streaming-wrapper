#!/usr/bin/python
from subprocess import call
import sys

for line in sys.stdin:
  tokens = line.strip().split('|')
  path = tokens[0]
  filename = path.split('/')[-1]
  command = tokens[1].replace('__filename__', filename)
  sys.stderr.write('getting ' + path + ' from hdfs\n')
  call(['hadoop', 'fs', '-get', path])
  sys.stderr.write('got ' + filename + ' from hdfs, running ' + command + '\n')
  call(command.split(' '))
  #you need to know what the output filename will be to put it back in HDFS
  sys.stderr.write('writing ' + filename + '.gz to hdfs\n')
  #make sure the converted directory is writable by your running streaming job
  call(['hadoop', 'fs', '-put', filename + '.gz', '/user/dev/converted/'])
