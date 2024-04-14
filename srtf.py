import operator as op
from process import Process
from algorithm import Algorithm
from table import Table
from gantt import Gantt
import copy
from eval import Eval

class SRTF:

    def __init__(self, processes: list):
        self.processes = processes
        self.gantt = Gantt()

    def solve(self):
        n = len(self.processes)
        rt = [p.bt for p in self.processes] # remaining burst times
        complete = 0 # tracker kung ilang process na ang complete
        t = 0  # Current time
        minm = 999999999 # for comparison purposes lang kasi need doon sa while loop later
        short = 0  # Index of the shortest remaining process
        check = False # checker kung ready na ba ang process

        gantt_timeline = [] 

        while complete != n:

            # check kung may process na ba na ready na may maliit na bt
            for j in range(n):
                if (
                    self.processes[j].at <= t #Check if process arrival time is within current time
                    and rt[j] < minm # Check if remaining time is smaller, kaya super large yung minm para hindi magkaroon ng conflict
                    and rt[j] > 0 # Check if remaining time is non-zero
                ):
                    minm = rt[j]
                    short = j
                    check = True

            if check == False:
                t += 1
                continue

            rt[short] -= 1  # Decrease remaining time of the selected process. Feel ko dito rin ang may mali kaso i cant see it. baka meron kang makita HAHAHAHA
            current_process = copy.deepcopy(self.processes[short])  # Create a copy hihi


            minm = rt[short]
            if minm == 0:
                minm = 999999999 # Reset minm for the next iteration

            if rt[short] == 0: # Process finished
                complete += 1
                check = False

                # Calculate and update process attributes
                fint = t + 1 # finish time ito
                self.processes[short].et = fint 
                self.processes[short].tt = fint - self.processes[short].at 
                self.processes[short].wt = self.processes[short].tt - self.processes[short].bt

            # Update execution time and add to timeline
            current_process.bt = rt[short]  # Update remaining time
            current_process.bursted_by = 1  # Executed for 1 time unit. Dito eh baka factor din. Hindi ko lang maisip kung ano ang tamang computation kasi HAHAHAHA
            gantt_timeline.append(current_process)

            t += 1

        # After the calculation loop:
        table = Table(self.processes)  # Create Table instance
        table.draw_table()  # Display the table

        # Prepare data for the Gantt chart
        gantt_data = []
        for process in gantt_timeline:
            for i in range(process.bursted_by): 
                gantt_data.append(process) 
                
        gantt = Gantt(gantt_data)  # Create Gantt instance
        gantt.draw()   # Display the Gantt chart

        eval = Eval(self.processes)  # Create Eval instance
        eval.display_eval()  # Display evaluation metrics