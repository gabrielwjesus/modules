from mitrecve import crawler
from ares import CVESearch

ans = 0 
cve = CVESearch()

while ans != 4:
    print('CVE Module')
    print('1 - Search for CVE (ex: CVE-2007-1894) or Item(ex: wordpress).')
    print('2 - Show last 20 Updated CVE.')
    print('3 - Outputs all available information for the specified CVE.')
    print('4 - Exit\n')
    
    ans = int(input())
    
    if ans == 1:
        itemSearch = input('What kind of CVE are you looking for:\nOr Insert the CVE:\n-> ')
        CVE = crawler.get_main_page(itemSearch)
        testItemSearch = itemSearch.split('-')
        if testItemSearch[0] != 'CVE':
            print(' -*- GETTING ALL CVE FOR ', itemSearch)
        for item in CVE:
            for itemList in item:
                print(itemList)
    
    elif ans == 2:
        last10 = cve.last('20')
        for last in last10:
            print(last)        
        
    elif ans == 3:
        itemSearch = input('Insert the CVE:\n-> ')
        result = cve.id(itemSearch)
        #Outputs all available information for the specified CVE (Common Vulnerability and Exposure)
        for key, value in result.items():
            print(key, ' : ', value)        
        
        ##cve.dbinfo() 
        #Amount of whitelist and blacklist records
        #Some server settings like the database name
        #Some database information like disk usage
        
        ##cve.browse(vendor) 
        #Returns a list of vendors or products of a specific vendor. 
        #This API call can be used in two ways; 
        #With or without the vendor. 
        #When the link is called without a vendor, it will return a list of possible vendors. 
        #When the link is called with a vendor, it enumerates the products for said vendor.
        
        ##cve.capec(idCVE) 
        #Common Attack Pattern Enumeration and Classification
        
        ##cve.cwe() 
        #Common Weakness Enumeration

    elif ans == 4:
        break
