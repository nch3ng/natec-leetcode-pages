class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.min_item = None
        self.top_item = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        # Empty case
        if not self.list:
            self.min_item = x
            self.list.append(x)
        else:
            self.list.append(x)
            self.min_item = min(self.list)
            # if x < self.min_item:
            #     self.min_item = x
        
        
        self.top_item  = x

        # print(self.list)
        # print(min([-2,0-3]))
        
    def pop(self):
        """
        :rtype: void
        """

        if not self.list:
            return

        value = self.list.pop()

        if not self.list:
            self.top_item = None
            self.min_item = None
        else:
            self.top_item = self.list[-1] 
            self.min_item = min(self.list)
        
        
    def top(self):
        """
        :rtype: int
        """
        return self.top_item

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_item
