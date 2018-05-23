import random


class Roll:

    def __init__(self, dice_string):
        print(dice_string)
        self.modifier = 0
        self.command = dice_string.upper()
        self.modifier = 0

        parts = self.command.split ('D')
        n_rolls = 1

        if parts[0] == '':
            self.nrolls = 1
        else:
            self.nrolls = int (parts[0])

        self.faces, self.modifier = self.get_roll_info(parts[1])


    def get_roll_info(self, s):
        modifier = 0
        faces = 10

        if "+" in s:
            modifier = modifier + int(s[s.find("+")+1:])
            faces = int(s[:s.find("+")])

        elif "-" in s:
            modifier = modifier - int(s[s.find ("-") + 1:])
            faces = int (s[:s.find ("-")])
        else:
            faces = int(s)

        return faces, modifier

    def roll_dice(self):
        rolls = []

        for j in range (self.nrolls):
            rolls.append (random.randint(1, self.faces) + self.modifier)

        #Fix rolls
        rolls = [self.faces if x > self.faces else x for x in rolls]
        rolls = [1 if x < 1 else x for x in rolls]

        return rolls


class WodRoll:

    def __init__(self, dice_string):
        parts = dice_string.split(" ")

        self.nrolls = int(parts[0])

        if len(parts) == 1:
            self.dificulty = 6
        else:
            self.dificulty = int(parts[1])

    def roll_dice(self):
        rolls = []

        for j in range (self.nrolls):
            rolls.append (random.randint (1, 10))

        message = self.get_message(rolls)

        return self.nrolls, self.dificulty, rolls, message

    def get_message(self, rolls):
        success = self.count_success (rolls)
        fails = self.count_success (rolls)
        critical_fail = self.count_ones (rolls)

        result = success - critical_fail

        if result == 0:
            return "Nenhum sucesso. ({})".format(result)
        elif result == -1:
            return "Falha Crítica. (1 falha)"
        elif result < -1:
            return "Deu MUITO errado. ({} falhas!)".format(result*(-1))
        elif result == 1:
            return "Você obteve 1 sucesso"
        elif result > 1:
            return "Voce obteve {} sucessos!".format(result)


    def count_success(self, seq):
        """Returns the amount of successes in a sequence of roll """
        return sum (1 for item in seq if item >= self.dificulty)

    def count_fail(self,seq):
        """Returns the amount of fails in a sequence of roll """
        return sum (1 for item in seq if item < self.dificulty)

    def count_ones(self, seq):
        """Returns the amount of critical failures in a sequence of roll """
        return sum (1 for item in seq if item == 1)
