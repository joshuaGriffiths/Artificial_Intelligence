# Joshua Griffiths in colaberation with Dylan Gema
# PS 2
import math


class Player:
    RED = "Red"
    BLUE = "Blue"


class GameMode:
    ONEPLAYER = "One Player"


class aI:
    allNodes = []
    nodeOverlap = {}
    opponentsEdges = []
    myEdges = []

    def __init__(self, nodes):

        self.allNodes = nodes
        for node in self.allNodes:
            self.nodeOverlap[node] = 0

    def buildTree(self, remaining):
        weighted_edges = []
        for edge in remaining:
            (node1, node2) = edge.getEdge()
            weight = self.nodeOverlap[node1] + self.nodeOverlap[node2]
            weighted_edges.append((edge, weight))

        return weighted_edges

    def overlap(self):
        for node in self.allNodes:
            self.nodeOverlap[node] = 0
            for edge in self.myEdges:
                (node1, node2) = edge.getEdge()
                self.nodeOverlap[node1] += 1
                self.nodeOverlap[node2] += 1

    def findBestEdge(self, remaining):

        self.overlap()
        edge_weight_tree = self.buildTree(remaining)
        best_edge_weight = 100
        best_edge = 0
        for node in edge_weight_tree:
            (edge, weight) = node
            # print("Edge: " + str(edge.getEdge()) + " Weight: " + str(weight))
            # print(best_edge_weight)
            if weight < best_edge_weight:
                best_edge_weight = weight
                best_edge = edge
        return best_edge

    def chooseBestEdge(self, myedges, oppedges, remaining):
        self.myEdges = myedges
        self.opponentsEdges = oppedges
        return self.findBestEdge(remaining)


class Edge:
    def __init__(self, v1, v2, p):
        self.edge = (v1, v2)
        self.player = p

    def getEdge(self):
        return self.edge

    def getPlayer(self):
        return self.player


class game:
    playerOne = 0
    playerTwo = 0
    edgeList = []
    redEdges = []
    blueEdges = []
    maxEdges = 0
    nodeCount = 0
    allNodes = []

    def __init__(self):
        self.gameStart()
        self.playGame()

    def setGameMode(self):
        self.game_mode = GameMode.ONEPLAYER

    def setScore(self):
        node_count_response = 8
        self.nodeCount = node_count_response
        self.maxEdges = choose(self.nodeCount, 2)

    def generateNodes(self):
        for count in range(self.nodeCount):
            self.allNodes.append(chr(ord('A') + count))

    def setPlayerColor(self):
        player_choice = raw_input("Red or Blue ")

        if player_choice == "r":
            self.playerOne = Player.RED
            self.playerTwo = Player.BLUE
            self.current_player = self.playerOne


        elif player_choice == "b" or "B" or "blue" or "Blue":
            self.playerOne = Player.BLUE
            self.playerTwo = Player.RED
            self.current_player = self.playerTwo

        else:
            print("Invalid choice")
            self.setPlayerColor()

    def gameStart(self):
        # print("Welcome to game")
        self.setGameMode()
        self.setScore()
        self.generateNodes()
        self.setPlayerColor()

    def playGame(self):

        while not self.gamesOver() and len(self.edgeList) < self.maxEdges:
            self.switchPlayer()
            self.chooseEdge()
            print("")

        if len(self.edgeList) == self.maxEdges:
            print("This game is a draw!")

        else:
            print(self.current_player + ", you lose!")
            self.switchPlayer()
            print(self.current_player + ", you win!")

    def gamesOver(self):
        playerList = []
        if self.current_player == Player.RED:
            playerList = self.redEdges
        else:
            playerList = self.blueEdges

        if len(playerList) < 3:
            return False

        for i in range(len(playerList) - 2):
            for j in range(i + 1, len(playerList) - 1):
                for k in range(j + 1, len(playerList)):
                    if (self.isBad([playerList[i], playerList[j], playerList[k]])):
                        return True

        return False

    def isBad(self, edgeList):
        # If there are only 3 unique characters, a triangle must exist
        unique_chars = []
        for edge in edgeList:
            for character in edge.getEdge():
                if character not in unique_chars:
                    unique_chars.append(character)
                return len(unique_chars) == 3

    def isValidEdge(self, v1, v2):
        def isEdgeInEdgeList(v1, v2, edgeList):
            if edgeList == []:
                return False
            for edge in edgeList:
                if edge.getEdge() == (v1, v2):
                    return True
            return False

        if v1 == v2:
            return False
        if v1 not in self.allNodes or v2 not in self.allNodes:
            return False
        return not isEdgeInEdgeList(v1, v2, self.edgeList)

    def getRemainingEdges(self):
        remaining_edges = []
        for i in range(self.nodeCount - 1):
            for j in range(i + 1, self.nodeCount):
                if self.isValidEdge(self.allNodes[i], self.allNodes[j]):
                    remaining_edges.append(Edge(self.allNodes[i], self.allNodes[j], []))
        return remaining_edges

    def printNodes(self):
        node_str = "Possible Start Nodes: "
        for node in self.allNodes:
            node_str += node + ", "
        print(node_str)

    def printEdges(self):
        red_edge_str = "Red Edges are:"
        blue_edge_str = "Blue Edges are: "
        for edge in self.edgeList:
            if edge.getPlayer() == "Red":
                red_edge_str += str(edge.getEdge()) + ","
            else:
                blue_edge_str += str(edge.getEdge()) + ","
        print(red_edge_str)
        print(blue_edge_str)

    def addEdge(self, edge_choice_lst):
        edge_to_add = Edge(edge_choice_lst[0], edge_choice_lst[1], self.current_player)
        self.edgeList.append(edge_to_add)
        if self.current_player == Player.RED:
            self.redEdges.append(edge_to_add)
        else:
            self.blueEdges.append(edge_to_add)

    def chooseEdge(self):
        if self.game_mode == GameMode.ONEPLAYER and self.current_player == self.playerTwo:
            self.chooseEdgeAI()
        else:
            self.chooseEdgePlayer()

    def chooseEdgePlayer(self):
        print(self.current_player + " your turn:")
        self.printNodes()
        self.printEdges()
        edge_choice = raw_input("Enter your edge: ")
        edge_choice_lst = edge_choice.split(",")
        edge_choice_lst = sorted(edge_choice_lst)
        if len(edge_choice_lst) != 2:
            print("Not a valid edge choice!\n")
            self.chooseEdge()
        elif not self.isValidEdge(edge_choice_lst[0], edge_choice_lst[1]):
            print("Not a valid edge choice!\n")
            self.chooseEdge()
        else:
            self.addEdge(edge_choice_lst)

    def chooseEdgeAI(self):
        # Find all remaining options
        ai_edges = []
        usr_edges = []
        if self.current_player == Player.RED:
            ai_edges = self.redEdges
            usr_edges = self.blueEdges
        else:
            ai_edges = self.blueEdges
            usr_edges = self.redEdges
        ai = aI(self.allNodes)
        edge_choice = ai.chooseBestEdge(ai_edges, usr_edges, self.getRemainingEdges())
        self.addEdge([edge_choice.getEdge()[0], edge_choice.getEdge()[1]])

    def switchPlayer(self):
        if self.current_player == self.playerOne:
            self.current_player = self.playerTwo
        else:
            self.current_player = self.playerOne


def choose(n, r):
    if r >= n:
        return 0
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def main():
    game()

main()
