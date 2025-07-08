def cond_salutation(message,lang):
    if lang == 'русский':
        from src.common_data.info_lables import word_hello, word_bye, word_dialog, exit
    elif lang == 'english':
        from src.common_data.info_lables_eng import word_hello, word_bye, word_dialog, exit
    
    if message.lower() in word_hello: #--Дефолт фразы бота|Приветствие-- !='skip'
        return word_hello.get(message.lower())
    elif message.lower() in word_bye:
        return (f'{word_bye.get(message.lower())}\n'
                f'{exit}'
            )
    elif message.lower() in word_dialog:
        return word_dialog.get(message.lower())
    else:
        return 'skip'

def cond_wordcommand(message,lang): # --Завершение диалога--
    if lang == 'русский':
        from src.common_data.info_lables import input_comm
    elif lang == 'english':
        from src.common_data.info_lables_eng import input_comm
    
    if message.lower() in input_comm:
        return input_comm.get(message)
