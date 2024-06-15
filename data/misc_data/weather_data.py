weather_data = {
    #WIND HERE?
    # things like the wind blows? could have another SIMPLE default system for adding wind to possible descriptions?!
    "sunny": {
        "default": {
            "morning": ["The early sun makes you squint.", "It's a beautiful day.", "It's bathed in the morning sun."],
            "afternoon": ["The sky is a clear blue.", "The sky is vast and unclouded.", "Heat beats down from overhead", "The noon sun is hot."],
            "evening": ["The setting sun bathes everything in a soft purple haze.", "The sky is a beautiful mix of orange and purple.", "The sunset casts a haze of purple hues." "The light mellows as the sunsets.", "It starts to get colder."],
            "night": ["It's a warm night.", "Stars twinkle brightly above you.", "It's dark out.", "The night sky looms overhead."]
        },
        "waterfront": { #WAVES FOR ALL 3?
            # MAYBE A DEFAULT TAG DECORATOR, THATS NOT WEATHER?!?!?
            "morning": ["Waves gently lap at the shore.", "The morning light sparkles on the water", ],
            "afternoon": ["Sunlight dances on the water's surface", "The horizon stretches wide and far."],
            "evening": ["The sun sets over the water, casting a golden glow across the waves."],
            "night": ["The moon reflects on the calm water, a silver path illuminated in the darkness."]
        },
        "urban": {
            "morning": ["The city awakens in golden light, casting long shadows on the bustling streets."],
            "afternoon": ["Sunlight dominates the urban landscape, the concrete jungle alive under the high sun."],
            "evening": ["The city's pace slows as the sun sets, its last light lingering on the tallest buildings."],
            "night": ["Neon lights flicker to life, battling the darkness enveloping the city."]
        },
        "indoors": {
            "morning": ["Lances of sunlight pierce through the blinds.", "Motes of dust float around, caught in a beam of sunlight.", "A warm glow comes from the window.", "Streams of sunlight fill the room.", "Bands of light filter in through the blinds.", "The morning sun makes the dust in the air visible." ],
            "afternoon": ["The room is brightly lit from the sun", "Rays of sunlight streak through the window.", "The sun highlights the dust, drifting aimlessly about."],
            "evening": ["Lances of sunlight pierce through the blinds.","A blend of purple and orange hues bathe the room.", "Sunlight sneaks in through the blinds, casting sharp shadows.", "Rays from the sun catch the floating dust"],
            "night": ["Moonlight sneaks in through the window.", "Faint moonlight casts a gentle glow across the room.", "It's a dark night.", "It's dark out."]
        }
    },
    "grey": {
        "default": {
            "morning": ["It's cold and gloomy.", "The sky is overcast.","A blanket of grey looms overhead.", "The morning is grey and dim.", "Clouds cast the world in soft, dull shadows.", "It's cloudy."],
            "afternoon": ["It's cold and gloomy.", "A soft shroud of mist covers the landscape.", "The overhead sun is marked only by a slightly lighter patch.", "The afternoon sun is covered from the clouds."],
            "evening": ["It's cold and gloomy.", "The evening air grows colder", "The sunset is hidden behind a thick veil of grey."],
            "night": ["The night is cold.", "It's chilly.", "It's dark without the moonlight.", "The moon hides behind the clouds.", "The moon peeks through fleeting gaps in the clouds."]
        },
        "waterfront": {
            "morning": ["Grey skies over the water give the morning a serene, calm feel."],
            "afternoon": ["The waters look steel under the overcast sky, boats bobbing quietly."],
            "evening": ["Dull light reflects off the water as the day fades, a blanket of grey enveloping the horizon."],
            "night": ["Muted sounds by the waterfront, as the cloudy night sky merges with the dark waters."]
        },
        "urban": {
            "morning": ["City dwellers rush under umbrellas, their footsteps quick and splashing through puddles as they navigate the rainy streets."],
            "afternoon": ["Rain dampens the urban buzz, streets less crowded while water streams down building facades and gutters."],
            "evening": ["Puddles reflect the city lights, creating a mirage of colors on the wet pavement as the rain continues to fall."],
            "night": ["Rain and city lights mingle, the streets slick with reflections, the sounds muffled and yet amplified by the water."]
        },
        "indoors": {
            "morning": ["The cold gloom outdoors is visible from here.", "A dull morning glow comes through the windows.", ],
            "afternoon": ["The cold gloom outdoors is visible from here.", "Soft, diffuse light filters through the blinds.", ],
            "evening": ["The cold gloom is visible through the windows.", "Grey twilight fades into the night", "Shadows blend into each other as the evening progresses."],
            "night": ["The wind howls from outdoors."]
        }
    },
    "rain": {
        "default": { #YOU CAN GET WET IF OUTDOORS, SO DESCRIPTIONS CAN SAY THAT!
            "morning": [
                #defaults that work with all times
                "The rain drizzles around you.", "Rain drums on the rooftops", "Muffled thunder rumbles in the distance.",
                "The rain continues heavily", "A thunderclap echoes.", "Lightning flashes.", "The storm rages on.",
"Puddles ripple in the rain."
                #morning spec
                "It's raining this morning.", "It's a wet morning."
            ],
            "afternoon": [
#defaults that work with all times
                "The rain drizzles around you.", "Rain drums on the rooftops", "Thunder rumbles in the distance.",
                "The rain continues heavily", "A thunderclap echoes.", "Lightning flashes.", "The storm rages on.",
                "Puddles ripple in the rain."

                "The rain continues through the afternoon."
            ],
            "evening": [
#defaults that work with all times
                "The rain drizzles around you.", "Rain drums on the rooftops", "Muffled thunder rumbles in the distance.",
                "The rain continues heavily", "A thunderclap echoes.", "Lightning flashes.", "The storm rages on.",
"Puddles ripple in the rain."

                "The rain continues in the evening.", "Flashes of lightning illuminate the dark landscape.",
            ],
            "night": [
#defaults that work with all times
                "The rain drizzles around you.", "Rain drums on the rooftops", "Muffled thunder rumbles in the distance.",
                "The rain continues heavily", "A thunderclap echoes.", "Lightning flashes.", "The storm rages on.",
"Puddles ripple in the rain."

                "A lightning strike casts brief, stark light."
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
        "urban": {
            "morning": [
                "Early commuters face rain and thunder, their hurried footsteps splashing on the wet concrete, flinching as thunder cracks."
            ],
            "afternoon": [
                "The city’s pulse slows under the storm’s assault, streets less crowded, as lightning casts sharp, quick shadows among the buildings."
            ],
            "evening": [
                "Rain-soaked streets reflect the city lights, the sounds of thunder blending with the urban hum."
            ],
            "night": [
                "Rain and thunder transform the nighttime city into a scene from a film, every flash of lightning dramatizing the urban architecture."
            ]
        },
        "indoors": {
            "morning": [
                #defaults that work with all times
                "The wind howls from outside.", ""
                "Raindrops patter against the window panes", "The rainfall is relentless, pouring atop the roof.",
                "Muffled thunder rumbles in the distance.", "Rain streaks the windows.", "Sheets of rain cascade down the windows",
                "Raindrops drum against the windows, and race down the glass.",
                "The rain continues.", "A thunderclap echoes from outside.", "Lightning flashes, briefly illuminating the room.", "The storm rages on.",
            ],
            "afternoon": [
                # defaults that work with all times
                "The wind howls from outside.", ""
                                                "Raindrops patter against the window panes",
                "The rainfall is relentless, pouring atop the roof.",
                "Muffled thunder rumbles in the distance.", "Rain streaks the windows.",
                "Sheets of rain cascade down the windows",
                "Raindrops drum against the windows, and race down the glass.",
                "The rain continues.", "A thunderclap echoes from outside.",
                "Lightning flashes, briefly illuminating the room.", "The storm rages on.",
            ],
            "evening": [
                #defaults that work with all times
                "The wind howls from outside.", ""
                "Raindrops patter against the window panes", "The rainfall is relentless, pouring atop the roof.",
                "Muffled thunder rumbles in the distance.", "Rain streaks the windows.", "Sheets of rain cascade down the windows",
                "Raindrops drum against the windows, and race down the glass.",
                "The rain continues.", "A thunderclap echoes from outside.", "Lightning flashes, briefly illuminating the room.", "The storm rages on.",
            ],
            "night": [
                #defaults that work with all times
                "The wind howls from outside.", ""
                "Raindrops patter against the window panes", "The rainfall is relentless, pouring atop the roof.",
                "Muffled thunder rumbles in the distance.", "Rain streaks the windows.", "Sheets of rain cascade down the windows",
                "Raindrops drum against the windows, and race down the glass.",
                "The rain continues.", "A thunderclap echoes from outside.", "Lightning flashes, briefly illuminating the room.", "The storm rages on.",
            ]
        }
    }
}
