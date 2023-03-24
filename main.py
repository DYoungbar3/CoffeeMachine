#!/usr/bin/env python3

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def current_resources(resources):
    str_list = []
    for k,v in resources.items():
        print(f'{k.capitalize()}: {v}')

def main():
    avail_water = resources['water']
    avail_milk = resources['milk']
    avail_coffee = resources['coffee']

    choice = input("What would you like: (espresso/latte/cappuccino): ")

    if choice.lower() == 'off':
        exit()

    elif choice.lower() == 'report':
        current_resources(resources)

    elif choice.lower() == 'espresso':
        if MENU["espresso"]['ingredients']['water'] <= avail_water and MENU['espresso']['ingredients']['coffee'] <= avail_coffee:
            print(f'You have chosen espresso.  That will be ${MENU["espresso"]["cost"]}')
        elif MENU["espresso"]['ingredients']['water'] > avail_water and MENU['espresso']['ingredients']['coffee'] <= avail_coffee:
            print("Sorry, we don't have enough water")
        elif MENU["espresso"]['ingredients']['water'] <= avail_water and MENU['espresso']['ingredients']['coffee'] > avail_coffee:
            print("Sorry, we don't have enough coffee")
        else:
            print("Sorry, we don't have enough water or coffee")

    elif choice.lower() == 'latte':
        if MENU['latte']['ingredients']['water'] <= avail_water and MENU['latte']['ingredients']['milk'] <= avail_milk and MENU['latte']['ingredients']['coffee'] <= avail_coffee:
            print(f"You have chosen latte. That will be ${MENU['latte']['cost']}")
        elif MENU['latte']['ingredients']['water'] > avail_water and MENU['latte']['ingredients']['milk'] <= avail_milk and MENU['latte']['ingredients']['coffee'] <= avail_coffee:
            print("Sorry, we don't have enough water")
        elif MENU['latte']['ingredients']['water'] <= avail_water and MENU['latte']['ingredients']['milk'] > avail_milk and MENU['latte']['ingredients']['coffee'] <= avail_coffee:
            print("Sorry, we don't have enough milk")
        elif MENU['latte']['ingredients']['water'] <= avail_water and MENU['latte']['ingredients']['milk'] <= avail_milk and MENU['latte']['ingredients']['coffee'] > avail_coffee:
            print*("Sorry, we don't have enough coffee")
        elif MENU['latte']['ingredients']['water'] > avail_water and MENU['latte']['ingredients']['milk'] > avail_milk and MENU['latte']['ingredients']['coffee'] <= avail_coffee:
            print("Sorry, we don't have enough water or milk")
        elif MENU['latte']['ingredients']['water'] > avail_water and MENU['latte']['ingredients']['milk'] <= avail_milk and MENU['latte']['ingredients']['coffee'] > avail_coffee:
            print("Sorry, we don't have enough water or coffee")
        elif MENU['latte']['ingredients']['water'] <= avail_water and MENU['latte']['ingredients']['milk'] > avail_milk and MENU['latte']['ingredients']['coffee'] > avail_coffee:
            print("Sorry, we don't have enough milk or coffee")
        else:
            print("Sorry, we don't have enough water, milk, or coffee")

    elif choice.lower() == 'cappuccino':
        if MENU['cappuccino']['ingredients']['water'] <= avail_water and MENU['cappuccino']['ingredients']['milk'] <= avail_milk and MENU['cappuccino']['ingredients']['coffee'] <= avail_coffee:
            print(f"You have chosen cappuccino. That will be ${MENU['cappuccino']['cost']}")
        elif MENU['cappuccino']['ingredients']['water'] > avail_water and MENU['cappuccino']['ingredients']['milk'] <= avail_milk and MENU['cappuccino']['ingredients']['coffee'] <= avail_coffee:
            print("Sorry, we don't have enough water")
        elif MENU['cappuccino']['ingredients']['water'] <= avail_water and MENU['cappuccino']['ingredients']['milk'] > avail_milk and MENU['cappuccino']['ingredients']['coffee'] <= avail_coffee:
            print("Sorry, we don't have enough milk")
        elif MENU['cappuccino']['ingredients']['water'] <= avail_water and MENU['cappuccino']['ingredients']['milk'] <= avail_milk and MENU['cappuccino']['ingredients']['coffee'] > avail_coffee:
            print*("Sorry, we don't have enough coffee")
        elif MENU['cappuccino']['ingredients']['water'] > avail_water and MENU['cappuccino']['ingredients']['milk'] > avail_milk and MENU['cappuccino']['ingredients']['coffee'] <= avail_coffee:
            print("Sorry, we don't have enough water or milk")
        elif MENU['cappuccino']['ingredients']['water'] > avail_water and MENU['cappuccino']['ingredients']['milk'] <= avail_milk and MENU['cappuccino']['ingredients']['coffee'] > avail_coffee:
            print("Sorry, we don't have enough water or coffee")
        elif MENU['cappuccino']['ingredients']['water'] <= avail_water and MENU['cappuccino']['ingredients']['milk'] > avail_milk and MENU['cappuccino']['ingredients']['coffee'] > avail_coffee:
            print("Sorry, we don't have enough milk or coffee")
        else:
            print("Sorry, we don't have enough water, milk, or coffee")

main()