#This is where you write your funtion. Functions are just reusable segments of code that can be called more than once without having to rewrite the code again
def computePay(h,r):                        #Variables h and r are what are assigned inside the variable. These values will be assigned when the function is called later in the code.
    if h > 40.0:                            #Does the math for computing all the different things you need.
        ovrTmHrs = h -40.0
        ovrTmRate = r *1.5
        normPay = 40 * r
        ovrTmPay = ovrTmHrs * ovrTmRate
        return ovrTmPay + normPay           # The return value will be the result of the functions code. This will get passed back to the grossPay varible when it gets called later in the code.
    else:
        return h * r                        # The return value will be the result of the functions code. This will get passed back to the grossPay varible when it gets called later in the code.

# Runtime start here

# This is where the program will get user input and store it as a vairable.
hrs = input("Enter Hours: ")
hrs = float(hrs)
rate = input("Enter Pay Rate: ")
rate = float(rate)

grossPay = computePay(hrs, rate)  # Calls the stored function from earlier in the code. This is where the information that gets put into the funtion gets placed sent into the function.  Also the grossPay variable is assigned the output of the function

print("Pay: ", grossPay)   #Shows the results of the function


