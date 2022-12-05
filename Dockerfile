FROM jupyter/datascience-notebook:python-3.8.8

# Install Jupyterlab
USER root
RUN pip install --upgrade jupyterlab jupyterlab-git
RUN jupyter lab build
COPY requirements_container.txt .
RUN pip install -r requirements_container.txt
RUN jupyter server extension enable --py jupyterlab_git
RUN pip install nbgitpuller
RUN jupyter serverextension enable --py nbgitpuller --sys-prefix

# Install gcloud + crcmod
RUN apt-get -y update && \
    apt-get -y install gcc python2.7 python-dev python-setuptools wget ca-certificates \
       # These are necessary for add-apt-respository
       software-properties-common && \

    # Install Git >2.0.1
    add-apt-repository ppa:git-core/ppa && \
    apt-get -y update && \
    apt-get -y install git && \

    # Setup Google Cloud SDK (latest)
    mkdir -p /builder && \
    wget -qO- https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz | tar zxv -C /builder && \
    CLOUDSDK_PYTHON="python2.7" /builder/google-cloud-sdk/install.sh --usage-reporting=false \
        --bash-completion=false \
        --disable-installation-options && \

    # install crcmod: https://cloud.google.com/storage/docs/gsutil/addlhelp/CRC32CandInstallingcrcmod
    easy_install -U pip && \
    pip install -U crcmod && \
    apt-get install python3-pip -y -q && \
    pip3 install -U crcmod && \

    # Clean up
    apt-get -y remove gcc python-dev python-setuptools wget python3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf ~/.config/gcloud

ENV PATH=/builder/google-cloud-sdk/bin/:$PATH
RUN git config --system credential.helper gcloud.sh
