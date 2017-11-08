from random import randint

class Human:

    def __init__(self, name, damage, hp):
        self.name = name
        self.damage = damage
        self.hp = hp

class Pet:

    def __init__(self, name, pet_ability):
        self.name = name
        self.pet_ability = pet_ability

    def ability(self, owner, target):
        if self.name == "chicken":
            a = randint(30, 70)
            c = randint(1, 3)
            if c == 1:
                owner.medical_box += 1
            owner.cash += a
            return a
        if self.name == "dragon":
            a = randint(3, 7)
            owner.damage += a
            owner.dodge += randint(1, 2)
            if owner.dodge > 35:
                owner.dodge = 35
            return a
        if self.name == "fairy":
            a = randint(0, 15)
            owner.hp += 15 + a
            c = randint(1, 3)
            owner.maxhp += c
            if owner.hp > owner.maxhp:
                owner.hp = owner.maxhp
            return a, c

class Hero(Human):

    def __init__(self, name, damage, hp, maxhp, dodge, medical_box, bullets, cash, firearm):
        super().__init__(name, damage, hp)
        self.maxhp = maxhp
        self.dodge = dodge
        self.medical_box = medical_box
        self.bullets = bullets
        self.cash = cash
        self.firearm = firearm

    def heal(self):
        self.hp += 15
        self.medical_box -= 1
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def whoop(self, langu):
        a = randint(1, 3)
        if a == 1:
            if langu == "eng":
                print("Headshot!")
            else:
                print("Хедшот!")
        elif a == 2:
            if langu == "eng":
                print("Yeah son!")
            else:
                print("Еее бой!")
        else:
            if langu == "eng":
                print("So easy to crush this bitches!")
            else:
                print("Так легко убивать этих безмозглышей!")

    def attack(self, target, firearm):
        if self.bullets > 0:
            taken_damage = randint(round(self.damage * 0.7), round(self.damage * 1.4))
            self.bullets -= 1
            target.hp -= taken_damage
        else:
            taken_damage = randint(round(self.damage * 0.8), round(self.damage * 1.3))
            target.hp -= taken_damage
        return taken_damage

    def shopping(self, langu):
        purchasing = input()
        purchase = purchasing.lower()
        fire__arm = None
        if langu == "eng":
            if purchase == "exit":
                print("Okay :(")
            elif purchase == "pistol":
                if fire__arm == None:
                    if self.cash >= 80:
                        print("Success! Your damage increased by 3, and you have 4 bullets")
                        fire__arm = "pistol"
                        self.damage += 3
                        self.bullets += 4
                        self.cash -= 80
                    else:
                        print("You haven't enough money")
                else:
                    print("You already have one fire arm")
            elif purchase == "shotgun":
                if fire__arm == None:
                    if self.cash >= 260:
                        print("Success! Your damage increased by 10, and you have 4 bullets")
                        fire__arm = "shotgun"
                        self.damage += 10
                        self.bullets += 4
                        self.cash -= 260
                    else:
                        print("You haven't enough money")
                else:
                    print("You already have one fire arm")
            elif purchase == "rifle":
                if fire__arm == None:
                    if self.cash >= 1000:
                        print("Success! Your damage increased by 50, and you have 4 bullets")
                        fire__arm = "rifle"
                        self.damage += 50
                        self.bullets += 4
                        self.cash -= 1000
                    else:
                        print("You haven't enough money")
                else:
                    print("You already have one fire arm")
            elif purchase == "dagger":
                if self.cash >= 120:
                    print("Success! Your damage increased by 3")
                    self.damage += 3
                    self.cash -= 120
                else:
                    print("You haven't enough money")
            elif purchase == "saber":
                if self.cash >= 400:
                    print("Success! Your damage increased by 11")
                    self.damage += 11
                    self.cash -= 400
                else:
                    print("You haven't enough money")
            elif purchase == "axe":
                if self.cash >= 1000:
                    print("Success! Your damage increased by 35")
                    self.damage += 35
                    self.cash -= 1000
                else:
                    print("You haven't enough money")
            elif purchase == "shield":
                if self.cash >= 120:
                    print("Success! Your max hp increased by 15")
                    self.maxhp += 15
                    self.cash -= 150
                else:
                    print("You haven't enough money")
            elif purchase == "flak jacket":
                if self.cash >= 400:
                    print("Success! Your max hp increased by 40")
                    self.maxhp += 40
                    self.cash -= 400
                else:
                    print("You haven't enough money")
            elif purchase == "exosuit":
                if self.cash >= 1000:
                    print("Success! Your max hp increased by 100")
                    self.maxhp += 100
                    self.cash -= 1000
                else:
                    print("You haven't enough money")
            elif purchase == "small potion":
                if self.cash >= 150:
                    print("Success! You healed by 20 hp")
                    self.hp += 20
                    if self.hp > self.maxhp:
                        self.hp = self.maxhp
                    self.cash -= 150
                else:
                    print("You haven't enough money")
            elif purchase == "potion":
                if self.cash >= 400:
                    print("Success! You healed by 65 hp")
                    self.hp += 65
                    if self.hp >= self.maxhp:
                        self.hp = self.maxhp
                    self.cash -= 400
                else:
                    print("You haven't enough money")
            elif purchase == "super potion":
                if self.cash >= 1000:
                    print("Success! Your hp is full!")
                    self.hp = self.maxhp
                    self.cash -= 1000
                else:
                    print("You haven't enough money")
            else:
                print("Hmm what?")
        else:
            if purchase == "выход":
                print("Окей :(")
            elif purchase == "пистолет":
                if fire__arm == None:
                    if self.cash >= 80:
                        print("Успех! Твой урон увеличен на 3, и ты получил 4 патрона")
                        fire__arm = "pistol"
                        self.damage += 3
                        self.bullets += 4
                        self.cash -= 80
                    else:
                        print("У тебя недостаточно денег")
                else:
                    print("You already have one fire arm")
            elif purchase == "дробовик":
                if fire__arm == None:
                    if self.cash >= 260:
                        print("Успех! Твой урон увеличен на 10, и ты получил 4 патрона")
                        fire__arm = "shotgun"
                        self.damage += 10
                        self.bullets += 4
                        self.cash -= 260
                    else:
                        print("У тебя недостаточно денег")
                else:
                    print("You already have one fire arm")
            elif purchase == "винтовка":
                if fire__arm == None:
                    if self.cash >= 1000:
                        print("Успех! Твой урон увеличен на 50, и ты получил 4 патрона")
                        fire__arm = "rifle"
                        self.damage += 50
                        self.bullets += 4
                        self.cash -= 1000
                    else:
                        print("У тебя недостаточно денег")
                else:
                    print("You already have one fire arm")
            elif purchase == "кинжал":
                if self.cash >= 120:
                    print("Успех! Твой урон увеличен на 3")
                    self.damage += 3
                    self.cash -= 120
                else:
                    print("У тебя недостаточно денег")
            elif purchase == "сабля":
                if self.cash >= 400:
                    print("Успех! Твой урон увеличен на 11")
                    self.damage += 11
                    self.cash -= 400
                else:
                    print("У тебя недостаточно денег")
            elif purchase == "топор":
                if self.cash >= 1000:
                    print("Успех! Твой урон увеличен на 35")
                    self.damage += 35
                    self.cash -= 1000
                else:
                    print("У тебя недостаточно денег")
            elif purchase == "щит":
                if self.cash >= 120:
                    print("Успех! Твой максимум хп увеличен на 15")
                    self.maxhp += 15
                    self.cash -= 150
                else:
                    print("У тебя недостаточно денег")
            elif purchase == "бронежилет":
                if self.cash >= 400:
                    print("Успех! Твой максимум хп увеличен на 40")
                    self.maxhp += 40
                    self.cash -= 400
                else:
                    print("У тебя недостаточно денег")
            elif purchase == "экзокостюм":
                if self.cash >= 1000:
                    print("Успех! Твой максимум хп увеличен на 100")
                    self.maxhp += 100
                    self.cash -= 1000
                else:
                    print("У тебя недостаточно денег")
            elif purchase == "малое зелье":
                if self.cash >= 150:
                    print("Успех! Ты восстановил 20 хп")
                    self.hp += 20
                    if self.hp > self.maxhp:
                        self.hp = self.maxhp
                    self.cash -= 150
                else:
                    print("У тебя недостаточно денег")
            elif purchase == "зелье":
                if self.cash >= 400:
                    print("Успех! Ты восстановил 65 хп")
                    self.hp += 65
                    if self.hp >= self.maxhp:
                        self.hp = self.maxhp
                    self.cash -= 400
                else:
                    print("У тебя недостаточно денег")
            elif purchase == "супер зелье":
                if self.cash >= 1000:
                    print("Успех! Ты полностью исцелен!")
                    self.hp = self.maxhp
                    self.cash -= 1000
                else:
                    print("У тебя недостаточно денег")
            else:
                print("Чего чего?")
        return fire__arm

