import random
import time
name = input("Введите свое имя: ")
print("Загрузка... Пожалуйста, подождите!")
time.sleep(3)
print("Прогрузка модулей...")
time.sleep(1)
print("Загрузка персонажа...")
time.sleep(2)
nazvanie = input("Добро пожаловать, {}! Вы - будущий диктатор небольшого, но перспективного государства. Введите название своей страны: ".format(name))
print("Теперь вся власть над страной в ваших руках. Править страной не так просто, как кажется. Вам предстоит грамотно балансировать между четырьмя фракциями и бюджетом. Что хорошо одним - плохо другим. В зависимости от Ваших решений фракциям будут добавляться/отниматься очки доверия. Если к концу года доверие любой фракции будет равным 0 или 10, Вас свергнут. Поэтому каждый год Вам надо будет принимать сложные решения, от которых зависит судьба Вашей державы. Также будут происходить события, на ход которых вы не сможете повлиять.")
print("Технические правила: Вы можете отвечать 'да' или 'Да', если согласны, и 'нет' или 'Нет' при отказе. Также в определённых вопросах Вам необходимо будет ввести натуральное число.")
ready = input("Вы готовы, дикататор? ")
if ready == "нет" or ready == "Нет":
    print("Вы проиграли, хоть и начать-то не успели. Мда.")
    time.sleep(1917)
year=0
years=0
jhjh=random.randrange(0,2)
uroven=int(input("Выберите уровень сложности. 1 - легкий, 2 - средний, 3 - тру хардкор, 4 - мне повезёт! "))
if uroven == 1:
    narod=5
    liberal=5
    aligarx=5
    army=5
    bank=4000
elif uroven==2:
    if jhjh==0:
        narod=random.randrange(3,5)
        liberal=random.randrange(3,5)
        army=random.randrange(3,5)
        aligarx=random.randrange(3,5)
        bank=random.randrange(1500,2500)
    else:
        narod=random.randrange(6,8)
        liberal=random.randrange(6,8)
        army=random.randrange(6,8)
        aligarx=random.randrange(6,8)
        bank=random.randrange(1500,2500)
           
elif uroven==3:
    if jhjh==0:
        narod=random.randrange(2,4)
        liberal=random.randrange(2,4)
        army=random.randrange(2,4)
        aligarx=random.randrange(2,4)
        bank=random.randrange(1000,1500)
    else:
        narod=random.randrange(7,9)
        liberal=random.randrange(7,9)
        army=random.randrange(7,9)
        aligarx=random.randrange(7,9)
        bank=random.randrange(1000,1500)
else:
    narod=random.randrange(2,8)
    liberal=random.randrange(2,8)
    army=random.randrange(2,8)
    aligarx=random.randrange(2,8)
    bank=random.randrange(800,3000)
