# Descrição do Programa

O programa apresenta um **menu principal** com as seguintes opções de funcionalidades:

1. **Incluir**
2. **Listar**
3. **Excluir**
4. **Editar**

## Funcionamento

O programa executa todas as funções em um **loop contínuo**, até que o usuário insira uma **opção inválida** (um número maior do que o total de opções disponíveis). 

### Processamento de Dados

- Para cada ação solicitada, os dados são:
  1. **Lidos** do arquivo JSON correspondente.
  2. **Manipulados** conforme a operação escolhida (Incluir, Listar, Excluir ou Editar).
  3. **Salvos** de volta no arquivo JSON.

### Garantia de Integridade

O programa mantém a integridade dos dados com a verificação prévia se um **item já existe** antes de ser adicionado (no caso da opção **Incluir**). 

### Tratamento de Exceções

O programa também implementa o **tratamento de exceções** para lidar com entradas inválidas e garantir que ele **não quebre** durante a execução, proporcionando uma experiência de uso mais robusta e estável.
