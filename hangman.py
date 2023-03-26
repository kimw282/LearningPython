import random

word_list_animals = ('baboon badger bat bear beaver buffalo camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra '
         'ant beetle butterfly bedbug bee bumblebee caterpillar cicada '
         'cockroach cricket dragonfly firefly flea fly gnat grasshopper '
         'hornet junebug ladybug larva lice locust maggot mantis mayfly '
         'mosquito moth roach scarab silkworm silverfish spider stickbug '
         'termite wasp waterbug weevil ').split()

'''
word_list_places = ('Afghanistan Albania Algeria Andorra Angola Argentina Armenia Australia Austria Azerbaijan '
                    'Bahamas Bahrain Bangladesh Barbados Belarus Belgium Belize Benin Bhutan Bolivia Bosnia '
                    'Botswana Brazil Brunei Bulgaria Burma Burundi Cambodia Cameroon Canada Chad Chile China Comoros'
                    'Croatia Cuba Cyprus Czechia Denmark Djibouti Dominica Ecuador Egypt Eritrea Estonia Eswatini '
                    'Ethiopia Fiji Finland France Gabon Georgia Germany Ghana Greece Grenada Guatemala Guinea '
                    'Haiti Honduras Hungary Iceland India Indonesia Iran Iraq Ireland Israel Italy Jamaica Japan '
                    'Jordan Kazakhstan Kenya Kiribati NorthKorea SouthKorea Laos Latvia Lebanon Lesotho Liberia Libya Liechtenstein '
                    'Lithuania Luxembourg Macedonia Madagascar Malawi Malaysia Maldives Mali Malta Mauritania Mauritius '
                    'Mexico Micronesia Moldova Monaco Mongolia Montenegro Morocco Mozambique Namibia Nauru Nepal Netherlands'
                    'NewZealand Nicaragua Niger Nigeria Norway Oman Pakistan Palau Panama PapuaNewGuinea Paraguay Peru Philippines '
                    'Poland Portugal Qatar Romania Russia Rwanda Samoa SaudiArabia Senegal Serbia Seychelles SierraLeone '
                    'Singapore Slovakia Slovenia SolomonIslands Somalia SouthAfrica Spain SriLanka Sudan Suriname Sweden '
                    'Switzerland Syria Tajikistan Tanzania Thailand Togo Tonga Tunisia Turkey Turkmenistan Tuvalu Uganda '
                    'Ukraine UnitedArabEmirates UnitedKingdom England Britain America Uruguay Uzbekistan Vanuatu VaticanCity '
                    'Venezuela Vietnam Yemen Zambia Zimbabwe '
                    '').split()
'''

