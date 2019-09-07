def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'.upper()
result = get_summ('Learn','python')
print(result)
    
