import heapq

from functions import N, N_Calc, P, E


def SPG(k, SBS, EP, CP):
  k = [(0, 0)]*k
  heapq.heapify(k)
  Nsbs = N_Calc(SBS, EP, CP)
  for cp in CP:
    S = set()
    S.add(cp)
    e = E(S, C, Nsbs, SBS)
    heapq.heappush(k, (e, cp))
    heapq.heappop(k)
  return k
