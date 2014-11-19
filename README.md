An example of using a Python wrapper script to run arbitrary executables against files stored in HDFS

Example:
```
hadoop fs -put data/ .
hadoop fs -put inputs/ .
hadoop fs -mkdir converted
hadoop fs -chmod 777 converted
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-*.jar -file wrapper.py -mapper wrapper.py -input inputs -output dummy
```
