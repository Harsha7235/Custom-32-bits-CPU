class VMTranslator:

    def translate(self, code):

        lines = code.split("\n")
        asm = []

        for line in lines:

            parts = line.strip().split()

            if not parts:
                continue

            if parts[0] == "push" and parts[1] == "constant":

                value = parts[2]

                asm.append(f"LOADI 1 {value}")
                asm.append("PUSH 1")

            elif parts[0] == "add":

                asm.append("POP 2")
                asm.append("POP 1")
                asm.append("ADD 1 2")
                asm.append("PUSH 1")

        return asm