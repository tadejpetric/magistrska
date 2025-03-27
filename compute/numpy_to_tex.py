

matrix = """
[[0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0]
 [0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0]
 [0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0]
 [0 0 0 0 1 1 0 0 0 0 0 0 0 0 1 1]
 [1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0]
 [1 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1]
 [0 0 0 0 0 0 1 1 0 0 0 0 1 1 0 0]
 [0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0]
 [0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0]
 [0 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0]
 [0 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0]]
""".strip()

print("\\begin{bmatrix}")

for line in matrix.splitlines():
    stack = []
    line_stack = []
    line_started = False
    for chr in line:
        if chr == "[":
            line_started = True
        elif chr == "]":
            assert len(stack) > 0
            elements = "".join(stack)
            line_stack.append(elements)
            break
        elif chr == " " and line_started:
            assert len(stack) > 0
            elements = "".join(stack)
            line_stack.append(elements)
            stack = []
        elif chr == " ":
            continue
        else:
            stack.append(chr)
    

    print("\t"+" & ".join(line_stack) + "\\\\")

print("\\end{bmatrix}")