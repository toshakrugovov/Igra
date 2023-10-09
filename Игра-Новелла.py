import time


def clear_screen():
    print("\033[H\033[J")

def display_text(text, speed=0.001):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()

def display_print(text):
    clear_screen()
    display_text(text)
    time.sleep(1)
    

c = 0
def func(): 
    global c
    c += 1
    return c


display_print("Загадочный студент: \"Дорогой друг, ты вошёл в игру - новеллу 'Тайна забытого храма'\"")
clear_screen() 

znakomstvo = input("Пришло время, чтобы познакомиться \n"
                   "Загадочный студент: \"Как тебя зовут? \" ")

display_print("Загадочный студент: \"Приятно познакомиться, "+ znakomstvo + "!\"")

display_print("Вы отправляетесь в захватывающее приключение, чтобы раскрыть тайну забытого храма.\n"
              "Вам предстоит решать загадки, исследовать таинственные комнаты и принимать решения,\n"
              "Которые будут влиять на ваш прогресс и итоговый результат.\n")
display_print("На начало игры Ваш прогресс составляет: ") 
print (c)   
time.sleep(1)
clear_screen() 

display_print("Вы — известный археолог, специализирующийся на исследовании древних храмов.\n"
              "Ваше последнее открытие — древний храм, о котором никто не знал.\n"
              "По легенде, внутри храма находится мощь, способная исполнить любое желание.\n"
              "Вы отправляетесь в путешествие, чтобы разгадать загадки храма и найти эту мощь.\n")
clear_screen()

display_print("Глава 1: Вход в храм\n"
              
              "Вы стоите перед входом в древний храм. Вам нужно решить первую загадку, чтобы войти в храм и получить XP.\n")



while True:
            try:
                display_print("Загадка: \"Что можно взять в руки, но нельзя увидеть?\"")
                spisok1 = ["  1) Воздух \n", " 2) Любовь  \n", " 3) Время   \n", " 4) Музыку    \n"]
                print(spisok1[0], spisok1[1],spisok1[2],spisok1[3])
                lox = int(input("Выбери правильный ответ: "))
                break
                    
            
            except ValueError:
                print("Загадочный студент: \"Дорогой юзер, повтори попытку\"")
                
if lox == 1:
     display_print("Загадочный студент: \"Молодец! Ты разгадал загадку и получаешь 50XP к прогрессу\"")
     display_print("Твой прогресс:  ") 
     c += 50
     print(c)
     time.sleep(1)
    
if lox == 2:
     display_print("Загадочный студент: \"К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\"")
     display_print("Твой прогресс:  ") 
     print(c)
     time.sleep(1)

if lox == 3:
     display_print("Загадочный студент: \"К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\"")
     display_print("Твой прогресс:  ") 
     print(c)
     time.sleep(1)
     
if lox == 4:
     display_print("Загадочный студент: \"К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\"")
     display_print("Твой прогресс:  ") 
     print(c)
     time.sleep(1)
     
     
     
display_print("Глава 2: Зал с тремя дверьми\n"
              "Вы входите в зал с тремя дверьми.\n"
              "На каждой двери есть загадка и тебе надо их разгадать, чтобы набрать больше XP прогресса\n")

while True:
            try:
                display_print("Загадка (первая дверь): \"Что имеет корни, но не может расти?\"")
                spisok1 = ["  1) Дерево \n", " 2) Река  \n", " 3) Математическое уравнение   \n", " 4) Зубы    \n"]
                print(spisok1[0], spisok1[1],spisok1[2],spisok1[3])
                lox = int(input("Выбери правильный ответ: "))
                break
                    
            
            except ValueError:
                print("Загадочный студент: \"Дорогой юзер, повтори попытку\"")
                
if lox == 1:
     display_print("Загадочный студент: \"К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\"")
     display_print("Твой прогресс:  ") 
     print(c)
     time.sleep(1)
    
if lox == 2:
     display_print("Загадочный студент: \"К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\"")
     display_print("Твой прогресс:  ") 
     print(c)
     time.sleep(1)

