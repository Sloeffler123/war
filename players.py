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
    def convert_value(self,card):
        if card <= 10:
            return card
        match card:
            case 11:
                card = 'jack'
                return card
            case 12:
                card = 'queen'
                return card
            case 13:
                card = 'king'
                return card
            case 14:
                card = 'ace'
                return card

player_1 = Player('first')
player_2 = Player('second')

def match_up(player1,player2):
        print(f'Player 1: {player1.deck[0]} vs. Player 2: {player2.deck[0]}')
        card_1 = player1.check_face(player1.deck[0])
        card_2 = player2.check_face(player2.deck[0])
        player1.deck.remove(player1.deck[0])
        player2.deck.remove(player2.deck[0])
        if card_1 > card_2:
            card_1 = player1.convert_value(card_1)
            card_2 = player2.convert_value(card_2)
            print(f'Player 1 wins this round') 
            print(f'Player 1 gained {card_2}')
            player1.deck.append(card_2)
            player1.deck.append(card_1)
        elif card_1 == card_2:
            print('Then its warrrrrrrr')
            card_1 = player1.convert_value(card_1)
            card_2 = player2.convert_value(card_2)
            # real code
            player_1_war_lst = [card_1]
            player_2_war_lst = [card_2]
            on = True
            while on:
                for i in range(4):
                    player_1_war_lst.append(player1.deck[i])
                    player1.deck.remove(player1.deck[i])
                    player_2_war_lst.append(player2.deck[i])
                    player2.deck.remove(player2.deck[i])
                print(f'Player 1:{player_1_war_lst[-1]} vs. Player 2:{player_2_war_lst[-1]}') 
                print(player_1_war_lst)
                print(player_2_war_lst)  
                one = player1.check_face(player_1_war_lst[-1])
                two = player2.check_face(player_2_war_lst[-1])
                if one > two:
                    print('Player 1 wins')
                    print(f'Player 1 gained: {player_2_war_lst}')
                    player1.deck + player_1_war_lst + player_2_war_lst
                    on = False
                elif one == two:
                    print('Another Warrrrrr')
                    pass
                else:
                    print('Player 2 wins')
                    print(f'Player 2 gained: {player_1_war_lst}')
                    player2.deck + player_1_war_lst + player_2_war_lst
                    on = False
        else:
            card_1 = player1.convert_value(card_1)
            card_2 = player2.convert_value(card_2)
            print(f'Player 2 wins this round')  
            print(f'Player 2 gained {card_1}')
            player2.deck.append(card_1)
            player2.deck.append(card_2)   

while len(player_1.deck) > 0 or len(player_2.deck) > 0:
    input('Press space to show cards')
    match_up(player_1,player_2)