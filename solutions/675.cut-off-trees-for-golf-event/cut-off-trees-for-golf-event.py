from collections import deque
class Solution:
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def cutOffTree(self, forest):
        #print(forest)
        rows = len(forest)
        if rows == 0:
            return 0

        cols = len(forest[0])
        if cols == 0:
            return 0

        forest.append([0] * cols)
        for row in forest:
            row.append(0)

        trees = {(r, c) for c in range(cols) for r in range(rows) if forest[r][c] > 1}

        visited = {(0, 0)}
        queue = [(0, 0)]
        while len(queue) != 0:
            r, c = queue.pop()
            for nr, nc in ((r + dr, c + dc) for dr, dc in self.d):
                if (nr, nc) not in visited and forest[nr][nc] > 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        if trees.difference(visited):
            return -1

        trees = sorted(trees, key=lambda t: forest[t[0]][t[1]])
        if trees[0] != (0, 0):
            trees.insert(0, (0, 0))
        num_trees = len(trees)
        #print('TREES:', trees)

        total_steps = 0
        for i in range(1, num_trees):
            pr, pc = p = trees[i - 1]
            qr, qc = q = trees[i]
            cost = abs(pr - qr) + abs(pc - qc)

            queue, next_queue = [], [] # Using list: 0.53s, 0.52s, 0.54s
            #queue, next_queue = deque(), deque() # Using deque: 1.45s, 1.50s, 1.46s
            queue.append(p)
            visited, pending_visited = {p}, set()
            while len(queue) + len(next_queue) != 0:
                if len(queue) == 0:
                    queue = next_queue
                    next_queue = deque()

                    visited.update(pending_visited)
                    pending_visited = set()
                    cost += 2

                (r, c) = queue.pop() # Using list
                #(r, c) = queue.popleft() # Using deque
                #print('POP', r, c, cost)

                safe_dr = qr - r
                safe_dr = safe_dr and safe_dr // abs(safe_dr)
                safe_dc = qc - c
                safe_dc = safe_dc and safe_dc // abs(safe_dc)
                for dr, dc in self.d:
                    nbr = (r + dr, c + dc)
                    if nbr not in visited and forest[nbr[0]][nbr[1]] > 0:
                        #print('SAFE', (safe_dr, safe_dc), 'D', (dr, dc))
                        if (dr == safe_dr and dc != -safe_dc) or (dc == safe_dc and dr != -safe_dr):
                            queue.append(nbr)
                            visited.add(nbr)
                            ncost = cost
                            #print('PUSH', nbr)
                        else:
                            next_queue.append(nbr)
                            pending_visited.add(nbr)
                            ncost = cost + 2
                            #print('PUSH NEXT', nbr)
                        if nbr == q:
                            #print('COST:', p, q, ncost)
                            total_steps += ncost
                            queue = next_queue = list()
                            break

                # print('MAP', cost)
                # for rr in range(rows):
                #     for cc in range(cols):
                #         if (rr, cc) == (r, c):
                #             print('*', end='')
                #         elif (rr, cc) in queue:
                #             print('Q', end='')
                #         elif (rr, cc) in visited:
                #             print('+', end='')
                #         elif (rr, cc) in next_queue:
                #             print('N', end='')
                #         else:
                #             print(forest[rr][cc], end='')
                #     print()

        return total_steps