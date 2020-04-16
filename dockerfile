FROM python:3.7.6

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

#Install Cron
RUN apt-get update
RUN apt-get -y install cron

RUN mkdir /crawler

COPY requirements.txt /crawler

RUN pip3 install --upgrade pip
RUN pip3 install -r /crawler/requirements.txt

COPY . /crawler/

WORKDIR /crawler
# Run the command on container startup
CMD cron && tail -f /var/log/cron.log