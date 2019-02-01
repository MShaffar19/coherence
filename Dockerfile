FROM centos:7
RUN yum install -y glibc-static libstdc++-static autoconf automake gcc gcc-c++ make libtool git wget
RUN wget https://raw.githubusercontent.com/liesware/coherence/master/install.sh
RUN sh install.sh
RUN cp /coherence_git/coherence/coherence02/bin/coherence /usr/bin/
RUN rm -rf /coherence_git/