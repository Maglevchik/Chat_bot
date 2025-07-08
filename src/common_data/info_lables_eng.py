def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
response_unknown = 'Sorry, I cannot process this(('
response_random = ["I don't have an answer to your request", "I'll think about it", "Let's change the topic"]
exit = 'To end the dialogue, type "exit".' # Renamed to avoid conflict with Python's 'exit'
word_hello = {
    'hello': 'Hello',
    'hi there': 'Welcome', # 'здравствуйте' is more formal than 'hello', 'hi there' captures some of that
    'good day': 'Good day to you too',
    'how is life': 'So-so, chilling', # 'По-тихоньку, на чиле' is very informal, 'So-so, chilling' is a close approximation
    'whats up': 'Wassup, dude' # 'дарова' is very informal slang
}
word_bye = {
    'bye': 'Bye',
    'goodbye': 'See you soon',
    'have a good evening': 'Good night',
    'need to rest': 'Okay',
    'later': 'See ya' # 'пакеда' is very informal slang
}

input_comm = {
    'exit': 'exit_dialog' # Renamed 'выход' to 'exit'
}
chat_bot_key_phrase = [
    'how will',# 'сколько будет 0'
    'tell anecdote',# 'расскажи анекдот 1'
    'sphere'# 'шар 2'
]
main_phrase = [
    'Chat-bot:   ',
    'You:   ',
    'Welcome to the chat-bot!',
    'Exiting!',
    'To learn more about the chat-bot type "botinfo";\nTo learn how to use the bot type "workcomm".\n' # 'рабком' -> 'workcomm'
]
response_dict = {
    'workcomm': ('Working commands: ' # 'рабком' -> 'workcomm'
    f'\n[1] To end the session type "{get_key(input_comm, 'exit_dialog')}";'
    f'\n[2] To use the calculator type "{chat_bot_key_phrase[0]}";'
    f'\n[3] To see an anecdote type "{chat_bot_key_phrase[1]}";' # Changed index to 1 for tell a joke
    f'\n[4] To use the magic sphere type the appeal "{chat_bot_key_phrase[2]}";'),
    
    'botinfo': ('Information about the chat-bot: ' # 'ботинфо' -> 'botinfo'
    '\n[1] Can greet;'
    '\n[2] Can perform mathematical operations such as addition, subtraction, multiplication, division, exponentiation, square root extraction;'
    '\n[3] Can tell anecdotes;'
    '\n[4] Can be clairvoyant and predict the future with a magic sphere;'
    '\n[5] Can say hello, to see this type "hellogoodbye";'), # 'приветпока' -> 'hellogoodbye'
    
    'hellogoodbye': ('I have answers to these words: ' # 'приветпока' -> 'hellogoodbye'
    f'\n[1] Greeting words: {', '.join(word_hello.keys())}. '
    f'\n[2] Farewell words: {', '.join(word_bye.keys())}')
}

word_dialog = {
    'ping':'Kong',
    'king':'Kong',
    'pew':'Pow',
    'bot':'On site', # 'На месте' could also be 'Here'
    'why':'This is my point of view',
    'thanks':'You are welcome',
    "can you help me?": "Of course! How can I be useful?",
    "I have a question.": "Good day! I'm listening carefully.",
    "thank you for your help!": "Always at your service! Glad to help.",
    "I would be very grateful if you...": "I will do my best. Please specify.",
    "you helped a lot!": "Glad to hear! My job is to help you.",
}

