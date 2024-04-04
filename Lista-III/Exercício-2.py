while True:
    user = (input('Usuário: '))
    senha = (input('Senha: '))
    if user != senha:
        print('Usuário e senha registrados')
        break
    else:
        print('Sua senha não pode ser igual ao nome de usuário')
        print('Por favor, tente novamente.')