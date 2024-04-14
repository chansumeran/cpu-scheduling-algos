"""
    Main terminal program. Dito natin ilagay yung user interface na kung saan mag-iinput yung user ng processes. Dapat daw
    user input yung processes: how many processes --> input arrival time --> input burst time
"""

from fcfs import FCFS
from priority import Priority
from rr import RR
from sjf import SJF
from srtf import SRTF
from process import Process
from algorithm import Algorithm
from colorama import Fore
import os


class UI:

    def __init__(self) -> None:
        self.fcfs = FCFS()
        self.priority = Priority()
        self.rr = RR()
        self.sjf = SJF()
        pass

    def run(self):
        isRunning = True

        while isRunning:
            algorithm = self._prompt_algorithm()
            if algorithm == "6":
                os.system("cls")
                continue
            elif algorithm == "7":
                isRunning = False
                continue
            else:
                algorithm = int(algorithm)

            processes = self._prompt_processes(algorithm)

            quantum = 0
            if algorithm == Algorithm.RR.value:
                quantum = int(input("Quantum: "))

            self._solve(algorithm, processes, quantum=quantum)

            isRunning = self._prompt_continue()

    def _solve(self, algorithm, processes, quantum=0):
        if algorithm == Algorithm.FCFS.value:
            self.fcfs = FCFS(processes)
            self.fcfs.solve()
        elif algorithm == Algorithm.PRIORITY.value:
            self.priority = Priority(processes)
            self.priority.solve()
        elif algorithm == Algorithm.SJF.value:
            SJF(processes).solve()
        elif algorithm == Algorithm.RR.value:
            RR(processes=processes, quantum=quantum).solve()
        elif algorithm == Algorithm.SRTF.value:
            SRTF(processes).solve()

    def _prompt_processes(self, algorithm):
        num_processes = int(input("Number of processes >> "))
        processes = []
        for i in range(num_processes):
            if algorithm in [
                Algorithm.FCFS.value,
                Algorithm.SJF.value,
                Algorithm.SRTF.value,
            ]:
                process_attrs = (
                    str(input(f"Process {i+1} [AT BT]: ")).strip().split(sep=" ")
                )
                process_attrs = list(map(int, process_attrs))
                processes.append(
                    Process(i + 1, at=process_attrs[0], bt=process_attrs[1])
                )

            elif algorithm == Algorithm.PRIORITY.value:
                process_attrs = (
                    str(input(f"Process {i+1} [Priority BT]:")).strip().split(sep=" ")
                )
                process_attrs = list(map(int, process_attrs))
                processes.append(
                    Process(i + 1, priority=process_attrs[0], bt=process_attrs[1])
                )

            elif algorithm == Algorithm.RR.value:
                process_attrs = (
                    str(input(f"Process {i+1} [BT]:")).strip().split(sep=" ")
                )
                process_attrs = list(map(int, process_attrs))
                processes.append(Process(i + 1, bt=process_attrs[0]))

        return processes

    def _prompt_algorithm(self):
        valid = False
        choices = list(map(str, range(1, 8)))
        while not valid:
            print(
                f"\n[1] First Come First Serve\n[2] Shortest Job First\n[3] Shortest Remaining Time First\n[4] Priority\n[5] Round Robin\n{Fore.CYAN}[6] Clear Screen {Fore.WHITE}\n{Fore.RED}[7] Exit{Fore.WHITE}\n\nSelect algorithm >> ",
                end="",
            )
            try:
                choice = input()
                if choice in choices:
                    valid = True
                else:
                    print(f"{Fore.RED}Usage: [1-5]\nPlease try again.{Fore.WHITE}")
            except:
                print(f"{Fore.RED}Usage: [1-5]\nPlease try again.{Fore.WHITE}")

        return choice

    def _prompt_continue(self):
        print(
            f"\nDo you want to continue? [{Fore.GREEN}y{Fore.WHITE} {Fore.LIGHTRED_EX}n{Fore.WHITE}]"
        )
        choice = str(input(">> "))
        return choice == "y"
