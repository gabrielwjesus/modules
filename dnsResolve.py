import dns.resolver

address = input("Insert the Address to get DNS Resolver: ")

resultA = dns.resolver.resolve(address, 'A')
for ipval in resultA:
    print(ipval.to_text()+"\n")