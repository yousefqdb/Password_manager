
# Encrypted Password Manager

This is a passwword manager that uses AES-256 encryption to encrypt passwords
## installation

```bash
  pip install cryptography
```
    
## Help menu
![App Screenshot](https://i.postimg.cc/VLMYtmxK/github-pswd-mngr.png)

## Account search (Search by username or platform)
![App Screenshot](https://i.postimg.cc/fbWZ1XJP/Screenshot-2023-11-27-210450.png)

## Creating an account
![App Screenshot](https://i.postimg.cc/d1LFVYRm/Screenshot-2023-11-27-210532.png)

## Deleting an account
![App Screenshot](https://i.postimg.cc/D01w7hFp/dfdfdfdf.png)



## Setup

Change your db.txt directory, admin_acc.txt directory and encryption key in

```bash
  Password_manager/config/main.json
```

Change the directory of your main.json file mentioned above in

```bash
  Password_manager/functions/json.py
```


Run create_login_key.py and choose a key to encrypt

Put the encrypted key in the admin_acc.txt file

## To run the program
```bash
  cd Password_manager
  python3 main.py

```