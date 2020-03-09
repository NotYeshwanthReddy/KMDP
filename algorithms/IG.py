import numpy as np
from functions import N, N_Calc, P, E

  def IG(k, SBS, EP, CP):
  S = np.array((),dtype=np.uint8)
  Nsbs = N_Calc(SBS, EP, CP)
  while(len(S) < k):
    max_E=0
    max_P=0
    for cp in CP:
      temp_S = np.append(S, cp)
      e = E(temp_S, C, Nsbs, SBS)
      if (e > max_E):
        max_E = e
        max_P = cp
    S = np.append(S, max_P)
    index = np.argwhere(CP==max_P)
    CP = np.delete(CP, index)
  return S
