class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_pos = [(ind,i) for ind,i in enumerate(position)]
        new_pos.sort(key = lambda x:x[1],reverse=True)
        result = 0
        car_is_overtake = -1
        for i in new_pos:
            time = (target - i[1]) / speed[i[0]]
            if time >car_is_overtake:
                car_is_overtake = time
                result +=1
        return result