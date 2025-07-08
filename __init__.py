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
            self.num = 0
            while True:
                time.sleep(0.01)
                self.num += 1
                data = self.task_queue.get()
                if not data["alive"] or self.num >= (60 * 100):
                    break
                if data["tasks"]:
                    self.num = 0
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

def check_for_bad_prints(file):
    #this is so damn inneficient oh well

    with open(file, "r") as prints:
        file_data = prints.readlines()
        print_num = 0
        line = 0

        for i in file_data:
            line += 1
            if 'print(' in i:
                print_num += 1

                if print_num > 1:
                    return False
        return True

def start_app(data):
    os.system(f"python {data[0]}")


if __name__ == "__main__":

    to_run_mp = []
    
    with open(f"{os.getcwd()}/dict.json", "r") as data:

        for app in json.loads(data.read())["mp_apps"]:
            if app[0] == "True":
                if check_for_bad_prints(f"{os.getcwd() + app[1]}"):
                    to_run_mp.append(app[1])
                else:
                    Print(f"err: {app[1]} has too many prints")

    multi = Multiprocess(len(to_run_mp), {"start_app": start_app})

    for process in multi.slaves:
        multi.submit_task(["start_app", [f"{os.getcwd() + to_run_mp[process]}", process]], process)
