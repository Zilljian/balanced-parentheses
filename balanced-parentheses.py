from queue import Queue
import time

start_time = time.time()


def is_fit(pair):
    temp_val = pair[0] * DIAGONAL[1] - pair[1] * DIAGONAL[0]
    if temp_val >= 0 and pair[0] <= DIAGONAL[0]: return True
    return False


queue = Queue()
inputLine = open('input.txt', 'r').read()

if len(inputLine) % 2 == 0:
    DIAGONAL = (len(inputLine) / 2, len(inputLine) / 2)
    counter = 1
    queue.put((0, 0))

    while not queue.empty():
        temp = queue.get()
        nextChar = sum(temp)

        if nextChar < len(inputLine):
            if inputLine[nextChar] == '(':
                if is_fit((temp[0] + 1, temp[1])):
                    queue.put((temp[0] + 1, temp[1]))
                else: counter -= 1
            elif inputLine[nextChar] == ')':
                if is_fit((temp[0], temp[1] + 1)):
                    queue.put((temp[0], temp[1] + 1))
                else:
                    counter -= 1
            elif inputLine[nextChar] == '?':
                if is_fit((temp[0] + 1, temp[1])):
                    queue.put((temp[0] + 1, temp[1]))
                    if is_fit((temp[0], temp[1] + 1)):
                        queue.put((temp[0], temp[1] + 1))
                        counter += 1
                elif is_fit((temp[0], temp[1] + 1)):
                    queue.put((temp[0], temp[1] + 1))
        else: break
    print("%.2f seconds are left" % (time.time() - start_time))
    print(counter)
else:
    print("Incorrect sequence of parentheses!")
