# eCommercePANDAS

Bem-vindo ao repositório de previsão de vendas! Este projeto tem como objetivo fornecer uma solução robusta para a previsão de vendas de lojas, utilizando técnicas avançadas de regressão. Se você está buscando aprimorar suas estratégias de negócios, identificar padrões sazonais ou simplesmente otimizar o desempenho de suas lojas, este é o lugar certo.

## **Funcionalidades Principais**

- **Modelos de Regressão**: Implementações de modelos de regressão avançados para previsão de vendas focando em Séries temporais
- **Análise de Desempenho**: Métricas detalhadas para avaliação do desempenho dos modelos, permitindo que você escolha a abordagem que melhor se adapte aos seus requisitos específicos.
- **Informações Essenciais**: Fornece insights úteis, como máximos de vendas alcançados e médias de vendas por loja, para que você possa tomar decisões informadas e estratégicas.

## Dependências

É necessário que a ferramenta docker seja instalada no ambiente que será utilizado. Para isso é possível verificar o arquivo [Docker-Doc](https://github.com/gorlando04/eCommercePANDAS/tree/main/Documentation/Docker) para verificar como a instalação da ferramenta deve ser feita.


## **Como Começar**

1. **Clone o Repositório**: Comece clonando este repositório em sua máquina local.
    
    ```bash
    git clone https://github.com/gorlando04/eCommercePANDAS.git
    ```
    
2. ****************************************Configure o ambiente****************************************: Crie o container que será utilizado
    
    ```bash
    docker run  --name PANDAS_REG_LIN --rm -it -v $HOME/Desktop/eCommercePANDAS:/PANDAS -w /PANDAS --shm-size=1g --ulimit memlock=-1 -p 8888:8888 ubuntu
    ```
    
3. **Instale as Dependências**: Certifique-se de ter as dependências necessárias instaladas. Utilize o seguinte comando para instalar as bibliotecas Python necessárias:

```jsx
./init.sh
```

1. ************************************Inicie o sistema:************************************ Execute o arquivo que permite a realização de consultas e previsões de vendas

```jsx
python3 start.py
```

## Como fazer consultas

No seguinte link, é possível visualizar uma breve demonstração de como funciona nosso sistema: https://drive.google.com/file/d/1P2VVAOu1uaim3O5v6c6sRcJwr9EVh9vn/view?usp=sharing


Inicialmente é necessário acessar o seguinte link: t.me/gabinho_bot

Após acessar o link é necessário se conectar a sua conta no telegram para poder interagir com o sistema.

Os prints abaixo mostram como deve ser realizadas as buscas:

![Screenshot from 2024-01-29 19-19-44](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/458fb9f6-429c-428c-b797-7bf2a86d00e9)


![Screenshot from 2024-01-29 19-20-08](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/cb237dc4-701e-464e-b36b-14d5ff03e1a5)

![Screenshot from 2024-01-29 19-20-21](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/8dcc76b6-6d40-4faf-be94-756ba0b5fe9a)


![Screenshot from 2024-01-29 19-20-38](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/0849964e-fb54-4a6f-bf58-0911ecf2d7f3)


![Screenshot from 2024-01-29 19-20-47](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/ce837c45-aa66-474b-a94b-2e9fc37950cf)


![Screenshot from 2024-01-29 19-21-02](https://github.com/gorlando04/eCommercePANDAS/assets/91696970/3c511a31-692a-413c-9aaf-c9433406beb3)




## Instanciando em um ambiente de Cloud

Este projeto também está configurado para funcionar em um ambiente de nuvem, utilizando os serviços disponibilizados pela Oracle, que felizmente oferece um serviço gratuito de qualidade e que permite que uma máquina virtual seja instanciada. Como a configuração deste ambiente é um pouco mais extensa que a configuração via docker, será disponbilizado um arquivo ( [Doc-Cloud](https://github.com/gorlando04/eCommercePANDAS/blob/main/Documentation/Cloud/README.md) ) que contém os passos que devem ser seguidos para instanciar a máquina virtual


## Documentações

Neste repositório também existe uma documentação para cada uma das ferramentas utilizadas, tal como Docker ou MongoDB. Estas ferramentas estão em [Documentation](https://github.com/gorlando04/eCommercePANDAS/tree/main/Documentation) e contém informações sobre as ferramentas e como elas funcionam. Em cada documentação existe uma breve introdução prática sobre as ferramentas utilizadas contendo as principais informações necessárias para o entendimento. Além disso caso haja erro em nossa documentação uma [Issue](https://github.com/gorlando04/eCommercePANDAS/issues) pode ser criada para a correção ser realizada.

## Contribuições

TO DO
