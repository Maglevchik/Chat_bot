def save_conversation(log_list, filename='conversation.txt'):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for line in log_list:
                file.write(line + '\n')
    except IOError as e:
        print(f'Error during save file: {e}')



def load_conversation(filename='conversation.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Прочитать все строки и удалить начальные/конечные пробелы (включая \n)
            return [line.strip() for line in file if line.strip()] # <--- Генератор списка для очистки строк
    except FileNotFoundError:
        print('File not found')
        return []