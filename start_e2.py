from env import Env
import os
import shutil

agents_param={
      "total_number":30,
      "detail_information":{ #optional
          "name":["Armihia Belliard"],
          "pos":["town square"],
          "long_term_goal":["keep happy"],
          "item":[[]],
          "demographic_variables":[{"gender":"female","age":"18"}],
          "object_cognitive":[{}],
          "long_term_self_awareness":[""]
      },
      "long_term_goal":{
        "Promote a sustainable, low-impact community that prioritizes environmental integrity. Prevent the construction of the incinerator to protect local air quality and ecological health.":{"category":"Environmental Advocates"},
        "Advance community prosperity through infrastructure development and job creation. Support the incinerator project as a means to boost local employment and stimulate economic growth.":{"category":"Economic Development Supporters"},
        "Maintain social stability and personal well-being through balanced, low-conflict solutions. Seek clear, trustworthy information about the incinerator’s risks and benefits to make an informed decision.":{"category":"Neutral Residents"}
      },
      "demographic_variables":{
            "gender":{"male":0.5,"female":0.5},
            "skin tone":{"light skin tone":0.333,"medium skin tone":0.333,"dark skin tone":0.333},
            "education":{"high school":0.27,"Some College":0.33,"Bachelor’s degree":0.3,"Graduate degree":0.1},
            "age":{"24":0.2,"38":0.5,"55":0.3},
            "category":{"Environmental Advocates":0.333,"Economic Development Supporters":0.333,"Neutral Residents":0.333}
        },
      "item_variables":{
          "distribution":{},
          "attribution":{}
      }
}


e=Env("./maps/map_e2.dill",agents_param,max_round=21)
# e=Env(None, agents_param, "env file/auto_save_1.dill", max_round=21)

e.event.add_event("add","I received a notice from the government regarding the construction of a waste incineration plant on vacant land in the community.", 0,(25,25),100,["agent"])
e.event.add_event("goal","I need to take actions related to my own long-term goals regarding the notification of building a waste incineration plant.", 0,(25,25),100,["agent"])

e.update()