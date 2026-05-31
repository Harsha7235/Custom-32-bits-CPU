class CodeAnalyzer:

    def analyze(self, code):

        lines = code.strip().split("\n")

        issues = []

        if len(lines) == 0:
            issues.append("Program is empty")

        if "HALT" not in code:
            issues.append("Program should end with HALT")

        for i,line in enumerate(lines):

            parts = line.split()

            if len(parts) == 0:
                continue

            instr = parts[0]

            valid = [
                "LOADI","ADD","SUB","MUL","DIV",
                "LOAD","STORE",
                "PUSH","POP",
                "JMP","JZ",
                "CALL","RET",
                "HALT"
            ]

            if instr not in valid:
                issues.append(f"Unknown instruction at line {i+1}")

        if len(issues) == 0:

            return {
                "status":"good",
                "message":"Program looks correct and ready to run"
            }

        return {
            "status":"warning",
            "issues":issues
        }