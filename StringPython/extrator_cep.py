endereco = "Rua das Flores 72, Apartamento 1002, Lanjeiras,, Rio de Janeiro, RJ, 23440-120"

import re #Regular Expression - RegEx

#cep = 5 digitos + hifen(opicional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco) #match ou none caso o padrão não seja encontrado

if busca:
    cep = busca.group()
    print(cep)
