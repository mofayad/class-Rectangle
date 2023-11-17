class Rectangle :
    def __init__(self, longueur,  largeur) :
        self.longueur = longueur
        self.largeur = largeur
    
    def aire(self) :
        return self.longueur * self.largeur
    
    def perimetre(self) :
        return (self.longueur + self.largeur) * 2
    
    def isCarre(self) :
        if self.longueur == self.largeur :
            return True
        else :
            return False
        
    def AfficherRectangle(self) :
        print('La longueur est: ',self.longueur)
        print('La largeur est :',self.largeur)
        print('Aire est: ',self.aire())
        print('Périmètre est: ',self.perimetre())
        if self.isCarre() :
            print("Il s'agit d'un carré")
        else :
            print("Il ne s'agit pas d'un carré")
