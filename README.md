# GS2024-PYTHON
GLOBAL SOLUTION 1º Semestre 2024 de Python
<h1>Projeto de Monitoramento de Qualidade da Água</h1>

<h1>Vídeo:</h1>
https://youtu.be/srrtl1I8-tY



<table>
  <tr>
    <th> Nome </th>
    <th> RM </th>
  </tr>
  <tr>
    <td> Gabriel Belo </td>
    <td> 551669 </td>
  </tr>
  <tr>
    <td>Gustavo Pierre</td>
    <td>558928</td>
  </tr>
  <td> Gabriel Galerani </td>
  <td> 557421 </td>
</table>


Descrição do Projeto

Este projeto consiste em um sistema de monitoramento de qualidade da água, que verifica os níveis de temperatura, pH e oxigênio dissolvido em amostras de água. Utilizando dados aleatórios gerados para simular leituras de sensores, o sistema verifica se esses dados estão dentro dos limites aceitáveis e gera alertas caso algum valor esteja fora dos parâmetros estabelecidos. Além disso, gráficos são gerados para visualizar as tendências dos dados coletados.

 Instruções de Uso

1. Clone o repositório:
   sh
   git clone [URL do repositório]
   cd [diretório do projeto]
   

2. Instale as dependências:
   Certifique-se de ter o Python instalado. Utilize o pip para instalar o Matplotlib, caso ainda não esteja instalado:
   sh
   'pip install matplotlib'
   

3. Execute o script:
   Para rodar o projeto, execute o seguinte comando no terminal:
   sh
   'python monitoramento_agua.py'
   

4. Visualize os resultados:
   - O script verificará os limites das leituras de temperatura, pH e oxigênio dissolvido, e exibirá quaisquer alertas gerados.
   - Gráficos serão exibidos mostrando as leituras das variáveis monitoradas.

Requisitos

- Python 3.6+
- Biblioteca Matplotlib

 Dependências

- Matplotlib: Biblioteca utilizada para a geração de gráficos. Instale com o comando:
  sh
  'pip install matplotlib'
  

Detalhes do Código

- Geração de Dados: Dados aleatórios para temperatura, pH e oxigênio são gerados para simular leituras de sensores.
- Verificação de Limites: Função que verifica se os dados estão dentro dos limites aceitáveis e gera alertas.
- Exibição de Alertas: Função que exibe os alertas gerados, caso existam.
- Plotagem de Gráficos: Função que gera gráficos para visualizar as tendências das variáveis monitoradas.

 Informações Adicionais

Este projeto foi desenvolvido como uma demonstração de um sistema básico de monitoramento de qualidade da água, utilizando Python e bibliotecas padrão para gerar e visualizar dados. Ele pode ser expandido para incorporar leitura de dados reais de sensores e integrar com sistemas de alerta mais avançados.
