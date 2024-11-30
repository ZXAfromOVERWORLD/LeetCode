class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        R=len(box)
        C=len(box[0])
        def rotate(box):
            new=[[None]*R for x in range(C)]
            for i in range(R):
                for j in range(C):
                    new[j][i]=box[R-i-1][j]
            return new
        rbox=rotate(box)
        R=len(rbox)
        C=len(rbox[0])
        for j in range(C):
            last=R-1
            for current in range(R-1,-1,-1):
                match rbox[current][j]:
                    case "*":
                        last=current-1
                    case "#":
                        rbox[current][j]="."
                        rbox[last][j]="#"
                        last= last-1
                    case _:
                        continue
        return rbox



