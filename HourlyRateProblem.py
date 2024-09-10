hours = int(input("how many hours have you worked"))
rateofpay = int(input("Enter rate of pay per hour"))
totalpay = 0
if hours > 40 and hours < 60:
    totalpay = (rateofpay*40) + ((hours - 40)*(rateofpay*1.5))
elif hours < 40 and hours > 0:
    totalpay = (rateofpay*hours)
else:
     print("invalid number of hours entered")
