Name: kafka	
Version: 0.8.1.1  
Release: 1%{?dist}  
Summary: A high-throughput distributed messaging system.	
Group: Applications/Internet
License: MIT
URL: http://kafka.apache.org/
Source: https://www.apache.org/dyn/closer.cgi?path=/kafka/0.8.1.1/kafka-0.8.1.1.tgz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires(pre): shadow-utils
%description
Apache Kafka is publish-subscribe messaging rethought as a distributed commit log.

Fast
A single Kafka broker can handle hundreds of megabytes of reads and writes per second from thousands of clients.

Scalable
Kafka is designed to allow a single cluster to serve as the central data backbone for a large organization. It can be elastically and transparently expanded without downtime. Data streams are partitioned and spread over a cluster of machines to allow data streams larger than the capability of any single machine and to allow clusters of co-ordinated consumers

Durable
Messages are persisted on disk and replicated within the cluster to prevent data loss. Each broker can handle terabytes of messages without performance impact.

Distributed by Design
Kafka has a modern cluster-centric design that offers strong durability and fault-tolerance guarantees. 

This package includes kafka-server(kafka-broker) process.


%pre
getent group kafka >/dev/null || groupadd -r kafka
getent passwd kafka >/dev/null || \
    useradd -r -g kafka -d /opt/kafka -s /sbin/nologin \
    -c "Kafka Server Service" kafka
exit 0

%prep
%setup -q

# This SPEC build is Only Packaging.
%build

%install

# Copy the kafka file to the right places
%{__mkdir_p} %{buildroot}/opt/kafka-%{version}
%{__mkdir_p} %{buildroot}/var/opt/kafka
%{__cp} -R kafka/* %{buildroot}/opt/kafka-%{version}/
%{__ln_s} /opt/kafka-%{version} %{buildroot}/opt/kafka

# Copy the service file to the right places
%{__mkdir_p} %{buildroot}/etc/init.d
%{__mkdir_p} %{buildroot}/etc/sysconfig
%{__mkdir_p} %{buildroot}/var/log/kafka
%{__mkdir_p} %{buildroot}/var/run/kafka

%{__mv} init.d/kafka-server %{buildroot}/etc/init.d
%{__mv} sysconfig/kafka-server %{buildroot}/etc/sysconfig/kafka-server

%files
%defattr(777,kafka,kafka)
/opt/kafka
%defattr(-,kafka,kafka,755)
/opt/kafka-%{version}
%dir /var/log/kafka
%dir /var/run/kafka
%defattr(755,root,root)
/etc/init.d/kafka-server
%defattr(644,root,root)
/etc/sysconfig/kafka-server

%clean
%{__rm} %{buildroot}/opt/kafka

%preun
if [ "$1" = "0" ]; then
    /sbin/service kafka-server stop
    /sbin/chkconfig kafka-server off
fi


%changelog
* Mon May 5 2014 Kimura Sotaro
- kafka-0.8.1.1 Packaging

* Fri Apr 30 2014 Kimura Sotaro
- kafka-0.8.1 Packaging

