# This file contains configurations for kafka-server startup
KAFKA_HEAP_OPTS="-Xmx1G -Xms1G"
KAFKA_JMX_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.authenticate=false  -Dcom.sun.management.jmxremote.ssl=false"
KAFKA_JVM_PERFORMANCE_OPTS="-server -XX:+UseCompressedOops -XX:+UseParNewGC -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled -XX:+CMSScavengeBeforeRemark -XX:+DisableExplicitGC -Djava.awt.headless=true"

GC_LOG_FILE_NAME=kafkaServer-gc.log
KAFKA_GC_LOG_OPTS="-Xloggc:$LOG_DIR/$GC_LOG_FILE_NAME -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps "

KAFKA_LOG4J_OPTS="-Dkafka.logs.dir=$LOG_DIR -Dlog4j.configuration=file:$KAFKA_CONF/log4j.properties"

KAFKA_OPTS=""
