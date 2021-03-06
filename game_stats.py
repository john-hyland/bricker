import sys
import os.path


class GameStats:
    """ Stores score and other game statistics. """

    def __init__(self):
        """ Class constructor. """
        self.high_scores = self.load_high_scores()
        self.current_score = 0
        self.lines = 0
        self.level = 1

    def load_high_scores(self):
        """ Load high scores from file. """
        scores = []
        if os.path.isfile("high_scores.txt"):
            with open("high_scores.txt") as f:
                lines = f.readlines()
            lines = [x.strip() for x in lines]
            for line in lines:
                split = line.split("\t")
                if len(split) == 2:
                    initials = split[0]
                    score = int(split[1])
                    scores.append(HighScore(initials, score))
            scores = self.sort_scores(scores)
        return scores

    def save_high_scores(self, scores):
        """ Save high scores to file. """
        scores = self.sort_scores(scores)
        with open("high_scores.txt", "w") as text_file:
            for x in scores:
                text_file.write(x.initials + "\t" + str(x.score) + "\n")

    def is_high_score(self):
        """ Returns true if score can be placed on board. """
        if len(self.high_scores) < 10:
            return True
        lowest = sys.maxsize
        for score in self.high_scores:
            if score.score < lowest:
                lowest = score.score
        return self.current_score > lowest

    def add_high_score(self, initials):
        """ Adds new score, sorts and limits to top 10, saves to disk. """
        self.high_scores.append(HighScore(initials, self.current_score))
        self.high_scores = self.sort_scores(self.high_scores)
        self.save_high_scores(self.high_scores)

    @staticmethod
    def sort_scores(scores):
        """ Sorts scores, limits to top 10. """
        scores.sort(key=lambda x: x.score, reverse=True)
        while len(scores) > 10:
            del(scores[-1])
        return scores

    def add_lines(self, count):
        """ Increments cleared lines, sets level. """
        self.lines += count
        self.level = (self.lines // 20) + 1


class HighScore:
    """ Stores a single high score. """

    def __init__(self, initials, score):
        self.initials = initials
        self.score = score


