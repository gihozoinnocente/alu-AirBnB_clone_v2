sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releasses/test /data/web_static/shared

echo "This is a test" | sudo tee /data/web_static/../index.html
sudo ln -sf /data/web_static/../ /data/

sudo chown -R ubuntu:ubuntu /data/