import socket #Socket gives us everything necessary to connect to another node
import ipaddress #Used for various tasks related to Ips including checking if a string is an ip
import re #Helps validate input


port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
#Will be used for number of ports user wants

port_min = 0     
port_max = 65535 

#Cool Banner
print("""
                                               ...                                        
                                           .         .                                    
                                          .  %&@&%&#           AIverson Port Scanner                           
                                     .       (%#((((                 Go Sixers....                      
                                  .   %&@@@%##((#((   .                                   
                                 .  %(#@@@@@(###(#@@@(                                    
                                .  /(#(&@@@@@&(&@@@@@##  .                                
                               .  *@&(#@@.####%%&@@@#((  .                                
                              .  *@@@(@%/(#*,..,&/,@((#  .                                
                                @@@@ (@@@@@@@@@@(*#####(  .                               
                            .  @@@@.,@@@@@@@@@#%@@@ @@@@  .                               
                           .  %@@@ @@@@@@@@@@/#(@@  ((#(  .                               
                           .  @@@/##%%%@@@@@@@@@@@.  #(#  .                               
                          .  *&@ /(#(#&&@@@@@@@@@@.  ,#(  .                               
                         .  *((* .##(( &@@@@@@@@@@@  (&%  .                               
                         .  #/%.  /((,  @@@@@@@@@@@ #%&#*   .                             
                          .       *@@@   @@@@@@@@@*/***#%@@  .                            
                               .  ,@@    /@@@@@@@@ ,/*****@  ..                           
                              .  %@@@.     @%%@@@( .******//..   .                        
                              .  @@@@   .  .%#(%@    . //,.**//(   .                      
                              .       .      ###%      ,...*****/*  .                     
                                         ..  ##(#      ,...*/*****,  .                    
                                      .   ,(*(((#      ,,*...,*****.                      
                                       ,//****//.,,     *,...,/%***/  .                   
                                    ///********....&*,.*.....,&%**/*,                     
                    .  %/,       *#**/****,  * ....&%&%%& ,*.,&***%   .                   
                       .&  .  /   /***(     *,.,....%&%%%%%%&/**(.                        
                     .  ,(%  .   ,       .   (..**,*....*(&(***                           
                         , &*,*.  .      .  @@@@@#,*,....//***                            
                       .       .          .                                               

                                                                            """)


print("\n****************************************************************")
print("\n* Personal Project                                             *")
print("\n* https://www.linkedin.com/in/joshua-ramos-b4538a172/          *")
print("\n****************************************************************")

openports = []

while True:
    ip_input = input("\n Enter target ip address to scan: ") #Takes user input
    try:
        valid_ip = ipaddress.ip_address(ip_input) #Checks if Ip is valid
        print("Proccessing...........................")
        break
    except: #If ip is wrong print statement and try again. 
        print("That ip was a brick try again")
        

        

while True:
    print("Enter the range of ports you would like to scan. <int>-<int> between 0-65535")
    port_input = input("Enter the port range: ")
    
    port_range_spacing = port_range_pattern.search(port_input.replace(" ",""))
    #This makes sure if the user enters either 1 - 100 or 1-100 it would work 
    if port_range_spacing:
        port_min = int(port_range_spacing.group(1))#doing this so we can seperate lower ports
        port_max = int(port_range_spacing.group(2))#and higher ports
        break
        
for port in range(port_min, port_max):
    try:
        redsox = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #I don't like the Redsox btw
#We have to use the socket module. This is because this gives us everything we need to conenct
#To another computer. socket.AF_INET means Address family, and INET just represents ipv4
# socket.SOCK_STREAM just means to use tcp

        redsox.settimeout(0.5) #After every scan it waits 0.5s before the next scan
        redsox.connect((ip_input, port)) #Trys to connect to the ip and port entered.
        #If the command works then it will be allowed to append to open_ports
        openports.append(port)
        
    except:
        pass


for port in openports:
    print("Port {} is open on {}.".format(port, ip_input))
        

