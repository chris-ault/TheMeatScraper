#!/bin/bash

# Add the Google Chrome repository to the sources list
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list

# Import the Google Chrome signing key
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

# Update the package lists
sudo apt-get update

# Install Google Chrome
sudo apt-get install google-chrome-stable