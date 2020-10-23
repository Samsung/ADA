FROM python:3.8

# Install modules required in production environment
COPY ./devops/requirements/prod.txt /tmp/requirements.txt
RUN  python3.8 -m pip install -r /tmp/requirements.txt

# Create user and directories, which are required for ADA service
RUN adduser --system --group --home /nonexistent --no-create-home --disabled-password ada \
&&  install -o root -g ada -m 775 -d "/var/log/ada" "/var/lib/ada" "/var/volumes/ada";

# Copy ADA service sources and generate python cache files
RUN  echo /var/lib > /usr/local/lib/python3.8/site-packages/paths.pth
COPY ./src/ada /var/lib/ada
RUN  python3.8 -m ada --version

# Declare volume for mounting config directory
VOLUME /var/volumes/ada

# Set configuration environment variables
ENV ADA_CONFIG    "/var/volumes/ada/config.yaml"
ENV ADA_DATABASE  "/var/volumes/ada/database.sqlite"
#ENV ADA_LOGFILE   "/var/log/ada/daemon.log"

# Forward ADA logs to docker log collector
#RUN ln -sf /dev/stdout "$ADA_LOGFILE";

# Change current user
USER ada

# Start ADA service as entrypoint
CMD exec python3.8 -m ada \
	--config   "$ADA_CONFIG" \
	--database "$ADA_DATABASE";