print("Народ:",narod)
print("Армия:",army)
print("Олигарх:",aligarx)
print("Либералы:",liberal)
print("Банк:",bank)
while year < 60:
    k = year % 10
    if (year>9)and(year<20)or(year>110)or(k>4)or(k==0):
        l = "лет"
    else:
        if k==1:
            l = "год"
        else:
            l = "года"
    print("Вы правите уже {} {}".format(years,l))
    year += 1
    years+=1
    slych = ["Вы обратились к народу.","Неизвестным был убит известный олигарх, поддерживавший власть и помогавший в борьбе с оппозицией.","В небольшом городе произошла техногенная катастрофа.","Военнослужащие помогли в борьбе с крупным пожаром."] #Случайные события
    sl = random.randrange(0,10)
    if random.randrange(0,5) == 0:
        le = random.randrange(1,100)
        ke = random.randrange(1,100)
        print("Ваш геолог обнаружил потенциальное месторождение нефти. Хотите ли вы вложится в его развитие(300 дублон), и потенциально получить доход(прямо сразу).Шанс на успех: {}%".format(le))
        v = input("Согласны? ")
        if v == "Да" or v == "да":
            time.sleep(2)
            if le >= ke:
                print("Успех!")
                bank+=random.randrange(600,1000)
            else:
                print("Не получилось")
                bank+=-300
        else:
            print("Вы отказались")
        print("Ваши деньги: ",bank)
    if sl == 0:
        print(slych[0])
        time.sleep(0.5)
        narod += 1
        liberal += random.randrange(0,1)
        army += 1
        aligarx += 1
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
    elif sl == 1:
        print(slych[1])
        time.sleep(0.5)
        aligarx -= 1
        liberal += 1
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank) 
        time.sleep(1)              
    elif sl == 2:
        print(slych[2])
        time.sleep(0.5)
        narod -= 1 
        bank -= random.randrange(300,500)
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)     
    elif sl == 3:
        print(slych[3])
        time.sleep(0.5)
        army += 1
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
             
    vopros1=input("Хотите ли вы собрать налоги со всего населения страны? ")
    if vopros1=="да" or vopros1=="Да":
        time.sleep(0.5)
        army-=1
        narod-=1
        aligarx-=1
        liberal-=1
        bank+=random.randrange(300,600)
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
    else:
        print("В этом году вы не собирали налоги")
        time.sleep(0.5)
        narod+=1
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
    vopros2=input("Хотите ли вы повысть влияние своей семьи? ")
    if vopros2=="Да" or  vopros2=="да":
        time.sleep(0.5)
        aligarx+=1
        narod-=1
        liberal-=random.randrange(1,2)
        army-=random.randrange(0,1)
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
        
    else:
        time.sleep(0.5)
        aligarx-=random.randrange(1,3)
        narod+=1
        liberal+=random.randrange(0,2)
        army+=random.randrange(0,1)
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
    vopros3=input("Хотите ли вы вложится в развитие социальных сфер державы? ")
    if vopros3=="Да" or vopros3=="да":
        time.sleep(0.5)
        bank-=random.randrange(150,450)
        narod+=1
        liberal+=random.randrange(1,3)
        army+=random.randrange(0,1)
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
    else:
        time.sleep(0.5)
        narod-=1
        liberal-=random.randrange(1,2)
        army-=random.randrange(0,1)
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
    vopros4=input("Будем ли развивать торговлю с бывшими врагами?")
    if vopros4=="Да" or vopros4=="да":
        time.sleep(0.5)
        army-=random.randrange(1,2)
        narod-=1
        liberal+=random.randrange(1,2)
        aligarx+=1
        bank+=150
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
    else:
        time.sleep(0.5)
        army+=random.randrange(1,2)
        narod+=1
        liberal-=random.randrange(1,2)
        aligarx-=1
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
    
        
    a = ["Провести военный парад с новой техникой?", "Инвестировать в бизнес крупного олигарха?", "Разрешить однополые браки?"] #Артем Я
    b = random.randrange(0,5)
    if b == 0:
        p = input(a[b])
        if p == "Да" or p == "да":
            time.sleep(0.5)
            nar = random.randrange(0,2)
            arm = random.randrange(0,1)
            narod += nar
            army -= arm
            bank -= random.randrange(500,1000)
            print("Народ:",narod)
            print("Армия:",army)
            print("Олигарх:",aligarx)
            print("Либералы:",liberal)
            print("Банк:",bank)
            time.sleep(1)
        elif p== "нет" or p == "Нет":
            print("Сегодня марши на площади греметь не будут.")
    if b == 1:
        p = input(a[b])
        if p == "Да" or p == "да" :
            time.sleep(0.5)
            alg = random.randrange(1,2)
            aligarx += alg
            bank -= random.randrange(500,2000)
            print("Народ:",narod)
            print("Армия:",army)
            print("Олигарх:",aligarx)
            print("Либералы:",liberal)
            print("Банк:",bank)
        elif p== "нет" or p=="Нет":
            print("Во вливании гос.средств отказано. Обойдется.")
            
    if b == 2:
        p = input(a[b])
        if p == "Да" or p == "да":
            time.sleep(0.5)
            lib = random.randrange(0,1)
            liberal += lib
            narod -= 1
            bank += random.randrange(1000,2500)
            print("Народ:",narod)
            print("Армия:",army)
            print("Олигарх:",aligarx)
            print("Либералы:",liberal)
            print("Банк:",bank)
            time.sleep(1)
        elif p== "нет" or p=="Нет":
            time.sleep(0.5)
            print("Наш народ в замешательстве, но правительства демократических стран шлют нам похвалу и средства.")
    slych2 = ["Произошёл террористический акт, погибщие и раненые.","На главном стадионе страны при поддержке метсных властей проведён концерт известной иностранной муз. группы.","Учёный из нашей страны получил крупную премию."] 
    s2 = random.randrange(0,2)
    if s2 == 0:
        print(slych2[0])
        time.sleep(0.5)
        narod -= 1
        bank -= 500
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)        
    elif s2 == 1:
        print(slych2[1])
        time.sleep(0.5)
        narod += 1
        bank += 250
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
             
    elif s2 == 2:
        print(slych2[2])
        time.sleep(0.5)
        bank += random.randrange(200,350)
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
             
    slych3 = ["На территории страны обнаружен древний город, за исследования мы можем брать большую плату.","Учёные создали новый военный самолёт. Правда дорогой.","Построен патриотический музей."]
    sl3 = random.randrange(0,10)
    if sl3 == 0:
        print(slych3[0])
        time.sleep(0.5)
        bank += random.randrange(300,500)
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)         
        time.sleep(1)  
    elif sl3 == 1:
        print(slych3[1])
        time.sleep(0.5)   
        bank -= random.randrange(300,500)
        army += 1
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
             
    elif sl3 == 2:
        print(slych3[2])
        time.sleep(0.5)
        bank -= random.randrange(100, 200)
        narod += 1
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
    voina = random.randrange(0,5)
    if voina == 1:
        pop1 = random.randrange(1,100)
        lop = random.randrange(1,100)
        print("Ваша страна оказалась на пороге войны. Злобный интроверт провоцирует вас начать боевые действия. Шанс на успех {}%".format(pop1))
        tup = input("Начать войну? ")
        if tup == "да" or tup == "Да":
            time.sleep(2)
            if pop1 >= lop:
                print("Вы победили в войне! Поздравляем!")
                narod+=1
                army+=1
                liberal+=1
                aligarx+=1
                bank+=random.randrange(400,700)
                print("Народ:",narod)
                print("Армия:",army)
                print("Олигарх:",aligarx)
                print("Либералы:",liberal)
                print("Банк:",bank)
                time.sleep(0.5)
            else:
                time.sleep(2)
                print("Вы проиграли войну, увы.")
                narod-=1
                army-=1
                liberal-=1
                aligarx-=1
                bank-=random.randrange(700,1000)
                print("Народ:",narod)
                print("Армия:",army)
                print("Олигарх:",aligarx)
                print("Либералы:",liberal)
                print("Банк:",bank)
                time.sleep(0.5)
        else:
            print("Вы не повелись на провокации врага и избежали войны")
            narod+=1
            army-=1
            time.sleep(0.5)
    slych4 = ["Олигарх связался с либералами. Это предательство.","Народ вышел на акцию протеста, скорее всего это устроили либералы.","Проведены масштабные учения армии. Поднят патриотический настрой населения."]
    sl4 = random.randrange(0,10)
    if sl4 == 0:
        print(slych4[0])
        time.sleep(0.5)
        aligarx -= 1
        liberal += 1
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
    elif sl4 == 1:
        print(slych4[1])
        time.sleep(0.5)
        liberal += 2
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)     
    elif sl4 == 2:
        print(slych4[2])
        time.sleep(0.5)
        army += 1
        narod +=1
        liberal -= 1
        bank -= 1500
        print("Народ:",narod)
        print("Армия:",army)
        print("Олигарх:",aligarx)
        print("Либералы:",liberal)
        print("Банк:",bank)
        time.sleep(1)
             
    print("Вот итоги ваших усилий за {} {} правления.".format(years,"год"))#Заодно можно попробовать сделать сравнение с предыдущим годом и высказать пожелания для следущего года    
    print("Народ:",narod)
    print("Армия:",army)
    print("Олигарх:",aligarx)
    print("Либералы:",liberal)
    print("Банк:", bank)
    time.sleep(3)
    
    if narod == 1:
        sel = input("Народ Вас возненавидел и готов устроить революцию. Хотите выделить деньги на его успокоение?")#Артем Я
        if sel == "да" or sel ==  "Да":
            print("Ну что ж, Вы идёте в правильном направлении.")
            print("Теперь давайте подумаем о сумме денег.")
            print("Сколько Вы готовы отдать? Чем больше, тем лучше.")
            pop = int(input("Снять:"))
            if pop > bank:
                  print("К сожалению, у Вас не достаточно средств. Удачи в следующем году!")
            elif pop < 500:
                  proc = random.randrange(0,70)
                  if proc < 50:
                      print("Этого было недостаточно для улучшения положения.")
                  else:
                      narod += random.randrange(1,2)
                      print("Вы оказались везунчиком, и народ немного притих.")
            elif pop >= 500:
                  proc = random.randrange(40,100)
                  if proc < 50:
                      print("Вы вложили много денег, но видимо сегодня не Ваш день, и народ не успокоился.")
                  else:
                      print("А вы хороший инвестор!")
                      narod += random.randrange(2,3)
        else:
            print("Народ явно возненавидит Вас и сместит власть в первом попавшемся случае!")
    if army == 1:
        sel = input("Армия в ярости от произвола командования. Готовится военный переворот. Хотите выделить деньги на их успокоение?")
        if sel == "да" or sel == "Да":
            print("Ну что ж, Вы идёте в правильном направлении.")
            print("Теперь давайте подумаем о сумме денег.")
            print("Сколько Вы готовы отдать? Чем больше, тем лучше.")
            pop = int(input("Снять:"))
            if pop > bank:
                  print("К сожалению, у Вас не достаточно средств. Удачи в следующем году!")
            elif pop < 800:
                  proc = random.randrange(0,70)
                  if proc < 50:
                      print("Этого было недостаточно для улучшения положения.")
                  else:
                      army += random.randrange(1,2)
                      print("Армия помиловала Вас!")#
            elif pop >= 800:
                  proc = random.randrange(40,100)
                  if proc < 50:
                      print("Видимо, что-то пошло не так!")#
                  else:
                      print("А вы хороший инвестор!")
                      army += random.randrange(2,3)
    if aligarx == 1:
        sel = input("Олигархи в ярости от Ваших действий. Они располагают властью сместить Вас. Хотите выделить деньги на их успокоение?")
        if sel == "да" or sel == "Да":
            print("Ну что ж, Вы идёте в правильном направлении.")
            print("Теперь давайте подумаем о сумме денег.")
            print("Сколько Вы готовы отдать? Чем больше, тем лучше.")
            pop = int(input("Снять:"))
            if pop > bank:
                  print("К сожалению, у Вас не достаточно средств. Удачи в следующем году!")
            elif pop < 400:
                  proc = random.randrange(0,70)
                  if proc < 50:
                      print("Олигархи не оценили вашей подачки и оценили это, как неуважение к себе!")
                  else:
                      aligarx += random.randrange(1,2)
                      print("Вы родились в рубашке!")
            elif pop >= 400:
                  proc = random.randrange(40,100)
                  if proc < 50:
                      print("Видимо, олигархы оказались сильно требовательными!")#
                  else:
                      print("Олигархам достаточно ваших пожертвоаний.")#
                      aligarx += random.randrange(2,3)
    if liberal == 1:
        sel = input("Либералы в ярости от ваших действий. Вот-вот страны-соперницы объявят нам экономическую блокаду. Хотите выделить средства либералам?")#Артем Я
        if sel == "да" or sel == "Да":
            print("Ну что ж, Вы идёте в правильном направлении.")
            print("Теперь давайте подумаем о сумме денег.")
            print("Сколько Вы готовы отдать? Чем больше, тем лучше.")
            pop = int(input("Снять:"))
            if pop > bank:
                  print("К сожалению, у Вас не достаточно средств. Удачи в следующем году!")
            elif pop < 300:
                  proc = random.randrange(0,70)
                  if proc < 50:
                      print("Кажется, Вы не очень любите либералов!")#
                  else:
                      liberal += random.randrange(1,2)
                      print("Либералы поняли Ваше положение и решили подождать лучших времён.")#
            elif pop >= 300:
                  proc = random.randrange(40,100)
                  if proc < 50:
                      print("Вы заплатили много денег, но они не дошли до протестующих!")#
                  else:
                      print("Это вполне устроило либералов.")#
                      liberal += random.randrange(2,3)
    if bank < 200:
        mn = input("Слышен громкий топот за дверями, чьи-то крики. Вдруг к Вам в покои врывается казначей. Он весь в поту и у него трясутся руки. Он падает на колени и обращается к Вам: В казне не хватает денег! Повысить налоги?")#про недостаток
        if mn == "Да" or mn =="да":
            narod -= random.randrange(1,2)
            liberal -= random.randrange(1,2)
            bank += random.randrange(1000, 2500)
            print("Народ:",narod)
            print("Армия:",army)
            print("Олигарх:",aligarx)
            print("Либералы:",liberal)
            print("Банк:",bank)
        if mn == "Нет" or mn == "нет":
            print("Вы прогоняете казначея. Но этой ночью Вам снятся страшные сны о падении государства.")
            
            
     
