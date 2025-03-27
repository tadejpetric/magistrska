import numpy as np

def str_to_obj(string: str) -> np.array:
    obj_list = []
    for line in string.splitlines():
        stack = []
        line_stack = []
        line_started = False
        for chr in line:
            if chr == "[":
                line_started = True
            elif chr == "]":
                assert len(stack) > 0
                elements = int("".join(stack))
                line_stack.append(elements)
                break
            elif chr == " " and line_started:
                assert len(stack) > 0
                elements = int("".join(stack))
                line_stack.append(elements)
                stack = []
            elif chr == " ":
                continue
            else:
                stack.append(chr)
        obj_list.append(line_stack)
    return np.array(obj_list)


if __name__ == "__main__":
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
    print(str_to_obj(matrix))