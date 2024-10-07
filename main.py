from machine_manager import MyMachine
from observers import StopObserver, StartupObserver, SleepObserver

if __name__ == "__main__":
    machine = MyMachine()
    machine.add_observer(StartupObserver)
    machine.start()
    machine.sleep()  # it works but sleep observer won't work because it's not added to observers
