# 최단 경로
1. 음수 사이클이 없다.
    - 음수 가중치는 가능
2. 방향 그래프(directed graph)
3. 가중치 그래프(weighted graph)
4. 경로의 길이
    - 엣지 가중치의 합


---
1. one-source(출발지 1개), all-destination(모든 도착지)
    - dikjstra : Greedy algorithm
        - 음수 가중치 X
    - Bellman-ford
        - 음수 가중치 O
2. all-source(모든 출발지), all-destination
    - floyd-warshall : Dynamic programming
    

