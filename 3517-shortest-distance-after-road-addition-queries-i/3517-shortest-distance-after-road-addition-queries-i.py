class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        INF=10**20
        ad_list = collections.defaultdict(list)
        for i in range (n-1):
            ad_list[i].append(i+1)
        ans=[]
        for a,b in queries:
            ad_list[a].append(b)
            done=[INF]*n
            q=collections.deque()
            q.append(0)
            done[0]=0
            while len(q)>0:
                current=q.popleft()

                for x in ad_list[current]:
                    if done[x]> done[current]+1:
                        done[x]=done[current]+1
                        q.append(x)
            print(len(q))

            ans.append(done[n-1])
        return ans
        
