from process import Process
from fcfs import FCFS
from sjf import SJF
from srtf import SRTF
from priority import Priority
from rr import RR


def main():

    # test_sjf()

    # test_priority()
    # test_rr()
    choices = list(map(str, range(1, 6)))
    print(choices)

    # test_fcfs()
    test_srtf()


def test_sjf():
    p1 = Process(1, 3, 4)
    p2 = Process(2, 5, 9)
    p3 = Process(3, 8, 4)
    p4 = Process(4, 0, 7)
    p5 = Process(5, 12, 6)

    processes = [p1, p2, p3, p4, p5]
    sjf = SJF(processes)
    sjf.solve()

def test_srtf():
    p1 = Process(1, 3, 4)
    p2 = Process(2, 5, 9)
    p3 = Process(3, 8, 4)
    p4 = Process(4, 0, 7)
    p5 = Process(5, 12, 6)

    processes = [p1, p2, p3, p4, p5]
    srtf = SRTF(processes)
    srtf.solve()


def test_fcfs():
    p1 = Process(1, 3, 4)
    p2 = Process(2, 5, 9)
    p3 = Process(3, 8, 4)
    p4 = Process(4, 0, 7)
    p5 = Process(5, 12, 6)

    processes = [p1, p2, p3, p4, p5]
    fcfs = FCFS(processes)
    fcfs.solve()


def test_priority():
    p1 = Process(1, priority=3, bt=10)
    p2 = Process(2, priority=1, bt=1)
    p3 = Process(3, priority=4, bt=2)
    p4 = Process(4, priority=5, bt=1)
    p5 = Process(5, priority=2, bt=5)

    processes = [p1, p2, p3, p4, p5]
    priority = Priority(processes=processes)
    priority.solve()


def test_rr():
    p1 = Process(1, bt=24)
    p2 = Process(2, bt=3)
    p3 = Process(3, bt=3)

    processes = [p1, p2, p3]
    rr = RR(processes, 4)
    rr.solve()


if __name__ == "__main__":
    main()
    # print("sssss"[:-1])
    # print("s" * 10)
