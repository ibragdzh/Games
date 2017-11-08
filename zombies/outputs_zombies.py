from time import sleep

def portal(langu):
    if langu == "eng":
        print("Wow! Portal!!! You can go to the forest location")
        print("You gain one extra score!")
    else:
        print("Вау! Портал!!! Ты можешь перейти в локацию 'лес'")
        print("Ты получил дополнительное очко")
        print("")
    print("")
    sleep(2)
    print("                   __,aaPPPPPPPPaa,__                       ")
    print("                ,adP''''          `''Yb,_                   ")
    print("             ,adP'                     `'Yb,                ")
    print("           ,dP'     ,aadPP'''''YYba,_     `'Y,              ")
    print("          ,P'    ,aP'             `''Ya,     'Y,            ")
    print("         ,P'    aP'     _________     `'Ya    `Yb,          ")
    print("        ,P'    d'    ,adP''''''''Yba,    `Y,    'Y,         ")
    print("       ,d'   ,d'   ,dP'            `Yb,   `Y,    `Y,        ")
    print("       d'   ,d'   ,d'    ,dP''Yb,    `Y,   `Y,    `b        ")
    print("       8    d'    d'   ,d'      'b,   `Y,   `8,    Y,       ")
    print("       8    8     8    d'    _   `Y,   `8    `8    `b       ")
    print("       8    8     8    8     8    `8    8     8     8       ")
    print("       8    Y,    Y,   `b, ,aP     P    8    ,P     8       ")
    print("       I,   `Y,   `Ya    ''''     d'   ,P    d'    ,P       ")
    print("       `Y,   `8,    `Ya         ,8'   ,P'   ,P'    d'       ")
    print("        `Y,   `Ya,    `Ya,,__,,d'    ,P'   ,P'    ,P        ")
    print("         `Y,    `Ya,     `'''''     ,P'   ,d'    ,P'        ")
    print("          `Yb,    `'Ya,_          ,d'    ,P'    ,P'         ")
    print("            `Yb,      ''YbaaaaaadP'     ,P'    ,P'          ")
    print("              `Yba,                   ,d'    ,dP'           ")
    print("                 `'Yba,__       __,adP'     dP'             ")
    print("                     `''''''''''''''                        ")
    print("")
    sleep(2)
    if langu == "eng":
        print("Zombies in the forest can do extra attack to you, and they have increased stats!!!")
    else:
        print("Зомби в лесу могут выполнять дополнительные атаки на тебя, и они сильнее!!!")

def hell_difficult(pl, zomb, comp, langu):
    if langu == "eng":
        print("Wow!!! You have reached the hell of difficulty!")
        print("Pets upgraded!")
        print("You got two axes, one exosuit and 1500 $")
        print("")
        sleep(4)
        print("But zombies not dreams!")
        print("Their attack increased by 15, hp by 40!")
        print("Bigger extra attack and dodge chance")
        print("")
        sleep(4)
        print("Good luck")
    else:
        print("Вот это да! Ты досиг адского уровня сложности!")
        print("Питомцы усилены!")
        print("Ты получил два топора, один экзокостюм и 1500 $")
        print("")
        sleep(4)
        print("Но зомби не дремлют!")
        print("Их атака увеличена на 15, хп на 40,")
        print("а также увеличен шанс дополнительной атаки и уворота")
        print("")
        sleep(4)
        print("")
    pl.cash += 1500
    pl.damage += 80
    pl.maxhp += 80
    comp.pet_ability += 20
    zomb.damage += 15
    zomb.dodge += 15

def twentyscore(pl, zomb, langu):
    if langu == "eng":
        print("Wow! New checkpoint! Zombies attack increased, you healed by 50 hp!")
        print("And you got two sabers")
        print("Now zombies can dodge your attacks!!!")
    else:
        print("Вау! Вы достигли 20 очков! Урон зомби увеличен, хп восстановлено на 50!")
        print("Также вы получили две сабли!")
        print("Теперь зомби могут уворачиваться от твоих атак")
    pl.damage += 24
    zomb.damage += 12
    pl.hp += 50
    zomb.dodge = 15
    if pl.hp > pl.maxhp:
        pl.hp = pl.maxhp

def pet_selection(langu):
    if langu == "eng":
        print("Please, enter the pet name, who you want to choose:")
        print("Chicken: have a chance to give you some extra money and medical box")
        print("Dragon: have a chance to increase your damage and dodge chance, but not > 30 %")
        print("Fairy: have a chance to heal you and increase max hp")
    else:
        print("Пожалуйста, введите имя питомца, которого вы хотите выбрать")
        print("Курочка: имеет шанс дать вам несколько дополнительных $ и аптечку")
        print("Дракон: имеет шанс увеличить на немного твой урон и шанс уворота, но не более 30 %")
        print("Фея: имеет шанс восстановить вам немного хп и увеличить максимум")

