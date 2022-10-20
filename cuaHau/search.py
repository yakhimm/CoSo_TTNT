from __future__ import annotations
from typing import Callable, TypeVar,Generic,Optional,List,Dict
from heapq import heappush, heappop

S=TypeVar('S') # for int, string any type
     
class PriorityQueue(Generic[S]):
    def __init__(self) -> None:
        self.l: List[S] = []

    @property
    def empty(self):
        if self.l:
            return False
        else:
            return True    

    def push(self, item: S) -> None:
        heappush(self.l, item)  # use in huaristic

    def pop(self) -> S:
        return heappop(self.l)  

# node is some position in maze and parent is from where we get that node
class box(Generic[S]):
    def __init__(self, state: S, p: Optional[box], cost = 0.0, h = 0.0) -> None:
        self.state = state
        self.p= p
        self.cost = cost
        self.h= h

    def __lt__(self, other: box) -> bool:
        return (self.cost + self.h) < (other.cost + other.h)

#helper function for backtracking using parent node
def goal_to_start(n: box[S]) -> List[S]:
    b_p: List[S] = [n.state]

    while n.p is not None:
        b_p.append(n.state)
        n=n.p
    b_p.reverse()
    return b_p

    
def uniform(start: S, check_end: Callable[[S], bool], check_next_node: Callable[[S], List[S]]) -> Optional[box[S]]:
    
    my_p_q = PriorityQueue()
    satte=box(start, None,0.0 )
    my_p_q.push(satte)

    visited: Dict[S, float] = {start: 0.0}

    while  my_p_q.empty== False:
        recent_box = my_p_q.pop()
        current_state = recent_box.state
      
        if check_end(current_state) == True:  # if goal state has been reached.........
            return recent_box
        else:
            for elements in check_next_node(current_state):
                n_c = recent_box.cost + 1  

                if elements not in visited or  n_c < visited[elements] :
                    visited[elements] = n_c
                    state=box(elements, recent_box, n_c)
                    my_p_q.push(state)
    return None  