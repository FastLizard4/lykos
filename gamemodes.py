# To add new game modes, rename this file to 'gamemodes.py' then add them in
# Basic frame for the game modes in src/gamemodes.py

# *** DO NOT TOUCH ANY OF THE CODE BETWEEN THE LINES 4 AND 17 ***

from src.messages import messages
import src.settings as var

from src.gamemodes import (

    GameMode,
    game_mode,
    reset_roles,

)

# Add custom game modes from this point

# Seerless mode created by Timson
@game_mode("overcast", minp = 7, maxp = 16, likelihood = 3)
class OvercastMode(GameMode):
    """Intuition and creativity are key to success in a darkened world."""
    def __init__(self, arg=""):
        super().__init__(arg)
        self.SHARPSHOOTER_CHANCE = 1
                                              #    SHAMAN   , CRAZED SHAMAN , WOLF SHAMAN
        self.TOTEM_CHANCES = {       "death": (      2      ,       1       ,      0      ),
                                "protection": (      4      ,       1       ,      0      ),
                                   "silence": (      3      ,       1       ,      0      ),
                                 "revealing": (      6      ,       1       ,      0      ),
                               "desperation": (      0      ,       1       ,      0      ),
                                "impatience": (      2      ,       1       ,      0      ),
                                  "pacifism": (      0      ,       1       ,      0      ),
                                 "influence": (      2      ,       1       ,      0      ),
                                "narcolepsy": (      0      ,       1       ,      0      ),
                                  "exchange": (      0      ,       1       ,      0      ),
                               "lycanthropy": (      0      ,       1       ,      0      ),
                                      "luck": (      0      ,       1       ,      0      ),
                                "pestilence": (      0      ,       1       ,      0      ),
                               "retribution": (      0      ,       1       ,      0      ),
                              "misdirection": (      1      ,       1       ,      0      ),
                                    "deceit": (      0      ,       1       ,      0      ),
                             }
 
        # get default values for wolf shaman's chances
        for totem, (s, cs, ws) in self.TOTEM_CHANCES.items():
            self.TOTEM_CHANCES[totem] = (s, cs, var.TOTEM_CHANCES[totem][2])
 
        self.ROLE_INDEX =         (   7   ,   8   ,   9   ,  10   ,  11   ,  12   ,  13   ,  14   ,  15   ,  16   )
        self.ROLE_GUIDE = reset_roles(self.ROLE_INDEX)
        self.ROLE_GUIDE.update({ # village roles
            "hunter"            : (   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ),
            "shaman"            : (   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ),
            "village drunk"     : (   0   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ),
            "guardian angel"    : (   0   ,   0   ,   0   ,   0   ,   0   ,   1   ,   1   ,   1   ,   1   ,   1   ),
            "harlot"            : (   0   ,   0   ,   0   ,   0   ,   0   ,   0   ,   0   ,   1   ,   1   ,   1   ),
            "matchmaker"        : (   0   ,   0   ,   0   ,   0   ,   0   ,   0   ,   0   ,   0   ,   0   ,   1   ),
            # wolf roles
            "wolf"              : (   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ),
            "minion"            : (   1   ,   0   ,   0   ,   0   ,   0   ,   0   ,   0   ,   0   ,   0   ,   0   ),
            "traitor"           : (   0   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ),
            "wolf cub"          : (   0   ,   0   ,   0   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   2   ),
            "werecrow"          : (   0   ,   0   ,   0   ,   0   ,   0   ,   1   ,   1   ,   1   ,   1   ,   1   ),
            "hag"               : (   0   ,   0   ,   0   ,   0   ,   0   ,   0   ,   0   ,   1   ,   1   ,   1   ),
            # neutral roles
            "crazed shaman"     : (   0   ,   0   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ),
            "vengeful ghost"    : (   0   ,   0   ,   0   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ),
            # templates
            "assassin"          : (   0   ,   0   ,   0   ,   0   ,   1   ,   1   ,   2   ,   2   ,   3   ,   3   ),
            "gunner"            : (   0   ,   0   ,   0   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ),
            "bureaucrat"        : (   0   ,   0   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ,   1   ),
            })
