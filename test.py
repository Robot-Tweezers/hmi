from multiprocessing import Process, Lock
from time import sleep

def update():
        for i in range(10):
                print(f"Child message {i}")
                sleep(1)


class GUIchild:
    def update(self):
            i = 0
            while True:
                    print(f"Child message {i}")
                    i += 1
                    sleep(1)

class GUI:
    def __init__(self):
            self.child = GUIchild()

            self.p = Process(target=self.child.update())
            self.p.start()

if __name__ == "__main__":
    # g = GUI()

    c = GUIchild()
    p = Process(target=update, args=())
    p.start()

    for i in range(10):
        print("Father")
        sleep(1)

    p.join(6)
    print("Done")
