

from collections import deque

tools = deque([int(x) for x in input().split()])
substances  = list([int(x) for x in input().split()])
challenges = list([int(x) for x in input(). split()])

while substances and tools and challenges:
    result = tools[0] * substances[-1]

    if result in challenges:
        tools.popleft()
        substances.pop()
        challenges.remove(result)
    else:
        tools[0] += 1
        tools.append(tools.popleft())
        substances[-1] -= 1
        if substances[-1] <= 0:
            substances.pop()

if challenges:
    print('Harry is lost in the temple. Oblivion awaits him.')
else:
    print('Harry found an ostracon, which is dated to the 6th century BCE.')

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")
if substances:
    print(f"Substances: {', '.join(map(str, substances))}")
if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")
