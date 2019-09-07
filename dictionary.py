dictionary = {'city': 'Москва', 'temperature': 20}
print(dictionary['city'])
dictionary['temperature'] = dictionary['temperature'] - 5
print(dictionary)
print(dictionary.get('country'))
dictionary.get('country', 'Россия')
dictionary['date'] = '27.05.2019'
print(len(dictionary))
print(dictionary)