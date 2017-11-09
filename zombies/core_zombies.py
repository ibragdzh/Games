# ---------------------------------------------- VARIABLES ----------------------------------------------#
# player & zomboss: main characters 
# companion: player's pet
# score: killed zombies
# fire_arm: ancillary var for attack if you have fire arm's bullets
# extra_chance_min: ancillary var for extra attack
# extra_attack: extra attack chance
# min_win_money & max_win_money: ancillary var for increase win money each round
# win_money: each round wins money
# abi: ancillary var for use pet's ability chance
# mb_find: ancillary var for chance to medical box
# simple_heal_chance: each round have a chance to heal player for 1-15 hp
# zomboss_hp: ancillary for increase zombie's hp each death
# zomboss_hp_increase: ancillary var for choose - 1, 2 or 3 hp increase each death

# Список будущих обновлений 
# -----------------------------------------------------------------------------------------
# Сделать анимацию точек как в вк
# Добавить базу данных для сохранения прогресса игроков
# Поработать над балансом, особенно twentyscore
# Усилить питомцев

import config_zombies
import outputs_zombies
import accounts_zombies
# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #
import progressbar
from random import randint
from time import sleep

def game(lang):
    bar = progressbar.ProgressBar()
    if lang == "eng":
        player = config_zombies.Hero(input("My name is: "), 30, 350, 350, 0, 4, 0, 80, None)
    else:
        player = config_zombies.Hero(input("Мое имя: "), 30, 350, 350, 0, 4, 0, 80, None)
    zomboss = config_zombies.Zombie(None, 20, 70, 0)
    zomboss_hp = 70
    score = 0
    fire_arm = None
    extra_chance_min = 1
    extra_chance = 0
    min_win_money = 25
    max_win_money = 55
    if lang == "eng":
        print("Click Enter to start game!")
    else:
        print("Нажмите Enter для начала игры")
    input()
    for i in range(100):
        bar.update(i)
        sleep(0.005)
    bar.finish()
    print("")
    zomboss.naming(lang)
    while True:
        outputs_zombies.pet_selection(lang)
        companion_selecting = input()
        companion = companion_selecting.lower()
        for i in range(100):
            bar.update(i)
            sleep(0.005)
        bar.finish()
        print("")
        sleep(1)
        if lang == "eng":
            if companion == "chicken":
                companion = config_zombies.Pet("chicken", 25)
                print("Good luck in bitches smashing with golden chicken!")
                break
            elif companion == "dragon":
                companion = config_zombies.Pet("dragon", 25)
                print("Good luck in bitches smashing with fire dragon!")
                break
            elif companion == "fairy":
                companion = config_zombies.Pet("fairy", 25)
                print("Good luck in bitches smashing with wonder fairy!")
                break
            else:
                print("Hmm what?!")
                continue
        else:
            if companion == "курочка":
                companion = config_zombies.Pet("chicken", 25)
                print("Удачи в раздавливании этих бичей вместе с золотой курочкой!")
                break
            elif companion == "дракон":
                companion = config_zombies.Pet("dragon", 25)
                print("Удачи в раздавливании этих бичей вместе с огненным драконом!")
                break
            elif companion == "фея":
                companion = config_zombies.Pet("fairy", 25)
                print("Удачи в раздавливании этих бичей вместе с волшебной феей!")
                break
            else:
                print("Чего?!")
    while True:
        outputs_zombies.stats(player, zomboss, score, lang)
        if fire_arm != None:
            takendamage = player.attack(zomboss, fire_arm)
            if lang == "eng":
                print("Pew-pew! Fuckin zombie got", takendamage, "damage from you")
                if player.bullets == 0:
                    if fire_arm == "pistol":
                        print("You haven't bullets. Throw back this void pistol")
                        player.damage -= 5
                        fire_arm = None
                    elif fire_arm == "shotgun":
                        print("You haven't bullets. Throw back this void shotgun")
                        player.damage -= 18
                        fire_arm = None
                    elif fire_arm == "rifle":
                        print("You haven't bullets. Throw back this void rifle")
                        player.damage -= 50
                        fire_arm = None
            else:
                print("Пиу-пиу! Гребаный зомби получил от тебя", takendamage, "урона")
                if player.bullets == 0:
                    if fire_arm == "пистолет":
                        print("Патроны закончились, выкинь нахер этот пустой пистолет")
                        player.damage -= 5
                        fire_arm = None
                    elif fire_arm == "дробовик":
                        print("Патроны закончились, выкинь нахер этот пустой дробовик")
                        player.damage -= 18
                        fire_arm = None
                    elif fire_arm == "винтовка":
                        print("Патроны закончились, выкинь нахер эту пустую винтовку")
                        player.damage -= 50
                        fire_arm = None
        else:
            takendamage = player.attack(zomboss, None)
            if lang == "eng":
                print("Oh oh! You take", takendamage, "damage")
            else:
                print("Ох ох! Ты нанес этому придурку", takendamage, "урона")
        abi = randint(1, 100)
        if abi <= companion.pet_ability:
            if companion.name == "chicken" or companion.name == "dragon":
                b = companion.ability(player, zomboss)
            else:
                b, d = companion.ability(player, zomboss)
            if companion.name == "chicken":
                if lang == "eng":
                    print("Your chicken was give you", b, "$")
                else:
                    print("Твоя курочка принесла тебе", b, "$")
            elif companion.name == "dragon":
                if lang == "eng":
                    print("Your dragon increase your damage by", b, "and dodge by 1-2 %")
                else:
                    print("Твой дракон увеличил твой урон на", b, "и шанс уворота на 1-2 %")
            else:
                if lang == "eng":
                    print("Your fairy heal you by", (15 + b), "hp and", d, "maxhp")
                else:
                    print("Твоя фея восстановила тебе", (15 + b), "хп и увеличила максимум хп на", d)
        print("")
        sleep(2)
        if zomboss.hp <= 0:
            score += 1
            mb_find = randint(1, 100)
            simple_heal_chance = randint(1, 100)
            x = randint(4, 9)
            y = randint(4, 9)
            min_win_money += x
            max_win_money += y
            win_money = randint(min_win_money, max_win_money)
            player.whoop(lang)
            if lang == "eng":
                print(player.name + ", you've killed this bastard!")
                print("You earned", win_money, "$")
            else:
                print(player.name + ", ты слышал этот вопль?")
                print("Ты получил", win_money, "$")
            if mb_find <= 10:
                if lang == "eng":
                    print("Wow,", player.name, "find one medical box")
                else:
                    print("Ого!", player.name, "нашел аптечку")
                player.medical_box += 1
            if simple_heal_chance <= 15:
                simple_heal = randint(1, 15)
                player.hp += simple_heal
                if player.hp > player.maxhp:
                    player.hp = player.maxhp
                if lang == "eng":
                    print("Yeah, heeeeal... You gain", simple_heal, "hp")
                else:
                    print("Оооо, жиииизни... Ты восстановил", simple_heal, "хп")
            player.cash += win_money
            zomboss_hp_increase = randint(3, 5)
            zomboss_hp += zomboss_hp_increase
            zomboss.hp = zomboss_hp
            zomboss.naming(lang)
            print("")
            if score == 10:
                outputs_zombies.portal(lang)
                zomboss.damage += 6
                extra_chance += 25
            if score == 20:
                outputs_zombies.twentyscore(player, zomboss, lang)
            if score == 30:
                outputs_zombies.hell_difficult(player, zomboss, companion, lang)
                zomboss_hp += 40
                extra_chance += 20
            print("")
            sleep(3)
        else:
            takendamage = zomboss.attack(player)
            dodging = randint(1, 100)
            if dodging <= player.dodge:
                player.hp += takendamage
                if lang == "eng":
                    print("Dodge!")
                    print("")
                else:
                    print("Уворот!")
                    print("")
            else:
                if lang == "eng":
                    print("Oh shit! This brainfucker attacked you by", takendamage, "damage!")
                else:
                    print("Мать твою! Этот мозгое* нанес тебе", takendamage, "урона!")
                print("")
                sleep(2)
            extra_attack = randint(extra_chance_min, 100)
            if extra_attack <= extra_chance:
                if lang == "eng":
                    print("Johnny, mother fucker, this bastards are hiding on the trees!!!")
                else:
                    print("Джонни, мать твою, эти ублюдки прячутся на деревьях!!!")
                takendamage = zomboss.attack(player)
                dodging = randint(1, 100)
                if dodging <= player.dodge:
                    player.hp += takendamage
                    if lang == "eng":
                        print("Dodge!")
                        print("")
                    else:
                        print("Уворот!")
                        print("")
                else:
                    if lang == "eng":
                        print("Oh shit! This brainfucker attacked you by", takendamage, "damage!")
                    else:
                        print("Этот мозгое* опять нанес тебе", takendamage, "урона!")
                print("")
                sleep(2)
            if player.hp <= 0:
                if lang == "eng":
                    print("You die :_(")
                else:
                    print("Ты погиб :_(")
                break
        if lang == "eng":
            print(player.name + ", do you want to use medical box? 'Yes' or 'no'")
        else:
            print(player.name + ", хочешь ли ты использовать аптечку? 'Да' или 'нет'")
        i = input()
        i = i.lower()
        if lang == "eng":
            if i == "yes":
                if player.medical_box > 0:
                    player.heal()
                    print("You used medical box, so you gain 15 hp :D")
                    print("You have left", player.medical_box, "medical boxes")
                    print("")
                else:
                    print("You haven't medical boxes :(")
                    print("")
            else:
                print("Ok, as you wish")
                print("")
        else:
            if i == "да":
                if player.medical_box > 0:
                    player.heal()
                    print("Ты использовал аптечку и восстановил себе 15 хп :D")
                    print("Твой запас аптечек:", player.medical_box)
                    print("")
                else:
                    print("Но у тебя ведь нет аптечек")
                    print("")
            else:
                print("Окей, как хочешь")
                print("")
        if lang == "eng":
            print(player.name + ", do you want to visit shop?")
        else:
            print(player.name + ", хочешь заглянуть в магазин?")
        i = input()
        i = i.lower()
        if lang == "eng":
            if i == "yes":
                print("")
                print("-_" * 40 + "-")
                print("")
                print("You have", player.cash, "$")
                outputs_zombies.shop(lang)
                print("")
                print("_-" * 40 + "_")
                print("")
                fire_arm = player.shopping(lang)
            else:
                print("Okay :_(")
                print("")
        else:
            if i == "да":
                print("")
                print("-_" * 40 + "-")
                print("")
                print("У тебя", player.cash, "$")
                outputs_zombies.shop(lang)
                print("")
                print("_-" * 40 + "_")
                print("")
                fire_arm = player.shopping(lang)
            else:
                print("Окей :_(")
                print("")

while True:
    language = input("""----------------------------------------------------------------
Hello! PLease, choose the game language: 'russian' or 'english'

Привет! Пожалуйста, выбери язык игры: 'русский' или 'английский'
----------------------------------------------------------------
Your choice / Твой выбор: """)
    language = language.lower()
    print("")
    if language == "russian" or language == "русский":
        language = "rus"
        break
    elif language == "english" or language == "английский":
        language = "eng"
        break
    else:
        print("""Enter the words as they written in ''
Вводи слова так, как они написаны в ''""")
        print("")
        continue

outputs_zombies.description(language)
game(language)