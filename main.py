import os # Может понадобиться для удаления файла настроек при тестировании
from src.funct.conditions import cond_salutation, cond_wordcommand
from src.funct.functions import chat_bot
from src.funct.file_operation import save_conversation, load_conversation
from settings import UserSettingsManager



new_language_x = ''

def main():
    # Создаем экземпляр UserSettingsManager.
    # В этот момент он автоматически попытается загрузить настройки из 'user_settings.json'.
    settings = UserSettingsManager()

    # Теперь вы можете получить доступ к загруженным настройкам:
    current_language = settings.get_setting("language")
    current_user_name = settings.get_setting("user_name")

    print(f"Бот запущен. Текущий язык: {current_language}")
    print(f"Имя пользователя: {current_user_name}")


    # Далее идет ваш код для изменения настроек, как и раньше:
    new_user_name = input("Введите ваше имя (или нажмите Enter, чтобы оставить текущее): ")
    if new_user_name:
        settings.set_setting("user_name", new_user_name)

    valid_languages = ["русский", "english"] 
    current_lang_display = settings.get_setting("language")

    while True:
        new_language_input = input(f"Выберите язык (русский/english), нажмите Enter для текущего ({current_lang_display}): ").lower()

        if new_language_input == "":
            print(f"Язык оставлен текущим: {current_lang_display}.")
            new_language_x = current_lang_display
            break
        elif new_language_input in valid_languages:
            settings.set_setting("language", new_language_input)
            new_language_x = new_language_input
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 'русский', 'english' или просто нажмите Enter.")

    print("Последние настройки перед завершением:", settings.get_all_settings())
    
    
    #--Подгруз логов диалога--
    conversation = load_conversation()

    if new_language_x == 'русский':
        from src.common_data.info_lables import main_phrase
        print(main_phrase[0] + f'Привет, {new_user_name if new_user_name==True else current_user_name}!')
    elif new_language_x == 'english':
        from src.common_data.info_lables_eng import main_phrase
        print(main_phrase[0] + f'Hello, {new_user_name if new_user_name==True else current_user_name}!')
    print(
    f'\n{main_phrase[0]}{main_phrase[4]}'
    f'\n{main_phrase[0]}{main_phrase[2]}'
    )
    
    while True:
        #--Запрос пользователя--
        user_input = input()

        response_salutation = cond_salutation(user_input, new_language_x)
        response_comm = cond_wordcommand(user_input, new_language_x)

        if response_comm == 'exit_dialog': #--Завершение диалога--
            print(main_phrase[0]+main_phrase[3])
            save_conversation(conversation)
            break

        elif response_salutation != 'skip': #--Дефолт фразы бота|Приветствие--
            response = response_salutation

        else: #--Сложные фразы(Расширеный функционал)--
            response = chat_bot(user_input, new_language_x)

            #--Ответ Чат-бота--
        print(main_phrase[0] + response)

        #--Запись диалога--
        conversation.append(main_phrase[1] + user_input)
        conversation.append(main_phrase[0] + response)
    



if __name__ == "__main__":
    main()
