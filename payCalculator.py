def computePay(h,r):
    if h > 40.0:
        ovrTmHrs = h -40.0
        ovrTmRate = r *1.5
        normPay = 40 * r
        ovrTmPay = ovrTmHrs * ovrTmRate
        return ovrTmPay + normPay
    else:
        return h * r

hrs = input("Enter Hours: ")
hrs = float(hrs)
rate = input("Enter Pay Rate: ")
rate = float(rate)

grossPay = computePay(hrs, rate)
print("Pay: ", grossPay)


