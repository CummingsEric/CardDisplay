import pygame

class Display:
    def __init__(self, width=4, height=2, card_color='grey'):
        pygame.init()
        self.card_height = 1056
        self.card_width = 691
        self.SCREEN_WIDTH = width*self.card_width+10*width
        self.SCREEN_HEIGHT = height*self.card_height+10*height
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.background_color = (54, 57, 62)

    def GenDisplay(self, card_info, save_location):
        pygame.event.get()
        self.screen.fill(self.background_color)
        for card in card_info:
            self.drawCard(card)
        pygame.image.save(self.screen, save_location)

    def drawCard(self, card):
        x = card[1][0]
        y = card[1][1]
        show_card = card[0][1]
        type_card = card[0][0]
        if(show_card):
            image_path = "./assets/" + type_card + ".png"
        else:
            image_path = "./assets/blue_back.png"
        image = pygame.image.load(image_path)
        self.screen.blit(image, (10*x+5+self.card_width*x, 10*y+5+self.card_height*y))

#dis = Display(4,2)
#cards = [(('1H', False), (0, 0)),(('2H', False), (1, 0)),(('3H', True), (2, 0)),(('4H', False), (3, 0))]
#dis.GenDisplay(cards, 'display.jpg')
