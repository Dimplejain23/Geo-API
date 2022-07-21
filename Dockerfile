FROM osgeo/gdal:ubuntu-small-latest

# Ensure locales configured correctly
RUN dpkg --configure --force-overwrite -a
RUN apt-get clean && apt-get autoremove && apt-get update --fix-missing && apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LC_ALL='en_US.utf8'

RUN apt-get install python3-pip python3-dev libcairo2-dev -y
RUN apt-get install postgresql postgresql-client postgis -y
RUN apt-get install gunicorn -y

# Change TimeZone
ENV TZ=Asia/Kolkata

# Clean APK cache
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# App code will be deployed into /code within docker container
WORKDIR /code

# Add and install Python modules.
ADD requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]