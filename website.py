import time, os

class multithread:

    class slave:
        def __init__(self):
            self.alive = True
            self.task = []
            self.output = ""
            
        def read_output(self):
            while self.output == "":
                pass
            got_value = self.output
            self.output = ""
            return got_value
        
        def wait(self):
            while self.alive:
                if self.task:
                    self.output = self.task[0](*self.task[1])
                    self.task = []
                time.sleep(0.1)
        
            

    def __init__(self, threads_to_make: int):
        import threading
        self.slaves = {}

        for i in range(threads_to_make):
            thread_made = self.slave()
            slave_made = threading.Thread(target=thread_made.wait)
            slave_made.start()
            self.slaves[i] = thread_made

thread = multithread(1)

os.system(f"python -m http.server 8000 --bind 192.168.1.105 --directory {os.getcwd()}/website")