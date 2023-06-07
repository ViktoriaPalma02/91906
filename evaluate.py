import validators 
import whois

#testbad = "This domain sucks"
#testgood = "This domain is good"
#Function to evaluate URL
def ev_url(url_input):
    print("This is a url:", url_input)

    #try:
    domain = whois.whois(url_input)
    #if domain == True:
     #   print(domain)
    print(domain)
    #    return False
    #except:
     #   return True

real = "this is a registered domain"
notreal = "this is not a registered domain"

def domain(url_input):
    if validators.domain(url_input):
        try:
            return print("this is a registerd domain")
        except:
            return print("This is not a registerd domain")
    else:
        return print("This wont work")


#Evaluate if user inputs URL
print("Hi please input a URL")
user_input = input()
#print(user_input)

validate_url = validators.url(user_input)
if validate_url:    
    print("This is a Url")
    #a = domain(user_input)
    a = ev_url(user_input)
    #print(a)


    #ev_url(user_input)
else:
    print("not a url")
    print("But we try anyways")
    #domain = whois.whois(user_input)
   # print(domain)

#print(ev_url, user_input)
#print("Placeholder")

