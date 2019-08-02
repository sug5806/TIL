MST(Minimum (cost) Spanning Tree)

최소비용 신장트리
1. 연결되어 있다.(Connected)
2. 최소 엣지 수 
    - **|E| = |V| - 1 -> 트리의 조건**
    - E(G') 진 부분집합-> E(G)
3. MST를 구현할때의 조건
   - 엣지에 부여된 가중치의 최소합이다.
   - 무방향 그래프
   - 가중치 그래프
4.  탐욕 알고리즘(Greedy algorithm)
    1.  Kruskal algorithm -> 엣지의 가중치를 기반으로 Cut Property를 나눈다
    2.  Prim algorithm -> 
    3.  Sollin algorithm

탐욕 알고리즘
- 전역적 최적해(global optimum)를 찾기위해 
- 탐욕알고리즘이 성공하기 위한 조건
    1. Greedy choice property
        - 지역 최적해를 선택해 나가면 전역 최적해에 도달할 수 있다
    2. Optimal substructure
        - 문제에 대한 최적해가 부분 문제에 대한 최적해를 포함할 때


1 트리 : Connected acyclic graph (연결이 되어있으며 원형이 없는 그래프)
 - e = n-1

