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

TO DO

## Instanciando em um ambiente de Cloud

TO DO

## Documentações

Neste repositório também existe uma documentação para cada uma das ferramentas utilizadas, tal como Docker ou MongoDB. Estas ferramentas estão em [Documentation](https://github.com/gorlando04/eCommercePANDAS/tree/main/Documentation) e contém informações sobre as ferramentas e como elas funcionam. Em cada documentação existe uma breve introdução prática sobre as ferramentas utilizadas contendo as principais informações necessárias para o entendimento. Além disso caso haja erro em nossa documentação uma [Issue](https://github.com/gorlando04/eCommercePANDAS/issues) pode ser criada para a correção ser realizada.

## Contribuições

TO DO
