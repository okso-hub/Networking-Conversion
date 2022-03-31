# Networking Conversion

To run this project, direct to the correct folder and run the command `python main.py`.

Then, you will be asked to enter the mode in which you want to convert:

For the first one "Binary to IP", you enter a 32 digit binary number which will be converted to 4 decimal numbers, being an adress in IP format.

```
❯ python3 main.py
Enter binary number: 00100010010100010001000100000011

Binary number: 00100010010100010001000100000011 
IP address: 34.81.17.3
```

In the second one "IP to binary", you enter an adress in IP format which will then be converted to a 32 digit binary number.

```
❯ python3 main.py
Enter IP adress: 291.168.213.15
IP Adress: 291.168.213.15
Binary number: 100100011101010001101010100001111
```

And the third one "Generate everything else" takes in an IP adress and the subnet mask which will then generate the:

- Network Adress
- Device Part
- Broadcast
- Default Gateway
- Max possible IP Adress

```
❯ python3 main.py
Enter IP Address: 192.168.213.15
Enter Subnet Mask: 255.255.255.192

Network Address: 192.168.213.0
Device Part: 0.0.0.15
Broadcast: 192.168.213.63
Default Gateway: 192.168.213.1
Max IP: 192.168.213.62
```
