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



## remote server:

```
ssh -i poo.pem ubuntu@3.95.249.36
tmux
ulimit -S -n 100000
docker run -p 8000:8000 --rm -i -t 072570841742 pyenv/bin/python3 benchy.py remote_server --help
```

## ruby test

```
ssh -i poo.pem ubuntu@54.198.239.123
tmux
docker run -p 8000:8000 --rm -i -t 6c90fff1d550 pyenv/bin/python3 benchy.py test_01_ruby_puma --host 0.0.0.0 --port 8000 --workers 1 --threads 2 --target-uri http://3.95.249.36:8000/
# new tmux window
dstat -C 0,1,total -d -g -i -l -m -n -p -r -T -y --aio --fs --ipc --lock --raw --socket --unix
```

## bench it

```
ulimit -S -n 100000
ssh -i poo.pem ubuntu@54.166.157.52

```
