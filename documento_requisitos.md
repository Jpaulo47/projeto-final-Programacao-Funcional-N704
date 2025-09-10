# Documento de Requisitos - Sistema de Gerenciamento de Tarefas

## Informações do Projeto

**Nome do Projeto:** Sistema Simplificado de Gerenciamento de Tarefas  
**Linguagem:** Python  
**Paradigma:** Programação Funcional  
**Data:** 2024  
**Versão:** 1.0  

## Equipe de Desenvolvimento

| Nome | Matrícula | Papel |
|------|-----------|-------|
| [João paulo da silva rodrigues] | [2319025] | Desenvolvedor Principal |
| [José William Alves de Oliveira] | [2326237] | Documentação |
| [Francisco Wanderson da Silva] | [2323860] | Testes |
| [Rayane dos Santos Silva] | [2326292] | Análise de Requisitos |
| [Nome do Integrante 5] | [Matrícula] | Gerente de Projeto |
| [Nome do Integrante 6] | [Matrícula] | Revisor de Código |

## 1. Requisitos Funcionais (RF)

| ID | Descrição |
|----|-----------|
| RF01 | O sistema deve permitir cadastrar uma nova tarefa com descrição |
| RF02 | O sistema deve permitir listar todas as tarefas cadastradas |
| RF03 | O sistema deve permitir filtrar tarefas por status (concluídas/pendentes) |
| RF04 | O sistema deve permitir marcar uma tarefa como concluída |
| RF05 | O sistema deve exibir um resumo com estatísticas das tarefas |
| RF06 | O sistema deve fornecer uma interface de menu para interação com o usuário |
| RF07 | O sistema deve permitir visualizar apenas tarefas pendentes |
| RF08 | O sistema deve permitir visualizar apenas tarefas concluídas |

## 2. Requisitos Não Funcionais (RNF)

| ID | Descrição |
|----|-----------|
| RNF01 | O sistema deve ser desenvolvido em linguagem Python |
| RNF02 | O sistema deve garantir a execução sem erros |
| RNF03 | O sistema deve implementar conceitos de programação funcional |
| RNF04 | O sistema deve ter código bem documentado e comentado |
| RNF05 | O sistema deve ser executável em ambiente Python 3.x |
| RNF06 | O sistema deve manter dados em memória durante a execução |
| RNF07 | O sistema deve fornecer feedback adequado ao usuário |
| RNF08 | O sistema deve ter interface de linha de comando |

## 3. Mapeamento de Requisitos para o Código

| Requisito | Função(ões) no Código |
|-----------|----------------------|
| RF01 | `adicionar_tarefa(descricao)` |
| RF02 | `listar_tarefas()`, `exibir_tarefas()` |
| RF03 | `filtrar_tarefas_por_status(status)` |
| RF04 | `marcar_concluida(tarefa_id)` |
| RF05 | `obter_resumo_tarefas()`, `exibir_resumo()` |
| RF06 | `menu_principal()` |
| RF07 | `filtrar_tarefas_por_status(False)` |
| RF08 | `filtrar_tarefas_por_status(True)` |
| RNF01 | Todo o código-fonte em Python |
| RNF02 | Validações e tratamento de erros em todas as funções |
| RNF03 | `operar_sobre_tarefas()`, `criar_filtro_por_status()`, funções lambda, list comprehensions |
| RNF04 | Comentários e docstrings em todas as funções |
| RNF05 | Compatibilidade com Python 3.x garantida |
| RNF06 | Lista global `tarefas` para armazenamento |
| RNF07 | Mensagens de feedback em todas as operações |
| RNF08 | Interface de menu implementada em `menu_principal()` |

## 4. Identificação dos Conceitos de Programação Funcional

### 4.1 Função de Alta Ordem
**Localização:** Linha 67-78 em `operar_sobre_tarefas(lista_tarefas, operacao)`

