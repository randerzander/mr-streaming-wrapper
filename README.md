An example of using a Python wrapper script to run arbitrary executables against files stored in HDFS. For example, this wrapper could be used to simultaneously perform OCR on a large number of PDFs, perform video or audio transcoding, etc. using any application that can be controlled via the CLI. The advantage is that there is no need to modify the application to work with Hadoop.

It works as follows:

The "inputs" folder contains one file per unit of work to be performed in parallel. Each file should contain the HDFS URI of a source file.

Because source files are enumerated in independent files, the MR job can run with as many mappers as there are files in the "inputs" folder.

Map tasks run wrapper.py, which receives the HDFS URI of a source file, performs an HDFS get, and runs an arbitrary shell process against it. Whatever form the output takes is stored in the "converted" folder.

Example:
```
hadoop fs -put data/ .
hadoop fs -put inputs/ .
hadoop fs -mkdir converted
hadoop fs -chmod 777 converted
# HDP 2.1 or earlier
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-*.jar -file wrapper.py -mapper wrapper.py -input inputs -output dummy
# HDP 2.2 or later
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file wrapper.py -mapper wrapper.py -input inputs -output dummy
# HDP 2.2 on Windows
hadoop jar C:\hdp\hadoop-2.6.0.2.2.0.0-2041\share\hadoop\tools\lib\hadoop-streaming-2.6.0.2.2.0.0-2041.jar -file wrapper.py -mapper wrapper.py -input inputs -output dummy
```
