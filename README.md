# Password generator

The aim of application is to provide a different password for each site that you need.
The password is generated with a random key (from RANDOM.ORG) contatenated with the name of site (e.g. gmail), using SHA256. An example is: 
> password_for_gmail = SHA256("Va_dsUI2%éws" + "gmail") = 25d8dce1b66348602ff3e35fca441da4776aa9eed0784aeb4f9458d074982b41


### Libraries
You need to install _rdoclient library_, in this way:
- Download the repository from  https://github.com/RandomOrg/JSON-RPC-Python.
- Start the installation in /JSON-RPC-Python with the python command.
```sh
$ sudo setup.py install
``` 

### Running

Open terminal on /code/ and digit:
```sh
$ python3 main.py
```

At the end of the process, it will been created a .txt file that contains the key. I strongly recommend to save the key on an external device (e.g. usb key), and for make it more secure, write it on a piece of paper.
