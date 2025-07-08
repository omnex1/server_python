import os, json

from multiprocessing import Process, Queue
import time

class Multiprocess:

    class Slave(Process):
        def __init__(self, num, task_queue, result_queue, functions):
            super().__init__()
            self.num = num
            self.task_queue = task_queue
            self.result_queue = result_queue
            self.functions = functions

        def run(self):
            while True:
                data = self.task_queue.get()
                if not data["alive"]:
                    break
                if data["tasks"]:
                    func_name, args = data["tasks"]
                    output = self.functions[func_name](args)
                    self.result_queue.put({"slave": self.num, "output": output})

    def __init__(self, slave_num, functions):
        self.slaves = {}
        self.result_queues = {}
        for i in range(slave_num):
            task_queue = Queue()
            result_queue = Queue()
            slave = self.Slave(i, task_queue, result_queue, functions)
            slave.start()
            self.slaves[i] = task_queue
            self.result_queues[i] = result_queue

    def submit_task(self, task_data, child_index):
        self.slaves[child_index].put({"tasks": task_data, "alive": True})

    def get_result(self, child_index):
        if not self.result_queues[child_index].empty():
            return self.result_queues[child_index].get()
        return None

    def stop_process(self, child):
        self.slaves[child].put({"tasks": [], "alive": False})


def Print(value):
    print(f"{__file__} --- {value}")

#the initial program. runs all specified python scripts
class start():

    #its good practice for this script to not use print without the file its printing or things will spam with no info on the script thats doing it. this forces me to be smart
    def check_for_bad_prints(self, file):
        #this is so damn inneficient oh well

        with open(file, "r") as prints:
            file_data = prints.readlines()
            print_num = 0
            wrong_prints = []
            line = 0

            for i in file_data:
                line += 1
                if 'print(' in i:
                    print_num += 1

                    if print_num > 1:
                        wrong_prints.append(line)

            
            if print_num > 1:
                raise TypeError(f"err: please use Print() not print() in line(s) {wrong_prints}")
            
        return True

    def __init__(self):
        os.system("cls")

        #getting the dictionary from dict.json and setting self.data to be that so we can access it
        test = open(f"{os.getcwd()}/dict.json", "r")
        self.data = json.loads(test.read())
        test.close()

        Print(self.data)

        self.run_apps()
    
    def run_apps(self):
        
        process_apps = []
        main_tasks = []
        for i in self.data["apps"]:
            #i[0] is the name
            #i[1] is whether it should be on
            #i[2] is whether the process is ran my multiprocess or main
            #i[3] is the arguments that should be passed
            #i[4] is any commands that need to be ran

            #if the app is enabled add the app to the list to run
            if i[1] == "True":
                if i[2] == "process":
                    process_apps.append(i)
                else:
                    main_tasks.append(i)

        #build multiprocess based off of the number of py files to run
        self.process = Multiprocess(len(process_apps), {"start_py": self.start_py})

        slave_num = 0

        

        for i in process_apps:

            #checking if my code doesnt have too many prints
            if self.check_for_bad_prints(os.getcwd() + i[0]):
                
                #actually running the apps by assigning cpu processes to do that
                self.process.submit_task(["start_py", f"python {os.getcwd() + i[0]} {i[2]}"], slave_num)
        
            slave_num += 1
    
        for i in main_tasks:
            with open(f"{os.getcwd() + i[0]}", "r") as file:
                exec(file.read())
                for j in i[4]:
                    os.system(j)


            try: 
                with open(f"{os.getcwd() + i[0]}", "r") as file:
                    exec(file.read())
                    for j in i[4]:
                        os.system(j)
            except:
                for i in init.process.slaves:
                    init.process.stop_process(i)
                raise ImportError("failed running the module")
    def start_py(self, data):
        os.system(data)

if __name__ == "__main__":
    
    init = start()



    #kills the processes once done
    for i in init.process.slaves:
        init.process.stop_process(i)

