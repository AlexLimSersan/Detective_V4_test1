weather_data = {
    #SUN: always cold(ish) except noon. Wind + occasional greyness.
    #RAIN: Light rain, wind, grey. Occasional thunder but nothing crazy.
    #STORM: a fuckn STORM!!! on some crazy weather shit. should be fairly rare and more likely to happen from rain, not just sun.
    #later, have transition texts here.


    "sun": {
        "default": {
            "morning": ["The early sun makes you squint.", "It's a beautiful day.", "It's bathed in the morning sun.", "The early sun peeks over the horizon.",
                        "Morning light spreads out with an amber glow.", "Purple and gold hues paint the morning sky.", "A mix of pink and blue streak the sky...",
                        "The sun makes you squint.",
                        "A cool breeze blows by your ears.", "Wind rushes by.", "A draft of wind picks up some dirt.", "You're hit with a gust of wind.",
                        #birdz
                        "Birds chirp.", "A bird soars through the sky.", "A flock of birds fly by in the distance.",

                        ],
            "afternoon": ["The sky is a clear blue.", "The sky is vast and unclouded.", "The noon sun is unrelenting.", "Heat beats down from overhead",
                          "The noon sun is hot.", "The sun beats down on your back.", "The noon sun sears your back.",
                          "Sharp shadows are cast from the overhead sun.",

                          "A refreshing breeze blows by.", "The wind howls.", "Wind rushes by your ear.", "A gust of wind catches some debris.",
                          "Rain sprinkles down in a fine mist."
                          ],
            "evening": ["The setting sun bathes everything in a soft purple haze.", "Sunlight basks your surroundings amber.",
                        "The sky is a beautiful mix of orange and purple.","The sunset casts a haze of purple hues.",
                         "The light mellows as the sunsets.", "The daylight starts to fade...",

                        "It starts to get colder.", "The temperature drops...",
                        "The sun makes you squint.",

                        "The wind howls.", "An evening breeze blows by...", "Dirt and dust spiral briefly with the wind.",
                        "A gust of wind presses your clothes against you.", "The wind thrusts debris towards you, forcing you to squint."

                        ]
            ,
            "night": ["It's a cold night.", "Stars twinkle brightly above.", "It's dark out.", "The night sky looms overhead.", "Pale moonlight basks your surroundings",
                        "The moon hangs above."
                      "Air rushes by your ear.", "Wind howls in the distance.", "A strong breeze makes your clothes flutter.",
                      "A sudden wind catches debris in a small vortex.", "A faint breeze blows against you."

                      ]
        },
        "urban": {
            "morning": ["The surrounding buildings cast long shadows.", "The morning sun patterns the walls.",
                        "The sun peeks behind rooftops.", "Dust floats by you, caught in a beam of light...", "Patches of sun are caught on the floor.", "Motes of dust idly float around..."

                        ],
            "afternoon": ["Sunlight beats down directly overhead.","Concrete heats in the noon sun.",
                          "The noon sun is unrelenting.", "Clouds float in front of the sun. It's noticeably colder."

                          ],
            "evening": ["The surrounding buildings cast long shadows.", "The evening sun patterns the walls...",
                        "The sun hides behind concrete.", "Motes of dust float by, caught in a beam of light...",
                        "Patches of the sunset are caught on surrounding walls.", "Motes of dust idly float around..."

                        ],
            "night": [""]
        },
        "indoors": {
            "morning": ["Lances of sunlight pierce the blinds.", "Motes of dust float around, caught in a beam of sunlight.",
                        "A warm glow comes from the window.", "Streams of sunlight fill the room.", "Bands of light filter in through the blinds.",
                        "The morning sun makes the dust in the air visible.", "The morning sun filters through the window..."
                        "A draft of air breezes by..."

                        ],
            "afternoon": ["Bright light comes through the blinds.", "Rays of sunlight streak through the window.", "The sun highlights the dust, drifting aimlessly about."

                          ],
            "evening": ["Rows of sunlight pierce through the blind.","A blend of purple and orange hues bathe the room.",
                        "Sunlight sneaks in through the blinds, casting sharp shadows.", "Rays from the sun catch the floating dust."

                        ],
            "night": ["Moonlight filters in through the window.", "Faint moonlight casts a gentle glow across the room.",

                      ]
        },
        "waterfront": { #WAVES FOR ALL 3?
            # MAYBE A DEFAULT TAG DECORATOR, THATS NOT WEATHER?!?!?
            "morning": ["Waves gently lap at the shore.", "The morning light sparkles on the water", ],
            "afternoon": ["Sunlight dances on the water's surface", "The horizon stretches wide and far."],
            "evening": ["The sun sets over the water, casting a golden glow across the waves."],
            "night": ["The moon reflects on the calm water, a silver path illuminated in the darkness."]
        },

    },
    "rain": { #light rain, cold gloomy, perhaps ocassional thunder..
        "default": {
            "morning": ["It's cold and wet.", "Your breath condenses as you exhale", "You exhale a fleeting puff of mist.",
                        "Your nose starts to numb in the cold.", "The chill stings your cheeks.", "Each exhale forms a small cloud.",
                        "Your fingers grow numb in the cold.", "The cold stings.",

                        "The sky is overcast.", "A blanket of grey looms overhead.",
                        "The clouds darken...", "The sky darkens...", #transition?
                        "Rain drizzles around you.", "The rain seeps into your clothes.",
                        "Rain splashes against your face.", "Raindrops dribble against you.",
                        "The rain continues..",
                        "Muffled thunder rumbles in the distance.", "A thunderclap echoes.", "Lightning flashes.",
                        "Puddles ripple in the rain."
                        
                        "The morning is grey and dim.", "Clouds blanket the morning sun.", "The morning is cold and gloomy."
                        ],
            "afternoon": [
                        "It's cold and gloomy.", "It's cold and wet.", "Your breath condenses as you exhale.", "You exhale a fleeting puff of mist.",
                        "The sky is overcast.","A blanket of grey looms overhead.", "Clouds blanket the world in dull shadows.",
                        "The clouds darken...", "The sky darkens...", #transition?
                        "Rain drizzles around you.", "The rain seeps into your clothes.",
                        "Rain splashes against your face.", "Raindrops dribble against you.",
                        "The rain continues..",
                        "Muffled thunder rumbles in the distance.", "A thunderclap echoes.", "Lightning flashes.",
                        "Puddles ripple in the rain."
                
                        "The overhead sun is marked only by a slightly lighter patch.", "The afternoon sun is covered from the clouds.",

            ],
            "evening": [
                    "It's cold and gloomy.", "It's cold and wet.", "Your breath condenses as you exhale.",
                    "You exhale a fleeting puff of mist.",
                    "The sky is overcast.", "A blanket of grey looms overhead.",
                    "Clouds blanket the world in dull shadows.",

                    "The cold numbs your nose.", "Your cheeks sting.", "Each exhale forms a lingering cloud.",
                    "Your fingers start to numb.", "The cold stings.",

                    "Rain drizzles around you.", "The rain seeps into your clothes.",
                    "Rain splashes against your face.", "Raindrops dribble against you.",
                    "The rain continues..",
                    "Muffled thunder rumbles in the distance.", "A thunderclap echoes.", "Lightning flashes.",
                    "Puddles ripple in the rain."
                    
                    "The clouds mask the sunset...", "The sky darkens with the setting sun...",  # transition?
                    "A chill sets in...","The sun slowly inches under the horizon...","The sun hides itself..",
                    "The evening air grows colder", "The sunset is hides behind a veil of grey."

                        ],
            "night": [
                "It's cold tonight.", "You shiver.", "Your breath condenses as you exhale.",
                "You exhale a fleeting puff of mist.", "The night sky is blanketed under clouds.",
                "Clouds blanket the night in dull shadows.",

                "The cold numbs your hands.", "Your nose stings.", "A lingering cloud forms with every exhale.",
                "Your fingers start to numb.", "The cold is sharp.",

                "Rain drizzles around you.", "Cold rain seeps into your clothes.",
                "Rain splashes against your face.", "Raindrops dribble against you.",
                "The rain continues..",
                "Muffled thunder rumbles in the distance.", "A thunderclap echoes.", "Lightning flashes.",
                "Puddles ripple in the rain."

                "The night is cold.", "It's chilly.", "It's dark without the moonlight.",
                "The moon hides behind the clouds.", "The moon peeks through fleeting gaps in the clouds."
                "Fleeting gaps in the clouds lets you see the moon.", "Stars are briefly visible as the clouds drift by."

                      ]
        },

        "urban": {
            "morning": [
                    "Rain patters against the rooftops.", "Water streams down the side of buildings.", "Water sheets off your surroundings",
                    "The rain makes the concrete glisten.", "Puddles ripple as they catch the raindrops.", "Rain trickles down the contours of your face.",

                        ],
            "afternoon": [
                    "Rain patters against the rooftops.", "Water streams down the side of buildings.", "Water sheets off your surroundings",
                    "The rain makes the concrete glisten.", "Puddles ripple as they catch the raindrops.", "Rain trickles down the contours of your face.",


                          ],
            "evening": [
                    "Rain patters against the rooftops.", "Water streams down the side of buildings.", "Water sheets off your surroundings",
                    "The rain makes the concrete glisten.", "Puddles ripple as they catch the raindrops.", "Rain trickles down the contours of your face.",


                        ],
            "night": [
                    "Rain patters against the rooftops.", "Water streams down the side of buildings.", "Water sheets off your surroundings",
                    "The rain makes the concrete glisten.", "Puddles ripple as they catch the raindrops.", "Rain trickles down the contours of your face.",
                    "Shadows blend into each other."


                      ]
        },
        "indoors": {
            "morning": [
                "A dull morning glow comes through the windows.",
                "The wind howls from outside.",
                "Raindrops race down the windowpanes.",
                "The window rattles, the rain drums on.",
                "Rain patters against the windows.",
                "Soft, diffuse light comes through the blinds.",
                "Muffled thunder rumbles in the distance.",
                "Rainfall fills the background ambiance.",
                "The window panes shake with the wind."
                        ],
            "afternoon": [
                "A dull glow comes through the windows.",
                "The wind howls from outside.",
                "Raindrops race down the windowpanes.",
                "The window rattles, the rain drums on.",
                "Rain patters against the windows.",
                "Soft, diffuse light comes through the blinds.",
                "Muffled thunder rumbles in the distance.",
                "Rainfall fills the background ambiance.",
                "The window panes shake with the wind.",

            ],
            "evening": [
                "A dull glow comes through the windows.",
                "The wind howls from outside.",
                "Raindrops race down the windowpanes.",
                "The window rattles, the rain drums on.",
                "Rain patters against the windows.",
                "Soft, diffuse light comes through the blinds.",
                "Muffled thunder rumbles in the distance.",
                "Rainfall fills the background ambiance.",
                "The window panes shake with the wind.",

            ],
            "night": [
                "A dull glow comes through the windows.",
                "The wind howls from outside.",
                "Raindrops race down the windowpanes.",
                "The window rattles, the rain drums on.",
                "Rain patters against the windows.",
                "Soft, diffuse light comes through the blinds.",
                "Muffled thunder rumbles in the distance.",
                "Rainfall fills the background ambiance.",
                "The window panes shake with the wind.",

            ]
        },
        "waterfront": {
            "morning": ["Grey skies over the water give the morning a serene, calm feel."],
            "afternoon": ["The waters look steel under the overcast sky, boats bobbing quietly."],
            "evening": [
                "Dull light reflects off the water as the day fades, a blanket of grey enveloping the horizon."],
            "night": ["Muted sounds by the waterfront, as the cloudy night sky merges with the dark waters."]
        }
    },
    "storm": { #WORK ON IT LATER BOI
        "default": { #YOU CAN GET WET IF OUTDOORS, SO DESCRIPTIONS CAN SAY THAT!
            "morning": [
                #defaults that work with all times
                "Rain drizzles around you.", "Muffled thunder rumbles in the distance.",
                "The rain continues heavily", "A thunderclap echoes.", "Lightning flashes.", "The storm rages on.",
                "Puddles ripple in the rain.", "The rain picks up.",
                #morning spec
                "It's raining this morning.", "It's a wet morning."
            ],
            "afternoon": [
#defaults that work with all times
                "The rain drizzles around you.", "Rain drums on the rooftops", "Thunder rumbles in the distance.",
                "The rain continues heavily", "A thunderclap echoes.", "Lightning flashes.", "The storm rages on.",
                "Puddles ripple in the rain.",

                "The rain continues..."
            ],
            "evening": [
#defaults that work with all times
                "The rain drizzles around you.", "Rain drums on the rooftops", "Muffled thunder rumbles in the distance.",
                "The rain continues heavily", "A thunderclap echoes.", "Lightning flashes.", "The storm rages on.",
                "Puddles ripple in the rain.",

                "The rain continues...", "Flashes of lightning illuminate the dark landscape.",
            ],
            "night": [
#defaults that work with all times
                "The rain drizzles around you.", "Rain drums on the rooftops", "Muffled thunder rumbles in the distance.",
                "The rain continues heavily", "A thunderclap echoes.", "Lightning flashes.", "The storm rages on.",
                "Puddles ripple in the rain."

                "A lightning strike casts brief, stark light.",

                "The rain is relentless.", "You brace against the wind.", "Lightning cracks."
            ]
        },
        "urban": {
            "morning": [
            ],
            "afternoon": [
            ],
            "evening": [
            ],
            "night": [
            ]
        },
        "indoors": {
            "morning": [
                #defaults that work with all times
                "The wind howls from outside.",
                "Raindrops patter against the window panes", "The rainfall is relentless, pouring atop the roof.",
                "Muffled thunder rumbles in the distance.", "Rain streaks the windows.", "Sheets of rain cascade down the windows",
                "Raindrops drum against the windows, and race down the glass.",
                "The rain continues.", "A thunderclap echoes from outside.", "Lightning flashes, briefly illuminating the room.", "The storm rages on.",
            ],
            "afternoon": [
                # defaults that work with all times
                "The wind howls from outside.", "Raindrops patter against the window panes",
                "The rainfall is relentless, pouring atop the roof.",
                "Muffled thunder rumbles in the distance.", "Rain streaks the windows.",
                "Sheets of rain cascade down the windows",
                "Raindrops drum against the windows, and race down the glass.",
                "The rain continues.", "A thunderclap echoes from outside.",
                "Lightning flashes, briefly illuminating the room.", "The storm rages on.",
            ],
            "evening": [
                #defaults that work with all times
                "The wind howls from outside.",
                "Raindrops patter against the window panes", "The rainfall is relentless, pouring atop the roof.",
                "Muffled thunder rumbles in the distance.", "Rain streaks the windows.", "Sheets of rain cascade down the windows",
                "Raindrops drum against the windows, and race down the glass.",
                "The rain continues.", "A thunderclap echoes from outside.", "Lightning flashes, briefly illuminating the room.", "The storm rages on.",
            ],
            "night": [
                #defaults that work with all times
                "The wind howls from outside.",
                "Raindrops patter against the window panes", "The rainfall is relentless, pouring atop the roof.",
                "Muffled thunder rumbles in the distance.", "Rain streaks the windows.", "Sheets of rain cascade down the windows",
                "Raindrops drum against the windows, and race down the glass.",
                "The rain continues.", "A thunderclap echoes from outside.", "Lightning flashes, briefly illuminating the room.", "The storm rages on.",
            ]
        },
        "waterfront": {
            "morning": [
                "Morning showers mix with sporadic thunder, the sound amplified by the open water."
            ],
            "afternoon": [
                "Waves chop against the docks under the torrential rain, with thunder rolling overhead like a constant threat."
            ],
            "evening": [
                "The evening storm sends spray and foam from crashing waves, with lightning occasionally revealing the turmoil of the waterfront."
            ],
            "night": [
                "Thunderstorms rage over the water at night, the flashes of lightning intermittently illuminating the roiling sea."
            ]
        },

    }
}