class Zombie(Human):

    def __init__(self, name, damage, hp, dodge):
        super().__init__(name, damage, hp)
        self.dodge = dodge

    def attack(self, target):
        taken_damage = randint(round(self.damage * 0.7), round(self.damage * 1.2))
        target.hp -= taken_damage
        return taken_damage

    def naming(self, langu):
        self.name = randint(1, 10)
        if self.name == 1:
            if langu == "eng":
                self.name = "butcher"
            else:
                self.name = "мясника"
        elif self.name == 2:
            if langu == "eng":
                self.name = "baker"
            else:
                self.name = "булочника"
        elif self.name == 3:
            if langu == "eng":
                self.name = "biker"
            else:
                self.name = "байкера"
        elif self.name == 4:
            if langu == "eng":
                self.name = "tubular"
            else:
                self.name = "трубочиста"
        elif self.name == 5:
            if langu == "eng":
                self.name = "housewife"
            else:
                self.name = "домохозяйки"
        elif self.name == 6:
            if langu == "eng":
                self.name = "mechanic"
            else:
                self.name = "механика"
        elif self.name == 7:
            if langu == "eng":
                self.name = "sherif"
            else:
                self.name = "шерифа"
        elif self.name == 8:
            if langu == "eng":
                self.name = "security"
            else:
                self.name = "охраника"
        elif self.name == 9:
            if langu == "eng":
                self.name = "politician"
            else:
                self.name = "политика"
        else:
            if langu == "eng":
                self.name = "chief"
            else:
                self.name = "вождя"