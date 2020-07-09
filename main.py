import json
import os
import sys
import requests 


def load_spotify_api():
    with open('keys.json') as f:
        data = json.load(f)
    CLIENT_ID = data['GLOBAL_ID_SPOTIFY']
    CLIENT_SECRET = data['GLOBAL_SECRET_SPOTIFY']
    grant_type = 'client_credentials'
    body_params = {'grant_type' : grant_type}
    grant_type = 'client_credentials'
    body_params = {'grant_type' : grant_type}

    url='https://accounts.spotify.com/api/token'
    response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET))
    token_raw = json.loads(response.text)
    token = token_raw["access_token"]
    return token



def validate_login(username, password):
    print("Logging in...")
    token = load_spotify_api()
    print(token)
    return False


def update_user_config(username, password):
    login_result = validate_login(username, password)
    if login_result:
        data = {
            "username": username,
            "password": password
        }
        with open('userconfig.json', 'w') as outfile:
            json.dump(data, outfile)

def get_user_config():
    with open('userconfig.json') as json_file:
        data = json.load(json_file)
        print("Username: ", data["username"])
        print("Password: ", data["password"])
        

def parse_args(args):
    single_flags = ["-h", "--login", "--userConfig"]
    help_message = "get some help"
    error_message = "u done fucked up"

    if (args[1] in single_flags):

        if (args[1] == "-h"):
            return help_message
        elif(args[1] == "--login"):
            print("Enter Username:")
            username = input()
            print("Enter Password:")
            password = input()
            update_user_config(username, password)
        elif(args[1] == "--userConfig"):
            #TODO PRINT USER CONFIG
           pass 
    else:
        if (args[1] == "-p"):
            # TODO Switch to this playlist
            pass
        elif (args[1] == "-ar"):
            # TODO Switch to this artist
            pass
        elif (args[1] == "-a"):
            # TODO Switch to this album
            pass
        elif (args[1] == "-q"):
            # TODO Switch to this playlist
            pass
        else:
            print(error_message)


           


def main():

    # TODO PULL FROM FILES


    single_flags = ["-h", "--login" "--userConfig"]

    n = len(sys.argv) 
    #single flags need to be dealt with
    # -login
    if (sys.argv[1] in single_flags and n > 2):
        return error_message
    else:
        print(parse_args(sys.argv))



    # # Arguments passed 
    # print("\nName of Python script:", sys.argv[0]) 
    
    # print("\nArguments passed:", end = " ") 
    # for i in range(1, n): 
    #     print(# Arguments passed 
    # print("\nName of Python script:", sys.argv[0]) 
    
    # print("\nArguments passed:", end = " ") 
    # for i in range(1, n): 
    #     print(sys.argv[i], end = " ") 
        
    # Addition of numbers 
    # Sum = 0
    # Using argparse module 
    # for i in range(1, n): 
    #     Sum += int(sys.argv[i]) 
        
    # print("\n\nResult:", Sum) , end = " ") 
        
    # # Addition of numbers 
    # Sum = 0
    # # Using argparse module 
    # for i in range(1, n): 
    #     Sum += int(sys.argv[i]) 
        
    # print("\n\nResult:", Sum) 



if __name__ == '__main__':
    main()