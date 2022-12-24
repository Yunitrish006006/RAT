FROM python:3.9.13
WORKDIR /bot
COPY requirements.txt /bot/
RUN pip install -r requirements.txt
copy . /bot
CMD python no_cog_cmd.py