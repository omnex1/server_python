import os, json

#the initial program. runs all specified python scripts
class start():

    def __init__(self):
        os.system("cls")

        #getting the dictionary from dict.json and setting self.data to be that so we can access it
        test = open(f"{os.getcwd()}/dict.json", "r")
        self.data = json.loads(test.read())
        test.close()

        print(self.data)

        self.run_apps()
    
    def run_apps(self):
        for i in self.data["apps"]:
            #i[0] is the name
            #i[1] is whether it should be on
            #i[2] is the arguments that should be passed
            if bool(i[1]):
                #if the app is enabled
                os.system(f"python {os.getcwd() + i[0]} {i[2]}")


if __name__ == "__main__":
    start()

