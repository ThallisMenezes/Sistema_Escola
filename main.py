import json
import random
import string
import re

estudantes = []
professores = []
disciplinas = []
turmas = []

def incluir():
# Inicializa a váriavel file_name antes do bloco if para salvar o arquivo com o nome correto
    file_name_incluir = ""
    while True:
        try:
            input_incluir = int(input("1. Estudante\n2. Professor\n3. Disciplina\n4. Turma\nDigite a opção: "))
        except ValueError:
            print("Digite uma opção!")
            continue

        if input_incluir == 1:
            id = ''.join(random.choices(string.digits, k=10))
            nome = input("Digite o nome do estudante: ")
            idade = input("Idade: ")
            cpf = input("Cpf: ")
            matricula = input("Matrícula: ")
            turma = input("Turma: ")
            estudantes.append({
                "id": id,
                "nome": nome,
                "idade": idade,
                "cpf": cpf,
                "matricula": matricula,
                "turma": turma
            })
            file_name_incluir = "Estudantes"

        elif input_incluir == 2:
            id = ''.join(random.choices(string.digits, k=10))
            nome = input("Digite o nome do professor: ")
            idade = input("Idade: ")
            cpf = input("Cpf: ")
            disciplina = input("Disciplina: ")
            turma = input("Turmas: ")
            professores.append({
                "id": id,
                "nome": nome,
                "idade": idade,
                "cpf": cpf,
                "disciplina": disciplina,
                "turma": turma
            })
            file_name_incluir = "Professores"

        elif input_incluir == 3:
            id = ''.join(random.choices(string.digits, k=10))
            nome = input("Digite o nome da disciplina: ")
            professor = input("Professor: ")
            disciplinas.append({
                "id": id,
                "nome": nome,
                "professor": professor
            })
            file_name_incluir = "Disciplinas"

        elif input_incluir == 4:
            id = ''.join(random.choices(string.digits, k=10))
            nome = input("Digite o nome da turma: ")
            turmas.append({
                "id": id,
                "nome": nome
            })
            file_name_incluir = "Turmas"
        else:
            continue
        break

#Carregar dados, caso contrário inicializa uma lista vazia
    try:
        with open(f"{file_name_incluir}.json", "r", encoding="utf-8") as file_read:
            dados = json.load(file_read)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = []

    if file_name_incluir == "Estudantes":
        for estudante in estudantes:
            if estudante not in dados:
                dados.append(estudante)
    elif file_name_incluir == "Professores":
        for professor in professores:
            if professor not in dados:
                dados.append(professor)
    elif file_name_incluir == "Disciplinas":
        for disciplina in disciplinas:
            if disciplina not in dados:
                dados.append(disciplina)
    elif file_name_incluir == "Turmas":
        for turma in turmas:
            if turma not in dados:
                dados.append(turma)

#Salvando os dados no respectivo arquivo
    with open(f"{file_name_incluir}.json", "w", encoding="utf-8") as file_write:
        json.dump(dados, file_write, ensure_ascii=False, indent=4)



def listar():
    file_name_list = ""
    while True:
        try:
            input_listar = int(input("1. Estudantes\n2. Professores\n3. Disciplinas\n4. Turmas\nSelecione a opção desejada: "))
        except ValueError:
            print("Digite uma opção!")
            continue
        if input_listar == 1:
            file_name_list = "Estudantes.json"
        elif input_listar == 2:
            file_name_list = "Professores.json"
        elif input_listar == 3:
            file_name_list = "Disciplinas.json"
        elif input_listar == 4:
            file_name_list = "Turmas.json"
        else:
            print("Aplicação encerrada!")
            break

        with open(f"{file_name_list}", "r", encoding="utf-8") as arquivo:
            read_json = json.load(arquivo)
            print(read_json)

