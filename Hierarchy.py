#### HIERARCHY CLASS ###########################################################

class Hierarchy:
    adj_list = {}

    # Initializes the adjacency list and sets the root node
    def __init__(self, boss):
        self.adj_list[boss] = []

    # Adds new employees to the hierarchy, given who they report to
    # the person they report to needs to already be in the hierarchy
    def add(self, person, reports_to):
        reporting = self.adj_list.get(reports_to, None)
        if (reporting == None):
            print(f"[ERR] No such person {reports_to}")
        else:
            self.adj_list[reports_to].append(person)
            self.adj_list[person] = []

    # finds who a employee reports to
    def reports_to(self, person):
        for i in self.adj_list:
            if (person in self.adj_list[i]):
                return i
        else:
            return None

    # Removes an employee from the hierarchy
    def remove(person):
        reporting = self.reports_to(person)
        if (reporting == None):
            print("[ERR] Cannot remove the boss!")
        else:
            self.adj_list[reporting] += adj_list[person]
            self.adj_list[reporting].remove(person)
            self.adj_list.pop(person)

    # Returns all employees reporting to a specific employee/manager
    def get_hierarchy(self, person):
        loop_list = []
        reporting_list = []
        for i in self.adj_list[person]:
            loop_list.append(i)
        while (len(loop_list) != 0):
            a = loop_list.pop()
            reporting_list.append(a)
            loop_list += self.adj_list[a]
        return reporting_list

#### EOF #######################################################################
