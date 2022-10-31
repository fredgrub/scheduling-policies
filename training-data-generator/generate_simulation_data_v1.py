from scheduling_simulator import SchedulingSimulator

def main():
    workload_file = "lublin_256.swf"
    number_of_tuples = 2
    number_of_trials = 200 
    state_size = 4
    queue_size = 12
    random_seed = 42

    simulator = SchedulingSimulator(workload_file, number_of_tuples, number_of_trials, state_size, queue_size, random_seed)
    # simulator.simulate()
    simulator.clear_state()

if __name__ == "__main__":
    main()