**Justificativa:** A função `operar_sobre_tarefas` é uma função de alta ordem porque recebe outra função (`operacao`) como parâmetro e a aplica sobre uma lista de tarefas. Isso permite flexibilidade na manipulação de dados, seguindo o princípio de que funções podem ser tratadas como valores de primeira classe.

**Uso no código:**
```python
def operar_sobre_tarefas(lista_tarefas, operacao):
    return [operacao(tarefa) for tarefa in lista_tarefas]
```

### 4.2 Função Lambda
**Localização:** Linha 95 em `filtrar_tarefas_por_status(status)`

**Justificativa:** A função lambda é utilizada em conjunto com a função `filter()` para aplicar o filtro criado pela closure. A expressão lambda `lambda tarefa: filtro(tarefa)` é uma função anônima que aplica o filtro sobre cada tarefa.

**Uso no código:**
```python
return list(filter(lambda tarefa: filtro(tarefa), tarefas))
```

### 4.3 List Comprehension
**Localização:** Linha 102-108 em `obter_descricoes_tarefas_pendentes()`

**Justificativa:** A list comprehension é utilizada para transformar e filtrar dados de forma concisa e funcional. A expressão `[tarefa['descricao'] for tarefa in tarefas if not tarefa['concluida']]` cria uma nova lista contendo apenas as descrições das tarefas pendentes.

**Uso no código:**
```python
return [tarefa['descricao'] for tarefa in tarefas if not tarefa['concluida']]
```

### 4.4 Closure
**Localização:** Linha 80-90 em `criar_filtro_por_status(status_desejado)`

**Justificativa:** A função `criar_filtro_por_status` é uma closure porque retorna uma função interna (`filtro_interno`) que captura e "lembra" a variável `status_desejado` do escopo da função externa, mesmo após a função externa ter terminado sua execução.

**Uso no código:**
```python
def criar_filtro_por_status(status_desejado):
    def filtro_interno(tarefa):
        return tarefa['concluida'] == status_desejado
    return filtro_interno
```

## 5. Casos de Teste

| Caso de Teste | Ação | Resultado Esperado | Resultado Obtido |
|---------------|------|-------------------|------------------|
| CT01 | Adicionar a tarefa "Comprar pão" | A lista de tarefas deve conter um item com a descrição "Comprar pão" e status "pendente" | ✓ Aprovado |
| CT02 | Listar todas as tarefas | Deve exibir todas as tarefas cadastradas com ID, status e descrição | ✓ Aprovado |
| CT03 | Filtrar tarefas pendentes | Deve retornar apenas tarefas com status "concluida": false | ✓ Aprovado |
| CT04 | Filtrar tarefas concluídas | Deve retornar apenas tarefas com status "concluida": true | ✓ Aprovado |
| CT05 | Marcar tarefa ID 1 como concluída | A tarefa com ID 1 deve ter status alterado para "concluida": true | ✓ Aprovado |
| CT06 | Marcar tarefa inexistente | Deve retornar False e exibir mensagem de erro | ✓ Aprovado |
| CT07 | Exibir resumo das tarefas | Deve mostrar total, concluídas, pendentes e percentual | ✓ Aprovado |
| CT08 | Obter descrições de tarefas pendentes | Deve retornar lista com apenas descrições das tarefas pendentes | ✓ Aprovado |
| CT09 | Aplicar transformação sobre tarefas | Deve aplicar função de transformação sobre todas as tarefas | ✓ Aprovado |
| CT10 | Usar closure para filtrar por status | Deve criar e usar filtro específico para status desejado | ✓ Aprovado |

## 6. Estrutura do Sistema

### 6.1 Arquivos do Projeto
- `sistema_tarefas.py` - Código-fonte principal
- `documento_requisitos.md` - Este documento
- `checklist_projeto.md` - Checklist de desenvolvimento

### 6.2 Dependências
- Python 3.x
- Nenhuma biblioteca externa necessária

### 6.3 Como Executar
```bash
python sistema_tarefas.py
```

## 7. Declaração de Uso de Inteligência Artificial

