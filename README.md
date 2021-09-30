# DevOps cloud

Repositório para desenvolver as atividades do módulo de cloud do treinamento DevOps.

## Realizando o deploy da VM

Para conseguir rodar o código desse repositório você deve instalar as dependências:
```
pip install -r requirements.txt
```
Você também deve realizar o download do arquivo openrc no horizon e executar o comando nele, da seguinte forma:
```
source arquivo-openrc.sh
```
Agora com as variáveis de ambiente já definidas e as dependências instaladas, basta executar o arquivo [main.py](https://github.com/Daviiap/openstack-deployment/blob/main/src/main.py).

## Usando um arquivo de configuração

Caso você deseje criar sua VM a partir de um arquivo de configurações, basta criar um arquivo .yml, seguindo a estrutura do arquivo [instance_example.yml](https://github.com/Daviiap/openstack-deployment/blob/main/instances/instance_example.yml) e especificar o caminho para o mesmo, quando for solicitado.

## Subindo o flickor para a cloud
Para subir a aplicação para a VM, basta executar o script [config.sh](https://github.com/Daviiap/openstack-deployment/blob/main/deploy/config.sh)
```
bash deploy/config.sh
```
<!-- ## Verificando o estado da aplicação

Para verificar se o servidor do flickor está online use o script [verifica_flickor.sh](https://git.lsd.ufcg.edu.br/caetano.albuquerque/devops-cloud/-/blob/master/Migrando_flickor/verifica_flickor.sh)

```
bash Migrando_flickor/verifica_flickor.sh [IP da VM]:5000
``` -->
