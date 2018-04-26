# CSCI421-Encrypted-Chat
Encrypted Chat Communication with Python (GUI)

This project is intended to show a proof of concept for an encrypted chat program that is designed to conceal when users send messages. 
If someone was eavesdropping on the packets between a normal TCP connection of two users, they may be able to identify when a user sends a 
message. If the eavesdropper can pinpoint the packet containing a message, they would be able to read the message and invade the privacy
of the two users. 

Applying an encryption algorithm does add to the security of the chat. However, the eavesdropper may still be able to identify
the packets of messages. Then, the eavesdropper can attack the message and attempt to decrypt it. A potential solution is to generate
a continuous stream of fake messages to further shroud when messages are being sent. Taking it another step further, the program
randomly determines when to send the fake messages and also randomizes characters in the fake messages. As the eavesdropper watches
the packets flow between the two users, they should see random spikes of packets all containing encrypted messages. This should prevent
an eavesdropper from pinpointing when a user sends a legitimate message. Even by viewing all the data in the packets, the eavesdropper
should have a difficult time distinguishing which messages are fake and which are not since all the messages are encrypted. 


Usage: python chatRoom.py

One instance of the program acts as a Server and hosts the chat room. Select 'Server' radio button and click 'Connect.' Choose a port
to open for the chat room and send messages through. Click 'Launch.' Now the host should be ready for a client to connect. With
another instance, the program acts as the Client and connects to the Server instance. Choose the 'Client' radio button anc click
'Connect.' Enter the IP address and port number of the instance it is attempting to connect with. Click 'Connect.' Now, the Client 
should be connected to the Server and both instances should be able to send messages between each other. In the background, fake
messages are being sent over the network creating random spikes of packets. The messages are encrypted with the monoalphabetic cipher.
