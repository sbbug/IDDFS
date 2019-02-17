from collections import defaultdict


path = []
#使用邻接表来表示有向图
class Graph:

    def __init__(self, vertices):

        # 图的顶点个数
        self.V = vertices

        # 存储图形的默认字典
        self.graph = defaultdict(list)

        # 定义一个方法，往有向图添加方法
    def addEdge(self, u, v):
        self.graph[u].append(v)

    #执行深度限制搜索的方法
    def DLS(self, src, target, maxDepth):
        path.append(src)
        '''
        :param src: 起点
        :param target: 终点
        :param maxDepth: 搜索的最大深度
        :return:
        '''
        #如果找到目标，返回真
        if src == target:
            print(path)
            return True

        # 如果到达最大深度，停止循环.
        if maxDepth <= 0:
            print(path)

            return False

        # 搜索该顶点的邻接顶点，采取递归搜索
        for i in self.graph[src]:
            if (self.DLS(i, target, maxDepth - 1)):
                return True
            path.remove(i)
        return False

    #搜索方法入口
    def IDDFS(self, src, target, maxDepth):
        '''
        :param src: 起点
        :param target: 终点
        :param maxDepth: 搜索的最大深度
        :return:
        '''
        #从0开始到maxDepth进行测试
        for i in range(maxDepth):
            path.clear()
            if (self.DLS(src, target, i)):
                return True

        return False


if __name__ == "__main__":

    # 创建一个有向图
    g = Graph(7);
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(2, 6)

    #搜索目标
    target = 6;
    #最大深度
    maxDepth = 3;
    #开始点
    src = 0

    if g.IDDFS(src, target, maxDepth) == True:
        print("可达")
    else:
        print("不可达")

