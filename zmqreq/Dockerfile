FROM python:3.6.8-alpine3.10

RUN set -x \
    && apk update \
    && apk --no-cache add \
        libstdc++ \
        protobuf \
    && apk --no-cache add --virtual .builddeps \
        autoconf \
        automake \
        build-base \
        cmake \
        git \
        libtool \
        pkgconfig \
        protobuf-dev \
    && git clone  https://github.com/google/sentencepiece \
    && cd sentencepiece \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make -j $(nproc) \
    && make install \
    ## && ldconfig -v \
    ## cleanup
    && make clean

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    && apk del .builddeps

CMD ["bash"]
