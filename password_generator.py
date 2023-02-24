import random
import string
import PySimpleGUI as sg

class PassGen:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(15,1)),
            sg.Input(key='site',size=(20,1))],
            [sg.Text('E-mail/Usuario', size=(15,1)),
            sg.Input(key='usuario',size=(20,1))],
            [sg.Text('Quantidade de caracteres', size=(26,1)), sg.Combo(values=list(range(30)),key='total_chars', default_value=1,size=(5,1))],
            [sg.Output(size=(37,5))],
            [sg.Button('Gerar senha')]
        ]
        self.janela = sg.Window('Password Generator', layout)
        
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar senha':
                nova_senha = self.password_generator(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)
                
    def salvar_senha(self, nova_senha, valores):
        with open('./senha.txt', 'a', newline='') as arquivo:
            arquivo.write(f"site:{valores['site']}, usuario:{valores['usuario']}, nova senha: {nova_senha}\n")
        print('Senha salva para o arquivo "Senhas.txt"')

    def password_generator(self, Len_pass):
        ascii_options = string.ascii_letters
        number_option = string.digits
        punt_options = string.punctuation
        option = ascii_options + number_option + punt_options
        password_user = ""
        for i in range(0, Len_pass['total_chars']):
            digit = random.choice(option)
            password_user = password_user + digit
        return password_user

gen = PassGen()
gen.Iniciar()