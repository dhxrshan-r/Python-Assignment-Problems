import datetime
class Flashcard(object):
    
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer
        self.last_update=datetime.datetime.now()
        self.correct=0
        self.review=0
    
    def mark_correct(self):
        
        self.last_update=datetime.datetime.now()
        self.correct+=1
        self.review+=1

    def mark_incorrect(self):
        
        self.last_update=datetime.datetime.now()
        self.review+=1

    def get_success_rate(self):
        return self.correct/self.review

    def __lt__(self, other):
        return self.last_update<other.last_update
        
    def __gt__(self, other):
        return self.last_update > other.last_update


    def __str__(self):
        return "Prompt: " +self.prompt+"\nAnswer: "+self.answer  
    

class FlashcardDeck:
    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        self.cards=cards

    def get_card_for_review(self):
        first_cards = self.cards.pop(0)
        self.cards.append(first_cards)
        return first_cards

    def __str__(self):
        total_reviewed = 0
        total_correct = 0
        for card in self.cards:
            total_reviewed+=card.review
            total_correct+=card.correct
        if total_reviewed != 0:
            success_rate = total_correct / total_reviewed
        else:
            success_rate=0
        return "There are "+str(len(self.cards))+" cards in the deck. Your success rate is "+str(success_rate)
    

""" Test 2 """  
def test_FlashcardDeck_Class():
    print("Testing FlashcardDeck class...", end="")
    deck = FlashcardDeck()

    card1 = Flashcard("Turing year of birth?", "1912")
    card2 = Flashcard("Einstein year of birth?", "1879")
    card3 = Flashcard("Newton year of birth?", "1643")

    deck.add_cards([card1, card2, card3])
    
    # the string representation of the deck should say how many cards are in the deck and overall success rate
    # overall success rate is calculated as total correct / total reviewed over all cards in the deck
    assert(str(deck) == "There are 3 cards in the deck. Your success rate is 0")

    # should pop out the first card in the deck, return it, and add the card back to the end of the deck
    card = deck.get_card_for_review()
    assert(str(card) == str(card1))
    card.mark_correct()

    card = deck.get_card_for_review()
    assert(str(card) == str(card2))
    card.mark_incorrect()

    assert(str(deck) == "There are 3 cards in the deck. Your success rate is 0.5")
    print("... done!")

if __name__ == '__main__':
    test_FlashcardDeck_Class()