import random as rd
class Password:
    test_size = 8 #basic password length 
    def __init__(self,size=None,luds=None):
        self.test_size = 9 if size == None else size
        self.tf = [True,True,True,True]
        if luds!=None:
            self.tf = luds
                    
                

    '''def domain_without_sampling(self):
        (l,u,d,s) = (True,True,True,True)
        #domain =##[#]
        domain.append(list(range(32,48))+list(range(58,65))+list(range(91,96))) if s else None
        domain.append(range(48,58)) if d else None
        domain.append(range(65,91)) if u else None
        domain.append(range(97,123)) if l else None
        for i in range(self.test_size):
            a = rd.randint(32,126)
            self.password = self.password + chr(a)
        return a ''' 
    def domain(self):
        Lowercase = 'abcdefghijklmnopqrstuvwxyz'
        Uppercase = Lowercase.upper()
        Numbers = '0123456789'
        Special_chr = '#$%&()*+,-./:;@\\'

        domain = ""
        
        if self.tf[0]: domain+=Lowercase
        if self.tf[1]: domain+=Uppercase
        if self.tf[2]: domain+=Numbers
        if self.tf[3]: domain+=Special_chr
        return domain

    def give_password(self):
        characters = self.domain()
        password = ""
        for i in range(self.test_size):
            password+= password.join(rd.sample(characters,1))
        return password