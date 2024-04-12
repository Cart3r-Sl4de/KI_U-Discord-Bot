import enum
from enum import Enum

class Claws(enum.Enum):
    tiger_claws = 1
    wolf_claws = 2
    bear_claws = 3
    brawler_claws = 4
    stealth_claws = 5
    hedgehog_claws = 6
    raptor_claws = 7
    artillery_claws = 8
    cancer_claws = 9
    beam_claws = 10
    viridi_claws = 11
    pandora_claws = 12

class Orbitars(enum.Enum):
    standard_orbitars = 1
    guardian_orbitars = 2
    shock_orbitars = 3
    eyetrack_orbitars = 4
    fairy_orbitars = 5
    paw_pad_orbitars = 6
    jetstream_orbitars = 7
    boom_orbitars = 8
    gemni_orbitars = 9
    aurum_orbitars = 10
    centurion_orbitars = 11
    arlon_orbitars = 12

class Blades(enum.Enum):
    first_blade = 1
    burst_blade = 2
    viper_blade = 3
    crusader_blade = 4
    royal_blade = 5
    optical_blade = 6
    samurai_blade = 7
    bullet_blade = 8
    aquarius_blade = 9
    aurum_blade = 10
    palutena_blade = 11
    gaol_blade = 12

class Clubs(enum.Enum):
    ore_club = 1
    babel_club = 2
    skyscraper_club = 3
    atlas_club = 4
    earthmaul_club = 5
    ogre_club = 6
    halo_club = 7
    black_club = 8
    capricorn_club = 9
    aurum_club = 10
    hedraw_club = 11
    magnus_club = 12

class Bows(enum.Enum):
    fortune_bow = 1
    silver_bow = 2
    meteor_bow = 3
    divine_bow = 4
    darkness_bow = 5
    crystal_bow = 6
    angel_bow = 7
    hawkeye_bow = 8
    sagittarius_bow = 9
    aurum_bow = 10
    palutena_bow = 11
    phosphora_bow = 12

class Arms(enum.Enum):
    crusher_arm = 1
    compact_arm = 2
    electroshock_arm = 3
    volcano_arm = 4
    drill_arm = 5
    bomber_arm = 6
    bowl_arm = 7
    end_all_arm = 8
    taurus_arm = 9
    upperdash_arm = 10
    kraken_arm = 11
    pheonix_arm = 12

class Staffs(enum.Enum):
    insight_staff = 1
    orb_staff = 2
    rose_staff = 3
    knuckle_staff = 4
    ancient_staff = 5
    lancer_staff = 6
    flintlock_staff = 7
    somewhat_staff = 8
    scorpio_staff = 9
    laser_staff = 10
    dark_pit_staff = 11
    thanatos_staff = 12

class Cannons(enum.Enum):
    ez_cannon = 1
    ball_cannon = 2
    predator_cannon = 3
    poseidon_cannon = 4
    fireworks_cannon = 5
    rail_cannon = 6
    dynamo_cannon = 7
    doom_cannon = 8
    leo_cannon = 9
    sonic_cannon = 10
    twinbellow_cannon = 11
    cragalanche_cannon = 12
 
class Palms(enum.Enum):
    violet_palm = 1
    burning_palm = 2
    needle_palm = 3
    midnight_palm = 4
    cursed_palm = 5
    cutter_palm = 6
    pudgy_palm = 7
    ninja_palm = 8
    virgo_palm = 9
    aurum_palm = 10
    viridi_palm = 11
    great_reaper_palm = 12


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