if lox == 3:
    display_print("Загадочный студент: \"Молодец! Ты разгадал загадку и получаешь 50XP к прогрессу\"")
    display_print("Твой прогресс:  ") 
    c += 50
    print(c)
    time.sleep(1)
     
if lox == 4:
     display_print("Загадочный студент: \"К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\"")
     display_print("Твой прогресс:  ") 
     print(c)
     time.sleep(1)

while True:
            try:
                display_print("Загадка (вторая дверь): \"Что всегда уходит, но никогда не возвращается?\"")
                spisok1 = ["  1) Время \n", " 2) Деньги \n", " 3) Возможность  \n", " 4) Отец    \n"]
                print(spisok1[0], spisok1[1],spisok1[2],spisok1[3])
                lox = int(input("Выбери правильный ответ: "))
                break
                    
            
            except ValueError:
                print("Загадочный студент: \"Дорогой юзер, повтори попытку\"")
                
if lox == 1:
    display_print("Загадочный студент: \"Молодец! Ты разгадал загадку и получаешь 50XP к прогрессу\"")
    display_print("Твой прогресс:  ") 
    c += 50
    print(c)
    time.sleep(1)
    
if lox == 2:
     display_print("Загадочный студент: \"К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\"")
     display_print("Твой прогресс:  ") 
     print(c)
     time.sleep(1)

if lox == 3:
   display_print("Загадочный студент: \"К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\"")
   display_print("Твой прогресс:  ") 
   print(c)
   time.sleep(1)
     
if lox == 4:
     display_print("Загадочный студент: \"Отец, иногда возвращается (ха-ха)\n"
                   "К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\"")
     display_print("Твой прогресс:  ") 
     print(c)
     time.sleep(1)
     
while True:
            try:
                display_print("Загадка (третья дверь): \"Что  поднимается вверх, когда идёт дождь?\"")
                spisok1 = ["  1) Облака \n", " 2) Вода \n", " 3) Дым с курилки у МПТ  \n", " 4) Пар    \n"]
                print(spisok1[0], spisok1[1],spisok1[2],spisok1[3])
                lox = int(input("Выбери правильный ответ: "))
                break
                    
            
            except ValueError:
                print("Загадочный студент: \"Дорогой юзер, повтори попытку\"")

if lox == 1:
    display_print("Загадочный студент: \"К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\"")
    display_print("Твой прогресс:  ") 
    print(c)
    time.sleep(1)
    
if lox == 2:
     display_print("Загадочный студент: \"К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\"")
     display_print("Твой прогресс:  ") 
     print(c)
     time.sleep(1)

if lox == 3:
    display_print("Загадочный студент: \"К сожалению, ты не разгадал мою загадку, но за хорошее чувство юмора лови 20XP\"")
    display_print("Твой прогресс:  ") 
    c += 20
    print(c)
    time.sleep(1)
     
if lox == 4:
    display_print("Загадочный студент: \"Молодец! Ты разгадал загадку и получаешь  50XP к прогрессу\"")
    display_print("Твой прогресс:  ") 
    c += 50
    print(c)
    time.sleep(1)
     
display_print("Глава 3: Зал с ловушками\n"
              "Вы входите в зал с ловушками.\n"
              "Вам нужно выбрать правильный путь, чтобы избежать опасности и продолжить свой путь.")

while True:
            try:
                display_print("Загадка: \"Какой ключ откроет любую дверь?\"")
                spisok1 = ["  1) Золотой \n", " 2) Магический \n", " 3) Мастерский  \n", " 4) Лом    \n"]
                print(spisok1[0], spisok1[1],spisok1[2],spisok1[3])
                lox = int(input("Выбери правильный ответ: "))
                break
                    
            
            except ValueError:
                print("Загадочный студент: \"Дорогой юзер, повтори попытку\"")
                
if lox == 1:
    display_print("Загадочный студент: \"Ты в ловушке. Твой прогресс обнуляется. Глупец!!!\"")
    display_print("Твой прогресс:  ") 
    c = 0 
    print(c)
    time.sleep(1)
    
if lox == 2:
     display_print("Загадочный студент: \" Ты в ловушке. Твой прогресс обнуляется. Глупец!!!\"")
     display_print("Твой прогресс:  ") 
     c = 0 
     print(c)
     time.sleep(1)

