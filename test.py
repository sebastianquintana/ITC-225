import unittest
from costumer import costumer
from person import person


class testPerson(unittest,TestCase):
    def setUp(self):
        self.p=person("sebastian","142 sw 202 normandy park, wa 98166","sebastianquintan@gmail.com",
        44)

    def test_name(self):
        self.assertEqual(self.p.getName(),"sebastian")
    
    def test_adress(self):
        self.assertEqual(self.p.getAdress(),"142 sw 202 normandy park, wa 98166")

    def test_email(self):
        self.assertEqual(self.p.getEmail(),"sebastianquintan@gmail.com")

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.c=costumer(123,23,1,33,2,5)

    def test_Costumerid(self):
        self.assertEqual(self.c.getCostumerid(),123)    

    def test_personid(self):
        self.assertEqual(self.c.getPersonid(),23)
    
    def test_Reservation(self):
        self.assertEqual(self.c.getReservation,1)

    def test_Roomid(self):
        self.assertEqual(self.c.getRoomid(),33)
    
    def test_Paymentid(self):
        self.assertEqual(self.c.getPaymentid(),2)
    
    def test_Roomcardaccessid(self):
        self.assertEqual(self.c.getRoomcardaccessid(),5)


