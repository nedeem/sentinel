# Imports.
import os
import sys
import json
import requests
from colorama import Fore # For text colour.

# Config (Prints).
text = (f"{Fore.WHITE}") # Change the colour of text output in the client side
dividers = (f"{Fore.LIGHTRED_EX}") # Changes the [], | and : in the client side
success = (f"\n{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}] Program executed sucessfully.") # Success output.
response = (f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]")
successfully = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]") # Successfully output.
failed = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}FAILED{Fore.WHITE}]") # Failed output.
prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]") # Prompt output.
notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]") # Notice output.
question =  (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]") # Alert output.
alert =  (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]") # Alert output.
exited = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]") # Execited output.
disconnected = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}DISCONNECTED{Fore.WHITE}]") # Disconnected output.
command = (f"\n[{Fore.YELLOW}>_{Fore.WHITE}]: ") # Always asks for a command on a new line.

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# API.
# Example, uncomment lines 30-32 if API required.
with open('./src/modules/var/pipes/api_config.json') as f:
    data = json.load(f)
    key = data["aviationstack"]

# Program.
def flightinfo():
    print(f'{notice} How would you like to filter flight data? (icao24, number, date, dep_iata, arr_iata or status) ')
    option = input(f'{command}').lower()

    if option == 'number':
        number = input(f"{question} Enter a flight number: ")
        data = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={key}&flight_number={number}").json()['data']
        for i in range(0,len(data)):
            print(f"{response} Airline Name: {data[i]['airline']['name']}")
            print(f"{response} Flight Date: {data[i]['flight_date']}")
            print(f"{response} Status: {data[i]['flight_status']}")
            print(f"{response} Departure Airport: {data[i]['departure']['airport']}")
            print(f"{response} Departure Timezone: {data[i]['departure']['timezone']}")
            print(f"{response} Departure IATA/ICAO: {data[i]['departure']['iata']} | {data[i]['departure']['icao']}")
            print(f"{response} Departure Terminal/Gate: {data[i]['departure']['terminal']}{data[i]['departure']['gate']}")
            print(f"{response} Estimated Departure: {data[i]['departure']['estimated']}")
            print(f"{response} Actual Departure: {data[i]['departure']['actual']}")
            print(f"{response} Arrival Airport: {data[i]['arrival']['airport']}")
            print(f"{response} Arrival Timezone: {data[i]['arrival']['timezone']}")
            print(f"{response} Arrival IATA/ICAO: {data[i]['arrival']['iata']} | {data[i]['arrival']['icao']}")
            print(f"{response} Arrival Terminal/Gate: {data[i]['arrival']['terminal']}{data[i]['arrival']['gate']}")
            print(f"{response} Estimated Arrival: {data[i]['arrival']['estimated']}")
            print(f"{response} Actual Arrival: {data[i]['arrival']['actual']}")
            print("-------------------------------------------------------------------")
        print(success)
    if option == 'date':
        date = input(f"{question} Enter a flight date (YYYY-MM-DD): ")
        data = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={key}&date={date}").json()['data']
        for i in range(0,len(data)):
            print(f"{response} Airline Name: {data[i]['airline']['name']}")
            print(f"{response} Flight Date: {data[i]['flight_date']}")
            print(f"{response} Status: {data[i]['flight_status']}")
            print(f"{response} Departure Airport: {data[i]['departure']['airport']}")
            print(f"{response} Departure Timezone: {data[i]['departure']['timezone']}")
            print(f"{response} Departure IATA/ICAO: {data[i]['departure']['iata']} | {data[i]['departure']['icao']}")
            print(f"{response} Departure Terminal/Gate: {data[i]['departure']['terminal']}{data[i]['departure']['gate']}")
            print(f"{response} Estimated Departure: {data[i]['departure']['estimated']}")
            print(f"{response} Actual Departure: {data[i]['departure']['actual']}")
            print(f"{response} Arrival Airport: {data[i]['arrival']['airport']}")
            print(f"{response} Arrival Timezone: {data[i]['arrival']['timezone']}")
            print(f"{response} Arrival IATA/ICAO: {data[i]['arrival']['iata']} | {data[i]['arrival']['icao']}")
            print(f"{response} Arrival Terminal/Gate: {data[i]['arrival']['terminal']}{data[i]['arrival']['gate']}")
            print(f"{response} Estimated Arrival: {data[i]['arrival']['estimated']}")
            print(f"{response} Actual Arrival: {data[i]['arrival']['actual']}")
            print("-------------------------------------------------------------------")
        print(success)
    if option == 'dep_iata':
        dep_iata = input(f"{question} Enter a flight departure IATA: ")
        data = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={key}&dep_iata={dep_iata}").json()['data']
        for i in range(0,len(data)):
            print(f"{response} Airline Name: {data[i]['airline']['name']}")
            print(f"{response} Flight Date: {data[i]['flight_date']}")
            print(f"{response} Status: {data[i]['flight_status']}")
            print(f"{response} Departure Airport: {data[i]['departure']['airport']}")
            print(f"{response} Departure Timezone: {data[i]['departure']['timezone']}")
            print(f"{response} Departure IATA/ICAO: {data[i]['departure']['iata']} | {data[i]['departure']['icao']}")
            print(f"{response} Departure Terminal/Gate: {data[i]['departure']['terminal']}{data[i]['departure']['gate']}")
            print(f"{response} Estimated Departure: {data[i]['departure']['estimated']}")
            print(f"{response} Actual Departure: {data[i]['departure']['actual']}")
            print(f"{response} Arrival Airport: {data[i]['arrival']['airport']}")
            print(f"{response} Arrival Timezone: {data[i]['arrival']['timezone']}")
            print(f"{response} Arrival IATA/ICAO: {data[i]['arrival']['iata']} | {data[i]['arrival']['icao']}")
            print(f"{response} Arrival Terminal/Gate: {data[i]['arrival']['terminal']}{data[i]['arrival']['gate']}")
            print(f"{response} Estimated Arrival: {data[i]['arrival']['estimated']}")
            print(f"{response} Actual Arrival: {data[i]['arrival']['actual']}")
            print("-------------------------------------------------------------------")
        print(success)
    if option == 'arr_iata':
        arr_iata = input(f"{question} Enter a flight arrival IATA: ")
        data = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={key}&arr_iata={arr_iata}").json()['data']
        for i in range(0,len(data)):
            print(f"{response} Airline Name: {data[i]['airline']['name']}")
            print(f"{response} Flight Date: {data[i]['flight_date']}")
            print(f"{response} Status: {data[i]['flight_status']}")
            print(f"{response} Departure Airport: {data[i]['departure']['airport']}")
            print(f"{response} Departure Timezone: {data[i]['departure']['timezone']}")
            print(f"{response} Departure IATA/ICAO: {data[i]['departure']['iata']} | {data[i]['departure']['icao']}")
            print(f"{response} Departure Terminal/Gate: {data[i]['departure']['terminal']}{data[i]['departure']['gate']}")
            print(f"{response} Estimated Departure: {data[i]['departure']['estimated']}")
            print(f"{response} Actual Departure: {data[i]['departure']['actual']}")
            print(f"{response} Arrival Airport: {data[i]['arrival']['airport']}")
            print(f"{response} Arrival Timezone: {data[i]['arrival']['timezone']}")
            print(f"{response} Arrival IATA/ICAO: {data[i]['arrival']['iata']} | {data[i]['arrival']['icao']}")
            print(f"{response} Arrival Terminal/Gate: {data[i]['arrival']['terminal']}{data[i]['arrival']['gate']}")
            print(f"{response} Estimated Arrival: {data[i]['arrival']['estimated']}")
            print(f"{response} Actual Arrival: {data[i]['arrival']['actual']}")
            print("-------------------------------------------------------------------")
        print(success)
    if option == 'status':
        status = input(f"{question} Enter a flight status (scheduled, active, landed, cancelled, incident, diverted): ")
        data = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={key}&status={status}").json()['data']
        for i in range(0,len(data)):
            print(f"{response} Airline Name: {data[i]['airline']['name']}")
            print(f"{response} Flight Date: {data[i]['flight_date']}")
            print(f"{response} Status: {data[i]['flight_status']}")
            print(f"{response} Departure Airport: {data[i]['departure']['airport']}")
            print(f"{response} Departure Timezone: {data[i]['departure']['timezone']}")
            print(f"{response} Departure IATA/ICAO: {data[i]['departure']['iata']} | {data[i]['departure']['icao']}")
            print(f"{response} Departure Terminal/Gate: {data[i]['departure']['terminal']}{data[i]['departure']['gate']}")
            print(f"{response} Estimated Departure: {data[i]['departure']['estimated']}")
            print(f"{response} Actual Departure: {data[i]['departure']['actual']}")
            print(f"{response} Arrival Airport: {data[i]['arrival']['airport']}")
            print(f"{response} Arrival Timezone: {data[i]['arrival']['timezone']}")
            print(f"{response} Arrival IATA/ICAO: {data[i]['arrival']['iata']} | {data[i]['arrival']['icao']}")
            print(f"{response} Arrival Terminal/Gate: {data[i]['arrival']['terminal']}{data[i]['arrival']['gate']}")
            print(f"{response} Estimated Arrival: {data[i]['arrival']['estimated']}")
            print(f"{response} Actual Arrival: {data[i]['arrival']['actual']}")
            print("-------------------------------------------------------------------")
        print(success)
    if option == 'icao24':
        icao24 = input(f"{question} Enter a plane icao24: ")
        begin = input(f"{question} Enter a begin Unix timestamp for the flights interval: ")
        end = input(f"{question} Enter an end Unix timestamp for the flights interval: ")
        data = requests.get(f"https://opensky-network.org/api/flights/aircraft?icao24={icao24}&begin={begin}&end={end}").json()
        for i in range(0,len(data)):
            print(f"{response} Aircraft Callsign: {data[i]['callsign']}")
            print(f"{response} Departure Airport (Estimated): {data[i]['estDepartureAirport']}")
            print(f"{response} Arrival Airport (Estimated): {data[i]['estArrivalAirport']}")
            print(f"{response} Arrival Airport (Estimated): {data[i]['estArrivalAirport']}")
            print(f"{response} First Seen: {data[i]['firstSeen']}")
            print(f"{response} Last Seen: {data[i]['lastSeen']}")
            print("-------------------------------------------------------------------")
        print(success)
# Run module_name module.
if __name__ == '__main__':
    flightinfo()
