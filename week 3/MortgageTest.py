import Mortgage

mortgage1 = Mortgage.Mortgage(13, 25000, 24)
mortgage2 = Mortgage.Mortgage(9, 45000, 36)

print (" Loan 1:\n Loan Amount: {}\n Monthly Payment: {}\n Total Payment: {}".format(mortgage1.amount, mortgage1.monthly(), mortgage1.total()))

print ("\n Loan 2:\n Loan Amount: {}\n Monthly Payment: {}\n Total Payment: {}".format(mortgage2.amount, mortgage2.monthly(), mortgage2.total()))
