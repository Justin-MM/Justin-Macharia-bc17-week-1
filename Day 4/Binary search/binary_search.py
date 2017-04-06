class BinarySearch(list):
    def __init__(self, a, b):
        self.new_list = [x for x in range(b, (a*b)+1, b)]
        super(BinarySearch, self).__init__(self.new_list)
        self.a = a  # length of list to be created
        self.b = b  # step between consecutive variables

        self.new_list = [x for x in range(b, (a*b)+1, b)]
        self.length =  len(self.new_list)# returns the number of elements in the array
        self.count = 0 # number of times function iterated to find index of num being searched


    def search(self, find):

        new_list = self
        found = False
        start = 0 # index
        count = 0
        self.length = len(self)
        last = self.length - 1 #
        search_result = {'count':'', 'index':''}
        mid = ((start + last) // 2)

        while start <= mid:


            if (start == mid) and (new_list[start] > find):
                index = -1
                search_result["count"] = self.length
                search_result["index"] = index
                return search_result
            elif self[start] == find:
                index = start
                search_result["count"] = count
                search_result["index"] = index
                return search_result
            elif new_list[last] == find:
                index = last
                search_result["count"] = count
                search_result["index"] = index
                return search_result
            elif new_list[mid] == find:
                index = mid
                search_result['count'] = count
                search_result['index']= index
                return search_result

            else:
                if find < new_list[mid]:
                    start = start + 1 # index
                    last = mid - 1
                    mid = (start + last)//2
                elif find > new_list[mid]:
                    start = mid + 1 # index
                    last = last - 1
                    mid = (start + last)//2
            count += 1
        search_result = {'count':count,'index':-1}
        return search_result

__author__ = 'Justin M'


