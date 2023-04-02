# The link of the pages consist of 3 parts.
# First part before the first dot is called subdomain
# Last part after the second dot is called top level domain name(TLD)
# Mid part (in betweed the dots) is called domain name.



#www.techtorialacademy.com
#www  ->subdomain name
#techtorialacademy ->domaind name
# com -> tld


# Ask user to enter their website link.
# Assume that subdomain name will be www and tld will be com
# Print the domain name of the user's website link.

# Since we know string given will be starting with www.
# and ending with.com
link = input("Please, enter the link of your page: ")
domain_name = link.removeprefix("www.").removesuffix(".com")
print(f'The domain name of your page is{domain_name}')

































