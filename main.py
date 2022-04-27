#coded by: Alan Rios
import csv
import os



class Contato:
    def __init__(self,nome,telefone,email,id_contato,sobrenome = '',grupo = ''):
        self.id_contato = id_contato
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.email = email
        self.grupo = grupo
        


class Agenda:
    
    def __init__(self):
        self.lista_contatos = []
        self.lista_grupos = []
        self.total_ctt=0
        self.next_id = 0

    def add_contato(self,contato):
        self.lista_contatos.append(contato)
        self.next_id += 1
        self.total_ctt += 1
    
    def add_contato_no_id(self,contato):
        self.lista_contatos.append(contato)
    
    def excluir_contato(self,contato):
        for item in self.lista_contatos:
            if item.id_contato == contato[3]:
                self.lista_contatos.remove(item)
                break

    def alterar_contato(self,contato):
        count = 0
        ctt_alterado = []
        ctt_inalterado = contato
        for item in self.lista_contatos:
            if item.id_contato == contato[3]:
                ctt_alterado = [item.nome,item.telefone,item.email,item.id_contato,item.sobrenome,item.grupo]
                break
        
        opc = input('deseja alterar o nome do contato?(s/n): ')
        if opc == 's':
            count += 1
            ctt_alterado[0] = self.nome()
            ctt_alterado[4] = self.sobrenome()
        elif opc == 'n':
            pass

        opc = input('deseja alterar os numeros do contato?(s/n): ')
        if opc == 's':
            count += 1
            ctt_alterado[1] = self.telefone()
        elif opc == 'n':
            pass

        opc = input('deseja alterar os emails do cadastro?(s/n): ')
        if opc == 's':
            count += 1
            ctt_alterado[2] = self.email()
        elif opc == 'n':
            pass
        
        if count == 0:
            print('nenhum dado foi alterado')
        elif count > 0:
            print('realmente deseja alterar o contato de: ')
            print('-'*15)
            print('nome: ')
            print(ctt_inalterado[0],' ',ctt_inalterado[4])
            print('-'*15)
            print('telefones:')
            if type(ctt_inalterado[1]) == list:
                for item in ctt_inalterado[1]:
                    print(item)
            else:
                print(ctt_inalterado[1])
            print('-'*15)
            print('emails: ')
            if type(ctt_inalterado[2]) == list:
                for item in ctt_inalterado[2]:
                    print(item)
            else:
                print(ctt_inalterado[2])
            print('-'*30)
            print('-'*30)
            print('para: ')
            print('-'*15)
            print('nome: ')
            print(ctt_alterado[0],'',ctt_alterado[4])
            print('-'*15)
            print('telefones:')
            if type(ctt_alterado[1]) == list:
                for item in ctt_alterado[1]:
                    print(item)
            else:
                print(ctt_alterado[1])
            print('-'*15)
            print('emails: ')
            if type(ctt_alterado[2]) == list:
                for item in ctt_alterado[2]:
                    print(item)
            else:
                print(ctt_alterado[2])
            
            opc = input('(s/n)')
            if opc == 's':
                self.excluir_contato(ctt_inalterado)
                contato1 = Contato(ctt_alterado[0],ctt_alterado[1],ctt_alterado[2],ctt_alterado[3],ctt_alterado[4],ctt_alterado[5])
                self.add_contato_no_id(contato1)
                print('contato alterado')
            elif opc == 'n':
                print('contato nao alterado')

    @staticmethod
    def nome():
        while True:
            nome = input('nome: ')
            if nome.isalpha():
                return nome
            else:
                print('dado invalido')
    
    @staticmethod
    def sobrenome():
        while True:
            sobrenome = input('sobrenome: ')
            if sobrenome.isalpha() or sobrenome == '':
                return sobrenome
            else:
                print('dado invalido')

    @staticmethod
    def telefone():
        telefones = []
        while True:
            telefone = input('telefone: ')
            if telefone.isnumeric():
                telefones.append(telefone)
                opc = input('adicionar outro numero?(s/n) ')
                if opc == 's':
                    pass
                elif opc == 'n':
                    return telefones
            else:
                print('dado invalido')
    
    @staticmethod
    def email():
        emails = []
        while True:
            email = input('email: ')
            if '@' in email and '.' in email:
                emails.append(email)
                opc = input('adicionar outro email?(s/n) ')
                if opc == 's':
                    pass
                elif opc == 'n':
                    return emails
            else:
                print('dado invalido')

    def show_contatos(self):
        for contato in self.lista_contatos:
            print(contato.id_contato,contato.nome,contato.sobrenome)

    def show_detalhes(self,id_ctt):
        qtt = False
        cont = []
        for contato in self.lista_contatos:
            if contato.id_contato == id_ctt:
                cont.append(contato.nome)
                cont.append(contato.telefone)
                cont.append(contato.email)
                cont.append(contato.id_contato)
                cont.append(contato.sobrenome)
                qtt = True
                print('--------NOME-------')
                print(contato.nome, contato.sobrenome)
                print('------TELEFONE-----')
                for numero in contato.telefone:
                    print(numero)
                print('-------E-MAIL------')
                for email in contato.email:
                    print(email)
                print('-------------------')
                break
        return (qtt,cont)
    
    def show_grupos(self):
        tf = False
        print('-'*9,'GRUPOS','-'*9)
        if len(self.lista_grupos)>0:
            tf = True
            self.dicionario_menu = dict(enumerate(self.lista_grupos))
            for opcao in self.dicionario_menu:
                print(self.dicionario_menu.get(opcao))
        elif len(self.lista_grupos)==0:
            print('não existem grupos na agenda')
        print('-'*26)
        return tf
    
    def show_contatos_gp(self,lista):
        for contato in lista:
            print(contato[3],contato[0],contato[4])

    def coletar_grupo(self,grupo):
        lista_ctt = []
        print('-'*3,'CONTATOS NO GRUPO','-'*3)
        for contato in self.lista_contatos:
            if grupo in contato.grupo:
                lista = []
                lista.append(contato.nome)
                lista.append(contato.telefone)
                lista.append(contato.email)
                lista.append(contato.id_contato)
                lista.append(contato.sobrenome)
                lista.append(contato.grupo)
                lista_ctt.append(lista) 
        if len(lista_ctt) > 0:
            self.show_contatos_gp(lista_ctt)
            print('-'*26)
        elif len(lista_ctt) == 0:
            print('nao existem contatos no grupo')
        return lista_ctt 

    def salvar(self):
        lista = []
        for contato in self.lista_contatos:
            lista_contato = []
            lista_contato.append((contato.nome,','.join(contato.telefone),','.join(contato.email),contato.id_contato,contato.sobrenome,','.join(contato.grupo)))
            lista.append(*lista_contato)
        nome_arquivo = 'contatos.csv'
        arquivo = open(nome_arquivo,'w',encoding='utf-8')
        csv.writer(arquivo, delimiter=';', lineterminator='\n').writerows(lista)
        arquivo.close()



