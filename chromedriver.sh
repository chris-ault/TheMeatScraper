
#!/bin/bash

# Download the latest version of Chromedriver
LATEST_CHROMEDRIVER_VERSION=110.0.5481.30

# Download the Chromedriver binary
wget -N https://chromedriver.storage.googleapis.com/$LATEST_CHROMEDRIVER_VERSION/chromedriver_linux64.zip -P ~/Downloads

# Unzip the binary and move it to /usr/local/bin
sudo unzip -o ~/Downloads/chromedriver_linux64.zip -d /usr/local/bin/

# Set the correct permissions on the Chromedriver binary
sudo chmod +x /usr/local/bin/chromedriver

# Verify that Chromedriver is installed correctly
chromedriver --version