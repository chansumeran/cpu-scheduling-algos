import math
from gantt import Gantt
import copy
from table import Table
from eval import Eval


class RR:
    def __init__(self, quantum=0, processes=[]) -> None:
        self.processes = processes
        self.copy = copy.deepcopy(processes)
        self.current_time = 0
        self.quantum = quantum
        self.sorted = sorted(processes, key=lambda x: x.process_id)
        self.gantt = Gantt()
        self.gantt_timeline = []
        self.table = Table(self.copy)

    def solve(self):
        while self.has_burst_in_multiple():

            for current_process in self.sorted:

                if self.has_burst_single(current_process):
                    self.current_time += min(self.quantum, current_process.bt)

                    current_process.bursted_by = min(self.quantum, current_process.bt)

                    current_process.bt = current_process.bt - self.quantum
                    current_process.et = self.current_time
                    current_process.tt = current_process.et - current_process.at
                    current_process.wt = current_process.tt - current_process.bt

                    self.gantt_timeline.append(copy.deepcopy(current_process))

        self.gantt.processes = self.gantt_timeline
        self.gantt.draw()

        index = 0
        for i in self.copy:
            i.et = self.processes[index].et
            i.tt = self.processes[index].tt
            i.wt = self.processes[index].wt

            index += 1

        self.table.draw_table()

        eval = Eval(self.copy)
        eval.display_eval()

    def has_burst_in_multiple(self):
        for p in self.processes:
            if p.bt > 0:
                return True
        return False

    def has_burst_single(self, process):
        return process.bt > 0

    def find_by_id(self, id):
        for p in self.processes:
            if p.process_id == id:
                return p
        return None