class Sistema:
    def __init__(self):
        self.agenda = Agenda()
        self.organizado = Sistema.ler_arquivo()
        if len(self.organizado[0]) == 3:
            self.adicionar_organizado()
        elif len(self.organizado[0]) > 3:
            self.gerar_id()
            self.adicionar_organizado2()
        self.agenda.total_ctt = len(self.agenda.lista_contatos)
        self.main()

    
    def adicionar_organizado(self):
        for elemento in self.organizado:
            contato = Contato(elemento[0], elemento[1].split(','), elemento[2].split(','), str(self.agenda.next_id), '', [])
            self.agenda.add_contato(contato)
    
    def gerar_id(self):
        max = 0
        for elemento in self.organizado:
            if int(elemento[3]) > max:
                max = int(elemento[3])
        self.agenda.next_id = max+1

    def adicionar_organizado2(self):
        for elemento in self.organizado:
            contato = Contato(elemento[0], elemento[1].split(','), elemento[2].split(','), elemento[3], elemento[4],elemento[5].split(','))
            self.agenda.add_contato_no_id(contato)
            if elemento[5] != '' and elemento[5] != ' ':
                if elemento[5] not in self.agenda.lista_grupos:
                    lista_gp = elemento[5].split(',')
                    for gp in lista_gp:
                        if gp not in self.agenda.lista_grupos:
                            self.agenda.lista_grupos.append(gp)


    def pedir_dados(self):
        mensagem_erro = 'dado invalido'
        lista_telefone = []
        lista_email = []
        while True:
            nome = input('nome: ')
            if nome.isalpha():
                break
            else:
                print(mensagem_erro)

        while True:        
            sobrenome = input('sobrenome: ')
            if sobrenome.isalpha() or sobrenome == '' or sobrenome == ' ':
                break
            else:
                print(mensagem_erro)

        while True:
            telefone = input('telefone: ')
            if telefone.isnumeric():
                lista_telefone.append(telefone)
                opc = input('deseja adicionar outro numero?(s/n) ')
                if opc == 's':
                    pass
                elif opc == 'n':
                    break
            else:
                print(mensagem_erro)

        while True:
            email = input('email: ')
            if '@' in email and '.' in email:
                lista_email.append(email)
                opc = input('deseja adicionar outro email?(s/n) ')
                if opc == 's':
                    pass
                elif opc == 'n':
                    break
            else:
                print(mensagem_erro)
        id_ctt = self.agenda.next_id
        grupo = ''
        return Contato(nome,lista_telefone,lista_email,str(id_ctt),sobrenome,grupo)

    def selecionar(self):
        id1 = input('selecione o id: ')
        resp,ctt = self.agenda.show_detalhes(id1)
        return (resp,ctt)
    
    def selectCtt_Gp(self,lista):
        while True:
            id1 = input('selecione o id("back" para voltar): ')
            if id1 == 'back':
                break
            if id1.isnumeric():
                break
            else:
                print('digite um id valido')
        while True:
            if id1 == 'back':
                break
            else:
                for contato in lista:
                    if id1 == contato[3]:
                        resp,ctt = self.agenda.show_detalhes(id1)
                        return (resp,ctt)
                return (False,[])

    def show_menu_contato(self):
        print('-'*10,'ACOES','-'*10)
        menu = ['ALTERAR','EXCLUIR','ASSOCIAR GRUPO','VOLTAR']
        self.dicionario_menu = dict(enumerate(menu))
        for opcao in self.dicionario_menu:
            print(opcao+1, self.dicionario_menu.get(opcao))
        print('-'*27)

    def show_menu_grupo(self):
        print('-'*10,'ACOES','-'*10)
        menu = ['CRIAR GRUPO','MOSTRAR GRUPOS','EXCLUIR GRUPO','VOLTAR']
        self.dicionario_menu = dict(enumerate(menu))
        for opcao in self.dicionario_menu:
            print(opcao+1, self.dicionario_menu.get(opcao))
        print('-'*27)

    def menu_grupo(self):
        while True:
            os.system('cls')
            self.show_menu_grupo()
            opc = self.dicionario_menu[int(input('digite a opcao: '))-1]
            if opc == 'CRIAR GRUPO':
                os.system('cls')
                self.criar_grupo()
                input('pressione enter')
            elif opc == 'MOSTRAR GRUPOS':
                os.system('cls')
                tf = self.agenda.show_grupos()
                if tf == True:
                    lista = self.selecionar_grupo()
                    try:
                        if len(lista) > 0:
                            while True:
                                vf,cont = self.selectCtt_Gp(lista)
                                if vf == True:
                                    self.menu_contato(cont)
                                    break
                                else:
                                    print('digite o id de um contato presente no grupo')
                                    opc = input('deseja voltar?(s/n) ')
                                    if opc == 's':
                                        break
                                    elif opc == 'n':
                                       pass
                    except:
                        pass
                else:
                    pass
            elif opc == 'EXCLUIR GRUPO':
                os.system('cls')
                tf = self.agenda.show_grupos()
                if tf == True:
                    remover = input('digite o grupo que deseja remover("back" para voltar): ')
                    if remover == 'back':
                        break
                    else:
                        self.rem_grupo(remover)
                        input('pressione enter')
                else:
                    print('nao existem grupos na agenda')
            elif opc == 'VOLTAR':
                break


    def criar_grupo(self):
        grupo = input('digite o nome do grupo que deseja criar: ')
        if grupo.isascii():
            print('para criar um grupo, voce deve associar uma pessoa a ele inicialmente.')
            while True:
                idctt = input('digite o id do contato que deseja associar ao grupo("show" para mostrar os contatos): ')
                if idctt == 'show':
                    self.agenda.show_contatos()
                elif idctt.isnumeric():
                    tf = self.add_grupo(idctt,grupo)
                    if tf == True:
                        self.agenda.lista_grupos.append(grupo)
                        print('grupo criado com sucesso')
                        break
                    else:
                        print('digite um id existente na agenda')

    def rem_grupo(self,grupo):
        if grupo in self.agenda.lista_grupos:
            for contato in self.agenda.lista_contatos:
                if grupo in contato.grupo:
                    contato.grupo.remove(grupo)
                    self.agenda.lista_grupos.remove(grupo)
            print('grupo removido com sucesso')
        else:
            print('este grupo nao existe')

    def add_grupo(self,idctt,grupo):
        for contato in self.agenda.lista_contatos:
            if contato.id_contato == idctt:
                if grupo not in contato.grupo:
                    contato.grupo.append(grupo)
                    return True
        return False

    def selecionar_grupo(self):
        while True:
            grupo= input('digite o nome do grupo que deseja vizualizar("back" para voltar): ')
            if grupo == 'back':
                break
            elif grupo in self.agenda.lista_grupos:
                lista = self.agenda.coletar_grupo(grupo)
                return lista
            else:
                print('este grupo nao existe')

    def menu_contato(self,contato):
        while True:
            
            self.show_menu_contato()
            try:
                opc = self.dicionario_menu[int(input('digite a opcao: '))-1]
                if opc == 'ALTERAR':
                    os.system('cls')
                    self.agenda.alterar_contato(contato)
                    input('pressione enter')
                    os.system('cls')
                elif opc == 'EXCLUIR':
                    os.system('cls')
                    sel = input('realmente deseja excluir o contato?(s/n) ')
                    if sel == 's':
                        self.agenda.excluir_contato(contato)
                        print('contato excluido')
                        input('pressione enter')
                        os.system('cls')
                        break
                    elif sel == 'n':
                        os.system('cls')
                        print('contato nao excluido')
                        input('pressione enter')
                        os.system('cls')
                elif opc == 'ASSOCIAR GRUPO':
                    os.system('cls')
                    tf = self.agenda.show_grupos()
                    if tf == True:
                        grupo = input('digite o grupo que deseja associar: ')
                        if grupo in self.agenda.lista_grupos:
                            vf = self.add_grupo(contato[3],grupo)
                            if vf == True:
                                print('adicionado ao grupo com exito')
                                input('pressione enter')
                                os.system('cls')
                            elif vf == False:
                                print('nao foi possivel adicionar o contato ao grupo pois ele ja esta no grupo')
                                input('pressione enter')
                                os.system('cls')
                        else:
                            os.system('cls')
                            print('este grupo não existe')
                            input('pressione enter')
                            os.system('cls')
                    else:
                        os.system('cls')
                        print('não existem grupos na agenda')
                        sel = input('deseja criar um?(s/n) ')
                        if sel == 's':
                            os.system('cls')
                            self.criar_grupo()
                            input('pressione enter')
                            os.system('cls')
                        elif sel == 'n':
                            os.system('cls')
                            pass
                elif opc == 'VOLTAR':
                    break
            except:
                print('opcao invalida')

    def show_menu(self):
        print('-'*10,'MENU','-'*10)
        menu = ['MOSTRAR CONTATOS','ADICIONAR CONTATO','SELECIONAR CONTATO','GRUPOS','SAIR E SALVAR']
        self.dicionario_menu = dict(enumerate(menu))
        for opcao in self.dicionario_menu:
            print(opcao+1, self.dicionario_menu.get(opcao))
        print('-'*26)

    def main(self):
        while True:
            os.system('cls')
            self.show_menu()
            try:
                opc = self.dicionario_menu[int(input('digite a opcao: '))-1]
                if opc == 'MOSTRAR CONTATOS':
                    os.system('cls')
                    self.agenda.show_contatos()
                    input('pressione enter')
                elif opc == 'ADICIONAR CONTATO':
                    os.system('cls')
                    if self.agenda.total_ctt < 75:
                        contato = self.pedir_dados()
                        self.agenda.add_contato(contato)
                        os.system('cls')
                        print('contato adicionado com sucesso')
                        input('pressione enter')
                    elif self.agenda.total_ctt >=75:
                        print('agenda cheia, exclua algum contato')
                        input('pressione enter')
                elif opc == 'SELECIONAR CONTATO':
                    os.system('cls')
                    self.agenda.show_contatos()
                    tf,ctt = self.selecionar()
                    if tf == True:
                        self.menu_contato(ctt)
                    else:
                        print('id inexistente na agenda')
                        input('pressione enter')
                elif opc == 'GRUPOS':
                    os.system('cls')
                    self.menu_grupo()
                elif opc == 'SAIR E SALVAR':
                    os.system('cls')
                    self.agenda.salvar()
                    print('agenda salva')
                    break
            except:
                print('opcao invalida')

    @staticmethod
    def ler_arquivo():
        lista_ctt = []
        with open('contatos.csv','r',encoding='utf-8') as bancodados:
            dados = csv.reader(bancodados,delimiter=';')
            for dado in dados:
                lista_ctt.append(dado)
            bancodados.close()
            if len(lista_ctt[0]) == 3:
                organizado = Sistema.org_main(lista_ctt)
            elif len(lista_ctt[0]) > 3:
                organizado = lista_ctt
        return organizado

    
    @staticmethod
    def org_num(lista):
        for i in range(len(lista)):
            for j in range(len(lista[0])):
                if lista[i][j].isnumeric():
                    aux = lista[i][1]
                    lista[i][1] = lista[i][j]
                    lista[i][j] = aux
        return lista
    @staticmethod
    def org_email(lista):
        for i in range(len(lista)):
            for j in range(len(lista[0])):
                if '@' in lista[i][j]:
                    aux = lista[i][2]
                    lista[i][2] = lista[i][j]
                    lista[i][j] = aux
        return lista
    @staticmethod
    def org_main(lista):
        return Sistema.org_email(Sistema.org_num(lista))
        
        

sistema = Sistema()
