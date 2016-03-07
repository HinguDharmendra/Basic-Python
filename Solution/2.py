#amount=float(raw_input())
amount = 100.1234345634
print "real amount", amount
amount_changed=round(amount * 10)/10.0
print "round(amount * 10)/10.0 converts amount to float number i.e", amount_changed
print "output in nearest 5 paisa", round(amount, 5)




#Output:
#real amount 100.123434563
#round(amount * 10)/10.0 converts amount to float number i.e 100.1
#output in nearest 5 paisa 100.12343