def excluir():
    file_name_excluir = ""
    list_name = []
    while True:
        try:
            input_excluir = int(input("1. Estudantes\n2. Professores\n3. Disciplinas\n4. Turmas\nSelecione a opção desejada: "))
        except ValueError:
            print("Digite uma opção!")
            continue
        if input_excluir == 1:
            file_name_excluir = "Estudantes.json"
            list_name = estudantes
        elif input_excluir == 2:
            file_name_excluir = "Professores.json"
            list_name = professores
        elif input_excluir == 3:
            file_name_excluir = "Disciplinas.json"
            list_name = disciplinas
        elif input_excluir == 4:
            file_name_excluir = "Turmas.json"
            list_name = turmas
        else:
            print("Aplicação encerrada!")
            break

        with open(f"{file_name_excluir}", "r", encoding="utf-8") as file_read:
            read_dados = json.load(file_read)
            list_name = read_dados

            for index, dados in enumerate(list_name):
                print(f"{index}. {dados}")

        while True:
            try:
                indice = int(input("Digite o indice para excluir os dados: "))
            except ValueError:
                print("Digite uma opção!")
                continue
            try:
                confirma = int(input(f"Deseja excluir? {list_name[indice]}\n1. Sim\n2. Não\n"))
            except (ValueError, IndexError):
                print("Digite uma opção!")
                continue
            if confirma == 1:
                list_name.pop(indice)
            else:
                print("Cancelado")
                continue

            with open(f"{file_name_excluir}", "w", encoding="utf-8") as file_write:
                json.dump(list_name, file_write, ensure_ascii=False, indent=4)
            break
        break

def editar():
    lista = []
    file_name_editar = ""
    while True:
        try:
            input_editar = int(input("1. Estudantes\n2. Professores\n3. Disciplinas\n4. Turmas\nSelecione a opção desejada: "))
        except ValueError:
            print("Digite uma opção!")
            continue
        if input_editar == 1:
            file_name_editar = "Estudantes.json"
        elif input_editar == 2:
            file_name_editar = "Professores.json"
        elif input_editar == 3:
            file_name_editar = "Disciplinas.json"
        elif input_editar == 4:
            file_name_editar = "Turmas.json"
        else:
            break
        break

    if file_name_editar != "":
        with open(f"{file_name_editar}", "r", encoding="utf-8") as file_read:
            read = json.load(file_read)
            lista = read

        for index, dados in enumerate(lista):
            print(f"{index}. {dados}")

        while True:

            if not lista:
                print("Lista vazia\nAplicação encerrada!")
                break
            else:
                try:
                    editar = int(input("Digite o índice que deseja editar: "))
                except(ValueError,IndexError,KeyError):
                    print("Digite uma opção!")
                    continue

            tamanho = (len(lista))
            if editar <= tamanho:
                editavel = lista[editar]
                dicionario = dict(editavel)
            else:
                break

            if "nome" in dicionario:
                nome = input("Novo nome: ")
                dicionario["nome"] = nome
            elif "idade" in dicionario:
                idade = int(input("Nova idade: "))
                dicionario["idade"] = idade
            elif "cpf" in dicionario:
                cpf = input("Novo cpf: ")
                dicionario["cpf"] = cpf
            elif "matricula" in dicionario:
                matricula = input("Nova matricula: ")
                dicionario["matricula"] = matricula
            elif "turma" in dicionario:
                turma = input("Nova turma: ")
                dicionario["turma"] = turma
            elif "disciplina" in dicionario:
                disciplina = input("Nova disciplina: ")
                dicionario["disciplina"] = disciplina
            elif "professor" in dicionario:
                professor = input("Novo professor: ")
                dicionario["professor"] = professor
            else:
                print("Dados Inexistentes!")
            lista[editar] = dicionario

            with open(f"{file_name_editar}", "w", encoding="utf-8") as file_write:
                json.dump(lista, file_write, ensure_ascii=False, indent=4)
                print("Salvo com sucesso!")
    else:
        print("Aplicação encerrada!")


def menu():
    while True:
        try:
            entrada = int(input("1. Incluir\n2. Listar\n3. Excluir\n4. Editar\nOutro encerra!\nSelecione a opção desejada: "))
        except:
            print("Digite um número!")
            continue

        if entrada == 1:
            incluir()
            continue
        elif entrada == 2:
            listar()
            continue
        elif entrada == 3:
            excluir()
            continue
        elif entrada == 4:
            editar()
            continue
        else:
            print("Aplicação encerrada!")
            break

menu()