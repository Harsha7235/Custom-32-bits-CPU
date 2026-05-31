class PerformanceAnalyzer:

    def analyze(self, cpu):

        return {
            "instructions": cpu.instructions,
            "cycles": cpu.cycles,
            "memory_reads": cpu.memory.reads,
            "memory_writes": cpu.memory.writes,
            "stack_peak": cpu.peak_stack
        }