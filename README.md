# Sistema de Gerenciamento de Tarefas

Um sistema simples e funcional para gerenciar tarefas, desenvolvido em Python seguindo o paradigma de **Programação Funcional**.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como atividade acadêmica para demonstrar a aplicação prática dos conceitos de programação funcional em Python. O sistema permite adicionar, visualizar, filtrar e gerenciar tarefas de forma intuitiva através de uma interface de linha de comando.

## 🚀 Funcionalidades

- ✅ **Adicionar tarefas** - Cadastrar novas tarefas com descrição
- 📋 **Listar tarefas** - Visualizar todas as tarefas cadastradas
- 🔍 **Filtrar tarefas** - Separar tarefas por status (concluídas/pendentes)
- ✔️ **Marcar como concluída** - Alterar status das tarefas
- 📊 **Resumo estatístico** - Visualizar estatísticas das tarefas
- 🎯 **Interface amigável** - Menu interativo e intuitivo

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação
- **Paradigma Funcional** - Conceitos de programação funcional
- **Sem dependências externas** - Apenas bibliotecas padrão do Python

## 📁 Estrutura do Projeto

```
📦 Sistema de Gerenciamento de Tarefas
├── 📄 sistema_tarefas.py          # Código-fonte principal
├── 📄 documento_requisitos.md     # Documentação de requisitos
└── 📄 README.md                   # Este arquivo
```

## 🏃‍♂️ Como Executar

### Pré-requisitos
- Python 3.x instalado no sistema
- Terminal ou prompt de comando

### Execução
```bash
# Clone ou baixe o projeto
# Navegue até a pasta do projeto
cd "caminho/para/o/projeto"

# Execute o sistema
python sistema_tarefas.py
```

### Exemplo de Uso
```
========================================
SISTEMA DE GERENCIAMENTO DE TAREFAS
========================================
1. Adicionar tarefa
2. Listar todas as tarefas
3. Listar tarefas pendentes
4. Listar tarefas concluídas
5. Marcar tarefa como concluída
6. Exibir resumo
7. Sair
========================================
Escolha uma opção: 1
Digite a descrição da tarefa: Estudar Python
Tarefa 'Estudar Python' adicionada com sucesso!
```

## 🧩 Conceitos de Programação Funcional

O projeto demonstra a aplicação prática de quatro conceitos fundamentais da programação funcional:

### 1. 🔄 Função de Alta Ordem
**O que é:** Função que recebe outra função como parâmetro ou retorna uma função.

**No código:**
```python
def operar_sobre_tarefas(lista_tarefas, operacao):
    """
    Aplica uma operação sobre cada tarefa da lista
    """
    return [operacao(tarefa) for tarefa in lista_tarefas]
```

**Por que é útil:** Permite criar funções genéricas que podem ser reutilizadas com diferentes operações.

### 2. ⚡ Função Lambda
**O que é:** Função anônima (sem nome) definida inline.

**No código:**
```python
# Filtra tarefas usando lambda
return list(filter(lambda tarefa: filtro(tarefa), tarefas))
```

**Por que é útil:** Permite criar funções simples de forma concisa, sem precisar definir uma função separada.

### 3. 📝 List Comprehension
**O que é:** Forma concisa de criar listas baseadas em outras listas.

**No código:**
```python
def obter_descricoes_tarefas_pendentes():
    """
    Extrai apenas as descrições das tarefas pendentes
    """
    return [tarefa['descricao'] for tarefa in tarefas if not tarefa['concluida']]
```

**Por que é útil:** Substitui loops tradicionais por uma sintaxe mais limpa e funcional.

### 4. 🔒 Closure
**O que é:** Função que "lembra" variáveis do escopo onde foi criada.

**No código:**
```python
def criar_filtro_por_status(status_desejado):
    """
    Cria uma função de filtro específica para um status
    """
    def filtro_interno(tarefa):
        return tarefa['concluida'] == status_desejado
    return filtro_interno
```

