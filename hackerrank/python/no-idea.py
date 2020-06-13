class Happiness():
    def __init__(self, array):
        self.array = set(array)
        self.happiness = 0
    
    def calculateMyHappiness(self, A, B):
        like = set(A)
        dislike = set(B)

        

        diff_like = self.array.intersection(like)
        like_mood = len(diff_like)

        diff_dislike = self.array.intersection(dislike)
        dislike_mood = len(diff_dislike)

        self.happiness = like_mood - dislike_mood

        return self.happiness


if __name__ == '__main__':
    m, n = input().split()
    array = list(input().split())
    A = list(input().split())
    B = list(input().split())

    happy = Happiness(array)
    total_happiness = happy.calculateMyHappiness(A, B)

    print(total_happiness)
