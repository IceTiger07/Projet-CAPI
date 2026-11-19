
from code import validation_vote


def test_CA_01_1_strict_revote():
    #arrange
    liste_vote = [2,5,5]
    regle = "strict"
    tour = 1
    #act
    result = validation_vote(liste_vote,regle,tour)    
    #assert
    assert result == -1

# ce cas compte pour vérifier que si on a l'unanimité au tour 1, on la bonne valeur de retour
def test_CA_01_1_strict_validé():
    #arrange
    liste_vote = [5,5,5]
    regle = "strict"
    tour = 1
    #act
    result = validation_vote(liste_vote,regle,tour)    
    #assert
    assert result == 5

# ce cas compte pour vérifier que si on a pas l'unanimité au tour 2, on prends la moyenne
def test_CA_02_1_moyenne_validé_juste():
    #arrange
    liste_vote = [2,5,8]
    regle = "moyenne"
    tour = 2
    #act
    result = validation_vote(liste_vote,regle,tour)    
    #assert
    assert result == 5

def test_CA_02_1_moyenne_validé_medianne():
    #arrange
    liste_vote = [2,5,13]
    regle = "moyenne"
    tour = 2
    #act
    result = validation_vote(liste_vote,regle,tour)    
    #assert
    assert result == 5

# ce cas compte pour vérifier que meme avecc la règle de la moyenne osi on a pas l'unanimité au tour 1, on doit revoter
def test_CA_03_1_moyenne_tour1():
    #arrange
    liste_vote = [2,5,8]
    regle = "moyenne"
    tour = 1
    #act
    result = validation_vote(liste_vote,regle,tour)    
    #assert
    assert result == -1

def test_CA_03_1_moyenne_unanimité_():
    #arrange
    liste_vote = [5,5,5]
    regle = "moyenne"
    tour = 1
    #act
    result = validation_vote(liste_vote,regle,tour)    
    #assert
    assert result == 5

def test():
    test_CA_01_1_strict_revote()
    test_CA_01_1_strict_validé()
    test_CA_02_1_moyenne_validé_juste()
    test_CA_02_1_moyenne_validé_medianne()
    test_CA_03_1_moyenne_tour1()
    test_CA_03_1_moyenne_unanimité_()

test()
