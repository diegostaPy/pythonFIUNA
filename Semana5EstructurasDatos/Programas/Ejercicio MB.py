texto = [
    'azcbobobegghakl',
    'qotbobooboboboboobbptoboboobobbw',
    'lfvroxlpr',
    'bobbbobobbobbbodboobobygoboombibobobbobbyboob',
    'pkboobboboboboobbobobhobobobthehobowonde'
]

search = 'bob'

for i in texto:
    contador = 0
    inicio = 0
    while True:
        inicio = i.find(search, inicio)
        if inicio == -1:
            break
        contador += 1
        inicio += 1  # Evita contar la misma ocurrencia repetidamente
    print(f"La subcadena '{search}' aparece {contador} veces en la cadena")