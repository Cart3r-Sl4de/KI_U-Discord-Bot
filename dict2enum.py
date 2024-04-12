import enum
from enum import Enum

claws = {
  1: 'Tiger Claws', 2: 'Wolf Claws', 3: 'Bear Claws', 4: 'Brawler Claws', 5: 'Stealth Claws', 6: 'Hedgehog Claws', 7: 'Raptor Claws', 8: 'Artillery Claws', 9: 'Cancer Claws', 10: 'Beam Claws', 11: 'Viridi Claws', 12: 'Pandora Claws'
  }
orbitars = {1: 'Standard Orbitars', 2: 'Guardian Orbitars', 3: 'Shock Orbitars', 4: 'Eyetrack Orbitars', 5: 'Fairy Orbitars', 6: 'Paw Pad Orbitars', 7: 'Jetstream Orbitars', 8: 'Boom Orbitars', 9: 'Gemni Orbitars', 10: 'Aurum Orbitars', 11: 'Centurion Orbitars', 12: 'Arlon Orbitars'
           }
blades = {1: 'First Blade', 2: 'Burst Blade', 3: 'Viper Blade', 4: 'Crusader Blade', 5: 'Royal Blade', 6: 'Optical Blade', 7: 'Samurai Blade', 8: 'Bullet Blade', 9: 'Aquarius Blade', 10: 'Aurum Blade', 11: 'Palutena Blade', 12: 'Gaol Blade'
         }
clubs = {1: 'Ore Club', 2: 'Babel Club', 3: 'Skyscraper Club', 4: 'Atlas Club', 5: 'Earthmaul Club', 6: 'Ogre Club', 7: 'Halo Club', 8: 'Black Club', 9: 'Capricorn Club', 10: 'Aurum Club', 11: 'Hedraw Club', 12: 'Magnus Club'
        }
bows = {1: 'Fortune Bow', 2: 'Silver Bow', 3: 'Meteor Bow', 4: 'Divine Bow', 5: 'Darkness Bow', 6: 'Crystal Bow', 7: 'Angel Bow', 8: 'Hawkeye Bow', 9: 'Sagittarius Bow', 10: 'Aurum Bow', 11: 'Palutena Bow', 12: 'Phosphora Bow'
       }
arms = {1: 'Crusher Arm', 2: 'Compact Arm', 3: 'Electroshock Arm', 4: 'Volcano Arm', 5: 'Drill Arm', 6: 'Bomber Arm', 7: 'Bowl Arm', 8: 'End-All Arm', 9: 'Taurus Arm', 10: 'Upperdash Arm', 11: 'Kraken Arm', 12: 'Pheonix Arm'
       }
staffs = {1: 'Insight Staff', 2: 'Orb Staff', 3: 'Rose Staff', 4: 'Knuckle Staff', 5: 'Ancient Staff', 6: 'Lancer Staff', 7: 'Flintlock Staff', 8: 'Somewhat Staff', 9: 'Scorpio Staff', 10: 'Laser Staff', 11: 'Dark Pit Staff', 12: 'Thanatos Staff'
         }
cannons = {1: 'EZ Cannon', 2: 'Ball Cannon', 3: 'Predator Cannon', 4: 'Poseidon Cannon', 5: 'Fireworks Cannon', 6: 'Rail Cannon', 7: 'Dynamo Cannon', 8: 'Doom Cannon', 9: 'Leo Cannon', 10: 'Sonic Cannon', 11: 'Twinbellow Cannon', 12: 'Cragalanche Cannon'
          }
palms = {1: 'Violet Palm', 2: 'Burning Palm', 3: 'Needle Palm', 4: 'Midnight Palm', 5: 'Cursed Palm', 6: 'Cutter Palm', 7: 'Pudgy Palm', 8: 'Ninja Palm', 9: 'Virgo Palm', 10: 'Aurum Palm', 11: 'Viridi Palm', 12: 'Great Reaper Palm'
        }


# Dynamically create global variables for each claw
for key, value in palms.items():
    # Convert the value to a valid variable name by replacing spaces with underscores
    var_name = value.replace(" ", "_")
    '''# Assign the key as the value of the new global variable
    globals()[var_name] = key
    var_name = value.replace(" ", "_")'''
    print(f"{var_name.lower()} = {key}")

