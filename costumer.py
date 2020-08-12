class costumer():
    def __init__ (self, costumerid,personid,reservation,roomid,paymentid,roocardaccessid):
      self.costumerid = costumerid
      self.personid = personid
      self.reservation = reservation
      self.roomid = roomid
      self.paymentid = paymentid
      self.roomcardaccessid = roocardaccessid

    def getCostumerid (self):
      return self.costumerid
    
    def getPersonid(self):
        return self.personid

    def getReservation(self):
        return self.reservation

    def getRoomid(self):
        return self.roomid

    def getPaymentid(self):
        return self.paymentid

    def getRoomcardaccessid(self):
        return self.roomcardaccessid