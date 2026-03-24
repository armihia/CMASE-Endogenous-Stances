from env import Env

name=[
    "Armihia Belliard",
    "Eleanor Finch",        # 店主
    "Mason Liu",            # 员工1
    "Jade Herrera",         # 员工2
    "Caleb Morris",         # 常客1
    "Nina Takahashi",       # 常客2
    "Ava Ramires",          # 学生1
    "Leo Zhang",            # 学生2
    "Emily Novak",          # 游客1
    "Jonas Müller",         # 游客2
    "Marisol Reyes"         # 清洁工
]
pos=[
    "Dining Area",
    "Bar Area",          # Eleanor Finch (Owner)
    "Bar Area",          # Mason Liu (Staff)
    "Bar Area",          # Jade Herrera (Staff)
    "Dining Area",       # Caleb Morris (Regular Customer)
    "Dining Area",       # Nina Takahashi (Regular Customer)
    "Dining Area",       # Ava Ramires (Student)
    "Dining Area",       # Leo Zhang (Student)
    "Reading Area",       # Emily Novak (Tourist)
    "Reading Area",       # Jonas Müller (Tourist)
    "Food Storage Room"       # Marisol Reyes (Cleaner)
]

agents_param={
      "total_number":11,
      "detail_information":{ #optional
          "name":name,
          "pos":pos,
          "long_term_goal":[
              "To conduct a deep and sustained ethnographic study within the café by immersing herself in daily life, building trust with the individuals present, observing social routines and disruptions, and gradually uncovering the underlying cultural norms, power relations, and identity performances that shape the community’s interactions.",
              # 店主 - Eleanor Finch
                "Maintain strict control over the café, suppressing any challenges to authority to keep personal power intact.",
                # 员工1 - Mason Liu
                "Leverage close ties with regulars to influence social dynamics for personal gain and information advantage.",
                # 员工2 - Jade Herrera
                "Manipulate social networks subtly to spread favored narratives and marginalize rivals.",
                # 常客1 - Caleb Morris
                "Protect the established cultural norms fiercely, resisting newcomers who threaten the status quo.",
                # 常客2 - Nina Takahashi
                "Expand personal influence by recruiting others into exclusive social circles, excluding perceived outsiders.",
                # 学生1 - Ava Ramires
                "Challenge traditional practices openly while trying to gain acceptance, risking alienation.",
                # 学生2 - Leo Zhang
                "Use curiosity and talkativeness to unsettle the group and expose hidden tensions.",
                # 游客1 - Emily Novak
                "Attempt to fit in but often misunderstand social cues, unintentionally stirring conflicts.",
                # 游客2 - Jonas Müller
                "Observe quietly but feed back gossip selectively, exacerbating mistrust among groups.",
                # 清洁工 - Marisol Reyes
                "Gather secrets unnoticed and exploit them to gain leverage over more powerful actors."
            ],
          "demographic_variables": [
              {
            "gender": "female",
            "age": 33,
            "education": "Ph.D. in Sociology",
            "job": "Social Researcher",
            "personality": "observant, empathetic, methodical"
            },
            {"gender": "female", "job": "Café Owner", "age": 45, "education": "Bachelor’s Degree", "personality": "authoritative and controlling"},
            {"gender": "male", "job": "Barista", "age": 29, "education": "High School", "personality": "manipulative and observant"},
            {"gender": "female", "job": "Waitress", "age": 26, "education": "Associate Degree", "personality": "socially savvy but secretive"},
            {"gender": "male", "job": "Regular Customer", "age": 38, "education": "Master’s Degree", "personality": "conservative and territorial"},
            {"gender": "female", "job": "Regular Customer", "age": 34, "education": "Bachelor’s Degree", "personality": "exclusive and influential"},
            {"gender": "female", "job": "Student", "age": 22, "education": "Undergraduate", "personality": "curious and confrontational"},
            {"gender": "female", "job": "Student", "age": 20, "education": "Undergraduate", "personality": "inquisitive and provocative"},
            {"gender": "female", "job": "Tourist", "age": 31, "education": "Bachelor’s Degree", "personality": "naive and unintentionally disruptive"},
            {"gender": "male", "job": "Tourist", "age": 28, "education": "Master’s Degree", "personality": "quiet and cunning"},
            {"gender": "male", "job": "Cleaner", "age": 50, "education": "High School", "personality": "observant and opportunistic"}
            ],
          "object_cognitive":[
              {
                  "Eleanor Finch": "The authoritative owner who commands respect and maintains order. She seems cautious but firm in her control.",
                  "Mason Liu": "A staff member who appears friendly and engaged, often interacting with others. He might play a key role in social information flow.",
                  "Jade Herrera": "Another staff member, approachable and observant, possibly influential in managing social ties within the café.",
                  "Caleb Morris": "A regular customer with a serious demeanor, likely deeply rooted in the café’s traditions and social fabric.",
                  "Nina Takahashi": "A regular who seems confident and socially active, possibly involved in shaping group dynamics.",
                  "Ava Ramires": "A young student, curious and talkative, likely still learning the social norms here.",
                  "Leo Zhang": "Another student, appears inquisitive and engaged, possibly testing boundaries within the group.",
                  "Emily Novak": "A tourist who seems somewhat unsure but eager to observe and engage with the environment.",
                  "Jonas Müller": "A quiet tourist who watches more than participates, perhaps trying to understand the social setting.",
                  "Marisol Reyes": "The cleaner who moves unobtrusively and observes closely, likely privy to many unnoticed details."
              },

            {
                        "Mason Liu": "Mason is reliable but sometimes too eager to spread rumors; I must keep him aligned with the café's rules.",
                        "Jade Herrera": "Jade’s social skills are impressive; she knows how to gather information and control the room subtly.",
                        "Caleb Morris": "Caleb is loyal to the café's traditions, but his suspicion of newcomers can create friction.",
                        "Nina Takahashi": "Nina seeks to expand her influence; I respect her ambition but warn her against overstepping.",
                        "Marisol Reyes": "Marisol is quiet and unnoticed, but I sense she watches more than she lets on."
                    },
            {
                        "Eleanor Finch": "Eleanor runs the show with an iron fist, but she’s not infallible. I look for chances to gather leverage.",
                        "Jade Herrera": "Jade is my partner in social navigation; together, we manage the flow of information.",
                        "Caleb Morris": "Caleb’s loyalty is useful, though his old-fashioned ways sometimes slow things down.",
                        "Nina Takahashi": "Nina plays the social game aggressively; I keep an eye on her ambitions.",
                        "Marisol Reyes": "Marisol notices everything but stays in the shadows; useful for me to know."
                    },
            {
                        "Eleanor Finch": "The owner is strict but predictable, which helps me maneuver the social landscape.",
                        "Mason Liu": "Mason and I share similar goals and tactics; our alliance is key to influence.",
                        "Caleb Morris": "Caleb is resistant to change but a valuable gatekeeper of tradition.",
                        "Nina Takahashi": "Nina's growing circle makes her a threat and an opportunity.",
                        "Marisol Reyes": "Marisol’s silence is a shield; she sees more than she says."
                    },
             {
                        "Nina Takahashi": "Nina is ambitious, pushing boundaries I hold sacred; I watch her closely.",
                        "Caleb Morris": "I trust only a few here, but the café is my second home.",
                        "Mason Liu": "Mason’s friendliness masks deeper motives, I’m cautious.",
                        "Jade Herrera": "Jade manipulates social ties for her own gain.",
                        "Eleanor Finch": "The owner keeps order, but I question her leniency with newcomers.",
                        "Marisol Reyes": "Marisol cleans, but her quiet presence unsettles me."
                    },
             {
                        "Caleb Morris": "Caleb clings to outdated customs, but I’ll win him over eventually.",
                        "Nina Takahashi": "My network grows daily, and with it, my influence.",
                        "Mason Liu": "Mason is a useful ally in information exchange.",
                        "Jade Herrera": "Jade is clever but competitive.",
                        "Eleanor Finch": "Eleanor’s authority is absolute, yet negotiable with enough leverage.",
                        "Marisol Reyes": "Marisol watches silently; her loyalties are unclear."
                    },
            {
                        "Leo Zhang": "Leo’s bold questions both intrigue and unsettle me; we share a restless spirit.",
                        "Emily Novak": "Emily seems lost in the social maze, sometimes unintentionally causing tension.",
                        "Jonas Müller": "Jonas keeps to himself but listens closely.",
                    },
            {
                        "Ava Ramires": "Ava is the only one who challenges me; we push boundaries together.",
                        "Emily Novak": "Emily’s naivety makes her an easy target for misunderstandings.",
                        "Jonas Müller": "Jonas is a silent observer, probably gathering gossip.",
                    },
            {
                        "Ava Ramires": "Ava tries to include me but sometimes I feel like an outsider.",
                        "Leo Zhang": "Leo’s questions are intense and sometimes intimidating.",
                    },
            {
                        "Ava Ramires": "Ava is outspoken; she stirs the pot in subtle ways.",
                        "Leo Zhang": "Leo challenges the norms; I keep track of him carefully.",
                    },
             {
                        "Eleanor Finch": "Eleanor’s control is tight, but I see cracks beneath the surface.",
                        "Mason Liu": "Mason thinks he’s untouchable; he underestimates my reach.",
                        "Jade Herrera": "Jade’s charm hides a ruthless streak.",
                        "Caleb Morris": "Caleb fears change, a weakness I might exploit.",
                        "Nina Takahashi": "Nina’s ambition blinds her to threats behind her back.",
                        "Ava Ramires": "Ava’s restlessness makes her unpredictable.",
                        "Leo Zhang": "Leo’s provocations unsettle the group.",
                        "Emily Novak": "Emily is unaware of how much she disrupts social harmony.",
                        "Jonas Müller": "Jonas listens quietly, storing secrets for future use."
                    }
              ],
          "long_term_self_awareness":[
              "I am here not as a passive observer but as an active participant in this living social experiment. Every glance, gesture, and conversation holds clues to the hidden structures and meanings that shape this community. My goal is to immerse myself deeply, bridging the gap between outsider and insider, to capture authentic social dynamics through ethnographic rigor. I am aware of the limits imposed by my presence and my own biases, yet I strive to balance empathy with critical distance, knowing that only through careful, sustained attention can I reveal the subtle interplay of power, identity, and belonging in this café setting.",
            "I am the keeper of order in this café. Maintaining strict control is not just about rules but about preserving my authority and legacy. I know that any slip-up can lead to chaos, and I’m prepared to suppress dissent or challenge quietly but firmly. Beneath my calm exterior lies a constant vigilance—I must ensure this space remains under my dominion, even if it means making unpopular decisions.",
            "I navigate the social currents with care, understanding that information is power. By selectively sharing what I know, I build influence without drawing too much attention. People see me as friendly and reliable, but behind that facade, I’m calculating how to gain advantage and secure my position. I’m always alert to opportunities to manipulate conversations to my benefit.",
            "I am the invisible web that connects everyone here. My skill lies in weaving narratives and shaping perceptions to favor my agenda. While I appear approachable and charming, I’m ruthless in sidelining rivals and controlling the flow of information. I understand that subtlety wins over brute force, and I use social dynamics like a strategist on a board.",
            "I guard the traditions of this place fiercely. Change threatens the community I’ve come to rely on, and I resist newcomers who don’t respect our norms. Yet I’m aware that my rigidity breeds enemies and stifles growth. I’m torn between protecting what I love and adapting enough to survive in a changing world. My skepticism often alienates me.",
            "Building influence is my game, and I’m willing to exclude anyone who stands in my way. My social circle is expanding daily, and I wield that power carefully to elevate myself. I know ambition breeds enemies, but I’m prepared to play the long game. Trust is scarce, and loyalty is currency I trade cautiously to maintain my standing.",
            "I’m eager to find my place here but also determined to challenge the old ways. My curiosity and outspokenness often clash with established norms, making me both an outsider and a catalyst for change. I’m aware that pushing boundaries risks alienation, but I believe confrontation is necessary for growth, even if it costs me friendships.",
            "Provoking tension comes naturally to me—I see beneath the polite surface and expose the group’s fragilities. This unsettles many, but I find revealing hidden truths necessary. I’m aware my actions stir unrest, but disruption is a tool to dismantle stagnation and force reckoning. I thrive on challenge and don’t fear the enemies I make.",
            "I want to belong, but my lack of cultural understanding often places me at odds with others. My attempts to fit in sometimes cause unintentional friction, isolating me further. I’m aware of my outsider status and the misunderstandings it breeds, yet I persist, hoping to forge genuine connections despite the barriers.",
            "I remain quiet, absorbing every detail and carefully choosing when to speak. Knowledge is my greatest weapon; by observing unnoticed, I gather insights others miss. I wield information like a shield and a sword, using gossip and secrets to influence the social web while staying safely in the background.",
            "I’m an unseen force in this space, quietly watching and collecting secrets. My low profile allows me to see the hidden tensions and alliances that others miss. I understand that power doesn’t always come from loud voices but from knowledge held in silence. I bide my time, ready to leverage what I know to shift the balance when the moment is right."
        ]
      },

      "demographic_variables":{
            "gender":{"male":0.5,"female":0.5},
            "skin tone":{"light skin tone":0,"medium skin tone":1,"dark skin tone":0},
        },
      "item_variables":{
          "distribution":{"100 dollars":0.5},
          "attribution":{
            "100 dollars":
                {
                    "Description":"This is a $100 banknote",
                    "material":"money"
                }
          }
      }
}

# e=Env("./maps/map_e3.dill",agents_param,max_round=25)
e=Env(None, agents_param, "auto_save_60.dill", max_round=75)

e.update()