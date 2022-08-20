import json
import random
from inputs import clear
import mathclasses



def chance(percent):
    if random.randint(0, 100) < percent:
        return True
    else:
        return False

        
class Screen:
    def __init__(self, prompt, options, InputManager):
        self.prompt = prompt
        self.options = options
        self.InputManager = InputManager

    def run(self):
        print("This screen hasn't been properly configured!")
        self.InputManager.pause()
        return "Main Menu"

    def settings(self, previousScreen):
        clear()
        selection = self.InputManager.getInput("Options", ["1: Save", "2: View Inventory", "3: Go To Main Menu", "4: Go Back"])
        if selection == 1:
            self.saveCharacter()
            return previousScreen
        if selection == 2:
            self.viewInventory()
            return previousScreen
        if selection == 3:
            return "Main Menu"
        if selection == 4:
            return previousScreen

class MainMenu(Screen):
    def run(self):
        clear()
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            return "Pythagorean Theorem"
        if selection == 2:
            return "Main Menu"
        if selection == 3:
            clear()
            return ""

class PythagoreanTheorem(Screen):
    def run(self):
        clear()
        selection = self.InputManager.getInput(self.prompt, self.options)
        if selection == 1:
            return "Pythagorean Theorem Side C"
        if selection == 2:
            return "Pythagorean Theorem Leg"
        if selection == 3:
            clear()
            return "Main Menu"

class PythagoreanTheoremSideC(Screen):
    def run(self):
        print("Length Of Side A\n")
        a = self.InputManager.getNumber()
        print("\nLength Of Side B\n")
        b = self.InputManager.getNumber()
        self.InputManager.printResult(mathclasses.PythagoreanTheorem.findc(a,b))
        return "Pythagorean Theorem"

class PythagoreanTheoremLeg(Screen):
    def run(self):
        print("Length Of Known Leg\n")
        a = self.InputManager.getNumber()
        print("\nLength Of Side C\n")
        c = self.InputManager.getNumber()
        self.InputManager.printResult(mathclasses.PythagoreanTheorem.findleg(a,c))
        return "Pythagorean Theorem"


class ScreenManager:
    def __init__(self, InputManager):
        self.InputManager = InputManager

        self.screens = {
            "Main Menu": MainMenu("Main Menu", ["1: Pythagorean Theorem", "2: Option 2", "3: Exit"], self.InputManager),
            "Pythagorean Theorem": PythagoreanTheorem("Pythagorean Theorem", ["1: Find Side C", "2: Find A Leg", "3: Back"], self.InputManager),
            "Pythagorean Theorem Side C": PythagoreanTheoremSideC("Find Side C", [], self.InputManager),
            "Pythagorean Theorem Leg": PythagoreanTheoremLeg("Find A Leg", [], self.InputManager)
        }

    def runScreen(self, screenName):
        return self.screens[screenName].run()

    def clear(self):
        clear()
