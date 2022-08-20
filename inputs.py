import os

def clear():
    os.system(['clear','cls'][os.name == 'nt'])

class InputManager:
    def getInput(self, prompt, options):

        optionText = ""

        for i in options:
            optionText += i + "\n"
            if options.index(i) < len(options) - 1:
                optionText += "\n"

        print(prompt + "\n\n" + optionText)
        
        try:
            userInput = int(input(""))
        except:
            userInput = len(options) + 1

        while not userInput <= len(options):
            clear()
            print("That is not a valid option. Please enter a number between 1 and ", len(options), "\n")
            self.pause()
            clear()
            print(prompt + "\n\n" + optionText)
            
            try:
                userInput = int(input(""))
            except:
                userInput = len(options) + 1

        return userInput

    def getNumber(self):

        try:
            userInput = int(input("Enter a number\n"))
            number = True
        except:
            number = False

        while not number:
            try:
                print("\nThat is not a valid number. Please enter only numbers.")
                userInput = int(input("Enter a number\n"))
                number = True
            except:
                number = False

        return userInput

    def printResult(self, message):
        clear()
        print(f"{message}\n")
        self.pause()

    def pause(self):
        print("Press Enter To Continue")
        input()