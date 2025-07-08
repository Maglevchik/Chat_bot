import random


def chat_bot(message,lang):
    if lang == 'русский':
        from src.common_data.info_lables import response_dict, response_random, chat_bot_key_phrase
    elif lang == 'english':
        from src.common_data.info_lables_eng import response_dict, response_random, chat_bot_key_phrase
    
    #--Сложные фразы(Расширеный функционал)--

    #--Матем операции--
    if chat_bot_key_phrase[0] in message.lower():
        return math_numbers(message,lang)

    #--Анекдот и его категория--
    elif chat_bot_key_phrase[1] in message.lower():
        return tell_anecdote(message,lang)
    
    elif chat_bot_key_phrase[2] in message.lower():
        return sphere_rand(message,lang)

    else:
        response = response_dict.get(message.lower(), random.choice(response_random))
        return response

def math_numbers(message,lang):
    if lang == 'русский':
        from src.common_data.info_lables import response_unknown, math_manual, math_operations, math_num_phrase
    elif lang == 'english':
        from src.common_data.info_lables_eng import response_unknown, math_manual, math_operations, math_num_phrase
    
    parts = message.lower().split()

    try:
        num1 = float(parts[2])
        operation = parts[3]
        num2 = float(parts[4])
        print(operation)
        if operation in math_operations:
            return f'{math_num_phrase[0]}{math_operations[operation](num1,num2)}'
    except(IndexError,ValueError,BaseException,UnboundLocalError,ZeroDivisionError):
        return response_unknown + '\n' + math_manual

def tell_anecdote(message,lang):
    if lang == 'русский':
        from src.common_data.info_lables import response_unknown, anecdote_manual, told_anecdotes, anecdotes_categories, tell_anecdot_phrase
    elif lang == 'english':
        from src.common_data.info_lables_eng import response_unknown, anecdote_manual, told_anecdotes, anecdotes_categories, tell_anecdot_phrase
    
    parts = message.lower().split()
    category = None
    
    if len(parts) >= 3: 
        category_index = 2 #Старт итерации после 2х ключевых слов
        category_parts = [] #Ячейка для объединения слов в категорию
        
        for i in range(category_index, len(parts)): # Объединяем части, если категория состоит из нескольких слов (например, "про животных")
            if parts[i] in anecdotes_categories: #Категория = 1 слово | Категория существует
                category = parts[i] 
                break
            
            else:
                category_parts.append(parts[i])
                if ' '.join(category_parts) in anecdotes_categories: #Категория > 1 слово | Категория существует
                    category = ' '.join(category_parts) 
                    break
        
        if category and category in anecdotes_categories: #Если категория существует и категория входит в anecdotes_categories
            available_anecdotes = [a for a in anecdotes_categories[category] if a not in told_anecdotes[category]]
            
            if not available_anecdotes:# Если все анекдоты в этой категории были рассказаны, сбросим список
                told_anecdotes[category] = []
                available_anecdotes = anecdotes_categories[category]
                return f'{tell_anecdot_phrase[0]}"{category}".{tell_anecdot_phrase[1]}{random.choice(available_anecdotes)}'
            
            else: #Если не все анекдоты из опред. категории рассказаны
                anecdote = random.choice(available_anecdotes)
                told_anecdotes[category].append(anecdote)
                return anecdote
        
        else: #Категория не существует или ее нет в anecdotes_categories
            return f'{tell_anecdot_phrase[2]} "{' '.join(parts[2:])}".{tell_anecdot_phrase[3]}{', '.join(anecdotes_categories.keys())}'
    
    else: #Памятка для понимания с ключ словами "расскажи анекдот"
        return response_unknown + '\n' + anecdote_manual

def sphere_rand(message,lang):
    if lang == 'русский':
        from src.common_data.info_lables import response_unknown, sphere_rand_manual, sphere_phrase
    elif lang == 'english':
        from src.common_data.info_lables_eng import response_unknown, sphere_rand_manual, sphere_phrase
    
    import random
    parts = message.lower().split()
    if len(parts) > 2:
        if parts[1] == sphere_phrase[0]:
            chosen_option = ' '.join(parts[2:])
            return f'{sphere_phrase[4]}{chosen_option},{sphere_phrase[5]}{random.randint(0, 100)} %.'
        elif parts[1] == sphere_phrase[1] and sphere_phrase[2] in parts:
            
            # Найти первое вхождение 'peach'
            first_peach_index = parts.index(sphere_phrase[2])
            #1й выбор
            first_option_parts = ' '.join([p.strip() for p in parts[2:first_peach_index] if p.strip()])
            #2й выбор
            second_option_parts = ' '.join([p.strip() for p in parts[first_peach_index + 1:] if p.strip()])
            first_second_option = [first_option_parts,second_option_parts] #Закидываются фразы
            options_to_choose_from = [p for p in first_second_option if p]
            if len(options_to_choose_from) == 2:
                chosen_option = random.choice(options_to_choose_from)
                return f'{sphere_phrase[6]}{chosen_option}!'
            else:
                return sphere_phrase[11]
        elif parts[1] == sphere_phrase[3]:
            chosen_option = random.choice([sphere_phrase[7],sphere_phrase[8],sphere_phrase[9]])
            return f'{sphere_phrase[10]}{chosen_option}.'
        else:
            return sphere_phrase[12]
    else:#Памятка для понимания с ключ словами "шар"
        return response_unknown + '\n' + sphere_rand_manual 

