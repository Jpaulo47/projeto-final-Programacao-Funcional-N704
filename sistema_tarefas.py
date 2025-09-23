#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Lista global para armazenar as tarefas
tarefas = []

def adicionar_tarefa(descricao):
    """
    Adiciona uma nova tarefa ao sistema.
    
    Args:
        descricao (str): Descrição da tarefa
        
    Returns:
        dict: Tarefa criada
    """
    nova_tarefa = {
        'id': len(tarefas) + 1,
        'descricao': descricao,
        'concluida': False
    }
    tarefas.append(nova_tarefa)
    return nova_tarefa

def listar_tarefas():
    """
    Lista todas as tarefas cadastradas.
    
    Returns:
        list: Lista de todas as tarefas
    """
    return tarefas.copy()

def marcar_concluida(tarefa_id):
    """
    Marca uma tarefa como concluída.
    
    Args:
        tarefa_id (int): ID da tarefa
        
    Returns:
        bool: True se a tarefa foi encontrada e marcada, False caso contrário
    """
    for tarefa in tarefas:
        if tarefa['id'] == tarefa_id:
            tarefa['concluida'] = True
            return True
    return False

# =============================================================================
# CONCEITOS DE PROGRAMAÇÃO FUNCIONAL
# =============================================================================

def operar_sobre_tarefas(lista_tarefas, operacao):
    """
    FUNÇÃO DE ALTA ORDEM: Recebe uma função como parâmetro e a aplica sobre uma lista de tarefas.
    
    Args:
        lista_tarefas (list): Lista de tarefas
        operacao (function): Função a ser aplicada sobre cada tarefa
        
    Returns:
        list: Lista resultante da aplicação da operação
    """
    return [operacao(tarefa) for tarefa in lista_tarefas]

def criar_filtro_por_status(status_desejado):
    """
    CLOSURE: Função que retorna uma função interna que captura a variável status_desejado.
    
    Args:
        status_desejado (bool): Status desejado (True para concluídas, False para pendentes)
        
    Returns:
        function: Função interna que filtra tarefas pelo status
    """
    def filtro_interno(tarefa):
        return tarefa['concluida'] == status_desejado
    return filtro_interno

def filtrar_tarefas_por_status(status):
    """
    Filtra tarefas por status usando closure e função lambda.
    
    Args:
        status (bool): True para concluídas, False para pendentes
        
    Returns:
        list: Lista de tarefas filtradas
    """
    # Usando closure para criar o filtro
    filtro = criar_filtro_por_status(status)
    
    # FUNÇÃO LAMBDA: Usada em conjunto com filter para aplicar o filtro
    return list(filter(lambda tarefa: filtro(tarefa), tarefas))

def obter_descricoes_tarefas_pendentes():
    """
    LIST COMPREHENSION: Extrai apenas as descrições das tarefas pendentes.
    
    Returns:
        list: Lista de descrições das tarefas pendentes
    """
    # List comprehension para transformar e filtrar dados
    return [tarefa['descricao'] for tarefa in tarefas if not tarefa['concluida']]

def aplicar_transformacao_tarefas(transformacao):
    """
    Aplica uma transformação sobre todas as tarefas usando função de alta ordem.
    
    Args:
        transformacao (function): Função de transformação
        
    Returns:
        list: Lista de tarefas transformadas
    """
    return operar_sobre_tarefas(tarefas, transformacao)

def obter_resumo_tarefas():
    """
    Gera um resumo das tarefas usando múltiplos conceitos funcionais.
    
    Returns:
        dict: Resumo com estatísticas das tarefas
    """
    # Usando list comprehension para contar tarefas por status
    total_tarefas = len(tarefas)
    tarefas_concluidas = len([t for t in tarefas if t['concluida']])
    tarefas_pendentes = total_tarefas - tarefas_concluidas
    
    return {
        'total': total_tarefas,
        'concluidas': tarefas_concluidas,
        'pendentes': tarefas_pendentes,
        'percentual_concluido': (tarefas_concluidas / total_tarefas * 100) if total_tarefas > 0 else 0
    }

# =============================================================================
# FUNÇÕES DE INTERFACE
# =============================================================================

def exibir_tarefas(lista_tarefas=None):
    """
    Exibe as tarefas de forma formatada.
    
    Args:
        lista_tarefas (list, optional): Lista específica de tarefas. Se None, exibe todas.
    """
    if lista_tarefas is None:
        lista_tarefas = tarefas
    
    if not lista_tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    print("\n" + "="*50)
    print("LISTA DE TAREFAS")
    print("="*50)
    
    for tarefa in lista_tarefas:
        status = "✓ CONCLUÍDA" if tarefa['concluida'] else "○ PENDENTE"
        print(f"ID: {tarefa['id']} | {status} | {tarefa['descricao']}")
    
    print("="*50)

def exibir_resumo():
    """
    Exibe um resumo das tarefas.
    """
    resumo = obter_resumo_tarefas()
    print("\n" + "="*30)
    print("RESUMO DAS TAREFAS")
    print("="*30)
    print(f"Total de tarefas: {resumo['total']}")
    print(f"Concluídas: {resumo['concluidas']}")
    print(f"Pendentes: {resumo['pendentes']}")
    print(f"Percentual concluído: {resumo['percentual_concluido']:.1f}%")
    print("="*30)

# =============================================================================
# FUNÇÃO PRINCIPAL E MENU
# =============================================================================

def menu_principal():
    """
    Menu principal do sistema.
    """
    while True:
        print("\n" + "="*40)
        print("SISTEMA DE GERENCIAMENTO DE TAREFAS")
        print("="*40)
        print("1. Adicionar tarefa")
        print("2. Listar todas as tarefas")
        print("3. Listar tarefas pendentes")
        print("4. Listar tarefas concluídas")
        print("5. Marcar tarefa como concluída")
        print("6. Exibir resumo")
        print("7. Sair")
        print("="*40)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ").strip()
            if descricao:
                tarefa = adicionar_tarefa(descricao)
                print(f"Tarefa '{tarefa['descricao']}' adicionada com sucesso!")
            else:
                print("Descrição não pode estar vazia.")
                
        elif opcao == "2":
            exibir_tarefas()
            
        elif opcao == "3":
            tarefas_pendentes = filtrar_tarefas_por_status(False)
            print("\nTAREFAS PENDENTES:")
            exibir_tarefas(tarefas_pendentes)
            
        elif opcao == "4":
            tarefas_concluidas = filtrar_tarefas_por_status(True)
            print("\nTAREFAS CONCLUÍDAS:")
            exibir_tarefas(tarefas_concluidas)
            
        elif opcao == "5":
            try:
                tarefa_id = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
                if marcar_concluida(tarefa_id):
                    print(f"Tarefa {tarefa_id} marcada como concluída!")
                else:
                    print(f"Tarefa com ID {tarefa_id} não encontrada.")
            except ValueError:
                print("ID deve ser um número inteiro.")
                
        elif opcao == "6":
            exibir_resumo()
            
        elif opcao == "7":
            print("Saindo do sistema...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    # Adicionar algumas tarefas de exemplo
    adicionar_tarefa("Estudar programação funcional")
    adicionar_tarefa("Fazer exercícios de Python")
    adicionar_tarefa("Revisar conceitos de closure")
    
    # Marcar uma tarefa como concluída para demonstração
    marcar_concluida(1)
    
    # Executar o menu principal
    menu_principal()
