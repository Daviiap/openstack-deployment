#!/usr/bin/bash
# Para funcionar a chave deve estar no mesmo diretorio

echo "Insira o nome da sua chave:"
read key

echo "Insira o ip da maquina:"
read machine

echo "Insira o nome do usuario (gitlab):"
read username

echo "Insira sua senha (gitlab):"
read -s password

ssh -i $key $machine 'git clone https://'$username':'$password'@git.lsd.ufcg.edu.br/ignacio/flickr_clone.git && curl -fsSL https://get.docker.com -o get-docker.sh && sudo bash get-docker.sh && cd flickr_clone && git checkout docker && sudo docker build -t flickor . && sudo docker run --rm -p 5000:5000 flickor'
