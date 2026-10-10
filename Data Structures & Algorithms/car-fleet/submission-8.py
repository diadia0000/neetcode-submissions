class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_pos = sorted(zip(position, speed), reverse=True)
        new_pos.sort(key = lambda x:x[0],reverse=True)
        result = 0
        car_is_overtake = -1
        for i in new_pos:
            time = (target - i[0]) / i[1]
            if time >car_is_overtake:
                car_is_overtake = time
                result +=1
        return result