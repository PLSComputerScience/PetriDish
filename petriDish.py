import random


#Color genome will determine the output of a birthed bug. 
'''
        Red     Green   Blue    
Red     Red     Yellow  purple

Green   Yellow  Green   Turqoise

Blue    Purple  Turgoise Blue

'''
#rainbow Defect will cause the bug to be multicolor, regardles of genes, which will increase chance of attracting mate when matting
#Albino defect will cause no pigment, decreasing chance of mate
#Bug will be neutral will any colors that share an allel or primary color. 

#Metabolic rate determines the food per cycle a bug must have to mate - x, and food per cycle to live Y (x,y) 
#overActive will cause the food to live increase, but food to mate remain the same
#performance will increase the food needed to mate

class bug():

    def __init__(self, name=None) -> None:
        self.name = name
        self.colorGene = {'red': None, 'green': None, 'blue': None, 'defect': {'rainbow': False, 'albino': False}}
        self.color = None
        self.colorDom = [None, None]
        self.attraction = []
        self.metabolism = {'metabolicRate': None, 'defect':{'overActive': False, 'performance': False}}
        self.aggression = None 
        self.speed = None
        self.hasMated = False
        self.stomache = 0

    def generateBug(self):
        def genColorDom(Color):
            match Color:
                case 'red':
                    dominance = (random.choice(['R', 'r']), random.choice(['R', 'r']))
                    self.colorGene['red'] = True
                case 'green':
                    dominance = (random.choice(['G', 'g']), random.choice(['G', 'g']))
                    self.colorGene['green'] = True
                case 'blue':
                    dominance = (random.choice(['B', 'b']), random.choice(['B', 'b']))
                    self.colorGene['blue'] = True
            return dominance
            
        self.color = random.choice(['red', 'green', 'blue'])
        self.colorDom= genColorDom(self.color)
        self.attraction = [self.color]
        self.metabolism['metabolicRate'] = (random.randrange(5) + 1, random.randrange(5) + 1)
        self.aggression = random.randrange(9) + 1
        self.speed = random.randrange(9) + 1
        return self

    def printBug(self):
        print('This bugs name is {} is {} with {} genes\nThis bus has an attraction to {} with a mate metabolism of {}\nThis bug needs {} food to live, with an aggression of {} and speed of {}'.format(self.name, self.color, self.colorDom, self.attraction, self.metabolism['metabolicRate'][0], self.metabolism['metabolicRate'][1], self.aggression, self.speed))

    def mateBug(self, mate, kidname=None): 
        self.hasMated = True
        mate.hasMated = True
        offspring = bug(kidname)


        def geneMix(geneOne, geneTwo):
            #Merging ColorDom Alpha Colors,  
            if geneOne.colorDom[0].isupper():
                if geneTwo.colorDom[0].isupper():
                    offspring.colorDom[0] = random.choice([geneOne.colorDom[0], geneTwo.colorDom[0]])
                else:
                    offspring.colorDom[0] = geneOne.colorDom[0]
            else:
                if geneTwo.colorDom[0].isupper():
                    offspring.colorDom[0] = geneTwo.colorDom[0]
                else:
                    offspring.colorDom[0] = random.choice([geneOne.colorDom[0], geneTwo.colorDom[0]])
            #Merging ColorDom Beta Colors,
            if geneOne.colorDom[1].isupper():
                if geneTwo.colorDom[1].isupper():
                    offspring.colorDom[1] = random.choice([geneOne.colorDom[1], geneTwo.colorDom[1]])
                else:
                    offspring.colorDom[1] = geneOne.colorDom[1]
            else:
                if geneTwo.colorDom[1].isupper():
                    offspring.colorDom[1] = geneTwo.colorDom[1]
                else:
                    offspring.colorDom[1] = random.choice([geneOne.colorDom[1], geneTwo.colorDom[1]])
            #Assigning the color
            #checking if defect in birth
            if random.randrange(100) == 100:
                match random.choice(['rainbow', 'albino']):
                    case 'rainbow':
                        offspring.colorGene['defect']['rainbow'] = True
                        offspring.colorGene['red'], offspring.colorGene['green'], offspring['blue'] = True
                        offspring.colorDom = (random.choice(['R','G','B']), random.choice(['R','G','B']))
                    case 'albino':
                        offspring.colorGene['defect']['albino'] = True
                        offspring.colorGene['red'], offspring.colorGene['green'], offspring['blue'] = False
                        offspring.colorDom = (None, None)
            #if not defect, assign color
            else:
                match (offspring.colorDom[0].lower(), offspring.colorDom[1].lower()):
                    case ('r','r'):
                        offspring.color = 'red'
                        offspring.colorGene['red'] = True
                    case ('r','g') | ('g', 'r'):
                        offspring.color = 'yellow'
                        offspring.colorGene['red'] = True
                        offspring.colorGene['green'] = True
                    case ('r', 'b') | ('b', 'r'):
                        offspring.color = 'purple'
                        offspring.colorGene['red'] = True
                        offspring.colorGene['blue'] = True
                    case ('g', 'g'):
                        offspring.color = 'green'
                        offspring.colorGene['green'] = True
                    case ('g', 'b') | ('b', 'g'):
                        offspring.color = 'turqoise'
                        offspring.colorGene['green'] = True
                        offspring.colorGene['blue'] = True
                    case ('b', 'b'):
                        offspring.color = 'blue'
                        offspring.colorGene['blue'] = True
            

        geneMix(self, mate)
        attractionMod = random.randrange(4) + 1
        attractionList = ['red', 'green', 'blue', 'purple', 'turqoise', 'yellow']
        for i in range(attractionMod):
            attractee = random.choice(attractionList)
            offspring.attraction.append(attractee)
            attractionList.remove(attractee)
        offspring.aggression = round((self.aggression + mate.aggression)/2)
        if self.metabolism['defect']['overActive'] == True | mate.metabolism['defect']['overActive'] == True | random.randrange(100) == 100:
            offspring.metabolism['defect']['overActive'] = True
            offspring.metabolism['metabolicRate'] = (round((self.metabolism['metabolicRate'][0] + mate.metabolism['metabolicRate'][0])/2), round((self.metabolism['metabolicRate'][1] + mate.metabolism['metabolicRate'][1])/2 + 2))
        elif self.metabolism['defect']['performance'] == True | mate.metabolism['defect']['performance'] == True | random.randrange(100) == 100:
            offspring.metabolism['defect']['performance'] = True
            offspring.metabolism['metabolicRate'] = (round((self.metabolism['metabolicRate'][0] + mate.metabolism['metabolicRate'][0])/2 + 2), round((self.metabolism['metabolicRate'][1] + mate.metabolism['metabolicRate'][1])/2))
        else:
            offspring.metabolism['metabolicRate'] = (round((self.metabolism['metabolicRate'][0] + mate.metabolism['metabolicRate'][0])/2 ), round((self.metabolism['metabolicRate'][1] + mate.metabolism['metabolicRate'][1])/2))
        offspring.speed = random.choice([round((self.speed + mate.speed) / 2 + random.randrange(2)), round((self.speed + mate.speed) / 2 - random.randrange(2))])
        return offspring
       
        
        