def shop(langu):
    print("")
    if langu == "eng":
        print("---------------------------------------------------")
        print("| --- ^^^ --- ^^ --- FIRE ARMS --- ^^ --- ^^^ --- |")
        print("| PISTOL - 80 $         :::            damage + 3 |")
        print("| SHOTGUN - 260 $       :::           damage + 10 |")
        print("| RIFLE - 1000 $        :::           damage + 50 |")
        print("|-------------------------------------------------|")
        print("| --- ^^^ --- ^^ --- STEELARMS --- ^^ --- ^^^ --- |")
        print("| DAGGER - 120 $        :::            damage + 3 |")
        print("| SABER - 400 $         :::           damage + 11 |")
        print("| AXE - 1000 $          :::           damage + 35 |")
        print("|-------------------------------------------------|")
        print("| --- ^^^ --- ^^ -- ^^ ARMOR ^^ -- ^^ --- ^^^ --- |")
        print("| SHIELD - 150 $        :::            maxhp + 15 |")
        print("| FLAK JACKET - 400$    :::            maxhp + 40 |")
        print("| EXOSUIT - 1000 $      :::           maxhp + 100 |")
        print("|-------------------------------------------------|")
        print("| --- ^^^ --- ^^^ --- HEALING --- ^^^ --- ^^^ --- |")
        print("| SMALL POTION - 150 $  :::               hp + 20 |")
        print("| POTION - 400 $        :::               hp + 65 |")
        print("| SUPER POTION - 1000 $ :::         gives full hp |")
        print("---------------------------------------------------")
        print("")
        print("You can combine a lot of weapons for big stats,")
        print("but you can't simultaneously have more than one fire arms!")
        print("For by something just input product name,")
        print("For exit just write exit")
    else:
        print("---------------------------------------------------")
        print("| --- ^^^ --- ^^ --- ОГНЕСТРЕЛ --- ^^ --- ^^^ --- |")
        print("| ПИСТОЛЕТ - 80 $       :::              урон + 3 |")
        print("| ДРОБОВИК - 260 $      :::             урон + 10 |")
        print("| ВИНТОВКА - 1000 $     :::             урон + 50 |")
        print("|-------------------------------------------------|")
        print("| --- ^^^ --- ^^^ ХОЛОДНОЕ ОРУЖИЕ ^^^ --- ^^^ --- |")
        print("| КИНЖАЛ - 120 $        :::              урон + 3 |")
        print("| САБЛЯ - 400 $         :::             урон + 11 |")
        print("| ТОПОР - 1000 $        :::             урон + 35 |")
        print("|-------------------------------------------------|")
        print("| --- ^^^ --- ^^ -- ^^ БРОНЯ ^^ -- ^^ --- ^^^ --- |")
        print("| ЩИТ - 150 $           :::      максимум хп + 15 |")
        print("| БРОНЕЖИЛЕТ - 400$     :::      максимум хп + 40 |")
        print("| ЭКЗОКОСТЮМ - 1000 $   :::     максимум хп + 100 |")
        print("|-------------------------------------------------|")
        print("| --- ^^^ --- ^^ -- ^^ ЗЕЛЬЯ ^^ -- ^^ --- ^^^ --- |")
        print("| МАЛОЕ ЗЕЛЬЕ - 150 $   :::               хп + 20 |")
        print("| ЗЕЛЬЕ - 400 $         :::               хп + 65 |")
        print("| СУПЕР ЗЕЛЬЕ - 1000 $  :::      хп = максимум хп |")
        print("---------------------------------------------------")
        print("")
        print("Ты можешь одновременно иметь несколько оружий,")
        print("но нельзя иметь одновременно более 1 огнестрельного оружия!")
        print("Чтобы купить что-либо просто напиши название товара,")
        print("Для выхода напиши выход")

def description(langu):
    if langu == "eng":
        print("""Please, read this game description:
At the start of game you have only name, 33 damage, 350 hp of 350 max hp, 4 medical boxes
and one pet for your choice.
Your aim: kill as much as possible zombies.
First zombie have 20 damage and 66 hp.
If you'll kill the zombie, he'll resurrect with 3, 4 or 5 more hp,
and you will get 1 score and some money to buy goods in shop,
and you have a chance to heal yourself for some hp or find medical box after murder.
Medical boxes heal you for 15 hp, but if you having, for example 340 hp of 350 max hp
using medical box, you'll get + 10 hp.
----------------------------------------------------------------------------------------------
GL & HF""")
    else:
        print("""Пожалуйста, прочти описание игры:
На старте игры вы имеете только имя, 33 урона, 350 из 350 хп, 4 аптечки
и один питомец на ваш выбор.
Ваша цель: убить как можно больше зомби
Первый зомби имеет 20 урона и 66 хп.
Если ты убиваешь зомби, то он возрождается с хп на 3, 4 или 5 хп,
и ты получаешь 1 очко и немного $ для покупок в магазине,
также есть шанс восстановить немного хп или найти аптечку.
Аптечки восстанавливают тебе 15 хп, но если ты, например, имеешь 340 хп из 350 максимальных,
то при использовании аптечки ты восстановишь лишь 10 хп.
-----------------------------------------------------------------------------------------------
GL & HF""")
    input()

def stats(pl, zomb, pl_score, langu):
    print("-" * 50)
    if langu == "eng":
        print("|     Your attack:", pl.damage)
        print("|     Your hp:", pl.hp, "/", pl.maxhp)
        print("|     Your dodge chance:", pl.dodge)
        print("|     Your medical boxes:", pl.medical_box)
        print("|     Your cash:", pl.cash, "$")
        print("|     Your score:", pl_score)
        print("|" + "-" * 49)
        sleep(2)
        print("|     Zombie", zomb.name, "attack:", zomb.damage)
        print("|     Zombie", zomb.name, "hp:", zomb.hp)
    else:
        print("|     Ваш урон:", pl.damage)
        print("|     Ваши хп:", pl.hp, "/", pl.maxhp)
        print("|     Ваш шанс уворота:", pl.dodge)
        print("|     Ваши аптечки:", pl.medical_box)
        print("|     Ваши сбережения:", pl.cash, "$")
        print("|     Ваш счет:", pl_score)
        print("|" + "-" * 49)
        sleep(2)
        print("|     Урон зомби " + zomb.name + ": " + str(zomb.damage))
        print("|     Хп зомби " + zomb.name + ": " + str(zomb.hp))
    print("-" * 50)
    sleep(2)