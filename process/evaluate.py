import validators 
import whois

#Function to evaluate domain values in url
def ev_url(url_input):
    print("This is a url:", url_input)

    domain = whois.whois(url_input)

    domain_name = list(map(domain.get, ["domain_name"]))
    creation_domain = list(map(domain.get,["creation_date"]))
    update_domain = list(map(domain.get, ["updated_date"]))

    if domain.get("domain_name") is not None:
        domain_registerd = True
    else:
        domain_registerd = False
        creation_domain = 0
        update_domain = 0

    print(domain_name)
    print(creation_domain)
    print(update_domain)
    print(domain_registerd)

#Evaluate if user inputs a URL
print("input a URL")
user_input = input()
validate_url = validators.url(user_input)
if validate_url:    
    print("This is a Url")
    evaluate = ev_url(user_input)
else:
    print("not a url")