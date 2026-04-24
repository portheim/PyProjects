from StrongPasswordChecker import password_check
import pytest


def test_password_check():
    assert password_check('0neF!sh') == False       ## Only 7 Characters == False
    assert password_check('0nehundr3d!') == False   ## No upper case == False
    assert password_check('0NEHUNDR3D!') == False   ## No lower case == False 
    assert password_check('0neHundred') == False    ## No special characters == False
    assert password_check('0neHundred!') == True    ## All conditions met == True
    assert password_check('##########1aB') == True  ## All conditions met == True