FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/venv

# Create virtual environment
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set work directory
WORKDIR /code

ADD requirements_base.txt /requirements_base.txt
ADD requirements_dev.txt /requirements_dev.txt

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install -r /requirements_dev.txt && \
    rm -rf /requirements_*.txt
