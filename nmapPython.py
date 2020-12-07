import nmap3,os

nmap = nmap3.Nmap()
nmapT = nmap3.NmapScanTechniques()
nmapH = nmap3.NmapHostDiscovery()

def main():
    ans = 0
    while ans != 3:
        print('Welcome to NMAP Python')
        print('1 - Show Menu\n2 - Insert Python Command Line\n3 - EXIT\n-> ')
        ans = int(input())
        if ans == 1:
            print('Nmap Python Menu')
            showMenu()
            
        elif ans == 2:
            print('Nmap Python Command Line')
            print('press 0 and click Enter to exit')
            command = input(">> ")
            commandLine(command)
        elif ans == 3:
            print('Good bye')
            break
        else:
            print('Invalid key')


def showMenu():
    print('1- Getting OS')
    print('2- Getting version')
    print('3- Scanning ports')
    print('4- Dns-brute-script (get subdomains)')
    print('5- DNS list Scan')
    print('6- Nmap subnet scan')
    print('7- Nmap Fin Scan')
    print('8- Nmap idle scan')
    print('9- Nmap Ping Scan')
    print('10- Nmap Syn Scan')
    print('11- Nmap TCP Scan')
    print('12- Nmap UDP Scan')
    print('13- Nmap port scan only')
    print('14- Nmap No PortScan')
    print('15- Nmap Art Discovery')   
    #insert Args with Nmap
    print('16- Nmap Scan Top Port -sV')
    
    ans = int(input())
    address = input("Insert the Address: ")
    
    if ans == 1 : print(nmap.nmap_os_detection(address))
    elif ans == 2: print(nmap.nmap_version_detection(address))
    elif ans == 3: print(nmap.scan_top_ports(address))
    elif ans == 4: print(nmap.nmap_dns_brute_script(address))
    elif ans == 5: print(nmap.nmap_list_scan(address))
    elif ans == 6: print(nmap.nmap_subnet_scan(address))
    elif ans == 7: print(nmapT.nmap_fin_scan(address))
    elif ans == 8: print(nmapT.nmap_idle_scan(address))
    elif ans == 9: print(nmapT.nmap_ping_scan(address))
    elif ans == 10: print(nmapT.nmap_syn_scan(address))
    elif ans == 11: print(nmapT.nmap_tcp_scan(address))
    elif ans == 12: print(nmapT.nmap_tcp_scan(address))
    elif ans == 13: print(nmapH.nmap_portscan_only(address))
    elif ans == 14: print(nmapH.nmap_no_portscan(address))
    elif ans == 15: print(nmapH.nmap_arp_discovery(address))    
    elif ans == 16: print(nmap.scan_top_ports(address,args="-sV"))
    else:
        print('Invalid Key. Try Again')
def commandLine(command):
    print(command)
    splitCommand = command.split()
    if splitCommand[0] == "Nmap" or splitCommand[0] == "nmap":
        os.system(command)
    else:
        print('Only Nmap Command is allowed\nInsert again')
    
main()