if lox == 3:
    display_print("Загадочный студент: \"Молодец! Ты разгадал загадку и получаешь 50XP к прогрессу\"")
    display_print("Твой прогресс:  ") 
    c += 50
    print(c)
    time.sleep(1)
     
if lox == 4:
    display_print("Загадочный студент: \"Конечно же ты это неправильный ответ, но лом спобобен намногое. Лови бонус.\"")
    display_print("Твой прогресс:  ") 
    c += 10
    print(c)
    time.sleep(1)
    
display_print("Глава 4: Секретная комната\n"
              "Вы находите секретную комнату храма.\n"
              "В ней вы видите алтарь с мощью, которая может исполнить желание.\n"
              "Однако, перед тем как взять мощь, вам нужно пройти последнюю загадку.\n")


while True:
            try:
                display_print("Загадочный студент: \" Сейчас последняя загадка соберись!!!\"")
                clear_screen() 
                display_print("Последняя загадка: \n"
                              "В глубине леса, в темной пещере, \n"
                              "Сокровище спрятано, не для всех смертных \n"
                              "Оно кишит золотом и драгоценностями ,\n"
                              "Но только тот, кто выберет правильный путь достоин его!\n")
                display_print("Загадочный студент: \" Выбери дорогу, которая приведет к нему:\"")
                spisok1 = ["  1) Путь из камней и грязи, полный испытаний \n", " 2) Тропа из цветов и ароматов, но скользкая и опасная \n",
                           " 3) Тропинка из песка и пыли, сухая и безжизненная  \n", " 4) Путь от МПТ (Нежинская) до МПТ (Нахимовский) в 8:00   \n"]
                print(spisok1[0], spisok1[1],spisok1[2],spisok1[3])
                lox = int(input("Выбери правильный ответ: "))
                break
                    
            
            except ValueError:
                print("Загадочный студент: \"Дорогой юзер, повтори попытку\"")
                
if lox == 1:
    display_print("Загадочный студент: \"Молодец! Ты разгадал загадку и получаешь 50XP к прогрессу\"")
    display_print("Твой прогресс:  ") 
    c += 50
    print(c)
    time.sleep(1)
    

if lox == 2:
     luser = {"Лох": "Загадочный студент: \"К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\""}
     print(luser["Лох"])
     time.sleep(1)
     display_print("Твой прогресс:  ") 
     print(c)
     time.sleep(1)

if lox == 3:
     display_print("Загадочный студент: \"К сожалению, ты не разгадал мою загадку и ничего не получаешь. Глупец!!!\"")
     display_print("Твой прогресс:  ") 
     print(c)
     time.sleep(1)
     
if lox == 4:
    display_print("Загадочный студент: \"Шутки шутками, но твой прогресс сгорает (ха-ха) \"")
    c = 0
    display_print(f"Твой прогресс: {c} ") 
    
    time.sleep(1)
     
display_print("Загадочный студент: \"Поздравляю, ты прошёл игру.\"\n"
              "Осталость узнать кто ты по масти и получаешь ли мощь ")
display_print("Разновидности мастей: \n"
              "менее 20 XP - ты лузер и потерялся в забытом храме\n"
              "50 - 90XP - ты мог лучше, но ты получаешь мощь и статус 'Новичок'\n"
              "90 - 200XP - ты хорошшшш, получаешь мощь и статус 'Любитель'\n"
              "200 - 300XP - ты ультра,  мега, хорош, получаешь мощь и статус'Дядька на опыте'\n ")


display_print("Твой прогресс к концу игры: ")
print(c)
time.sleep(1)

if c <= 20 :
    display_print("ты лузер и потерялся в забытом храме")
    
if 50<=c<=90:
    display_print("ты мог лучше, но ты получаешь мощь и статус 'Новичок'")
    
if 90<=c<=200:
    display_print("ты хорошшшш, получаешь мощь и статус 'Любитель'")
    
if 200<=c<=300:
    display_print(" ты ультра,  мега, хорош, получаешь мощь и статус 'Дядька на опыте'")
    
display_print("Конец!!!")