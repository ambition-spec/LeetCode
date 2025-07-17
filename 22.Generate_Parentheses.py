class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        result = []
        self.helper(n,n,'',result)
        return result

    def helper(self,l,r,item,result):
        if r < l:
            return
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.helper(l-1, r, item + '(', result)
        if r > 0:
            self.helper(l, r-1, item + ')', result)
#使用递归算法，self.helper（）函数为定义的每个节点：
#if r《l语句类似于剪枝的操作