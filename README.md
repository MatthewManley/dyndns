# DynDns
This is a tool I am creating to update a record in aws route 53 to point to my local network for ssh and other purposes. It is a work in progress

//TODO: Add more stuff to the readme

# Setup
Have python3 and virtual environments setup
Setup AWS CLI and access credentials
Create a virtual environment for the project. I named mine "dyndns_venv". Running the following command will create and activate the virtual environment
```
python3 -m virtualenv dyndns_venv
source dyndns_venv/bin/activate
```