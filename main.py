#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "0794D1DA-626C-4335-9A6D-8CE540E3F945",
  "name": "Project 01",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631383960380,
  "passages": [
    {
      "name": "Abandoned Steel Mill",
      "tags": "",
      "id": "1",
      "text": "After taking a dare at a party, You find yourself in front of the Abandoned Steel Mill with many of the party goers yelling for you to go ahead. You see most of it's windows are broken, and it's walls barely standing, and in some sections the Roof caved in. \n\n[[LEFT->Broken Window]]\n[[RIGHT->Fire escape]]\n[[TURN BACK->Head back to the party and lose your dare]]",
      "links": [
        {
          "linkText": "LEFT",
          "passageName": "Broken Window",
          "original": "[[LEFT->Broken Window]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Fire escape",
          "original": "[[RIGHT->Fire escape]]"
        },
        {
          "linkText": "TURN BACK",
          "passageName": "Head back to the party and lose your dare",
          "original": "[[TURN BACK->Head back to the party and lose your dare]]"
        }
      ],
      "hooks": [],
      "cleanText": "After taking a dare at a party, You find yourself in front of the Abandoned Steel Mill with many of the party goers yelling for you to go ahead. You see most of it's windows are broken, and it's walls barely standing, and in some sections the Roof caved in."
    },
    {
      "name": "Broken Window",
      "tags": "",
      "id": "2",
      "score":2,
      "text": "You headed left and find a broken window, that if you are careful enough, will get you into the building.\n\n[[WEST->The First Floor]]\n[[BACK->Abandoned Steel Mill]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "The First Floor",
          "original": "[[WEST->The First Floor]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Abandoned Steel Mill",
          "original": "[[BACK->Abandoned Steel Mill]]"
        }
      ],
      "hooks": [],
      "cleanText": "You headed left and find a broken window, that if you are careful enough, will get you into the building."
    },
    {
      "name": "Fire escape",
      "tags": "",
      "id": "3",
      "score":2,
      "text": "You turned right and head towards a what looks like a fire escape. You can tell just by looking at it that it could collaspe at any moment. \n\n[[UP->Second Floor Hallway]]\n[[BACK->Abandoned Steel Mill]]",
      "links": [
        {
          "linkText": "UP",
          "passageName": "Second Floor Hallway",
          "original": "[[UP->Second Floor Hallway]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Abandoned Steel Mill",
          "original": "[[BACK->Abandoned Steel Mill]]"
        }
      ],
      "hooks": [],
      "cleanText": "You turned right and head towards a what looks like a fire escape. You can tell just by looking at it that it could collaspe at any moment."
    },
    {
      "name": "Head back to the party and lose your dare",
      "tags": "",
      "id": "4",
      "score":50,
      "text": "You headed back to the party and lost your dare. Having been laughed at for coming back, you are now more curious about what might have happened if you hadn't come back. . . To Try Again Please type \"Quit\"",
      "links": [],
      "hooks": [],
      "cleanText": "You headed back to the party and lost your dare. Having been laughed at for coming back, you are now more curious about what might have happened if you hadn't come back. . . To Try Again Please type \"Quit\""
    },
    {
      "name": "Second Floor Hallway",
      "tags": "",
      "id": "5",
      "score":10,
      "text": "As soon as you step inside the building, the fire escape collapses. You say to yourself \"Looks like I'm finding a different way out.\". You see to your right what looks to be a set of stairs leading to the First Floor and to your left the hallway continues behind a corner. \n\n[[WEST->F2 Entrance to Foundry]]\n[[RIGHT->Stairs to F1]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "F2 Entrance to Foundry",
          "original": "[[WEST->F2 Entrance to Foundry]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Stairs to F1",
          "original": "[[RIGHT->Stairs to F1]]"
        }
      ],
      "hooks": [],
      "cleanText": "As soon as you step inside the building, the fire escape collapses. You say to yourself \"Looks like I'm finding a different way out.\". You see to your right what looks to be a set of stairs leading to the First Floor and to your left the hallway continues behind a corner."
    },
    {
      "name": "The First Floor",
      "tags": "",
      "id": "6",
      "score":10,
      "text": "You headed through the window and, while only managing to cut you hand when you landed, make it through successfully. After wrapping your hand using your jacket, You noticed you ended up in the break room. Using your phone as a Flashlight, you see it is filled with broken tables and chairs and the corner to you right being covered in rubble. You see a note on one of the tables and you also notice the door that leads to the hallway.\n\n[[FORWARD->F1 Hallway]]\n[[RIGHT->Note]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "F1 Hallway",
          "original": "[[FORWARD->F1 Hallway]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Note",
          "original": "[[RIGHT->Note]]"
        }
      ],
      "hooks": [],
      "cleanText": "You headed through the window and, while only managing to cut you hand when you landed, make it through successfully. After wrapping your hand using your jacket, You noticed you ended up in the break room. Using your phone as a Flashlight, you see it is filled with broken tables and chairs and the corner to you right being covered in rubble. You see a note on one of the tables and you also notice the door that leads to the hallway."
    },
    {
      "name": "F1 Hallway",
      "tags": "",
      "id": "7",
      "score":2,
      "text": "Heading out to the hall, you see to your left a dim light coming from, what you can make out from a sign on the wall, the foundry and to your right a way back to the entrance. You also can't shake the feeling of being watched.\n\n[[RIGHT->Entrance]]\n[[LEFT->Foundry Door]]",
      "links": [
        {
          "linkText": "RIGHT",
          "passageName": "Entrance",
          "original": "[[RIGHT->Entrance]]"
        },
        {
          "linkText": "LEFT",
          "passageName": "Foundry Door",
          "original": "[[LEFT->Foundry Door]]"
        }
      ],
      "hooks": [],
      "cleanText": "Heading out to the hall, you see to your left a dim light coming from, what you can make out from a sign on the wall, the foundry and to your right a way back to the entrance. You also can't shake the feeling of being watched."
    },
    {
      "name": "Entrance",
      "tags": "",
      "id": "8",
      "score":2,
      "text": "You see you are in the front lobby of the Steel mill. The other hall is completely blocked off by a gate and then see the front door.\n\n[[FORWARD->Front Door]]\n[[BACK->F1 Hallway]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Front Door",
          "original": "[[FORWARD->Front Door]]"
        },
        {
          "linkText": "BACK",
          "passageName": "F1 Hallway",
          "original": "[[BACK->F1 Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "You see you are in the front lobby of the Steel mill. The other hall is completely blocked off by a gate and then see the front door."
    },
    {
      "name": "Foundry Door",
      "tags": "",
      "id": "9",
      "score":2,
      "text": "You get the foundry door and see where the light is coming from. It seems to be coming from one of the forges. You say to yourself \"Thats impossible. This place has been close for years.\".\n\n[[BACK->F1 Hallway]]\n[[FORWARD->Foundry]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "F1 Hallway",
          "original": "[[BACK->F1 Hallway]]"
        },
        {
          "linkText": "FORWARD",
          "passageName": "Foundry",
          "original": "[[FORWARD->Foundry]]"
        }
      ],
      "hooks": [],
      "cleanText": "You get the foundry door and see where the light is coming from. It seems to be coming from one of the forges. You say to yourself \"Thats impossible. This place has been close for years.\"."
    },
    {
      "name": "Front Door",
      "tags": "",
      "id": "10",
      "score":5,
      "text": "You walk towards the front doors and see one set of the doors isn't barricaded. You wonder why someone would have barricaded all but one set. Just to see, you try the door but it doesn't budge, which makes this even stranger.\n\n[[BACK->Entrance]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Entrance",
          "original": "[[BACK->Entrance]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk towards the front doors and see one set of the doors isn't barricaded. You wonder why someone would have barricaded all but one set. Just to see, you try the door but it doesn't budge, which makes this even stranger."
    },
    {
      "name": "Foundry",
      "tags": "",
      "id": "11",
      "score":2,
      "text": "You head through the door but as soon as it shuts you hear its locks shift and engage. Now you find yourself locked in the Foundry and using the dim light from the Forge to your left, you see a set of stairs on the other side that lead to the walkways up above you. \n\n[[LEFT->Forge]]\n[[FORWARD->Stairs]]",
      "links": [
        {
          "linkText": "LEFT",
          "passageName": "Forge",
          "original": "[[LEFT->Forge]]"
        },
        {
          "linkText": "FORWARD",
          "passageName": "Stairs",
          "original": "[[FORWARD->Stairs]]"
        }
      ],
      "hooks": [],
      "cleanText": "You head through the door but as soon as it shuts you hear its locks shift and engage. Now you find yourself locked in the Foundry and using the dim light from the Forge to your left, you see a set of stairs on the other side that lead to the walkways up above you."
    },
    {
      "name": "Forge",
      "tags": "",
      "id": "12",
      "score":5,
      "text": "As you reach the forge you see that not only is this one is the only one on but the molten metal its melting down isn't flowing into the channel like it should be. On a closer look, it seems to be going down a channel that goes through the floor near a huge hole. The hole doesn't have much in it but as the forge bubbled for a second you swore you saw someone down there.\n\n[[BACK->Foundry]]\n[[RIGHT->Stairs]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Foundry",
          "original": "[[BACK->Foundry]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Stairs",
          "original": "[[RIGHT->Stairs]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you reach the forge you see that not only is this one is the only one on but the molten metal its melting down isn't flowing into the channel like it should be. On a closer look, it seems to be going down a channel that goes through the floor near a huge hole. The hole doesn't have much in it but as the forge bubbled for a second you swore you saw someone down there."
    },
    {
      "name": "Stairs",
      "tags": "",
      "id": "13",
      "score":5,
      "text": "On your way to the stairs, you hear something move behind you. You pick up the pace just in time because as soon as hit the stairs, whatever you heard move just started running towards you! You bolt up the stairs and get on to the walkway. You see a door straight ahead but only two paths, one to the right and left.\n\n[[LEFT->Captured Ending 1]]\n[[RIGHT->Right Path]]",
      "links": [
        {
          "linkText": "LEFT",
          "passageName": "Captured Ending 1",
          "original": "[[LEFT->Captured Ending 1]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Right Path",
          "original": "[[RIGHT->Right Path]]"
        }
      ],
      "hooks": [],
      "cleanText": "On your way to the stairs, you hear something move behind you. You pick up the pace just in time because as soon as hit the stairs, whatever you heard move just started running towards you! You bolt up the stairs and get on to the walkway. You see a door straight ahead but only two paths, one to the right and left."
    },
    {
      "name": "Right Path",
      "tags": "",
      "id": "14",
      "score":10,
      "text": "You take the right path without a second thought. You get to the door as the right path collapses behind you and see the creature starting to climb up the broken walkway. You head through the door and seal it. You look around and see the hall has a corner and continues beyond. \n\n[[FORWARD->Escape Ending 1]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Escape Ending 1",
          "original": "[[FORWARD->Escape Ending 1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You take the right path without a second thought. You get to the door as the right path collapses behind you and see the creature starting to climb up the broken walkway. You head through the door and seal it. You look around and see the hall has a corner and continues beyond."
    },
    {
      "name": "F2 Entrance to Foundry",
      "tags": "",
      "id": "15",
      "score":5,
      "text": "You get through the hallway and see a big metal door. As you get closer you see it is to the Foundry and you can see that one of the Forges is working. You say to yourself \"I thought this place was abandoned years ago?\" Even thought you read a hand written note on the door that says \"STAY OUT\", you decide to head into the Foundry because it seems to be your only way out.\n\n[[FORWARD->Catwalk]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Catwalk",
          "original": "[[FORWARD->Catwalk]]"
        }
      ],
      "hooks": [],
      "cleanText": "You get through the hallway and see a big metal door. As you get closer you see it is to the Foundry and you can see that one of the Forges is working. You say to yourself \"I thought this place was abandoned years ago?\" Even thought you read a hand written note on the door that says \"STAY OUT\", you decide to head into the Foundry because it seems to be your only way out."
    },
    {
      "name": "Stairs to F1",
      "tags": "",
      "id": "16",
      "score":2,
      "text": "As you head down the steps, you head down the hallway and see you ended up at the Lobby area but you can't get through due to a gate in the way.\n\n[[BACK->Second Floor Hallway]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Second Floor Hallway",
          "original": "[[BACK->Second Floor Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you head down the steps, you head down the hallway and see you ended up at the Lobby area but you can't get through due to a gate in the way."
    },
    {
      "name": "Catwalk",
      "tags": "",
      "id": "17",
      "score":2,
      "text": "When you get out on the Catwalk, you hear the doors lock engage behind you. You look around using the faint light the Forge is letting off and see two paths in front of you to get to the stairs. The path to the left is obviously not gonna work, it has a giant hole in it! The path the right isn't in much better shape but you should be able get to the stairs this way.\n\n[[DOWN->Foundry Main Level]]",
      "links": [
        {
          "linkText": "DOWN",
          "passageName": "Foundry Main Level",
          "original": "[[DOWN->Foundry Main Level]]"
        }
      ],
      "hooks": [],
      "cleanText": "When you get out on the Catwalk, you hear the doors lock engage behind you. You look around using the faint light the Forge is letting off and see two paths in front of you to get to the stairs. The path to the left is obviously not gonna work, it has a giant hole in it! The path the right isn't in much better shape but you should be able get to the stairs this way."
    },
    {
      "name": "Foundry Main Level",
      "tags": "",
      "id": "18",
      "score":5,
      "text": "Once on the main level for the Foundry, you can tell that something isn't right. You look towards the forge and see something crawling on it but can tell it hasn't noticed you yet. You see the door on the other side of Foundry. You think you can make a break for it but maybe if you take if slow you can get through without it seeing you.\n\n[[FAST->Captured ending 2]]\n[[SLOW->Door]]",
      "links": [
        {
          "linkText": "FAST",
          "passageName": "Captured Ending 2",
          "original": "[[FAST->Captured Ending 2]]"
        },
        {
          "linkText": "SLOW",
          "passageName": "Door",
          "original": "[[SLOW->Door]]"
        }
      ],
      "hooks": [],
      "cleanText": "Once on the main level for the Foundry, you can tell that something isn't right. You look towards the forge and see something crawling on it but can tell it hasn't noticed you yet. You see the door on the other side of Foundry. You think you can make a break for it but maybe if you take if slow you can get through without it seeing you."
    },
    {
      "name": "Captured Ending 2",
      "tags": "",
      "id": "19",
      "score":20,
      "text": "You decided to run towards the door but within a few steps you were caught. The creature takes you toward a hole near the Forge and throws you down before following.  You see bone piles and a pile of decomposing parts. As you begin to scream it uses the molten metal to cover and cook you and makes a tasty dinner. . .",
      "links": [],
      "hooks": [],
      "cleanText": "You decided to run towards the door but within a few steps you were caught. The creature takes you toward a hole near the Forge and throws you down before following.  You see bone piles and a pile of decomposing parts. As you begin to scream it uses the molten metal to cover and cook you and makes a tasty dinner. . ."
    },
    {
      "name": "Door",
      "tags": "",
      "id": "20",
      "score":2, 
      "text": "You decided to take it slow. You make it through the room just fine but as you open the door to the First Floor Hallway, it lets out a loud creak! This cathes the thing's attention and you head through and shut the door behind you. You hear it screaming and climbing all over the walls until it stops. You notice the Lobby at the other side and a Break room on the right side of the hall. \n\n[[RIGHT->Break Room]]\n[[FORWARD->Lobby]]",
      "links": [
        {
          "linkText": "RIGHT",
          "passageName": "Break Room",
          "original": "[[RIGHT->Break Room]]"
        },
        {
          "linkText": "FORWARD",
          "passageName": "Lobby",
          "original": "[[FORWARD->Lobby]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to take it slow. You make it through the room just fine but as you open the door to the First Floor Hallway, it lets out a loud creak! This cathes the thing's attention and you head through and shut the door behind you. You hear it screaming and climbing all over the walls until it stops. You notice the Lobby at the other side and a Break room on the right side of the hall."
    },
    {
      "name": "Captured Ending 1",
      "tags": "",
      "id": "21",
      "score":20,
      "text": "You head left but halfway through you fall through a big hole! You hit the ground hard and fast. You can't get up and the creature gets to you before you can even react. The creature takes you toward a hole near the Forge and throws you down before following. You see bone piles and a pile of decomposing parts. As you begin to scream it uses the molten metal to cover and cook you and makes a tasty dinner. . .",
      "links": [],
      "hooks": [],
      "cleanText": "You head left but halfway through you fall through a big hole! You hit the ground hard and fast. You can't get up and the creature gets to you before you can even react. The creature takes you toward a hole near the Forge and throws you down before following. You see bone piles and a pile of decomposing parts. As you begin to scream it uses the molten metal to cover and cook you and makes a tasty dinner. . ."
    },
    {
      "name": "Break Room",
      "tags": "",
      "id": "22",
      "score":5,
      "text": "You go into the Break Room and see the window you could have come through earlier. Using your Phone Flashlight you see its filled with broken tables and chairs, and in the far right corner, a pile of rubble from a huge hole in the ceiling. Knowing no other way out, You take the window.\n\n[[FORWARD->Escape Ending 2]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Escape Ending 2",
          "original": "[[FORWARD->Escape Ending 2]]"
        }
      ],
      "hooks": [],
      "cleanText": "You go into the Break Room and see the window you could have come through earlier. Using your Phone Flashlight you see its filled with broken tables and chairs, and in the far right corner, a pile of rubble from a huge hole in the ceiling. Knowing no other way out, You take the window."
    },
    {
      "name": "Lobby",
      "tags": "",
      "id": "23",
      "score":2,
      "text": "You head towards the Lobby and see the only door that isn't barricaded by weird looking steel formations and the hallway you were at earlier. You go and try the door but it doesn't budge. Thats when you realize its not just to keep whatever that thing is inside but also anyone who is dumb enough to enter the building.\n\n[[BACK->Break Room]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Break Room",
          "original": "[[BACK->Break Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You head towards the Lobby and see the only door that isn't barricaded by weird looking steel formations and the hallway you were at earlier. You go and try the door but it doesn't budge. Thats when you realize its not just to keep whatever that thing is inside but also anyone who is dumb enough to enter the building."
    },
    {
      "name": "Escape Ending 2",
      "tags": "",
      "id": "24",
      "score":50,
      "text": "As you head to the window to finally get out, you hear the thing break something far back in the ceiling. As you get closer to the window and see its head emerge from the ceiling, you see it has an almost spider like face. You run and jump through the window and successfully escape! You see your friends and run towards them and explain everything. They bust up laughing until they here a screech from the building. You all load up into the van and leave. The only thought in your mind is to how you shouldn't have gone to the party.",
      "links": [],
      "hooks": [],
      "cleanText": "As you head to the window to finally get out, you hear the thing break something far back in the ceiling. As you get closer to the window and see its head emerge from the ceiling, you see it has an almost spider like face. You run and jump through the window and successfully escape! You see your friends and run towards them and explain everything. They bust up laughing until they here a screech from the building. You all load up into the van and leave. The only thought in your mind is to how you shouldn't have gone to the party."
    },
    {
      "name": "Escape Ending 1",
      "tags": "",
      "id": "25",
      "score":50,
      "text": "As you head through the hall you hear the a door hit the ground! Then you hear the thing behind you! As you see the fire escape, you turn and see its body. Because of all the windows and Moon shining you see it looks like a huge mutated spider! You head down the fire escape and get away just in time! You head to your friends and explain. They are more concerned with the bloody hand until they hear something screech in the Builing. You all load in the van and head back. You only think about how something like that can exsist. . . or what it will do now that it seems to be free.",
      "links": [],
      "hooks": [],
      "cleanText": "As you head through the hall you hear the a door hit the ground! Then you hear the thing behind you! As you see the fire escape, you turn and see its body. Because of all the windows and Moon shining you see it looks like a huge mutated spider! You head down the fire escape and get away just in time! You head to your friends and explain. They are more concerned with the bloody hand until they hear something screech in the Builing. You all load in the van and head back. You only think about how something like that can exsist. . . or what it will do now that it seems to be free."
    },
    {
      "name": "Note",
      "tags": "",
      "id": "26",
      "score":5,
      "text": "You go towards the note and see it is mostly torn with only one word left on it. The word is \"Run\". It freaks you out but you also remember hearing stories of plenty of people exploring the place so it could just be a trick.\n\n[[BACK->The First Floor]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "The First Floor",
          "original": "[[BACK->The First Floor]]"
        }
      ],
      "hooks": [],
      "cleanText": "You go towards the note and see it is mostly torn with only one word left on it. The word is \"Run\". It freaks you out but you also remember hearing stories of plenty of people exploring the place so it could just be a trick."
    }
  ]
}


# ----------------------------------------------------------------


def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------


def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Moves: {} , Score: {}".format(moves, score))
		print("You are at the " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			
			if link["linkText"] == response:
				return link["passageName"]
  
	print("I don't understand what you are trying to do. Try again.")
	return location_label

# ----------------------------------------------------------------
print("The general command options are: left, right, forward, back, up, down, slow and fast")
location_label = "Abandoned Steel Mill"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves += 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score, moves)
	response = get_input()

if current_location == "Captured Ending 1":
  print("You have failed in escaping the monster and the Steel Mill. . . To try again, type 'QUIT' and run again.")
if current_location == "Captured Ending 2":
  print("You have failed in escaping the monster and the Steel Mill. . . To try again, type 'QUIT' and run again.")
if current_location == "Escape Ending 1":
  print("You have escaped the Steel Mill! Great Job!")
if current_location == "Escape Ending 2":
  print("You have escaped the Steel Mill! Great Job!")

print("Thanks for playing!")