class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {c: [] for c in range(numCourses)}
        for prereq in prerequisites:
            prereq_map[prereq[0]].append(prereq[1])
        # print(prereq_map)
        visited = set()
        result = []
        def possibleCourseOrdering(course, orderedCourse):
            if course in visited: return (False,[])
            if prereq_map[course]==[]: return(True, [course])

            visited.add(course)
            for prereq in prereq_map[course]:
                possiblePath,ordering = possibleCourseOrdering(prereq,orderedCourse)
                if not possiblePath: return (False,[])
                orderedCourse.extend(ordering)
            orderedCourse.append(course)
            visited.remove(course)
            prereq_map[course]=[]
            return(True,orderedCourse)

        for course in range(numCourses):
            # print(course)
            possiblePath,ordering = possibleCourseOrdering(course,[])
            # print(ordering)
            if not possiblePath: return []
            for order in ordering:
                if order not in result: result.append(order)
        return result


            