

class Heap:
    def __init__(self,data):
        self.heap_array=list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def pop(self):
        if len(self.heap_array)<=1:
            return None
        returned_data=self.heap_array[1]
        return returned_data

    def insert(self,data):
        if len(self.heap_array)==0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)
        index=len(self.heap_array)-1
        while index>1:
            if self.heap_array[index]>self.heap_array[index//2]:
                self.heap_array[index],self.heap_array[index//2]=self.heap_array[index//2],self.heap_array[index]
            index//=2
        return True

    def move_down(self.popped_idx):
        left_child_idx=popped_idx*2
        right_child_idx=popped_idx*2+1
        end_idx=len(self.heap_array)-1
        if left_child_idx > end_idx:
            return False
        elif left_child_idx == end_idx:
            return




    def delete(self, data):
        index=self.heap_array.index(data)
        end_in=len(self.heap_array)-1
        while index<=end_in:
            if index*2<end_in:
                
                



heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

li=[1,2,3,4]
li.pop()