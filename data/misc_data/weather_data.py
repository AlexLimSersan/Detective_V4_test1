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
            "afternoon": ["The sky is a clear blue.", "The sky is vast and unclouded.", "The noon sun is unrelenting.",
                          "Heat beats down from overhead",
                          "The noon sun is hot.", "The sun beats down on your back.", "The noon sun sears your back.",
                          "Sharp shadows are cast from the overhead sun.",
                          "A refreshing breeze blows by.", "The wind howls.", "Wind rushes by your ear.", "A gust of wind catches some debris.",
                          ],
            "evening": ["The setting sun bathes everything in a soft purple haze.", "Sunlight basks your surroundings in an amber glow.",
                        "The sky is a beautiful mix of orange and purple.","The sunset casts a haze of purple hues.",
                         "The sky mellows as the sunsets.", "The daylight starts to fade...",
                        "It starts to get colder.", "The temperature drops...",
                        "The sun makes you squint.",
                        "The wind howls.", "An evening breeze blows by...", "Dirt and dust spiral briefly with the wind.",
                        "A gust of wind presses your clothes against you.", "The wind thrusts debris towards you, forcing you to squint.",
                        ]
            ,
            "night": ["It's a cold night.", "Stars twinkle brightly above.", "It's dark out.",
                      "The night sky looms overhead.", "Pale moonlight basks your surroundings",
                      "The moon hangs above." "The moon hangs overhead, clear and bright.",
                      "Air rushes by you.", "Wind howls in the distance.", "A strong breeze makes your clothes flutter.",
                      "A sudden wind catches debris in a small vortex.", "A faint breeze blows against you.",

                      "Crickets chirp in the distance", "Crickets chirp nearby",
                      "The sound of crickets fills the otherwise silent night.",

                      ]
        },
        "cab":{
            "morning": ["The morning sun paints the cab gold.", "The early light makes the hood shimmer.",
                        ],
            "afternoon": ["Sunlight glares off the cab, making you squint.", "The cab basks in the noon sun.",
                          "The sunlight makes the hood glimmer.", "The leather seats are hot from the sun.",
                          ],
            "evening": ["The setting sun casts sharp shadows across the interior.","A beam of light reflects off the cab.",
                        "The cab gleams in the evening light.", "You can see the sunset in the mirror."],

            "night":["The moonlight casts the cab in a dull glow.","The cab idles under the night sky.",
                     "The interior is dark, lit only by the faint, scattered moonlight.",
                     "The headlights and his cigarette are the only source of light."],
               },

        "urban": {
            "morning": ["The surrounding buildings cast long shadows.", "The morning sun patterns the walls.",
                        "The sun peeks behind rooftops.", "Dust floats by you, caught in a beam of light...",
                        "Patches of sun are caught on the floor.", "Motes of dust idly float around...",
                        ],
            "afternoon": ["Sunlight beats down directly overhead.","Concrete bathes in the noon sun.",
                          "Motes of dust idly float around...",
                          "The noon sun is unrelenting.", "The temperature drops as clouds float by the sun, shading you.",
                          ],
            "evening": ["Long, drawn out shadows are cast from the setting sun.", "The evening sun patterns the walls...",
                        "The sun starts to descend.", "Motes of dust float by, caught in a beam of light...",
                        "Patches of the sunset are caught on surrounding walls.",
                        ],
            "night": ["The towering buildings are cloaked in darkness.", "Shadows loom between the buildings...",
                      "The darkness makes it seem like it stretches on, indefinitely.",
                      "Bricks glow in the moonlight, dull and pale.",
                      "The shadows blend into each other.",
                      ]
        },
        "indoors": {
            "morning": ["Lances of sunlight pierce the blinds.",
                        "A warm glow comes from the window.", "Streams of sunlight fill the room.",
                        "Bands of light filter in through the blinds.","The morning sun filters through the window...",
                        "The morning sun makes the dust in the air visible.",  "Motes of dust float around, caught in a beam of sunlight.",
                        "A draft of air comes from a window.",

                        "From outside, distant birds chirp.",

                        "The building groans.", "The floor creaks.",
                        ],
            "afternoon": ["Bright light comes through the blinds.", "Rays of sunlight streak through the window.",
                          "The noon sun glares in from the outside.", "Sunlight makes the blinds glow.",
                          "The sun highlights the dust, drifting aimlessly about.",
                          "From the window, a cool draft blows by you.",

                          "From outside, the birds quietly sing. ",
                          "The floor groans.", "The walls creak.",
                          ],
            "evening": ["Rows of sunlight pierce through the blind.","A blend of purple and orange hues bathe the room.",
                        "Sunlight sneaks in through the blinds, casting sharp shadows.", "Rays from the sun catch the floating dust.",
                        "A refreshing breeze blows from an open window.",

                        "A birds muffled chirps can be heard from outside.", "You hear the first few crickets start to chirp from outside.",
                        
                        "The walls utter a long, drawn out groan.","The floorboards creak under your weight.",
                        ],
            "night": ["Moonlight filters in through the window.", "Faint moonlight casts a gentle glow across the room.",
                      "Crickets chirp from outside.", "From outside, you can hear the soft croaking crickets.",
                      "The wind howls from outside.", "A cool breeze comes from a nearby window.",

                      "The building creaks, shifting in the night.", "A long, drawn out grown comes from the walls."
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
            "morning": ["It's cold and wet.", "Your breath condenses as you exhale.", "You exhale a fleeting puff of mist.",
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

                        "It's raining this morning.", "It's a wet morning.",
                        "Lightning arcs across the sky, followed by thunderous, roaring crack."



                        # storm
                       "Rain drizzles around you.",
                        "Muffled thunder rumbles in the distance.",
                        "The rain continues heavily", "A thunderclap echoes.", "Lightning flashes.",
                        "The storm rages on.",
                        "Puddles ripple in the rain.", "The rain picks up.",

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

                        #storm
                        "The rain drizzles around you.", "Rain drums on the rooftops", "Thunder rumbles in the distance.",
                        "The rain continues heavily", "A thunderclap echoes.", "Lightning flashes.", "The storm rages on.",
                        "Puddles ripple in the rain.",
                        #from cab
                        "Lightning arcs across the sky, followed by thunderous, roaring crack."
        
                        "The rain continues..."
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
                    "The evening air grows colder", "The sunset hides behind a veil of grey.",


                #storm
                "The rain drizzles around you.", "Rain drums on the rooftops", "Muffled thunder rumbles in the distance.",
                "The rain continues heavily", "A thunderclap echoes.", "Lightning flashes.", "The storm rages on.",
                "Puddles ripple in the rain.",
                #from cab
                "Lightning arcs across the sky, followed by thunderous, roaring crack."

                "The rain continues...", "Flashes of lightning illuminate the dark landscape.",

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
                "The moon hides behind the clouds.", "The moon peeks through fleeting gaps in the clouds.",
                "Fleeting gaps in the clouds lets you see the moon.", "Stars are briefly visible as the clouds drift by.",


#defaults that work with all times
                "The rain drizzles around you.", "Rain drums on the rooftops", "Muffled thunder rumbles in the distance.",
                "The rain continues heavily", "A thunderclap echoes.", "Lightning flashes.", "The storm rages on.",
                "Puddles ripple in the rain."
                #from cab
                "Lightning arcs across the sky, followed by thunderous, roaring crack."

                "A lightning strike casts brief, stark light.",

                "The rain is relentless.", "You brace against the wind.", "Lightning cracks."

                      ]
        },
        "cab": {

            "morning": ["Raindrops pelt the cab, streaking its windows.",
                        "The rain makes a rhythmic drumming sound against the roof.",
                        "The rain coats the hood with a dull sheen.",
                        "The headlights cast a pyramid in the rain."],

            "afternoon": ["Beads of rain race down the window.",
                          "Rain drums against the cab.",
                          "The cab is slick from the rain.",
                          ],

            "evening": ["Water trickles down the window.", "Raindrops splash against the cab."
                        "The rain makes a rhythmic drumming sound against the roof.",
                        "A cone of rain gleams in the headlights.",
                        ],

            "night": ["Raindrops patter against the cab.",
                      "A steady, rhythmic patter comes from the rain.",
                      "The headlights cast a pyramid in the rain."],
        },
        "urban": {
            "morning": [
                    "Rain splashes around you.", "Water streams down the side of buildings.",
                "Water sheets off your surroundings",
                    "The rain makes the concrete glisten.", "Puddles ripple as they catch each raindrop.",
                "Rain trickles down the contours of the walls.",
                #mornign
                "Rain crashes around you.", "Water crashes down the side of buildings.",
                "Water splashes against your surroundings",
                "The storm makes the concrete glisten.", "Puddles ripple as the raindrops pour down.",
                "Rain sheets off the contours of the walls.",
                "The stormwater pools near the corners."
                        ],
            "afternoon": [
                    "Rain patters against the walls.",
                "Water coats the buildings with a dull sheen.", "Water sheets off the bricks.",
                    "The concrete glistens in the rain.", "The raindrops fall around you.",
                "The rain gathers, streaming towards a drain.",

                "Rain hammers against the walls.",
                "Water coats the buildings with a slick, dull sheen.", "Water crashes off the bricks.",
                "The concrete shimmers in the rain.", "The wind roars, raindrops crash into you.",
                "The rain gathers into a large stream, racing towards a drain.",
                          ],
            "evening": [
                    "Rain patters against the rooftops.", "Water streams down the side of buildings.",
                "Water coats the ground.",
                    "The walls glisten in the rain.", "Puddles ripple under the falling rain.",
                "The rain gathers in puddles..",

                    #storm
                "Rain splashes against the rooftops.", "Water streaks down the side of buildings.",
                "The water pools on the ground.",
                "The walls glisten in the storm.", "Puddles ripple under the falling rain.",
                "The rain crashes around you.",
                        ],
            "night": [
                    "Rain patters against the walls.", "Water streams down the side of buildings.",
                "Water sheets off your surroundings",
                    "The rain makes the concrete glisten.", "Puddles ripple as they catch the raindrops.",
                "Rain trickles down your face.",
                #storm
                "Rain hammers against you.", "Water streams down your face.",
                "Water sheets off your surroundings",
                "The rain makes the concrete glisten.", "Puddles ripple as they catch the raindrops.",
                "Rain trickles down your face.",
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
                "The window panes shake with the wind.",

                #storm
                "The wind howls from outside.",
                "Raindrops patter against the window panes.", "The rainfall is relentless, pouring atop the roof.",
                "Muffled thunder rumbles in the distance.", "Rain streaks the windows.",
                "Sheets of rain cascade down the windows",
                "Raindrops drum against the windows, and race down the glass.",
                "The rain continues.", "A thunderclap echoes from outside.",
                "Lightning flashes, briefly illuminating the room.", "The storm rages on.",
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

                #storm
                "The wind howls from outside.", "Raindrops patter against the window panes.",
                "The rainfall is relentless, pouring atop the roof.",
                "Muffled thunder rumbles in the distance.", "Rain streaks the windows.",
                "Sheets of rain cascade down the windows",
                "Raindrops drum against the windows, and race down the glass.",
                "The rain continues.", "A thunderclap echoes from outside.",
                "Lightning flashes, briefly illuminating the room.", "The storm rages on.",

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

                # storm
                "The wind howls from outside.",
                "Raindrops patter against the window panes.", "The rainfall is relentless, pouring atop the roof.",
                "Muffled thunder rumbles in the distance.", "Rain streaks the windows.",
                "Sheets of rain cascade down the windows",
                "Raindrops drum against the windows, and race down the glass.",
                "The rain continues.", "A thunderclap echoes from outside.",
                "Lightning flashes, briefly illuminating the room.", "The storm rages on.",

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

                # storm
                "The wind howls from outside.",
                "Raindrops patter against the window panes.", "The rainfall is relentless, pouring atop the roof.",
                "Muffled thunder rumbles in the distance.", "Rain streaks the windows.",
                "Sheets of rain cascade down the windows",
                "Raindrops drum against the windows, and race down the glass.",
                "The rain continues.", "A thunderclap echoes from outside.",
                "Lightning flashes, briefly illuminating the room.", "The storm rages on.",

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
        "cab": {
        },
        "indoors": {
            "morning": [
            ],
            "afternoon": [
            ],
            "evening": [
            ],
            "night": [
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
