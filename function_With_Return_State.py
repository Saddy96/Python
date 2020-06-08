def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'John')
print(greet('es'), 'Nyre')
print(greet('fr'), 'Don')
