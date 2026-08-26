import datetime
class Flashcard(object):
    _last_assigned_update = datetime.datetime.min
    
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer
        self.last_update=self._get_monotonic_update()
        self.correct=0
        self.review=0
    
    @classmethod
    def _get_monotonic_update(cls):
        now = datetime.datetime.now()
        if now <= cls._last_assigned_update:
            now = cls._last_assigned_update + datetime.timedelta(microseconds=1)
        cls._last_assigned_update = now
        return now

    def mark_correct(self):
        self.last_update = self._get_monotonic_update()
        self.correct+=1
        self.review+=1

    def mark_incorrect(self):
        self.last_update = self._get_monotonic_update()
        self.review+=1

    def get_success_rate(self):
        if self.review == 0:
            return 0
        return self.correct/self.review

    def __lt__(self, other):
        return self.last_update<other.last_update
        
    def __gt__(self, other):
        return self.last_update > other.last_update


    def __str__(self):
        return "Prompt: " +self.prompt+"\nAnswer: "+self.answer
    
    
""" Test 1"""
import time
def test_Flashcard_Class():
    print("Testing Flashcard class...", end="")
    card1 = Flashcard("Turing year of birth?", "1912")
    time.sleep(0.5) # ensures there's a clear distinction between when the cards are created
    card2 = Flashcard("Einstein year of birth?", "1879")
    time.sleep(0.5)
    card3 = Flashcard("Newton year of birth?", "1643")

    assert(card1.prompt == "Turing year of birth?")
    assert(card1.answer == "1912")
    assert(card2.prompt == "Einstein year of birth?")
    assert(card2.answer == "1879")
    assert(card3.prompt == "Newton year of birth?")
    assert(card3.answer == "1643")
    
    # we compare cards based on the date it was last updated
    # the date updates when the card is created and when it is marked as correct or incorrect
    # see problem write-up for explanation of how to use the datetime module to do this
    assert(card1 < card2) # hint: implement the __lt__ method!
    assert(card2 < card3)
    assert(card1 < card3)

    card1.mark_correct()
    assert(card1 > card2)
    assert(card1 > card3)
    
    # success rate = ratio of number of times card is marked correct vs. number of times it has been reviewed
    # a card is reviewed when it is marked correct or incorrect
    assert(card1.get_success_rate() == 1) 

    card3.mark_correct()
    assert(card3 > card1)
    assert(card3 > card2)

    card1.mark_incorrect()
    assert(card1 > card2)
    assert(card1 > card3)
    # card1 has now been reviewed twice, once correctly, once incorrectly
    assert(card1.get_success_rate() == 0.5)

    card2.mark_incorrect()
    assert(card2.get_success_rate() == 0)

    # the string representation of the card should contain the prompt and answer
    assert(str(card1) == "Prompt: Turing year of birth?\nAnswer: 1912")
    assert(str(card2) == "Prompt: Einstein year of birth?\nAnswer: 1879")
    assert(str(card3) == "Prompt: Newton year of birth?\nAnswer: 1643")
    print("...done!")

if __name__ == '__main__':
    test_Flashcard_Class()