A equipe utilizou uma ferramenta de IA generativa para auxiliar em diferentes etapas do desenvolvimento do projeto, conforme detalhado abaixo. A regra da atividade que exige a documentação de como o chatbot foi utilizado e quais foram suas respostas foi seguida.

### 7.1 Refinamento de Código para um Estilo Funcional

Foi solicitado à IA uma alternativa mais funcional para a função `marcar_concluida`, que originalmente modificava a lista de tarefas diretamente.

* **Prompt utilizado:**
    > "Tenho esta função em Python que modifica um item de uma lista. Como posso reescrevê-la de uma forma mais funcional, evitando modificar a lista original diretamente e, em vez disso, retornando uma nova lista com os dados atualizados?"
    > ```python
    > # Código original enviado
    > def marcar_concluida(tarefa_id):
    >     for tarefa in tarefas:
    >         if tarefa['id'] == tarefa_id:
    >             tarefa['concluida'] = True
    >             return True
    >     return False
    > ```

* **Resposta da IA:**
    > Para seguir uma abordagem funcional, você deve evitar mutações de estado. A melhor forma de fazer isso é gerar uma nova lista baseada na original, aplicando a alteração desejada. Uma *list comprehension* é ideal para isso.
    >
    > Aqui está uma sugestão:
    > ```python
    > # Sugestão da IA
    > def marcar_concluida_funcional(lista_de_tarefas, tarefa_id):
    >     return [
    >         {**tarefa, 'concluida': True} if tarefa['id'] == tarefa_id else tarefa
    >         for tarefa in lista_de_tarefas
    >     ]
    > ```
    > Esta nova função é "pura", pois não tem efeitos colaterais: ela recebe uma lista e um ID, e retorna uma lista completamente nova, sem modificar a original.

### 7.2 Prevenção de Erros (Error Handling)

A equipe consultou a IA para tornar a função de resumo mais robusta, prevenindo um possível erro de divisão por zero.

* **Prompt utilizado:**
    > "Na minha função `obter_resumo_tarefas`, estou calculando o percentual de tarefas concluídas com a linha: `percentual = (tarefas_concluidas / total_tarefas) * 100`. O que acontece se a lista de tarefas estiver vazia e `total_tarefas` for zero? Como posso evitar um erro?"

* **Resposta da IA:**
    > Se `total_tarefas` for zero, sua linha de código irá gerar um erro do tipo `ZeroDivisionError`. Para evitar isso de forma elegante, você pode usar uma expressão condicional.
    >
    > A linha ficaria assim:
    > ```python
    > # Sugestão da IA
    > 'percentual_concluido': (tarefas_concluidas / total_tarefas * 100) if total_tarefas > 0 else 0
    > ```
    > Essa abordagem é concisa, legível e garante que seu programa não falhe caso a lista de tarefas esteja vazia.

### 7.3 Geração de Explicação Técnica para a Documentação

Foi solicitado à IA que gerasse uma justificativa clara para o uso de *closure* no projeto, para ser usada na documentação.

* **Prompt utilizado:**
    > "Meu código tem esta função:
    > ```python
    > def criar_filtro_por_status(status_desejado):
    >     def filtro_interno(tarefa):
    >         return tarefa['concluida'] == status_desejado
    >     return filtro_interno
    > ```
    > Por favor, gere uma justificativa técnica e clara para o meu documento, explicando por que essa função é um exemplo de *closure*."

* **Resposta da IA:**
    > Claro. Aqui está uma justificativa que você pode usar:
    >
    > A função `criar_filtro_por_status` é um exemplo clássico de *closure*. Uma *closure* ocorre quando uma função aninhada (`filtro_interno`) captura e "lembra" o valor de variáveis do escopo da função que a contém (`criar_filtro_por_status`), mesmo após a função externa ter concluído sua execução.
    >
    > O objeto retornado é a *closure*: uma função (`filtro_interno`) junto com seu ambiente capturado (a variável `status_desejado`). Isso permite criar "fábricas de funções" altamente especializadas.