word_list_misc = ('about, above, abuse, accept, accident, accuse, across, activist, actor, administration, '
                  'admit, adult, advertise, advise, affect, afraid, after, again, against, agency, aggression, '
                  'agree, agriculture, force, airplane, airport, album, alcohol, alive, almost, alone, along, '
                  'already, although, always, ambassador, amend, ammunition, among, amount, anarchy, ancestor, '
                  'ancient, anger, animal, anniversary, announce, another, answer, apologize, appeal, appear, '
                  'appoint, approve, archeology, argue, around, arrest, arrive, artillery, assist, astronaut, '
                  'astronomy, asylum, atmosphere, attach, attack, attempt, attend, attention, automobile, autumn, '
                  'available, average, avoid, awake, award, balance, balloon, ballot, barrier, battle, beauty, because, '
                  'become, before, begin, behavior, behind, believe, belong, below, betray, better, between, biology, '
                  'black, blame, bleed, blind, block, blood, border, borrow, bottle, bottom, boycott, brain, brave, '
                  'bread, break, breathe, bridge, brief, bright, bring, broadcast, brother, brown, budget, build, '
                  'building, bullet, burst, business, cabinet, camera, campaign, cancel, cancer, candidate, capital, '
                  'capture, career, careful, carry, catch, cause, ceasefire, celebrate, center, century, ceremony, '
                  'chairman, champion, chance, change, charge, chase, cheat, cheer, chemicals, chemistry, chief, child, '
                  'children, choose, circle, citizen, civilian, civil, rights, claim, clash, class, clean, clear, clergy, '
                  'climate, climb, clock, close, cloth, clothes, cloud, coalition, coast, coffee, collapse, collect, college, '
                  'colony, color, combine, command, comment, committee, common, communicate, community, company, compare, '
                  'compete, complete, complex, compromise, computer, concern, condemn, condition, conference, confirm, '
                  'conflict, congratulate, Congress, connect, conservative, consider, constitution, contact, contain, '
                  'container, continent, continue, control, convention, cooperate, correct, corruption, cotton, count, '
                  'country, court, cover, crash, create, creature, credit, crime, criminal, crisis, criticize, crops, '
                  'cross, crowd, crush, culture, curfew, current, custom, customs, damage, dance, danger, daughter, '
                  'debate, decide, declare, decrease, defeat, defend, deficit, define, degree, delay, delegate, demand, '
                  'democracy, demonstrate, denounce, depend, deplore, deploy, depression, describe, desert, design, '
                  'desire, destroy, detail, detain, develop, device, dictator, different, difficult, dinner, diplomat, '
                  'direct, direction, disappear, disarm, disaster, discover, discrimination, discuss, disease, dismiss, '
                  'dispute, dissident, distance, divide, doctor, document, dollar, donate, double, dream, drink, drive, '
                  'drown, during, early, earth, earthquake, ecology, economy, education, effect, effort, either, elect, '
                  'electricity, embassy, embryo, emergency, emotion, employ, empty, enemy, energy, enforce, engine, '
                  'engineer, enjoy, enough, enter, environment, equal, equipment, escape, especially, establish, estimate, '
                  'ethnic, evaporate, event, every, evidence, exact, examine, example, excellent, except, exchange, excuse, '
                  'execute, exercise, exile, exist, expand, expect, expel, experience, experiment, expert, explain, explode, '
                  'explore, export, express, extend, extra, extraordinary, extreme, extremist, factory, false, family, famous, '
                  'father, favorite, federal, female, fence, fertile, field, fierce, fight, final, financial, finish, fireworks, '
                  'first, float, flood, floor, flower, fluid, follow, force, foreign, forest, forget, forgive, former, '
                  'forward, freedom, freeze, fresh, friend, frighten, front, fruit, funeral, future, gather, general, '
                  'generation, genocide, gentle, glass, goods, govern, government, grain, grass, great, green, grind, ground, '
                  'group, guarantee, guard, guerrilla, guide, guilty, happen, happy, harvest, headquarters, health, heavy, '
                  'helicopter, hijack, history, holiday, honest, honor, horrible, horse, hospital, hostage, hostile, hotel, '
                  'house, however, human, humor, hunger, hurry, husband, identify, ignore, illegal, imagine, immediate, '
                  'immigrant, import, important, improve, incident, incite, include, increase, independent, individual, '
                  'industry, infect, inflation, influence, inform, information, inject, injure, innocent, insane, insect, '
                  'inspect, instead, instrument, insult, intelligence, intelligent, intense, interest, interfere, international, '
                  'Internet, intervene, invade, invent, invest, investigate, invite, involve, island, issue, jewel, joint, '
                  'judge, justice, kidnap, knife, knowledge, labor, laboratory, language, large, laugh, launch, learn, leave, '
                  'legal, legislature, letter, level, liberal, light, lightning, limit, liquid, listen, literature, little, '
                  'local, lonely, loyal, machine, magazine, major, majority, manufacture, march, market, marry, material, '
                  'mathematics, matter, mayor, measure, media, medicine, member, memorial, memory, mental, message, metal, '
                  'method, microscope, middle, militant, military, militia, mineral, minister, minor, minority, minute, '
                  'missile, missing, mistake, model, moderate, modern, money, month, moral, morning, mother, motion, mountain, '
                  'mourn, movement, movie, murder, music, mystery, narrow, nation, native, natural, nature, necessary, '
                  'negotiate, neighbor, neither, neutral, never, night, noise, nominate, normal, north, nothing, nowhere, '
                  'nuclear, number, object, observe, occupy, ocean, offensive, offer, office, officer, official, often, '
                  'operate, opinion, oppose, opposite, oppress, orbit, order, organize, other, overthrow, paint, paper, '
                  'parachute, parade, pardon, parent, parliament, partner, party, passenger, passport, patient, peace, '
                  'people, percent, perfect, perform, period, permanent, permit, person, persuade, physical, physics, '
                  'picture, piece, pilot, place, planet, plant, plastic, please, plenty, point, poison, police, policy, '
                  'politics, pollute, popular, population, position, possess, possible, postpone, poverty, power, praise, '
                  'predict, pregnant, present, president, press, pressure, prevent, price, prison, private, prize, probably, '
                  'problem, process, produce, profession, professor, profit, program, progress, project, promise, propaganda, '
                  'property, propose, protect, protest, prove, provide, public, publication, publish, punish, purchase, purpose, '
                  'quality, question, quick, quiet, radar, radiation, radio, railroad, raise, reach, react, ready, realistic, '
                  'reason, reasonable, rebel, receive, recent, recession, recognize, record, recover, reduce, reform, refugee, '
                  'refuse, register, regret, reject, relations, release, religion, remain, remains, remember, remove, repair, '
                  'repeat, report, represent, repress, request, require, rescue, research, resign, resist, resolution, '
                  'resource, respect, responsible, restaurant, restrain, restrict, result, retire, return, revolt, right, '
                  'river, rocket, rough, round, rubber, rural, sabotage, sacrifice, sailor, satellite, satisfy, school, '
                  'science, search, season, second, secret, security, seeking, seize, Senate, sense, sentence, separate, '
                  'series, serious, serve, service, settle, several, severe, shake, shape, share, sharp, sheep, shell, '
                  'shelter, shine, shock, shoot, short, should, shout, shrink, sickness, signal, silence, silver, similar, '
                  'simple, since, single, sister, situation, skeleton, skill, slave, sleep, slide, small, smash, smell, smoke, '
                  'smooth, social, soldier, solid, solve, sound, south, space, speak, special, speech, speed, spend, spill, '
                  'spirit, split, sport, spread, spring, square, stand, start, starve, state, station, statue, steal, steam, '
                  'steel, stick, still, stone, store, storm, story, stove, straight, strange, street, stretch, strike, strong, '
                  'structure, struggle, study, stupid, subject, submarine, substance, substitute, subversion, succeed, sudden, '
                  'suffer, sugar, suggest, suicide, summer, supervise, supply, support, suppose, suppress, surface, surplus, '
                  'surprise, surrender, surround, survive, suspect, suspend, swallow, swear, sweet, sympathy, system, target, '
                  'taste, teach, technical, technology, telephone, telescope, television, temperature, temporary, tense, '
                  'terrible, territory, terror, terrorist, thank, theater, theory, there, these, thick, thing, think, third, '
                  'threaten, through, throw, tired, today, together, tomorrow, tonight, torture, total, touch, toward, trade, '
                  'tradition, traffic, tragic, train, transport, transportation, travel, treason, treasure, treat, treatment, '
                  'treaty, trial, tribe, trick, troops, trouble, truce, truck, trust, under, understand, unite, universe, '
                  'university, unless, until, urgent, usual, vacation, vaccine, valley, value, vegetable, vehicle, version, '
                  'victim, victory, video, village, violate, violence, visit, voice, volcano, volunteer, wages, waste, watch, '
                  'water, wealth, weapon, weather, weigh, welcome, wheat, wheel, where, whether, which, while, white, whole, '
                  'willing, window, winter, withdraw, without, witness, woman, wonder, wonderful, world, worry, worse, worth, '
                  'wound, wreck, wreckage, write, wrong, yellow, yesterday, young').split(", ")

