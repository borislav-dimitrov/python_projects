# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

from __future__ import print_function # Py2 compat
from collections import namedtuple
import sys
from utils import timeit, load_files

# These define the structure of the history, and correspond to diff output with
# lines that start with a space, a + and a - respectively.
Keep = namedtuple('Keep', ['line'])
Insert = namedtuple('Insert', ['line'])
Remove = namedtuple('Remove', ['line'])

# See frontier in myers_diff
Frontier = namedtuple('Frontier', ['x', 'history'])

def myers_diff(a_lines, b_lines):
    """
    An implementation of the Myers diff algorithm.
    See http://www.xmailserver.org/diff2.pdf
    """
    # This marks the farthest-right point along each diagonal in the edit
    # graph, along with the history that got it there
    frontier = {1: Frontier(0, [])}

    def one(idx):
        """
        The algorithm Myers presents is 1-indexed; since Python isn't, we
        need a conversion.
        """
        return idx - 1

    a_max = len(a_lines)
    b_max = len(b_lines)
    for d in range(0, a_max + b_max + 1):
        for k in range(-d, d + 1, 2):
            # This determines whether our next search point will be going down
            # in the edit graph, or to the right.
            #
            # The intuition for this is that we should go down if we're on the
            # left edge (k == -d) to make sure that the left edge is fully
            # explored.
            #
            # If we aren't on the top (k != d), then only go down if going down
            # would take us to territory that hasn't sufficiently been explored
            # yet.
            go_down = (k == -d or
                    (k != d and frontier[k - 1].x < frontier[k + 1].x))

            # Figure out the starting point of this iteration. The diagonal
            # offsets come from the geometry of the edit grid - if you're going
            # down, your diagonal is lower, and if you're going right, your
            # diagonal is higher.
            if go_down:
                old_x, history = frontier[k + 1]
                x = old_x
            else:
                old_x, history = frontier[k - 1]
                x = old_x + 1

            # We want to avoid modifying the old history, since some other step
            # may decide to use it.
            history = history[:]
            y = x - k

            # We start at the invalid point (0, 0) - we should only start building
            # up history when we move off of it.
            if 1 <= y <= b_max and go_down:
                history.append(Insert(b_lines[one(y)]))
            elif 1 <= x <= a_max:
                history.append(Remove(a_lines[one(x)]))

            # Chew up as many diagonal moves as we can - these correspond to common lines,
            # and they're considered "free" by the algorithm because we want to maximize
            # the number of these in the output.
            while x < a_max and y < b_max and a_lines[one(x + 1)] == b_lines[one(y + 1)]:
                x += 1
                y += 1
                history.append(Keep(a_lines[one(x)]))

            if x >= a_max and y >= b_max:
                # If we're here, then we've traversed through the bottom-left corner,
                # and are done.
                return history
            else:
                frontier[k] = Frontier(x, history)

    assert False, 'Could not find edit script'

def diff2(e, f, i=0, j=0):
  #  Documented at http://blog.robertelder.org/diff-algorithm/
  N,M,L,Z = len(e),len(f),len(e)+len(f),2*min(len(e),len(f))+2
  if N > 0 and M > 0:
    w,g,p = N-M,[0]*Z,[0]*Z
    for h in range(0, (L//2+(L%2!=0))+1):
      for r in range(0, 2):
        c,d,o,m = (g,p,1,1) if r==0 else (p,g,0,-1)
        for k in range(-(h-2*max(0,h-M)), h-2*max(0,h-N)+1, 2):
          a = c[(k+1)%Z] if (k==-h or k!=h and c[(k-1)%Z]<c[(k+1)%Z]) else c[(k-1)%Z]+1
          b = a-k
          s,t = a,b
          while a<N and b<M and e[(1-o)*N+m*a+(o-1)]==f[(1-o)*M+m*b+(o-1)]:
            a,b = a+1,b+1
          c[k%Z],z=a,-(k-w)
          if L%2==o and z>=-(h-o) and z<=h-o and c[k%Z]+d[z%Z] >= N:
            D,x,y,u,v = (2*h-1,s,t,a,b) if o==1 else (2*h,N-a,M-b,N-s,M-t)
            if D > 1 or (x != u and y != v):
              return diff2(e[0:x],f[0:y],i,j)+diff2(e[u:N],f[v:M],i+u,j+v)
            elif M > N:
              return diff2([],f[N:M],i+N,j+N)
            elif M < N:
              return diff2(e[M:N],[],i+M,j+M)
            else:
              return []
  elif N > 0: #  Modify the return statements below if you want a different edit script format
    return [{"operation": "delete", "position_old": i+n} for n in range(0,N)]
  else:
    return [{"operation": "insert", "position_old": i,"position_new":j+n} for n in range(0,M)]

def myers_diff_length_half_memory(old, new):
    N = len(old)
    M = len(new)
    MAX = N + M

    V = [None] * (MAX + 2)
    V[1] = 0
    for D in range(0, MAX + 1):
        for k in range(-(D - 2*max(0, D-M)), D - 2*max(0, D-N) + 1, 2):
            if k == -D or k != D and V[k - 1] < V[k + 1]:
                x = V[k + 1]
            else:
                x = V[k - 1] + 1
            y = x - k
            while x < N and y < M and old[x] == new[y]:
                x = x + 1
                y = y + 1
            V[k] = x
            if x == N and y == M:
                return D

@timeit
def main():
    print('Reading files')
    a_lines, b_lines = load_files('file6.txt', 'file6.txt')

    print('Start getting the diff')
    diff = myers_diff(a_lines, b_lines)

    print('Saving the diff file')
    # save myers_diff
    with open('diff.txt', 'w') as diff_file:
        for elem in diff:
            if isinstance(elem, Keep):
                diff_file.write(f'*   {elem.line}\n')
            elif isinstance(elem, Insert):
                diff_file.write(f'ADD {elem.line}\n')
            else:
                diff_file.write(f'REM {elem.line}\n')

    # save diff2
    # with open('diff.txt', 'w') as diff_file:
    #   for dict_ in diff:
    #     if dict_['operation'] == 'insert':
    #         diff_file.write(f'+ {b_lines[dict_["position_new"]]}\n')
    #     elif dict_['operation'] == 'delete':
    #         diff_file.write(f'- {a_lines[dict_["position_old"]]}\n')

if __name__ == '__main__':
    sys.exit(main())
