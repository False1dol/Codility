# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    stack = []
    blocks = 0

    for height in H:
        while stack and stack[-1] > height:
            stack.pop()

        if not stack or stack[-1] < height:
            stack.append(height)
            blocks += 1

    return blocks
