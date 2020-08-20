import sys
import psutil


def generator(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return lines


def main(filepath):
    for line in generator(filepath):
        pass
    p = psutil.Process()
    with p.oneshot():
        vms = p.memory_info().vms / 2 ** 20
        cpu_times = p.cpu_times()
        total_time = cpu_times.user + cpu_times.system
    print(f'Virtual Memory Size = {vms:.3f}Mb')
    print(f'User Time + System Time = {total_time:.2f}s')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('usage: python3 generator.py filepath')
