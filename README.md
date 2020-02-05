## On server:

```
sudo apt-get update
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
sudo usermod -aG docker ubuntu
# Exit, relogin
git clone https://github.com/benwah/random.git
cd random
docker build .
```

Running:

docker run -p 8000:8000 --rm -i -t 315de90d1752 pyenv/bin/python3 benchy.py remote_server
