Property: https://www.youtube.com/watch?v=7C9RgOcvkvo

# DFS/BFS

- **탐색** : 데이터 중에서 원하는 데이터를 찾는 과정
- **그래프 탐색 알고리즘** : **DFS, BFS**

## 스택과 큐 자료구조

### 스택

- **FIFO**
  - (python) 기본 **List**로 구현한다
- 예시 코드

  ```python
  **stack = []**

  # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
  stack.append(5)
  stack.append(2)
  stack.append(3)
  stack.append(7)
  stack.pop()
  stack.append(1)
  stack.append(4)
  stack.pop()

  print(stack) # 최하단 원소부터 출력
  print(stack[::-1]) # 최상단 원소부터 출력
  ```

### 큐

- **LIFO**
  - (python) list로도 구현이 가능하지만 시간복잡도가 높아진다
- 예시 코드

  ```python
  **from collections import deque**

  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque()

  # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
  queue.append(5)
  queue.append(2)
  queue.append(3)
  queue.append(7)
  queue.popleft()
  queue.append(1)
  queue.append(4)
  queue.popleft()

  print(queue) # 먼저 들어온 순서대로 출력
  **queue.reverse()** # 다음 출력을 위해 역순으로 바꾸기
  print(queue) # 나중에 들어온 원소부터 출력
  ```

## 재귀 함수

- **Recursive Function**
- **DFS 구현**에 많이 사용된다
  - (python) 최대 재귀 깊이 제한 존재
  - **종료 조건**을 명시하여 함수를 종료시킨다
- 예시 코드

  ```python
  **>> factorial

  # 반복적으로 구현한 n!**
  def factorial_iterative(n):
      result = 1
      # 1부터 n까지의 수를 차례대로 곱하기
      for i in range(1, n + 1):
         result *= i
      return result

  **# 재귀적으로 구현한 n!**
  def factorial_recursive(n):
      **if n <= 1: # n이 1 이하인 경우 1을 반환 (종료 조건)**
          return 1
      # n! = n * (n - 1)!를 그대로 코드로 작성하기
      return n * factorial_recursive(n - 1)

  # 각각의 방식으로 구현한 n! 출력(n = 5)
  print('반복적으로 구현:', factorial_iterative(5))
  print('재귀적으로 구현:', factorial_recursive(5))
  ```

  ```python
  **>> 유클리드 호제법 (최대공약수)**

  def gcd(a, b):
  	**if a%b == 0: (종료 조건)**
  		return b
  	else:
  		return gcd(b, a%b)

  gcd(192, 162)

  ```

- **재귀함수**는 **반복문**을 이용하여 **동일**한 기능을 구현 할 수 있다
  - 각각이 불리, 유리한 경우가 존재
- 컴퓨터가 함수를 연속적으로 호출하면 메모리 내부의 스택 프레임에 쌓기게 된다,
  - 이를 이용해서 스택을 사용해야 할 때, 구현상 **스택** 라이브러리 **대신 재귀함수를 이용**하는 경우가 많다 ⇒ **DFS**

## DFS (Depth-First Search)

- **깊이 우선 탐색**
  - 깊은 부분을 우선적으로 탐색하는 알고리즘
  - **스택 / 재귀** 함수를 이용
- **동작 과정**

  1. **탐색 시작 노드**를 **스택**에 삽입 + 방문 처리
  2. 스택의 **최상단 노드에 방문하지 않은 인접한 노드가 하나라도 존재**하면,
     1. **그 노드를 스택에 넣고 방문 처리**
     2. 방문하지 않은 인접 노드가 **없으면 스택에서 최상단 노드를 꺼낸다**
  3. **종료 조건**까지, 2번을 반복

- (python) **그래프 → 2차원 리스트 형태로 표현**

  - 그래프 문제 : **노드가 1번 부터 시작**하는 경우가 많기 때문에,
    - [0]을 비워두고, **[1]번 부터 시작**한다

  ```python
  **# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
  >> 인접 리스트 방식 : 그래프**
  graph = [
    [],
    1 -> [2, 3, 8],
    2 -> [1, 7],
    3 -> [1, 4, 5],
    4 -> [3, 5],
    5 -> [3, 4],
    6 -> [7],
    7 -> [2, 6, 8],
    8 -> [1, 7]
  ]

  **# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
  >> 방문 체크 ([0]사용하지 않기 때문에 *9)**
  visited = [False] * 9

  **# DFS 함수 정의**
  def dfs(graph, v, visited):
      # 현재 노드를 **방문 처리
      visited[v] = True**
      print(v, end=' ')

      # 현재 노드와 **연결된 다른 노드를 재귀적으로 방문
      for i in graph[v]:
          if not visited[i]:
              dfs(graph, i, visited)**

  # 정의된 DFS 함수 호출
  dfs(graph, 1, visited)
  ```

## BFS (Breadth-First Search)

- **너비 우선 탐색**
  - 가까운 노드부터 우선적으로 탐색하는 알고리즘
  - **큐** 이용 \*\*\*\*
- **동작 과정**
  1. **탐색 시작 노드**를 **큐**에 삽입 + 방문 처리
  2. **큐에서 노드를 꺼낸 뒤**, 해당 노드의 **인접 노드 중에서 방문하지 않은 노드**를 **모두 큐에 삽입하고 방문 처리 (한 번에 넣어서 처리)**
  3. **종료 조건**까지, 2번을 반복
- 특정 조건에서의 **최단 경로 찾기 문제**에서 효율적
  - 거리에 따라 방문 노드가 결정되는 특징
  - 각 간선의 비용이 동일한 상황에서의 최단 거리 문제
- (python) **그래프 → 2차원 리스트 형태로 표현**

  - 그래프 문제 : **노드가 1번 부터 시작**하는 경우가 많기 때문에,
    - [0]을 비워두고, **[1]번 부터 시작**한다

  ```python
  **from collections import deque**

  # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
  **>> 인접 리스트 방식 : 그래프**
  graph = [
    [],
    1 -> [2, 3, 8],
    2 -> [1, 7],
    3 -> [1, 4, 5],
    4 -> [3, 5],
    5 -> [3, 4],
    6 -> [7],
    7 -> [2, 6, 8],
    8 -> [1, 7]
  ]

  **# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
  >> 방문 체크 ([0]사용하지 않기 때문에 *9)**
  visited = [False] * 9

  **# BFS 함수 정의**
  def bfs(graph, start, visited):
      # 큐(Queue) 구현을 위해 deque 라이브러리 사용
      queue = **deque([start])**
      # 현재 노드를 **방문 처리
      visited[start] = True**

      **# 큐가 빌 때까지 반복
      while queue:**
          # 큐에서 **하나의 원소를 뽑아 출력
          v = queue.popleft()**
          print(v, end=' ')
          # 해당 원소와 **연결된, 아직 방문하지 않은 원소들을 큐에 삽입
          for i in graph[v]:
              if not visited[i]:
                  queue.append(i)
                  visited[i] = True**

  # 정의된 BFS 함수 호출
  bfs(graph, 1, visited)
  ```
