# python3のイメージを基にする
FROM python:3
ENV PYTHONBUFFERED 1

# ビルド時に/codeというディレクトリを生成する
RUN mkdir /code

#　ワークディレクトリの設定
WORKDIR /code

# requirement.txtを/code/にコピーする
ADD requirements.txt /code/

# requirements.txtを基に"pip install"する
RUN pip install -r requirements.txt
ADD . /code/