anecdotes_categories = {
    "funny": [ # веселый
        "Why don't programmers play poker? Because they always show their cards to prove they weren't cheating.",
        "Red Riding Hood walks through the forest, meets the Wolf. Wolf: 'I'll eat you!' Red Riding Hood: 'I already ate!' Wolf: 'Then I'll eat you for breakfast!'",
        "Advertisement: 'Cleaner wanted. Big salary, but so much work you'll get tired counting it.'",
        "Two system administrators meet. One to the other: 'My Wi-Fi broke down at home yesterday. Had to turn on 3G. Almost died of greed.'",
        "What does one file say to another when they meet? 'You're my archival friend! Hope you're not infected!'",
        "Husband and wife are watching TV. Wife: 'What are you looking at?' Husband: 'Just an ad for toothpaste. Everyone looks so happy there!' Wife: 'Then buy yourself some toothpaste!' Husband: 'I already did, but happiness never came!'",
        "Patient to doctor: 'Doctor, I constantly feel like I'm late!' Doctor: 'And when did this start?' Patient: 'When did this start?!'",
        "Why did the tomato turn red? Because it saw the carrot wilt with embarrassment.",
        "Teacher: 'Vovochka, why are you so sad?' Vovochka: 'Because my brother died.' Teacher: 'Oh, my condolences! From what?' Vovochka: 'He went to a math test and couldn't solve a single problem.'",
        "Husband calls wife: 'Honey, I found a parking spot right at the store entrance!' Wife: 'Don't touch it! It's probably for invalids!'",
        "Two blondes meet. One: 'Imagine, I was given a book, and it has no pictures!' Second: 'Maybe you were given a volume with pictures, but no text!'",
        "Why are crocodiles flat? Because cars run them over when they cross the road!",
        "Girlfriend to boyfriend: 'Honey, do you love me?' Boyfriend: 'Do you love me?' Girlfriend: 'No.' Boyfriend: 'Me neither.'",
        "A man came to the doctor: 'Doctor, I have a problem: I wake up and can't remember my name!' Doctor: 'What's your name?' Man: 'Exactly!'",
        "Mom to son: 'Why are you taking so long with your math homework?' Son: 'Because I'm doing it in a column, not in my head!'",
        "Phone call: 'Hello, is this technical support? My computer isn't working!' 'Did you try turning it off and on again?' 'Yes, I tried. It didn't help!' 'Did you try hitting it?' 'I hit it. Now it won't turn on at all!'",
        "What should you do if you see a UFO? Take a picture of it. And then delete it so no one finds out you're crazy.",
        "Why don't hedgehogs fly? Because their wings are short.",
        "Wife to husband: 'Darling, I cooked dinner today according to a new recipe!' Husband: 'Wow! What kind of recipe?' Wife: 'It's called 'Something incomprehensible, but very tasty!'",
        "Two friends meet. One: 'How are you?' Second: 'Well, I'm getting married.' First: 'Congratulations! Who is she?' Second: 'Just one of those I didn't notice while I was looking for the ideal one.'"
    ],
    "holiday": [ # праздничный
        "Before New Year's, husband to wife: 'What should I get you, darling?' Wife: 'Something that will make me scream with joy!' Husband: 'Okay, a ticket to your ex's concert!'",
        "New Year. Wife to husband: 'Honey, did you buy champagne?' Husband: 'I bought it! But it seems to be for adults. It says: 'Drink only upon reaching adulthood'.' Wife: 'Well, we already are!'",
        "Santa Claus asks a boy: 'What do you want for New Year's?' Boy: 'A gift that I won't have to assemble!'",
        "At the corporate party, one employee to another: 'Do you think the boss will notice if we drink all the cognac?' Second: 'No, he'll notice if we don't drink it!'",
        "Wife to husband: 'Honey, for New Year's, give me something unforgettable!' Husband: 'Okay, I'll forget to congratulate you! And there will be no gift!'",
        "On March 8th, husband gives wife a frying pan. Wife: 'Darling, is this a new recipe?' Husband: 'No, this is a new way to convince you to cook!'",
        "Birthday. Guests tell the birthday boy: 'We wish you to have everything, and nothing for it!' And may the neighbors not hear!",
        "One friend to another: 'Last New Year, my wife gave me socks. This year - a tie. I feel like next year she'll give me a sweater so I can finally go outside and be fashionable!'",
        "Holiday. A man approaches a woman: 'Could you tell me the time?' Woman: 'Almost midnight. If you want, we can spend it together!' Man: 'Oh, no, thank you, I just wanted to know if I missed the last bus.'",
        "New Year's tree, gifts. A child pulls his father's sleeve: 'Dad, does Santa Claus exist?' Dad: 'Of course, son! Who else could bring you such a useless gift as this 1000-piece puzzle?'",
        "On New Year's, two snowmen talk. One to the other: 'Listen, aren't you afraid of melting?' Second: 'No, I'm afraid they'll remake me into a female snowman!'",
        "Why are there always dances at New Year's parties? So no one notices how much Olivier salad you ate.",
        "A man in a store before March 8th: 'Give me the biggest bouquet you have!' Salesman: 'Is she very offended?'",
        "Valentine's Day. Guy to girl: 'I love you more than my car!' Girl: 'Wow! What brand?'",
        "At the wedding, the toastmaster shouts: 'Bitter!' Guests: 'Bitter!' Groom: 'No-o-o! I'm fine!'",
        "One neighbor to another: 'How did you celebrate New Year's?' Second: 'As always. Ate, drank, slept. Then woke up, ate, drank, slept. And so on until Old New Year.'",
        "Two friends discuss holiday plans. 'I'm going to dress up as Santa and hand out gifts to children!' 'And then what?' 'And then I'll go and take them back!'",
        "A little girl writes a letter to Santa Claus: 'Dear Santa Claus! I want you to bring me a brother for New Year's. And please, don't forget a new console for me!'",
        "On Christmas, wife tells husband: 'Darling, I want you to be my Santa Claus.' Husband: 'What, as old and fat?'",
        "Guy to girl on Valentine's Day: 'I love you so much, I'm ready to do anything for you!' Girl: 'Really? Then go get some bread.'"
    ],
    "dark": [ # черный
        "Why don't children play hide-and-seek with their parents? Because parents always find them... with surveillance cameras.",
        "How do you make a corpse laugh? Tell it a joke it never heard in life.",
        "What do a schoolchild and a grave have in common? Both, if nothing is put into them, will remain empty.",
        "Why doesn't a maniac play cards? Because he always has an ace up his sleeve... and other body parts.",
        "In intensive care: 'Doctor, will he live?' 'Yes, of course. If we find a brain donor.'",
        "What does a cannibal do when he's sad? He looks for someone to cheer him up... for dinner.",
        "What toys are most dangerous for children? Those inherited from an older brother after his 'experiments'.",
        "What do autopsies do? They give us one last chance to look into the soul... or at least the stomach.",
        "The teacher asks Vovochka: 'Vovochka, why are you so dirty?' Vovochka: 'My friends and I were playing archaeologists!' Teacher: 'And what did you find?' Vovochka: 'Looks like a dinosaur! Look, I have a piece of skull on my head!'",
        "Husband to wife: 'Darling, I have two pieces of news for you: good and bad.' Wife: 'Start with the good.' Husband: 'I stopped snoring!' Wife: 'That's the bad news!'",
        "Woman in a store: 'Do you have fresh meat?' Salesman: 'Yes, just brought in!' Woman: 'Why is it moving?'",
        "What does a necromancer do when he's bored? He raises spirits.",
        "Why don't ghosts lie? Because they have nothing to hide, they're already exposed.",
        "In a mental hospital. One patient to another: 'Imagine, I found a million dollars yesterday!' Second: 'Wow! And I found a portal to a parallel world yesterday!' First: 'Cool! Where is it?' Second: 'I'll show you if you show me your million!'",
        "Funeral. One of the deceased's friends: 'He was such a kind man. Always shared.' Second: 'Yes, even his secrets with the police.'",
        "A man walks into a bar. Sees a skeleton sitting there. Asks: 'Bored?' Skeleton: 'Not really... Life is kicking, but not in the right direction.'",
        "What is 'dark humor'? It's when you laugh at something you shouldn't laugh at. And it's still funny.",
        "Why do doctors always look tired? Because they see too many people who don't want to live.",
        "Conversation between two cannibals: 'How do you like our new neighbor?' 'Well, so-so. Too many bones.'",
        "A man came to the dentist: 'Doctor, my tooth hurts!' Doctor: 'No problem, we'll extract it now!' Man: 'But it's my last tooth!' Doctor: 'Even more reason to celebrate!'"
    ],
    "life": [ # жизненный
        "Life is like a box of chocolates. Everything seems delicious, but in the end, there's always one that no one wants to finish.",
        "The only way not to make mistakes is to pretend you didn't make any.",
        "If it seems like everything is going wrong, try turning it off and on again. Sometimes it works.",
        "The older I get, the more I realize that 'going to bed early' and 'getting enough sleep' are different things. Especially when you have kids.",
        "Morning. Alarm rings. You're like: 'Oh, is it morning already? I thought it was just a continuation of the dream.'",
        "Adult life: that's when you're happy not with gifts, but with finally getting around to cleaning up, and no one noticed.",
        "If you don't know what to do, just lie down and sleep. Tomorrow is a new day, but sometimes it only makes problems worse.",
        "The hardest choice in life is 'What to watch on YouTube' after you've already watched everything useful and moved on to cat videos.",
        "Work is a place where you spend most of your life to be able to live in the remaining smaller part, trying to catch up on sleep.",
        "When you think things can't get worse, life throws not a surprise, but a second shift.",
        "Life is like a toilet: sometimes it's crap, sometimes it's water, and then you sit on it and think: 'Well, here we go again.'",
        "My diet: see food and want it. See food and want it. See food and want it.",
        "If I had one superpower, I'd choose the ability to always find the sock that got lost after washing.",
        "Adult life: that's when you buy yourself what you dreamed of as a child, and then realize you don't need it.",
        "Why is Monday so hard? Because it starts on Sunday evening.",
        "The most unpleasant thing about old age is when you forget why you went into a room, but remember you have a debt.",
        "My banquet hall is my bed, and my guests are cats.",
        "If you can't solve a problem, try to ignore it. Maybe it will solve itself, but most likely, it will just get bigger.",
        "I don't suffer from insomnia, I suffer from 'oh, another show' and 'yes, another meme'.",
        "Life is a constant waiting. First you wait for the weekend, then for vacation, then for retirement. And then - for death. Fun!"
    ],
    "computer": [ # компьютерный
        "Why don't programmers like dark themes? Because light attracts bugs, and they're already everywhere.",
        "A bug is not an error, it's an unresearched feature.",
        "Programmer: 'I have a bug in my code!' Sysadmin: 'That's not a bug, it's a 'freeze solid' function to save electricity!'",
        "How many programmers does it take to change a light bulb? None. They'll write a script that does it for them.",
        "I'm not fat, I'm just optimized for storing large data, including lunch.",
        "What is compilation? It's a magical process where your code turns into a bunch of incomprehensible symbols that still don't work.",
        "If computers had feelings, they'd cry from the number of attempts to 'fix' them by pressing all buttons at once.",
        "I tried to joke with my laptop, but it just gave 'Syntax Error' and restarted.",
        "My life is an endless loop: woke up, checked email, coded, procrastinated, coded more, slept, repeat.",
        "Two programmers meet. One: 'I have a bug here, it only appears once a week.' Second: 'Congratulations! You don't have a bug, you have a planned update!'",
        "Why do programmers have poor eyesight? Because they constantly stare at the monitor, not the real world.",
        "What is a deadline? It's a beast that always creeps up unnoticed, and then eats your free time.",
        "If you don't know how to solve a problem, try Googling it. If Google didn't help, then it's not a problem, but a feature.",
        "Conversation between two computers: 'Hello, how are you?' 'Fine, just caught a virus yesterday. Now I sneeze all the time.'",
        "Why don't programmers like going shopping? Because there's no 'Undo changes' button.",
        "I'm not lazy, I just prefer to automate everything I can.",
        "What does a programmer do when he's sad? He writes code that makes him happy... or at least compiles without errors.",
        "My computer is so old that it's faster to draw a picture in Paint than to open Photoshop.",
        "Why do programmers wear glasses? Because they see errors even in their sleep.",
        "What's the difference between a developer and a designer? A designer creates what's beautiful. A developer creates what works (and sometimes looks beautiful)."
    ],
    "school": [ # школьный
        "Teacher: 'Children, what subject do you like the most?' Vovochka: 'Sleep after lunch!'",
        "Why does a two look like a swan? Because it floats through the diary, leaving a trail behind.",
        "In chemistry class: 'Vovochka, tell me the formula for water.' Vovochka: 'H2O!' Teacher: 'Well done! And why is it H2O?' Vovochka: 'Because it's written in the textbook!'",
        "Mom to son: 'Why are you rushing so much?' Son: 'To school! I'm late for class, and there's a test!' Mom: 'So what?' Son: 'Well, what? If I get there on time, they'll give it to me!'",
        "Why do schoolchildren love Friday? Because it's the last day before the weekend when you can sleep in until noon.",
        "Teacher: 'Vovochka, how much is two plus two?' Vovochka: 'Is that with inflation?'",
        "Diary. Father: 'A two again?!' Son: 'But Dad, I tried!' Father: 'And what did you try for?' Son: 'I tried for vacation!'",
        "Geography lesson. Teacher: 'What is the largest country in the world?' Vovochka: 'My house, when I do homework!'",
        "What is algebra? It's when you learn to add letters and subtract numbers to get an incomprehensible answer.",
        "In biology class. Teacher: 'What animal can live without a head?' Student: 'Me!' Teacher: 'Why?!' Student: 'Because my head doesn't work!'",
        "Teacher: 'Petrov, why didn't you do your homework?' Petrov: 'I got sick.' Teacher: 'With what?' Petrov: 'Laziness.'",
        "Vovochka asks the teacher: 'Mary Ivanovna, can I go out for 5 minutes?' Teacher: 'Where?' Vovochka: 'I want to check if it's snowing.' Teacher: 'What if it's not?' Vovochka: 'Then I'll go home, put on my hat and gloves, and come back!'" ,
        "Mom: 'Son, have you done your homework?' Son: 'Yes, Mom.' Mom: 'Then why is there a C in the diary?' Son: 'That's not a C, Mom, that's a grade for creativity!'",
        "Teacher: 'Children, who can tell me an animal that lays eggs?' Vovochka: 'My grandmother, when her blood pressure went up!'",
        "At school. Teacher: 'Who was the first cosmonaut?' Vovochka: 'Yuri Gagarin!' Teacher: 'Correct! And who was the second?' Vovochka: 'That's a secret!'" ,
        "Teacher: 'Children, today we will study body parts.' Vovochka: 'Why do we need this?' Teacher: 'So you know where your head is and where your legs are!' Vovochka: 'But I thought my head was on my shoulders and my legs were on the floor!'" ,
        "In physical education class. Teacher: 'Children, run in a circle!' Vovochka: 'Can I sit in the center and spin?'",
        "Son: 'Dad, what is 'parental capital'?' Dad: 'That's when Dad has money and he spends it on himself!'",
        "Why do schoolchildren love holidays so much? Because it's a time when they can finally use their brains for something interesting besides studying.",
        "Dialogue between two students: 'Did you do your history homework?' 'Yes, but only up to the Middle Ages.' 'Wow! And I'm up to Napoleon!'"
    ],
    "family": [ # семейный
        "Wife to husband: 'Darling, I found a gray hair!' Husband: 'Don't worry, darling, that's experience!' Wife: 'Experience in what? In driving me to gray hair while you're still a brunette?!'",
        "Children are the flowers of life. But for some reason, you have to water them with money and fertilize them with nerves.",
        "A man calls his wife: 'Darling, I'm stuck in traffic! I'll probably be an hour!' Wife: 'Don't lie, I can hear you snoring on the couch!'",
        "Family dinner. Child: 'Mom, why is Dad bald?' Mom: 'Because he thinks a lot.' Child: 'And why do you have hair?' Mom: 'Because I think about you!'",
        "How do you know you're married? When you say 'we' and you mean 'she,' and when you say 'I,' you mean 'no one.'",
        "Wife: 'Darling, I cleaned so well yesterday! Everything sparkles!' Husband: 'Yes, darling, I noticed. Even the vacuum cleaner is sparkling with bewilderment!'",
        "Husband to wife: 'You know, I'm afraid of dentists?' Wife: 'I know, darling. That's why I married you - you're the only one who opens his mouth only when he sleeps, or when he eats my borsch!'",
        "Dad tells son: 'Son, remember, never take other people's things! And if you do, return them quickly!' Son: 'What about other people's toys?' Dad: 'Then play with them until the very end!'",
        "Mom calls son: 'Come eat lunch!' Son: 'I don't want to, I already ate!' Mom: 'Well, who's going to finish your portion for you?!'",
        "Wife to husband: 'Darling, I cooked dinner today!' Husband: 'Wow! What's the occasion?' Wife: 'The occasion is hunger!'",
        "Conversation between two girlfriends: 'My husband is such a romantic! For our anniversary, he gave me a bouquet of 100 roses!' 'And my husband gave me a bucket of potatoes! Said it was practical!'",
        "Children are such a joy that when they fall asleep, you feel your strength return to you.",
        "Husband to wife: 'Darling, I bought you something beautiful and expensive.' Wife: 'What is it?' Husband: 'A bus ticket so you can go to the shopping center!'",
        "Grandma to grandson: 'In our time, to get married, you had to be a good housekeeper, know how to cook, sew...' Grandson: 'And now, grandma, you need to know how to code and earn money!'",
        "At a family dinner. Son: 'Dad, were you ever young?' Dad: 'Of course! And even handsome!'",
        "Why do children always ask 'Why?' when you tell them something? Because they know the answer is often illogical.",
        "Husband: 'Darling, I love you!' Wife: 'And I love you even more!' Husband: 'No, I love you more!' Wife: 'Well, okay, I agree. The main thing is you admitted it!'",
        "Grandfather to granddaughter: 'Granddaughter, do you know why I have a gray beard?' Granddaughter: 'Because you're old, grandpa!'",
        "Wife to husband: 'Darling, I gained 5 kg!' Husband: 'Don't worry, darling, you just became more voluminous!'",
        "Mom: 'Son, why are you so sad?' Son: 'A girl rejected me.' Mom: 'Don't worry, son! You'll find another one who will love you! And who will look like me!'"
    ],
    "about animals": [ # про животных
        "A hare sits under a fir tree, trembling. A wolf runs by: 'Hare, why are you trembling?' Hare: 'Winter, it's cold!' Wolf: 'Then run!' Hare: 'If I run, I'll get eaten!'",
        "Cow: 'Moo-o-o!' Hare: 'Meow-o-o!' Wolf: 'What's wrong, Hare?' Hare: 'I'm just practicing! I want to become a cat!'",
        "Why don't elephants play hide-and-seek? Because their ears are too big to hide behind a tree.",
        "A lion in the zoo sadly looks at visitors. One of them asks: 'Sad?' Lion: 'Yeah, I'm waiting for my lunch. These tourists are suspiciously photogenic.'",
        "A fox runs through the forest, with a hunter behind it. Fox: 'Oh, what an idiot? I told him I'm on a diet!'",
        "What does one cat say to another when they meet? 'Meow! Where did you get so fluffy?'",
        "Why don't giraffes play basketball? Because it's hard for them to reach the ball without breaking their neck.",
        "A bear walks through the forest, sees a hare smoking. Bear: 'Hare, what are you smoking?' Hare: 'Grass!' Bear: 'Let me try!' Hare: 'No way! It's for me alone!'",
        "A crow sits on a tree with a piece of cheese. A fox approaches: 'Crow, sing me a song!' Crow: 'Caw-caw!' (cheese falls). Fox: 'Ha-ha! Fool!' Crow: 'But I sing, and you don't!'",
        "Two fish in an aquarium. One: 'How are you?' Second: 'Fine, only my head hurts from this glass.'",
        "Why don't sharks like computers? Because they constantly 'hang'!",
        "A man walks into a zoo, sees an elephant. Says: 'Wow, how huge!' Keeper: 'Yes, he's been on a diet recently!' Man: 'And does it help?' Keeper: 'No, he just got hungrier!'",
        "Why don't parrots go to school? Because they already know everything!",
        "A bear walks into a bar: 'Beer and nuts for me!' Bartender: 'Why so rude?' Bear: 'I'm a bear! I can afford to be rude!'",
        "What does a dog say when it's hungry? 'Woof-woof! Feed me!'",
        "Why do cats sleep so much? Because they're saving energy for night races around the apartment.",
        "A hamster runs in a wheel. A mouse watches: 'Where are you rushing?' Hamster: 'I'm running towards my dream!'",
        "Two mosquitoes talk. One: 'How was your summer?' Second: 'Great! I rested at the Sanatorium 'Blood-Thirsty!''",
        "Why don't penguins fly? Because they are too stylish to mess up their feathers in the air.",
        "What does a chameleon do when it's sad? It changes color to gray and blends in with the wall."
    ],
    "philosophical": [ # философский
        "If you don't know where you're going, any road will take you anywhere. The main thing is there's Wi-Fi along the way.",
        "Life is a box of chocolates. You never know what you'll pick, but you'll always eat the one with nuts first.",
        "We live to work. And we work to live. A vicious circle. And where's the lunch break in all this?",
        "The only way to understand life is to live it. Preferably with good coffee.",
        "Happiness is not a destination, but a way of traveling. Especially if the journey is to the couch.",
        "If you want to change the world, start with yourself. And then, maybe, change your Wi-Fi password.",
        "What is truth? What you yourself consider truth until you read Wikipedia.",
        "When you think you know everything, life throws a new lesson. And that lesson is usually very boring.",
        "Time is an illusion. Especially when you're waiting for a video to load.",
        "The biggest tragedy in life is not that you didn't reach your goal, but that you had no goal other than to finish watching a TV series.",
        "We are all specks of dust in this huge world. Some specks of dust are very dusty.",
        "If you have a dream, go for it. If you can't walk, crawl. If you can't crawl, lie down and sleep in the direction of your dream.",
        "The meaning of life is to find your meaning of life. And for it not to be at work.",
        "Why do we ask questions that have no answers? Because we're bored.",
        "Every morning is a new chance to start over. And every evening is a chance to regret not starting.",
        "Life is a game. And we are characters in it who constantly lose saves.",
        "What's the point of life if you're going to die anyway? The point is to have time to eat delicious food and watch all the movies.",
        "We are in such a hurry to live that we forget why we are living. And then we wonder why everything ended so quickly.",
        "Philosophy is when you ask questions that have no answers, and then you wonder why everyone looks at you strangely.",
        "If I had a chance to talk to my past self, I'd say: 'Don't eat that pizza. And buy Bitcoin.'"
    ],
    "about food": [ # про еду
        "Why don't chefs like diets? Because they stop them from enjoying life and trying all their masterpieces.",
        "What is 'healthy eating'? It's when you eat whatever you want, but only after you've eaten broccoli.",
        "Husband to wife: 'Darling, what's for dinner?' Wife: 'Nothing!' Husband: 'Wow! Something diet? Or did we forget to buy food again?'",
        "Why doesn't bread like water? Because it's afraid of becoming wet, sticky, and tasteless.",
        "The most delicious sandwich is the one someone made for you. And which you eat when no one is looking.",
        "One chef to another: 'I came up with a new recipe!' Second: 'And what's in it?' First: 'Apple pie. Without apples. And without pie.'",
        "What does a refrigerator do when it's empty? It starts to hum and hint that it's time to go to the store.",
        "When you're hungry, everything seems delicious. Especially someone else's sandwich that you just stole.",
        "What's the difference between dinner and breakfast? You can have dinner for dinner, but not breakfast. Only have breakfast.",
        "What is dessert? It's what you eat after a meal to forget that you just ate and start thinking about the next meal.",
        "I'm on a diet. I only eat what fits in my mouth. And a lot fits.",
        "Why is soup so liquid? Because it's shy about being thick.",
        "Husband: 'Darling, what's for lunch?' Wife: 'We have leftover dinner from yesterday.' Husband: 'Oh! That's my favorite kind of food!'",
        "How do you eat pizza correctly? First eat the crust, then the cheese, then everything else. Or just eat it however you can.",
        "If you want to lose weight, just close your eyes. And don't eat.",
        "What does a dumpling do when it's bored? It floats in the pot and waits to be eaten.",
        "Why are candies so delicious? Because they consist of happiness and sugar.",
        "A person walks into a restaurant. They are told: 'We brought you the most exquisite soup!' He looks: 'Where's the spoon?' They say: 'Sorry, we forgot it. Drink it like that!'",
        "My favorite food is food that doesn't require cooking.",
        "Dialogue in a cafe: 'Do you have anything that will help me forget about my problems?' 'Of course! Here's a double portion of tiramisu!'"
    ]
}
math_operations = {
    'plus': lambda x, y: x + y, '+': lambda x, y: x + y,
    'minus': lambda x, y: x - y, '-': lambda x, y: x - y,
    'multiply': lambda x, y: x * y, '*': lambda x, y: x * y, # 'умножить' -> 'multiply'
    'divide': lambda x, y: x / y, '/': lambda x, y: x / y, # 'поделить' -> 'divide'
    'power': lambda x,y: pow(x,y), '**': lambda x,y: pow(x,y), # 'степень' -> 'power'
    'root': lambda x, y: x**(1/y) if y != 0 else float('inf') if x > 0 else float('nan') # 'корень' -> 'root'
}
told_anecdotes = {category: [] for category in anecdotes_categories}
anecdotes_category_list = ', '.join(anecdotes_categories.keys())

