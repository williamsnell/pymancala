import time
class game:
    def __init__(self, player):
        self.board = [0, [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 0]
        #       [N, [A, B, C, D, E, F, G, H, I, J, K, L], M]
        self.initplayer = player
        self.player = player
        self.moveorder = []
        self.searchedpos = []
        self.movestring = ""
        #self.display()
    def playerswap(self):
        if self.player == 1:
            self.player = 2
        elif self.player == 2:
            self.player = 1
    def display(self, board = True):
        """
        [N] L K J I H G []
        [ ] A B C D E F [M]
        """
        if board == True:
            board = self.board
            ptm = self.player - self.initplayer
            if ptm != 0:
                p = 'Your Opponent'
            elif ptm == 0:
                p = 'You'
        else:
            player = board[0]
            if player == 2:
                p = 'Your Opponent'
            if player == 1:
                p = 'You'
            board = board[1]
            
        toprow = str(board[1][::-1][0:6])[1:-1]
        botrow = str(board[1][0:6])[1:-1]
        

                
        print("Opponent Score \t= \t" + str(board[0]))
        print("Your Score \t= \t" + str(board[2]) + '\n')
        print("\tL  K  J  I  H  G \t")
        print("[" + str(board[0]) + "]\t" + toprow + "\t[ ]")
        print("[ ]\t" + botrow + "\t[" + str(board[2]) + "]")
        print("\tA  B  C  D  E  F")
        print('\n' + 'Player to move: ' + p)
        print('-------------------------------------------------------------')      
    def check_legal(self, letter):
        letters_up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
        letters_lo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        
        if letter in letters_up:
            idx = letters_up.index(letter)
        elif letter in letters_lo:
            idx = letters_lo.index(letter)
        else:
            print("Input not recognised")
            return None
        
        if self.player == 1 and idx in [6, 7, 8, 9, 10, 11]:
            print("Wrong Player")
            return None
        if self.player == 2 and idx in [0, 1, 2, 3, 4, 5]:
            print("Wrong Player")
            return None
        
        return [letter, idx]
    def moveadd(self, letter):
        self.movestring += letter
        
    def get_ms(self):
        print(self.movestring)
                
    def _mmove(self, letter):
        letters_up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
        letters_lo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        
        if letter in letters_up:
            idx = letters_up.index(letter)
        elif letter in letters_lo:
            idx = letters_lo.index(letter)
            
        pits = self.board[1]
        
        if self.player == 1:
            combiboard = pits[0:6] + [self.board[2]] + pits[6:12]
         
        if self.player == 2:
            combiboard = pits[6:12] + [self.board[0]] + pits[0:6]
            idx -= 6
            
        count = combiboard[idx]
        lastpit = (idx + count)%13
        combiboard[idx] = 0
        
        i = 0
        j = 0
        
        while j < (count):
            combiboard[idx + i + 1] += 1
            
            i+=1
            if idx + i + 1 == 13:
                i = -1*idx - 1
            j+=1
        
        if lastpit in range(6):
            if combiboard[lastpit] == 1:
                combiboard[6] += 1
                combiboard[6] += combiboard[12-lastpit]
                combiboard[lastpit] = 0
                combiboard[12-lastpit] = 0
                
        if self.player == 1:
            self.board = [self.board[0], combiboard[0:6] + combiboard[7:13], combiboard[6]]
        
        if self.player == 2:
            self.board = [combiboard[6], combiboard[7:13] + combiboard[0:6], self.board[2]]
            
        if lastpit != 6:
            self.playerswap()
            
        self.moveadd(letter)
        
    def __move(self, let, state):
        player = state[0]
        board = state[1]
        
        pits = board[1]
        
        letters_up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
        letters_lo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        
        if let in letters_up:
            idx = letters_up.index(let)
        elif let in letters_lo:
            idx = letters_lo.index(let)
        
        if player == 1:
            combiboard = pits[0:6] + [board[2]] + pits[6:12]
         
        if player == 2:
            combiboard = pits[6:12] + [board[0]] + pits[0:6]
            idx -= 6
            
        count = combiboard[idx]
        lastpit = (idx + count)%13
        combiboard[idx] = 0
        
        i = 0
        j = 0
        
        while j < (count):
            combiboard[idx + i + 1] += 1
            
            i+=1
            if idx + i + 1 == 13:
                i = -1*idx - 1
            j+=1
        
        if lastpit in range(6):
            if combiboard[lastpit] == 1:
                combiboard[6] += 1
                combiboard[6] += combiboard[12-lastpit]
                combiboard[lastpit] = 0
                combiboard[12-lastpit] = 0
            
        if player == 1:
            board = [board[0], combiboard[0:6] + combiboard[7:13], combiboard[6]]
        
        if player == 2:
            board = [combiboard[6], combiboard[7:13] + combiboard[0:6], board[2]]
            
        if lastpit != 6:
            if player == 1:
                player = 2
            elif player == 2:
                player = 1
    
        return [player, board]
        
    def move(self, let, disp = True):
        if self.check_legal(let) == None:
            return None
        letter, idx = self.check_legal(let)
                    
        pits = self.board[1]
        
        if self.player == 1:
            combiboard = pits[0:6] + [self.board[2]] + pits[6:12]
         
        if self.player == 2:
            combiboard = pits[6:12] + [self.board[0]] + pits[0:6]
            idx -= 6
            
        count = combiboard[idx]
        lastpit = (idx + count)%13
        combiboard[idx] = 0
        
        i = 0
        j = 0
        
        while j < (count):
            combiboard[idx + i + 1] += 1
            
            i+=1
            if idx + i + 1 == 13:
                i = -1*idx - 1
            j+=1
        
        if lastpit in range(6):
            if combiboard[lastpit] == 1:
                combiboard[6] += 1
                combiboard[6] += combiboard[12-lastpit]
                combiboard[lastpit] = 0
                combiboard[12-lastpit] = 0
                
        if self.player == 1:
            self.board = [self.board[0], combiboard[0:6] + combiboard[7:13], combiboard[6]]
        
        if self.player == 2:
            self.board = [combiboard[6], combiboard[7:13] + combiboard[0:6], self.board[2]]
            
        if lastpit != 6:
            self.playerswap()
            
        if disp == True:
            self.display()
            
        self.moveadd(letter)
        
    def calc_score(self, string):
        pass
        # take string
        movelist = [x for x in string]
        # create first move
        player, board = self.__move(movelist[0], [1, [0, [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 0]])
        movelist.pop(0)
                
        # iterate
        while len(movelist) > 0:
            player, board = self.__move(movelist[0], [player, board])
            movelist.pop(0)
            
        # return score
        return [board[0], board[2]]
        
    def search(self, depth, let = None, a = None, b = None, state = None):
        """
        just focus on generating the moves
        state = player, board

        essentially for ab search you are trying to maximise scores for both 
        players
        
        depending on which player the search is evaluating on, the search will
        try and maximise the score of the player
        
        if a child has less current score, then the search will be stopped
        """
        if state == None:
            p = self.player
            pp = (self.player-1)*6
            p2, pits, p1 = self.board
        else:
            p = state[0]
            pp = (state[0] - 1)* 6
            p2, pits, p1 = state[1]


        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        possmove = letters[0+pp:6+pp]
        
        if depth == 0:
            if p == self.initplayer:
                result = self.__move(let, [p*-1+3, [p2, pits, p1]])[1]
                return [result[0], result[2]]
            
        '''if depth != 0:
            for x in possmove:
                bob = self.search(depth-1, x, a, b, [p*-1+3, [p2, pits, p1]])
                print(x)
                print(bob)'''
        
        '''if p == self.initplayer:
            val = -50
            for x in possmove:
                res = self.search(depth-1, x, a, b, state = [p*-1 + 3, [p2, pits, p1]])
                val = max(val,res[1])
                a = max(a, val)
                
                if a > b:
                    break
            return val
        else:
            val = 50
            for x in possmove:
                res = self.search(depth-1, x, a, b, state = [p*-1 + 3, [p2, pits, p1]])
                print(a, b)
                val = min(val, res[0])
                b = min(b, val)
                if b < a:
                    break

            return val'''
        
    def clear(self):
        self.searchedpos = []
    
if __name__ == "__main__":
       
    mancala = game(1)
    #ancala.move('K')
    #mancala.move('C')
    mancala.move('C')
    mancala.move('F')
    #mancala.move('K')
    mancala.search(1)

    

