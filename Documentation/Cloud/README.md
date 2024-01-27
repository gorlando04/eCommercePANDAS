# **Documentação do Ambiente de Cloud**

## **Introdução**

Bem-vindo à documentação abrangente sobre a configuração de um ambiente de Cloud da Oracle. Este guia foi elaborado para auxiliar tanto iniciantes quanto profissionais experientes na implementação bem-sucedida de um ambiente na nuvem da Oracle. A Oracle Cloud oferece uma ampla gama de serviços e soluções robustas para atender às necessidades diversificadas de negócios, desde infraestrutura como serviço (IaaS) até software como serviço (SaaS).

Ao longo deste documento, exploraremos passo a passo os principais aspectos da configuração do ambiente na Oracle Cloud, desde a criação de uma conta e provisionamento de recursos até a implementação de melhores práticas de segurança e escalabilidade. Independentemente de você estar buscando migrar sua infraestrutura existente, desenvolver e implantar aplicativos nativos na nuvem, ou explorar soluções específicas da Oracle, este guia fornecerá orientações detalhadas para otimizar sua experiência na nuvem.

## Ambiente da Oracle 

A Oracle oferece diversas máquinas gratuítas para os seus usuários usarem, com as seguintes configurações.


Máquinas Virtuais AMD:

2 Máquinas Virtuais baseadas em AMD.
Cada VM possui 1/8 de OCPU** e 1 GB de memória.
Máquinas Virtuais Arm-based Ampere A1:

4 núcleos baseados em Arm-based Ampere A1, totalizando 24 GB de memória.
Esses recursos podem ser utilizados como uma única VM ou distribuídos entre até 4 VMs.
Armazenamento de Bloco (Block Volumes):

2 volumes de bloco com um total de 200 GB de armazenamento.
Armazenamento de Objeto (Object Storage):

10 GB de Armazenamento de Objeto — Standard.
10 GB de Armazenamento de Objeto — Infrequent Access.
10 GB de Armazenamento de Arquivo Morto (Archive Storage).
Resource Manager:

Ambiente de Terraform gerenciado pelo Resource Manager.
OCI Bastions:

5 Bastiões (Bastions) para acesso seguro e gerenciamento remoto.


## **Criando uma instância na nuvem**

Antes de iniciar, é extremamente necessário criar uma conta na plataforma online da Oracle para ter acesso à todos os recursos que elas promovem. Para isso basta acessar o [link](https://signup.cloud.oracle.com/?sourceType=:ex:pev:::::RC_WWMK211213P00038:K8s_on_arm&SC=:ex:pev:::::RC_WWMK211213P00038:K8s_on_arm&pcode=WWMK211213P00038) e preencher com as suas informações para criar uma conta na plataforma.

Após isso, é necessário instalar o [OCI Command Line Interface (CLI)](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm).

Finalmente, é necessário realizar a autenticação da sua máquina virtual, utilizando os seguinte [tutorial](https://developer.hashicorp.com/terraform/tutorials/oci-get-started/oci-build?in=terraform%2Foci-get-started).

Após realizar todas essas instalações/autenticações, podemos iniciar o processo de instanciar uma máquina virtual, e para isso será necessário uma chave SSH pessoal para ser utilizada como mecanismo de acesso, e com tudo isso reunido, as imagens abaixo, demonstram o processo de criação.


Inicialmente, clique no MENU, e selecione a aba **Compute**

![Screenshot from 2024-01-27 16-34-33](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/9ea4e730-626c-42c0-b25b-1fdec8ae00ab)


Após isso, selecione a aba **Instances**

![Screenshot from 2024-01-27 16-34-38](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/a8b0863c-adef-4de7-a593-1046c7df5c6a)


Como, a instância já havia sido previamente criada, ela já estava presente, mas para criar uma nova clique em **Create Instance**

![Screenshot from 2024-01-27 16-35-00](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/2c958a5c-ae91-47b2-afe4-d3d1f7b70e79)


Nas duas imagens abaixo, nos modificamos a imagem base da nossa instância, para selecionar a versão do Ubuntu 20.04 e também nos melhoramos a máquina que nossa instância irá funcionar para não termos problemas com memória e nem processamento.

![Screenshot from 2024-01-27 16-36-15](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/171bf721-dd18-4594-b467-4768ff961925)

![Screenshot from 2024-01-27 16-36-33](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/dcc90965-2a92-4e58-9088-1b5759cb2ef1)


![Screenshot from 2024-01-27 16-37-23](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/5f76cd42-a605-4e1e-8643-8ab5d0e3111f)


Finalmente é necessário adicionar o arquivo id_rsa.pub que é gerado junto a sua chave ssh, mas é utilizada para ser enviada e permitir a autenticação.

![Screenshot from 2024-01-27 16-37-50](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/50690e70-01b6-40bc-8dc7-278943139039)

Após criar a instância a tela abaixo irá aparecer, e para conectar na máquina virtual é um processo muito simples, em que é necessário apenas digitar ssh@<IP_PUBLICO>, tal que o IP público estará no local em que se encontra o risco preto.



![WhatsApp Image 2024-01-27 at 4 48 43 PM](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/72717dfb-60c7-4f83-988a-c6012917ccac)


Após isso é necessário puxar o repositório do git para a máquina virtual, com o comando:

```
git clone https://github.com/gorlando04/eCommercePANDAS.git
```
Em seguida, instalar o docker na máquina virtual. Para isso basta apenas digitar:

```
sudo su

```
Para entrar no modo root, e após isso executar o seguinte arquivo:

```
#!/bin/sh

set -ex

sudo apt-get update -y
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

usermod -aG docker ubuntu
```
Após isso, basta apenas digitar o comando abaixo, para instanciar um container do docker, para manter o padrão.

```
docker run  --name PANDAS_REG_LIN --rm -it -v $HOME/eCommercePANDAS:/PANDAS -w /PANDAS --shm-size=1g --ulimit memlock=-1 -p 8888:8888 ubuntu

```

E desta maneira, basta apenas seguir os comandos utilizados no README.md principal deste repositório para conseguir fazer o sistema funcionar.

