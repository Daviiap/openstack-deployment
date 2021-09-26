#!/usr/bin/bash
# Para funcionar a chave deve estar no mesmo diretorio

echo "Insira o nome da chave"
read key

echo "Insira a maquina"
read machine

echo "Insira o nome do usuario"
read username

echo "Insira a senha"
read -s password

ssh -i $key $machine 'git clone https://'$username':'$password'@git.lsd.ufcg.edu.br/ignacio/flickr_clone.git && cd flickr_clone && git checkout docker && sudo docker build -t flickor . && sudo docker run --rm -p 5000:5000 flickor'
