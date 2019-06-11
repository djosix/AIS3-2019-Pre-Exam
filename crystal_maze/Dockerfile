FROM crystallang/crystal:0.28.0
RUN mkdir /server
COPY server.cr secret.cr flag.txt /server/
WORKDIR /server
RUN crystal build --release -o server server.cr
