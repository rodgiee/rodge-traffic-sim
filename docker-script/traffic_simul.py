import requests
import random
import time

def main():
    try: 
        file = open("websites.txt")
    except Exception as e: 
        print("ERROR WITH websites.txt:", type(e))
    else: 

        possible_websites = file.read().splitlines()

        while(True):
            rand_i = random.randint(0, len(possible_websites) - 1)
            current_website = possible_websites[rand_i]
            time.sleep(10)
            try:
                current_request = requests.get(current_website, timeout=5)
            except requests.exceptions.ConnectionError:
                pass
            except requests.exceptions.ReadTimeout:
                pass
            print(current_website + ": " + str(current_request.ok))
        

if __name__ == "__main__":
    main()