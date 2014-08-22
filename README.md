An example of using a Python wrapper script to run arbitrary executables against files stored in HDFS

Example:
```
hadoop fs -put data/ /user/dev/
hadoop fs -mkdir /user/dev/commands
hadoop fs -put commands.txt /user/dev/commands/
hadoop fs -mkdir /user/dev/converted
hadoop fs -chmod 777 /user/dev/converted
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-*.jar -file wrapper.py -mapper wrapper.py -input /user/dev/commands -output /user/dev/output
```