**Por que é útil:** Permite criar "fábricas de funções" especializadas.

## 🏗️ Estrutura do Código

### Organização das Funções

```python
# =============================================================================
# FUNCIONALIDADES BÁSICAS
# =============================================================================
def adicionar_tarefa(descricao)      # Adiciona nova tarefa
def listar_tarefas()                 # Lista todas as tarefas
def marcar_concluida(tarefa_id)      # Marca tarefa como concluída

# =============================================================================
# CONCEITOS DE PROGRAMAÇÃO FUNCIONAL
# =============================================================================
def operar_sobre_tarefas(...)        # Função de alta ordem
def criar_filtro_por_status(...)     # Closure
def filtrar_tarefas_por_status(...)  # Usa lambda
def obter_descricoes_tarefas_pendentes()  # List comprehension

# =============================================================================
# INTERFACE E APRESENTAÇÃO
# =============================================================================
def exibir_tarefas(...)              # Exibe tarefas formatadas
def exibir_resumo()                  # Mostra estatísticas
def menu_principal()                 # Menu interativo
```

### Estrutura de Dados

```python
# Cada tarefa é representada por um dicionário:
tarefa = {
    'id': 1,                          # Identificador único
    'descricao': 'Estudar Python',    # Descrição da tarefa
    'concluida': False                # Status (True/False)
}
```

## 🧪 Casos de Teste

O sistema foi testado com 10 casos de teste abrangentes:

| Teste | Descrição | Status |
|-------|-----------|--------|
| CT01 | Adicionar tarefa | ✅ Aprovado |
| CT02 | Listar todas as tarefas | ✅ Aprovado |
| CT03 | Filtrar tarefas pendentes | ✅ Aprovado |
| CT04 | Filtrar tarefas concluídas | ✅ Aprovado |
| CT05 | Marcar tarefa como concluída | ✅ Aprovado |
| CT06 | Marcar tarefa inexistente | ✅ Aprovado |
| CT07 | Exibir resumo das tarefas | ✅ Aprovado |
| CT08 | Obter descrições pendentes | ✅ Aprovado |
| CT09 | Aplicar transformação | ✅ Aprovado |
| CT10 | Usar closure para filtrar | ✅ Aprovado |

## 📊 Exemplo de Saída

```
==================================================
LISTA DE TAREFAS
==================================================
ID: 1 | ✓ CONCLUÍDA | Estudar programação funcional
ID: 2 | ○ PENDENTE | Fazer exercícios de Python
ID: 3 | ○ PENDENTE | Revisar conceitos de closure
==================================================

==============================
RESUMO DAS TAREFAS
==============================
Total de tarefas: 3
Concluídas: 1
Pendentes: 2
Percentual concluído: 33.3%
==============================
```

## 🎯 Objetivos de Aprendizado

Este projeto demonstra:

1. **Aplicação prática** dos conceitos de programação funcional
2. **Organização de código** em funções especializadas
3. **Tratamento de dados** de forma funcional
4. **Interface de usuário** simples e eficaz
5. **Documentação completa** de requisitos e funcionalidades

## 👥 Equipe de Desenvolvimento

| Nome | Matrícula | Papel |
|------|-----------|-------|
| [João paulo da silva rodrigues] | [2319025] | Desenvolvedor Principal |
| [José William Alves de Oliveira] | [2326237] | Documentação |
| [Francisco Wanderson da Silva] | [2323860] | Testes |
| [Rayane dos Santos Silva] | [2326292] | Análise de Requisitos |
| [Kamilly Almeida Braz] | [2323788] | Gerente de Projeto |
| [Matheus de Lima Silva] | [2323842] | Revisor de Código |

## 📚 Documentação Adicional

- **[Documento de Requisitos](documento_requisitos.md)** - Especificações completas do projeto

## 📝 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte de uma atividade de Programação Funcional.

