class Payment:
    total_fees = 0
    crd = 0
    debt = 0
    paid_std = []

    def __init__(self, student, fees):
        if fees < 0.5*self.total_fees:
            self.fees = 0
        else:
            self.fees = fees
            self.set_credit(fees)
            self.set_debit(fees)
            self.paid_std.append(student)
        if fees >= 0.5*self.total_fees:
            self.set_credit(fees)    
        else:
            self.fees = fees
            self.set_debit(fees)

    
    def set_credit(self, fees):
        if fees > self.total_fees:
            self.crd = fees - self.total_fees

    def set_debit(self, fees):
        if fees < self.total_fees:
            self.debt = self.total_fees - fees
   
    @classmethod
    def set_total_fees(cls, tuition, lib_fee, func_fee, med_fee):
        cls.total_fees = tuition + lib_fee + func_fee + med_fee
    
    @classmethod
    def get_paid_std(cls):
        return cls.paid_std
    
    @classmethod
    def get_total_fees(cls):
        return cls.total_fees
    
    def __str__(self):
        return f'Fees: {self.fees}\nCredit: {self.crd}\nDebit: {self.debt}'
   

        

