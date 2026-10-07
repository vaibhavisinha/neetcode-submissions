class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_map = dict(zip(position,speed))
        position.sort(reverse=True)
        fleet_stack = []

        for pos in position:
            curr_time = (target-pos)/position_speed_map[pos]
            if not fleet_stack:
                fleet_stack.append(curr_time)
                continue
            prev_time = fleet_stack[-1]
            if curr_time > prev_time: fleet_stack.append(curr_time)
        return len(fleet_stack)