# word_list = [word_list_animals, word_list_places, word_list_misc]
word_list = [word_list_animals, word_list_misc]

'''
hangman_pics = ["\n\n", "\n\n\n\n\n\n=========", 
        "\n      |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 
'''
hangman_pics = ["\n\n", "\n\n\n\n\n\n=========", 
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 

# Hangman Ascii Art from : https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c


def main():
    restart_game = "yes"
    
    print('''
==============================================================

*     *     *     *    *     ****   *     *     *     *    *
*     *    * *    **   *   **   *   **   **    * *    **   *
*     *    * *    * *  *  *         * * * *    * *    * *  *
*******   *****   *  * *  *   ****  *  *  *   *****   *  * *
*     *  *     *  *   **   **   **  *     *  *     *  *   **
*     *  *     *  *    *    *****   *     *  *     *  *    *

==============================================================

''')

    while restart_game != "no" and restart_game != "n":
        stop_flag = False
        while not stop_flag:
            theme = input("\nChoose theme: Input number or press Enter for random\n 1) Animals and Bugs"
                          "\n 2) Miscellaneous Words\n\n")
            if theme in ["1", "2"]:
                random_word = random.choice(word_list[int(theme) - 1])
                stop_flag = True
            elif theme == "":
                random_word = random.choice(random.choice(word_list))
                stop_flag = True
            else:
                print("\nInvalid input")
        
        guessed_words = []
        word = len(random_word)*"_ "
        i = 0
        guess_word = word.split()

        while i < 8:
            if word == " ".join(list(random_word)):
                print(f"\nYou win! The word is {random_word}.")
                break
            print(f"\n\n{word}")
            print(f"\nGuessed: {', '.join(sorted(guessed_words))}")
            # Prompts player to input their guess
            player_guess = str(input("\nInput guess: ")).lower()
            # If player's guess is the word
            if player_guess == random_word.lower():
                print(f"\nYou win! The word is {random_word}.")
                break
            # If player enters character or word that has already been guessed
            elif player_guess in guessed_words:
                print("\nChoose something new!")
            # If player enters valid response (one alphabet)
            elif player_guess.isalpha():
                # If player's guess is in the word
                if player_guess in random_word.lower():
                    # In order to ensure repeating characters
                    for num in range(len(random_word)):
                        if player_guess == random_word[num].lower():
                            guess_word[num] = player_guess
                            word = " ".join(guess_word)
                # If player's guess is not in the word
                else:
                    i += 1
                    # Prints hangman image
                    print(f"\n{player_guess} is not right!\n\n{hangman_pics[i]}.")
                guessed_words.append(player_guess)
            # If player enters invalid response
            else:
                print("\nInvalid input")
        if i == 8:
            print(f"\n\nBoo! You Lost!\nThe word is {random_word}")
        restart_game = input("\n\nRestart Game? [y/n]\n").lower().strip()
    if restart_game == "no" or restart_game == "n":
        print("\nThanks for playing! (＾∀＾）ゞ\n")


if __name__ == "__main__":
    main()