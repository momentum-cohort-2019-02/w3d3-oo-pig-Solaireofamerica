import random


class Players:
    """
    Super class for the CompPlayer and the HumanPlayer. Will pass in the scores from GameLoop. Each sub-class
    will have different functions for how they play. I.E. the comp will only hold if it has 20 points. 
    """
    def __init__(self, r_score, m_score):
        self._r_score = _r_score
        self._m_score = _m_score


class CompPlayer(Players):
    """
    The computer player that rolls the die and keeps rolling until they have 20 and holds.
    Stores the CompPlayer score
    """
    def __init__(self, r_score, m_score):
        super().__init__(r_score, m_score)
        self.cpu_r_score = r_score
        self.cpu_m_score = m_score


class HumanPlayer(Players):
    """
    The human controlled player who can roll the die and choose to hold at any time.
    Stores the Human's score
    """
    def __init__(self, r_score, m_score):
        super().__init__(r_score, m_score)
        self.cpu_r_score = r_score
        self.cpu_m_score = m_score


class GameLoop:
    """
    The main gameplay loop. Die roll method, yadda yadda.
    """
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.max_points = 100
        self.current_player = None


if __name__ == '__main__':
    p1 = super(CompPlayer)
    p2 = super(HumanPlayer)

    game = GameLoop(p1, p2)
    game.play_game()