#########################
    if narod <= 0 or narod >= 10:
        if narod <=0:
            print("Вы были слишком злы к народу")
            year=80
        else:
            print("Вы были слишком добры к народу")
            year=80
    if army <= 0 or army >= 10:
        if army <= 0:
            print("Вы были слишком злы к армии")
            year=80
        else:
            print("Вы были слишком добры к армии")
            year=80
    if aligarx <= 0 or aligarx >= 10:
        if aligarx <=0:
            print("Вы были слишком злы к олигархам")
            year=80
        else:
            print("Вы были слишком добры к олигархам")
            year=80
    if liberal <= 0 or liberal >= 10:
        if liberal <=0:
            print("Вы были слишком злы к либералам")
            year=80
        else:
            print("Вы были слишком добры к либералам")
            year=80
                                        
        print("Вы правите уже {} {}".format(year,l))        
ki = years % 10
if (years>9)and(years<20)or(years>110)or(ki>4)or(ki==0):
    li = "лет"
else:
    if ki==1:
        li = "год"
    else:
        li = "года"
if year == 60 :
        print("Вы прожили славную жизнь, диктатор. Под вашим правлением государство процветало. Увы, вы не можете жить вечно, и страна будет продлжать путь без вас. Но вы войдите в историю, как один из величайших правителей мира.")
