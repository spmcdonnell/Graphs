class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        queue.enqueue(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
            #    Pop the first item
            vertex = queue.dequeue()
        #    If not visited
            if vertex not in visited:
                #       DO THE THING!
                print(vertex)
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    #           Add that edge to the queue/stack
                    queue.enqueue(next_vert)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a queue/stack as appropriate
        stack = Stack()
        # Put the starting point in that
        # Enstack a list to use as our path
        stack.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while stack.size() > 0:
            #    Pop the first item
            path = stack.pop()
            vertex = path[-1]
        #    If not visited
            if vertex == destination_vertex:
                # Do the thing!
                return path
            if vertex not in visited:
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug
                    # Make a copy of path rather than reference
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    # if len(new_path) <= 1:


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for ancestor in ancestors:
        graph.add_vertex(ancestor[0])
        graph.add_vertex(ancestor[1])

    for ancestor in ancestors:
        graph.add_edges(ancestor[1], ancestor[0])

    print('Vertices:', graph.vertices)

    new_path = []

    for ancestor in ancestors:

        path = graph.dfs(starting_node, ancestor[0])

        print('Path:', path)

        if path != None and len(path) > len(new_path):

            new_path = path.copy()

            print('Updated path:', new_path)


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(ancestors, 6))


# General Info
# ------------

# 1. "Highlight previous experience living abroad and being able to adapt. Highlight language learning and connection to learning new skills/programming languages, and that you have learned how to learn"

# 2. "Highlight that because your current company is small, you are required to do a variety of things - never say 'Hey, its not my job"

# 3. "Highlight that you have taught English which has sharpened communication with people."

# 4. "Ask questions effectively so as to get clear answers and not offload work to someone else"

# 5. "Backflip onto mats analogy"


# Scenarios
# ---------

# Problems/Conflicts

# 1. "Designers don't know how to design for the web, rather for catelogs - I made resources for then"

# 2. "Disagreement with other devs. 2 strategies. 1. Let them go through and see the problem/solution for themselves. 2. Offer to try a solution just to see if it works, at the very least it eliminates a possibility"

# Initiative/Proud of

# 3. "Company was using shortcodes on pages and clients were breaking the page. I proposed using custom fields and figured out how to do it. It is now the standard we use for development"

# 4. "We made generic sites with one specific wordpress template. Boss didn't want to deviate and wasn't sure anything else was possbile. Designers wanted something new and creative. I figured out how to make new styles of sites, and now our range of products is greater"

# Difficult/Stressful situations

# 5. "Student wasn't interested in learning English. I related my own successfully learning techniques and I found out what kinds of things they were interested in and found English language versions so they could have fun while learning"

# 6. "Designer was late getting us a design, and my Boss had a meeting the next day with a client. I stayed up late and got it done in time, keeping in mind that having to do this is a rare occurance"

# Strengths/Weaknesses

# 7. "Strength is extreme attention to detail, which is a huge asset to dev companies and can be a hard thing to teach"

# 8. "Weakness is design. I studied basic design concepts, bought a tablet, learned how to use photoshop. Having some level of skill is much better than having none. I also am upfront about my weaknesses so they can be known and accounted for by the team."
