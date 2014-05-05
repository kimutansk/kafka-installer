kafka-installer
===============

Apache Kafka install package.

## Environment

* OS: CentOS 6.X
* CPU Arch: x64
* Middleware: Needs JDK6 or after（Oracle JDK or Open JDK）

## Download
https://github.com/kimutansk/kafka-installer/wiki/Download  


## Before you install kafka package

Before you install kafka package on a cluster,
there are some important steps you need to do to prepare your system.

1.Kafka needs zookeeper cluster.  
  For zookeeper cluster installation, you find install step on cdh.  
  http://www.cloudera.com/content/support/en/documentation/cdh5-documentation/cdh5-documentation-v5-latest.html  
  http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/5/RPMS/x86_64/  


## Installing kafka package

1.Download kafka rpm package.  
  wget https://s3.amazonaws.com/publicarchive/kafka/kafka-0.8.1.1-1.el6.x86_64.rpm  

2.Install the kafka RPM:
```
# sudo rpm -ivh kafka-0.8.1.1-1.el6.x86_64.rpm  
```

3.Set the configuration.  
  (Reference: http://kafka.apache.org/documentation.html#brokerconfigs )  
```
# sudo vi /opt/kafka/config/server.properties
```

The essential configurations default value are following:  

```
broker.id=0  
log.dirs=/opt/kafka/kafka-logs  
zookeeper.connect=localhost:2181  
```

4.Start or stop kafka cluster by following commands:

Start
```
# sudo service kafka-server start  
```

Stop
```
# sudo service kafka-server stop  
```

## Dependency libraries

Project    : Apache Kafka  
Version    : 0.8.1.1  
Lisence    : Apache License Version 2.0  
Source URL : http://kafka.apache.org/  

## License
This software is released under the MIT License, see LICENSE.txt.
