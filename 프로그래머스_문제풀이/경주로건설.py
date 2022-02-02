from collections import deque

INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(board):
    n = len(board)

    def bfs(start):
        graph = [[INF] * n for _ in range(n)]  # 미리 최대값을 가진 그래프를 생성한다.

        q = deque([start])  # BFS 탐색을 하기 위해 Deque을 만들어준다.
        graph[0][0] = 0  # 시작 위치까지 비용은 0으로 초기화

        while q:
            x, y, cost, head = q.popleft()  # 탐색을 돌기 시작

            for d in range(4):  # 4방향으로 돌면서
                nx = x + dx[d]
                ny = y + dy[d]
                # 방향이 같으면 100원 추가, 다르면 600원 추가
                new_cost = cost + 100 if head == d else cost + 600

                # nx, ny가 범위 안에 있고, 길이 있으며 해당 위치까지의 비용이 더 적을 경우에만 탐색
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and graph[nx][ny] > new_cost:
                    graph[nx][ny] = new_cost
                    q.append((nx, ny, new_cost, d))
        return graph[-1][-1]

    return min(bfs((0, 0, 0, 1)), bfs((0, 0, 0, 3)))