grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

def neibor(area,grid):
    for i in area:
        up=[i[0]-1,i[1]]
        down=[i[0]+1,i[1]]
        left=[i[0],i[1]-1]
        right=[i[0],i[1]+1]
        if i[0]-1>=0 and grid[i[0]-1][i[1]] and ([i[0]-1,i[1]] not in area): 
            area.append([i[0]-1,i[1]])
        if i[0]+1<len(grid) and grid[i[0]+1][i[1]] and ([i[0]+1,i[1]] not in area): 
            area.append([i[0]+1,i[1]])
        if i[1]-1>=0 and grid[i[0]][i[1]-1] and ([i[0],i[1]-1] not in area): 
            area.append([i[0],i[1]-1])
        if i[1]+1<len(grid[0]) and grid[i[0]][i[1]+1] and ([i[0],i[1]+1] not in area): 
            area.append([i[0],i[1]+1])        
    return len(area)

def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: i
    """
    maxarea=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            area=[]
            if grid[i][j]==1:
                area.append([i,j])
                num = neibor(area,grid)
                maxarea=max(maxarea,num)

    return maxarea

print maxAreaOfIsland(grid)