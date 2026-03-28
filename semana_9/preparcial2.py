# PUNTO 1
inbox, outbox = [], []

def transfer():
    if not outbox:
        while inbox:
            outbox.append(inbox.pop())

for i in range(int(input())):
    q = input().split()
    if q[0] == '1':
        inbox.append(q[1])
    elif q[0] == '2':
        transfer()
        outbox.pop()
    else:
        transfer()
        print(outbox[-1])

# PUNTO 2 
def preOrder(root):
    if root:
        print(root.info, end=' ')
        preOrder(root.left)
        preOrder(root.right)

# PUNTO 3 
for case in range(1, T+1):
    R, C, M, N = map(int, input().split())
    W = int(input())
    water = set(tuple(map(int, input().split())) for _ in range(W))

    moves = [(M,N),(M,-N),(-M,N),(-M,-N),(N,M),(N,-M),(-N,M),(-N,-M)]

    visited = {(0,0)}
    queue = deque([(0,0)])
    while queue:
        r, c = queue.popleft()
        for dr, dc in moves:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and (nr,nc) not in water and (nr,nc) not in visited:
                visited.add((nr,nc))
                queue.append((nr,nc))

    even = odd = 0
    for r, c in visited:
        k = sum(1 for dr,dc in moves if 0 <= r+dr < R and 0 <= c+dc < C and (r+dr,c+dc) not in water)
        if k % 2 == 0: even += 1
        else: odd += 1

    print(f"Case {case}: {even} {odd}")
