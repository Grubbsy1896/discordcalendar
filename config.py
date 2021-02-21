# Config for calendar bot

import datetime

# General Settings
settings = {
    "Token": "bot_token_goes_here",
    "Prefix": "c!",
    "announcement_channels": [ # So you can add more than 1 channel to announce in! 
        "0",
        "0"
    ]
}

# Holidays
holidays = {
    "January": {
        '1': 'New Year Day',
        '2': 'Science Fiction Day', 
        '3': '', 
        '4': '', 
        '5': '', 
        '6': '',
        '7': '', 
        '8': '', 
        '9': '',
        '10': '', 
        '11': '', 
        '12': '', 
        '13': '', 
        '14': '', 
        '15': '', 
        '16': '', 
        '17': '', 
        '18': '', 
        '19': '', 
        '20': '', 
        '21': '', 
        '22': '', 
        '23': '', 
        '24': '', 
        '25': '', 
        '26': '', 
        '27': '', 
        '28': '', 
        '29': '', 
        '30': '',
        '31': ''
    },
    "February": {
        '1': 'Change Your Password Day and G.I. Joe Day',
        '2': "Groundhog's Day", 
        '3': 'Doggy Date Night', 
        '4': 'World Cancer Day and National Thank a Mail Carrier Day', 
        '5': 'Disaster Day', 
        '6': 'Lame Duck Day',
        '7': "'e' Day", 
        '8': 'Laugh and Get Rich Day', 
        '9': 'National Pizza Day',
        '10': 'National Flannel Day', 
        '11': "National Don't Cry Over Spilt Milk Day", 
        '12': 'Darwin Day', 
        '13': 'World Radio Day', 
        '14': "Valentine's Day", 
        '15': 'Single Awareness Day', 
        '16': 'National Innovation Day and Kyoto Protocol Day', 
        '17': 'Random Act of Kindness Day', 
        '18': 'National Drink Wine Day', 
        '19': 'National Chocolate Mint Day', 
        '20': 'National Love Your Pet Day', 
        '21': 'International Mother Language Day', 
        '22': 'European Day for Victims of Crime', 
        '23': 'Curling is Cool Day', 
        '24': 'National Trading Card Day', 
        '25': 'Quiet Day', 
        '26': "Carnival Day, and For Pete's Sake Day", 
        '27': 'Pokémon Day', 
        '28': 'National Choclate Soufflé Day', 
        '29': 'Leap Day'
    },
    "March": {
        '1': "National Peanut Butter Lover's Day",
        '2': "International Rescue Cat Day", 
        '3': 'Talk In Third Person Day', 
        '4': "International Game Master's Day", 
        '5': 'Multiple Personality Day', 
        '6': 'National Alamo Day and National Oreo Cookie Day',
        '7': 'National Cereal Day', 
        '8': "International Women's Day", 
        '9': "Panic Day and Get Over It Day",
        '10': 'Mario Day', 
        '11': 'National Johnny Appleseed Day', 
        '12': 'National Plant A Flower Day', 
        '13': 'National K9 Veterans Day', 
        '14': 'Pi Day', 
        '15': 'National Kansas Day', 
        '16': 'Everything You Do Is Right Day', 
        '17': "St. Patrick's Day", 
        '18': 'National Sloppy Joe Day', 
        '19': 'National Chocolate Caramel Day', 
        '20': 'World Flour Day', 
        '21': 'World Down Syndrome Day', 
        '22': 'National Goof Off Day', 
        '23': 'National Chia Pet Day', 
        '24': 'National Chocolate Covered Raisin Day', 
        '25': 'National Medal of Honor Day', 
        '26': 'Epilepsy Awareness Day – Purple Day and National Nougat Day', 
        '27': 'National Scribble Day and National Joe Day', 
        '28': 'National Something on a Stick Day', 
        '29': 'National Vietnam War Veterans Day', 
        '30': 'National Pencil Day and National Take a Walk In The Park Day',
        '31': 'National Bunsen Burner Day and National Tater Day'
    },
    "April": {
        '1': "April Fool's Day",
        '2': 'National Peanut Butter and Jelly Day', 
        '3': 'World Party Day', 
        '4': 'National School Librarian Day', 
        '5': 'National Deep Dish Pizza Day', 
        '6': "New Beer's Eve",
        '7': 'National Beer Day', 
        '8': 'National Zoo Lovers Day', 
        '9': 'National Former Prisoner of War Recognition Day and National Winston Churchill Day',
        '10': 'Encourage A Young Writer Day', 
        '11': 'National Barber Shop Quartet Day', 
        '12': 'National For Twelves Day', 
        '13': 'National Thomas Jefferson Day and National Scrabble Day', 
        '14': 'Look Up at The Sky Day and National Reach as High as You Can Day', 
        '15': 'National Take a Wild Guess Day and National Titanic Remembrance Day', 
        '16': 'National Wear Your Pyjamas To Work Day', 
        '17': 'National Haiku Poetry Day', 
        '18': 'National Animal Cracker Day', 
        '19': 'National Hanging Out Day', 
        '20': 'Unofficial Weed Day.', 
        '21': 'National Kindergarten Day', 
        '22': 'National Earth Day', 
        '23': 'National Lost Dogs Awareness Day', 
        '24': 'National Pigs in a Blanket Day', 
        '25': 'National East Meets West Day', 
        '26': 'National Pretzel Day', 
        '27': 'National Tell a Story Day', 
        '28': 'National Superhero Day', 
        '29': 'National Zipper Day', 
        '30': 'National Adopt a Shelter Pet Day and National Bugs Bunny Day',
        '31': 'Congratulations! YOU FOUND A HIDDEN SECRET!'
    },
    "May": {
        '1': 'Law Day',
        '2': 'National Life Insurance Day', 
        '3': 'National Paranormal Day', 
        '4': 'National Star Wars Day', 
        '5': 'Cinco De Mayo', 
        '6': 'National Beverage Day',
        '7': '', 
        '8': 'National Have a Coke Day', 
        '9': '',
        '10': '', 
        '11': '', 
        '12': '', 
        '13': '', 
        '14': '', 
        '15': '', 
        '16': '', 
        '17': '', 
        '18': '', 
        '19': '', 
        '20': '', 
        '21': '', 
        '22': '', 
        '23': '', 
        '24': '', 
        '25': '', 
        '26': '', 
        '27': '', 
        '28': '', 
        '29': '', 
        '30': '',
        '31': ''
    },
    "June": {
        '1': '',
        '2': '', 
        '3': '', 
        '4': '', 
        '5': '', 
        '6': '',
        '7': '', 
        '8': '', 
        '9': '',
        '10': '', 
        '11': '', 
        '12': '', 
        '13': '', 
        '14': '', 
        '15': '', 
        '16': '', 
        '17': '', 
        '18': '', 
        '19': '', 
        '20': '', 
        '21': '', 
        '22': '', 
        '23': '', 
        '24': '', 
        '25': '', 
        '26': '', 
        '27': '', 
        '28': '', 
        '29': '', 
        '30': ''
    },
    "July": {
        '1': 'Independence Day (Canada)',
        '2': '', 
        '3': '', 
        '4': 'Independence Day (America)', 
        '5': '', 
        '6': '',
        '7': '', 
        '8': '', 
        '9': '',
        '10': '', 
        '11': '', 
        '12': '', 
        '13': '', 
        '14': '', 
        '15': '', 
        '16': '', 
        '17': '', 
        '18': '', 
        '19': '', 
        '20': '', 
        '21': '', 
        '22': '', 
        '23': '', 
        '24': '', 
        '25': '', 
        '26': '', 
        '27': '', 
        '28': '', 
        '29': '', 
        '30': '',
        '31': ''
    },
    "August": {
        '1': '',
        '2': '', 
        '3': '', 
        '4': '', 
        '5': '', 
        '6': '',
        '7': '', 
        '8': '', 
        '9': '',
        '10': '', 
        '11': '', 
        '12': '', 
        '13': '', 
        '14': '', 
        '15': '', 
        '16': '', 
        '17': '', 
        '18': '', 
        '19': '', 
        '20': '', 
        '21': '', 
        '22': '', 
        '23': '', 
        '24': '', 
        '25': '', 
        '26': '', 
        '27': '', 
        '28': '', 
        '29': '', 
        '30': '',
        '31': ''
    },
    "September": {
        '1': '',
        '2': '', 
        '3': '', 
        '4': '', 
        '5': '', 
        '6': '',
        '7': '', 
        '8': '', 
        '9': '',
        '10': '', 
        '11': '', 
        '12': '', 
        '13': '', 
        '14': '', 
        '15': '', 
        '16': '', 
        '17': '', 
        '18': '', 
        '19': '', 
        '20': '', 
        '21': '', 
        '22': '', 
        '23': '', 
        '24': '', 
        '25': '', 
        '26': '', 
        '27': '', 
        '28': '', 
        '29': '', 
        '30': '',
    },
    "October": {
        '1': '',
        '2': '', 
        '3': '', 
        '4': '', 
        '5': '', 
        '6': '',
        '7': '', 
        '8': '', 
        '9': 'Leif Erikson Day! Hinga Dinga Durgen!',
        '10': '', 
        '11': '', 
        '12': '', 
        '13': '', 
        '14': '', 
        '15': '', 
        '16': '', 
        '17': '', 
        '18': '', 
        '19': '', 
        '20': '', 
        '21': '', 
        '22': '', 
        '23': '', 
        '24': '', 
        '25': '', 
        '26': '', 
        '27': '', 
        '28': '', 
        '29': '', 
        '30': '',
        '31': 'Halloween'
    },
    "November": {
        '1': '',
        '2': '', 
        '3': '', 
        '4': '', 
        '5': '', 
        '6': '',
        '7': '', 
        '8': '', 
        '9': '',
        '10': '', 
        '11': '', 
        '12': '', 
        '13': '', 
        '14': '', 
        '15': '', 
        '16': '', 
        '17': '', 
        '18': '', 
        '19': '', 
        '20': '', 
        '21': '', 
        '22': '', 
        '23': '', 
        '24': '', 
        '25': '', 
        '26': '', 
        '27': '', 
        '28': '', 
        '29': '', 
        '30': ''
    },
    "December": {
        '1': '',
        '2': '', 
        '3': '', 
        '4': '', 
        '5': '', 
        '6': '',
        '7': '', 
        '8': '', 
        '9': '',
        '10': '', 
        '11': '', 
        '12': '', 
        '13': '', 
        '14': '', 
        '15': '', 
        '16': '', 
        '17': '', 
        '18': '', 
        '19': '', 
        '20': '', 
        '21': '', 
        '22': '', 
        '23': '', 
        '24': 'Christmas Eve', 
        '25': 'Christmas', 
        '26': 'Boxing Day', 
        '27': '', 
        '28': '', 
        '29': '', 
        '30': '',
        '31': "New Year's Eve"
    }
}



