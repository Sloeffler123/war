import random
cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'jack','jack','jack','jack','queen','queen','queen','queen','king','king','king','king','ace','ace','ace','ace',]
face_card_matchup = {'ace': 14, 'king': 13, 'queen': 12, 'jack': 11, 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2}
class Player:
    def __init__(self,player):
        self.player = player
        self.deck = []
        self.random_card_selector()
    def random_card_selector(self):
        for i in range(26):
            rand_card = random.choice(cards)
            cards.remove(rand_card)
            self.deck.append(rand_card)
    def check_face(self,card):
        return face_card_matchup.get(card)
            
player_1 = Player('first')
player_2 = Player('second')

def match_up(player1,player2):
        card_1 = player1.deck[0]
        card_2 = player2.deck[0]
        print(f'Player 1: {card_1} vs. Player 2: {card_2}')
        card_1 = player1.check_face(card_1)
        card_2 = player2.check_face(card_2)
        if card_1 > card_2:
            print(f'Player 1 wins this round')  
            card_1 = [key for key,val in face_card_matchup.items() if val == card_1]
            card_2 = [key for key,val in face_card_matchup.items() if val == card_2]
            player1.deck.append(card_2[0])
            player1.deck.remove(card_1[0])
            player1.deck.append(card_1[0])
            player2.deck.remove(card_2[0])
        else:
            print(f'Player 2 wins this round')  
            card_1 = [key for key,val in face_card_matchup.items() if val == card_1]
            card_2 = [key for key,val in face_card_matchup.items() if val == card_2]
            player2.deck.append(card_1[0])
            player2.deck.remove(card_2[0])
            player2.deck.append(card_2[0])
            player1.deck.remove(card_1[0])   
match_up(player_1,player_2)