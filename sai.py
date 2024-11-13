class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0


class Scheduler:
    def calculate_metrics(self, processes):
        total_turnaround_time = 0
        total_waiting_time = 0
        n = len(processes)
        
        for p in processes:
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time
            total_turnaround_time += p.turnaround_time
            total_waiting_time += p.waiting_time

        print(f"{'PID':<10}{'Arrival':<10}{'Burst':<10}{'Priority':<10}{'Completion':<15}{'Turnaround':<15}{'Waiting':<10}")
        for process in processes:
            print(f"{process.pid:<10}{process.arrival_time:<10}{process.burst_time:<10}{process.priority:<10}{process.completion_time:<15}{process.turnaround_time:<15}{process.waiting_time:<10}")
        print("\nAverage Turnaround Time:", total_turnaround_time / n)
        print("Average Waiting Time:", total_waiting_time / n)


class FCFS(Scheduler):
    def schedule(self, processes):
        processes.sort(key=lambda x: x.arrival_time)
        current_time = 0

        for p in processes:
            if current_time < p.arrival_time:
                current_time = p.arrival_time
            p.completion_time = current_time + p.burst_time
            current_time += p.burst_time

        self.calculate_metrics(processes)


class SJFPreemptive(Scheduler):
    def schedule(self, processes):
        current_time = 0
        completed = 0
        n = len(processes)
        while completed < n:
            available_processes = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]
            if available_processes:
                shortest_job = min(available_processes, key=lambda x: x.remaining_time)
                shortest_job.remaining_time -= 1
                if shortest_job.remaining_time == 0:
                    shortest_job.completion_time = current_time + 1
                    completed += 1
                current_time += 1
            else:
                current_time += 1
        self.calculate_metrics(processes)


class PriorityNonPreemptive(Scheduler):
    def schedule(self, processes):
        processes.sort(key=lambda x: (x.arrival_time, x.priority))
        current_time = 0
        for p in processes:
            if current_time < p.arrival_time:
                current_time = p.arrival_time
            p.completion_time = current_time + p.burst_time
            current_time += p.burst_time
        self.calculate_metrics(processes)


class RoundRobin(Scheduler):
    def __init__(self, time_quantum):
        self.time_quantum = time_quantum

    def schedule(self, processes):
        queue = []
        current_time = 0
        for p in processes:
            queue.append(p)
        while queue:
            process = queue.pop(0)
            if process.remaining_time > self.time_quantum:
                current_time += self.time_quantum
                process.remaining_time -= self.time_quantum
                queue.extend([p for p in processes if p.arrival_time <= current_time and p not in queue and p.remaining_time > 0])
                queue.append(process)
            else:
                current_time += process.remaining_time
                process.completion_time = current_time
                process.remaining_time = 0
        self.calculate_metrics(processes)


# Test the implementation
def main():
    processes = []
    n = int(input("Enter the number of processes: "))

    for i in range(n):
        arrival_time = int(input(f"Enter arrival time for Process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for Process {i + 1}: "))
        priority = int(input(f"Enter priority for Process {i + 1} (lower value = higher priority): "))
        processes.append(Process(pid=i + 1, arrival_time=arrival_time, burst_time=burst_time, priority=priority))

    print("\nSelect Scheduling Algorithm:")
    print("1. FCFS")
    print("2. SJF (Preemptive)")
    print("3. Priority (Non-Preemptive)")
    print("4. Round Robin (Preemptive)")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nFCFS Scheduling:")
        fcfs = FCFS()
        fcfs.schedule(processes)
    elif choice == 2:
        print("\nSJF (Preemptive) Scheduling:")
        sjf = SJFPreemptive()
        sjf.schedule(processes)
    elif choice == 3:
        print("\nPriority (Non-Preemptive) Scheduling:")
        priority = PriorityNonPreemptive()
        priority.schedule(processes)
    elif choice == 4:
        time_quantum = int(input("Enter Time Quantum for Round Robin: "))
        print("\nRound Robin Scheduling:")
        rr = RoundRobin(time_quantum=time_quantum)
        rr.schedule(processes)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
