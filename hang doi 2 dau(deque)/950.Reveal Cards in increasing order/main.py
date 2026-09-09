from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        draw = deque()
        deck.sort(reverse=True) 
        for card in deck:
            if draw:
                draw.appendleft(draw.pop())
            draw.appendleft(card)
            
        
        return list(draw)            
            
            