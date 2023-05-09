from random import shuffle
from time import sleep

class Player:

    def __init__(self,name,chips):
        self.name = name
        self.chips = chips
        self.hand = Hand()
    

class Card:

    def __init__(self,color,symbol,weight):
        self.color = color
        self.symbol = symbol 
        self.weight = weight

    def show_cards(self):
        print(self.weight + '\n' + self.color + '\n' + self.symbol + '\n')

    def show_card(self):
        print(self.weight + ' ' + self.color + ' ' + self.symbol + ' ')


class Deck:

    def __init__(self):
        self.cards = []

        #Creating the red cards

        color = 'Rojo'
        symbols = ['Diamantes', 'Corazones']
        weights = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for weight in weights:
            for symbol in symbols:
                self.cards.append(Card(color, symbol, weight))
        
        #Creating the black cards

        color = 'Negro'
        symbols = ['Trevoles', 'Espadas']
        weights = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for weight in weights:
            for symbol in symbols:
                self.cards.append(Card(color, symbol, weight))
        
        #Shuffling the cards

        shuffle(self.cards)

    def show_deck(self):
        for card in self.cards:
            card.show_cards()

    def deal_card(self):
        return self.cards.pop()

class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def show_hand(self):
        for card in self.cards:
            card.show_card()
    
    def total_weight(self):
        total = 0
        for card in self.cards:
            if card.weight == 'A':
                total += 11
            elif card.weight in ('J', 'Q', 'K'):
                total += 10
            else:
                total += int(card.weight)
        return total
    
    def throw_cards(self):
        self.cards = []
      
class Game:

    def __init__(self, player_name, player_chips):
        self.deck = Deck()
        self.player = Player(player_name, player_chips)
        self.dealer_hand = Hand()
    
    def start_game(self):

        while self.player.chips > 0:

            print('Bienvenido a BlackJack {}, tienes {} fichas \n'.format(self.player.name,self.player.chips))

            paso = False
            while paso == False:
                bet = int(input('Ingrese su apuesta: '))
                if bet <= 0:
                    print('Se tiene que apostar algo')
                elif bet > self.player.chips:
                    print('No tienes suficiente dinero')
                else: 
                    paso = True

            d = Deck()

            house = Player('Casa',100000)

            card1 = d.deal_card()
            card2 = d.deal_card()
            card3 = d.deal_card()
            card4 = d.deal_card()

            self.player.hand.add_card(card1)
            self.player.hand.add_card(card2)
            house.hand.add_card(card3)
            house.hand.add_card(card4)

            print(' ------------------------')
            print('| Estas son tus cartas:  |')
            print(' ------------------------')
            self.player.hand.show_hand()
            print('Tienes: {}'.format(self.player.hand.total_weight()))

            if self.player.hand.total_weight == 21:
                    print('BLACK JACK! Has ganado')
                    self.player.chips = self.player.chips + bet * 1.5
                    return

            keep_playing = True
            while keep_playing:

                if self.player.hand.total_weight() > 21:
                    print('Has perdido, la casa gana')
                    self.player.chips -= bet
                    keep_playing = False
                    break

                pregunta = int(input('Quieres otra carta? 1. Si 2. No '))

                if pregunta == 1:
                    cardxd = d.deal_card()
                    self.player.hand.add_card(cardxd)
                    print(' ------------------------')
                    print('| Estas son tus cartas:  |')
                    print(' ------------------------')
                    self.player.hand.show_hand()
                    print('Tienes: {}'.format(self.player.hand.total_weight()))

                elif pregunta == 2:
                    keep_playing = False
                    print(' ------------------------')
                    print('| La casa tiene:        |')
                    print(' ------------------------')
                    house.hand.show_hand()
                    print('La casa tiene: {}'.format(house.hand.total_weight()))
                    sleep(1)
                    while house.hand.total_weight() < self.player.hand.total_weight():
                        carddd = d.deal_card()
                        house.hand.add_card(carddd)
                        house.hand.show_hand()
                        print('La casa tiene: {}'.format(house.hand.total_weight()))

                    if house.hand.total_weight() > 21:
                        print('Has ganado')
                        self.player.chips += bet
                        break

                    if self.player.hand.total_weight() > house.hand.total_weight():
                        print('Has ganado')
                        self.player.chips += bet
                        break
                    elif self.player.hand.total_weight() == house.hand.total_weight():
                        print('Empatamos, pero la casa siempre gana')
                        self.player.chips -= bet
                        break
                    else:
                        print('La casa gana')
                        self.player.chips -= bet
                        break
            self.player.hand.throw_cards()
            house.hand.throw_cards()

        else:
            print('No tienes suficientes fichas') 

player1 = Player('Diego',100)

g = Game(player1.name,player1.chips)
g.start_game()
