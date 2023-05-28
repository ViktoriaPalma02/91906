import validators 

testbad = "This domain sucks"
testgood = "This domain is good"
#Function to evaluate URL
def ev_url(url_input):
    print("This is a url:", url_input)
    try:
        domain_info = validators.domain(url_input)
        return True
    except:
        return False
    
    while domain_info is True:
        print("PLEASE WORK")
  #  if validators.domain(url_input):
   #     print("This is a good domain")
    #    #print("this is good domain")
    #else:
     #   print("this is a bad domain")
      #  return testbad

        
    #True

#Evaluate if user inputs URL
print("Hi please input a URL")
user_input = input()
print(user_input)

validate_url = validators.url(user_input)
if validate_url:    
    print("Url")
    ev_url(user_input)
else:
    print("not a url")