elif narod < 1 or narod > 9:
    smert=input("Вас свергают. Вы сидите в своем кабинете и думаете: Суецид это выход? Может застрелиться?")
    if smert == "Да" or smert ==  "да":
        print("Вы застрелились. Позже вы были признаны худшим диктатром мира, ведь вы оказались трусом. Вся страна пытается вас забыть. Вы продержали власть {} {}".format(years,li))
    else:
        print("К вам в кабинет ворвался простой люд. Под воздействием всеобщей эйфарии вас под улюлюкание толпы нанизали на виллы. Печальная участь. Вы удерживали власть: {} {}".format(years,li))
elif army < 1 or army > 9:
    smert=input("Вас свергают. Вы сидите в своем кабинете и думаете: Суецид это выход? Может застрелиться?")
    if smert == "Да" or smert == "да":
        print("Вы застрелились. Позже вы были признаны худшим диктатром мира, ведь вы оказались трусом. Вся страна пытается вас забыть. Вы продержали власть {} {}".format(years,li))
    else:
        print("В ваш кабинет ворвались все генералы вашей страны и начали палисть по вам из всех орудий. То что от вас осталось было выкинуто на улицу на корм свиньям. Неповезло. Вы продержали власть: {} {}".format(years,li))
elif aligarx < 1 or aligarx > 9:
    smert=input("Вас свергают. Вы сидите в своем кабинете и думаете: Суецид это выход? Может застрелиться?")
    if smert == "Да" or smert == "да":
        print("Вы застрелились. Позже вы были признаны худшим диктатром мира, ведь вы оказались трусом. Вся страна пытается вас забыть. Вы продержали власть {}".format(years,li))
    else:
        print("В ваш кабинет вошли все сливки общества. После небольшого разговора, вы вдруг поняли, что вы привязаны к стулу, и вокруг все горит. Но к сожалению по вам скучать не станут. Вы проправили: {} {}".format(years,li))
elif liberal < 1 or liberal > 9:
    smert=input("Вас свергают. Вы сидите в своем кабинете и думаете: Суецид это выход? Может застрелиться?")
    if smert == "Да" or smert == "да":
        print("Вы застрелились. Позже вы были признаны худшим диктатром мира, ведь вы оказались трусом. Вся страна пытается вас забыть. Вы продержали власть {}".format(years,li))
    else:
        print("В ваш кабинет влетает текущаю оппозиция. Понимая вашу беспомощность, вас тут же предают суду, в результате которого, вы были переданы на пожизненное заключение в тюрьму враждебной страны. Там вы и умрете от статрости. Вы удержали власть: {} {}".format(years,li))
        



























    