math_manual = (
    f'\n[1] Syntax: type "{chat_bot_key_phrase[0]}" and specify the 1st number, operand, 2nd number respectively: "{chat_bot_key_phrase[0]} 2 divide 2";'
    f'\n[2] Incorrect writing of elements, '
    f'\n     (1st number and 2nd number): real numbers (integers, fractions, positive, negative, and zero),'
    f'\n     (operand): plus, +, minus, -, divide, /, multiply, *, power, **, root;'
    f'\n[3] Incorrectly written floating point, (.)=ok;'
    f'\n[4] Values indices do not match;'
    f'\n[5] Cannot divide by zero, and cannot specify zero as the root degree;'
)
anecdote_manual = (
    f'\n[1] Syntax: type "{chat_bot_key_phrase[1]}" and specify a category: "{chat_bot_key_phrase[1]} funny";'
    f'\n[2] Available categories: funny, holiday, dark, life, computer, school, family, about animals, philosophical, about food'
)
sphere_rand_manual = (
    f'\n[1] Syntax: type "{chat_bot_key_phrase[2]}" and specify an action: "{chat_bot_key_phrase[2]} !choose (1st elem. phrase) or (2nd elem. phrase)";'
    f'\n[2] Available actions:'
    f'\n[3] !info "text": Sphere randomly gives a % chance.' # 'инфа' -> 'info'
    f'\n[4] !choose "first" or "second": Sphere will choose one of the proposed.' # 'выбери' -> 'choose'
    f'\n[5] !yesno "question": Sphere will choose yes / no / uncertain.' # 'данет' -> 'yesno'
    )

math_num_phrase = [
    'Result: '
]
tell_anecdot_phrase = [
    'It seems I have told all anecdotes in the category ',
    '\nStarting over. Here is another one: \n',
    'Sorry, I do not know anecdotes on the topic: ',
    '\nTry one of the following categories: '
]
sphere_phrase = [
    '!info', 
    '!choose', 
    'or', 
    '!yesno', 
    'Sphere says: The probability that, ',
    ' is ',
    'Sphere says: I see truth in darkness and feel that, ',
    'yes',
    'no',
    'uncertain',
    'Sphere says: I think that, ',
    f'\n[1] You entered an insufficient number of phrases, enter two for the sphere to choose;\n[2] To understand the syntax type "{chat_bot_key_phrase[2]}";',
    f'\n[1] You incorrectly entered the 2nd keyword;\n[2] To understand the syntax type "{chat_bot_key_phrase[2]}";'
]