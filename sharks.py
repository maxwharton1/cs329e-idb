import json
sample = [
   {
       "sharks": [{
           "name" : "Kevin O'Leary",
           "invested" : "8,543,000",
           "deals" : 40,
           "episodes" : 131,
           "picture" : "https://s.abcnews.com/images/Business/GTY_kevin_oleary_2_kab_150929_16x9_992.jpg?resize=720"
         }],
       "company": {
         "name" : "Zipz",
         "episode" : "6-11",
         "founders" : ["Andrew McMurray"],
         "location" : "Santa Rosa, CA",
         "description" : "Single-serve wines in recyclable, high quality plastic stemware that looks and feels like glass.",
         "investment" : "2,500,000",
         "equity" : "10%",
         "picture" : "https://gazettereview.com/wp-content/uploads/2016/04/zipz-shark-tank-header.jpg?fit=1080%2C610&ssl=1"
       }
   },

   {
       "sharks": [{
           "name" : "Kevin O'Leary",
           "invested" : "8,543,000",
           "deals" : 40,
           "episodes" : 131,
           "picture" : "https://s.abcnews.com/images/Business/GTY_kevin_oleary_2_kab_150929_16x9_992.jpg?fit=1080%2C610&ssl=1"
         },
         {
           "name" : "Mark Cuban",
           "invested" : "19,850,000",
           "deals" : 85,
           "episodes" : 111,
           "picture" : "https://static.businessinsider.com/image/548a1d946bb3f7097aa03d8a-750.jpg?fit=1080%2C610&ssl=1"
         }],
       "company": {
         "name" : "Toygaroo",
         "episode" : "2-2",
         "founders" : ["Nikki Pope"],
         "location" : "Los Angeles, CA",
         "description" : "A subscription toy service.",
         "investment" : "200,000",
         "equity" : "40%",
         "picture" : "https://i0.wp.com/kirktaylor.com/wp-content/uploads/toygaroo-shark-tank-nikki-pope.jpg?fit=1080%2C610&ssl=1"
       }
   },

   {
       "sharks": [{
           "name" : "Kevin O'Leary",
           "invested" : "8,543,000",
           "deals" : 40,
           "episodes" : 131,
           "picture" : "https://s.abcnews.com/images/Business/GTY_kevin_oleary_2_kab_150929_16x9_992.jpg?resize=1080"
         }],
       "company": {
         "name" : "How Do You Roll?",
         "episode" : "4-16",
         "founders" : ["Peter Yung", "Yuen Yung"],
         "location" : "Austin, TX",
         "description" : "A chain of quick-service establishments selling quality made-to-order sushi rolls.",
         "investment" :  "1,000,000",
         "equity" : "20%",
         "picture" : "https://i1.wp.com/kirktaylor.com/wp-content/uploads/how-do-you-roll-shark-tank.jpg?resize=1080%2C608&ssl=1"
       }
   },

   {
       "sharks": [{
           "name" : "Kevin O'Leary",
           "invested" : "8,543,000",
           "deals" : 40,
           "episodes" : 131,
           "picture" : "https://s.abcnews.com/images/Business/GTY_kevin_oleary_2_kab_150929_16x9_992.jpg?resize=1080"
         },
         {
           "name" : "Robert Herjavec",
           "invested" : "16,598,333",
           "deals" : 57,
           "episodes" : 126,
           "picture" : "https://amp.businessinsider.com/images/56ad203b58c3238d008b69be-750-562.jpg?resize=1080"
         }],
       "company": {
         "name" : "Jump Forward",
         "episode" : "6-11",
         "founders" : ["Brian Duggan", "Adam McCombs"],
         "location" : "Chicago, IL",
         "description" : "  An online service allowing high school athletes and their parents to profile their skills to market themselves to colleges.",
         "investment" : "150,000",
         "equity" : "10%",
         "picture" : "https://gazettereview.com/wp-content/uploads/2016/04/Featured-9-e1459724712300.jpg?resize=1080"
       }
   },

   {
       "sharks": [{
           "name" : "Robert Herjavec",
           "invested" : "16,598,333",
           "deals" : 57,
           "episodes" : 126,
           "picture" : "https://amp.businessinsider.com/images/56ad203b58c3238d008b69be-750-562.jpg?resize=1080"
         }],
       "company": {
         "name" : "Zero Pollution Motors",
         "episode" : "6-27",
         "founders" : ["Ethan Tucker", "Pat Boone"],
         "location" : "New Paltz, NY",
         "description" : "Zero Pollution Motors is launching the urban car of the future, the AIRPod. The AIRPod vehicle is the solution to urban pollution and urban mobility. With its small size, a tiny price, zero pollution, and a fun and futuristic design, AIRPod marks a turning point in the range of urban vehicles. It is a real breath of fresh air in cities and the prelude to travel without pollution.",
         "investment" : "5,000,000",
         "equity" : "50%",
         "picture" : "https://upload.wikimedia.org/wikipedia/commons/a/a4/MDI_Air_Pod_%281%29.JPG?resize=1080"
       }
   },

   {
       "sharks": [{
           "name" : "Robert Herjavec",
           "invested" : "16,598,333",
           "deals" : 57,
           "episodes" : 126,
           "picture" : "https://amp.businessinsider.com/images/56ad203b58c3238d008b69be-750-562.jpg?resize=1080"
         }],
       "company": {
         "name" : "Chord Buddy",
         "episode" : "3-3",
         "founders" : ["Travis Perry"],
         "location" : "New Paltz, NY",
         "description" : "A two-month learning system that teaches which chords to play on the guitar.",
         "investment" : "175,000",
         "equity" : "20%",
         "picture" : "https://www.sharktankblog.com/wp-content/uploads/Chord-Buddy-on-Shark-Tank-Show.jpg?resize=1080"
       }
   },

   {
       "sharks": [{
           "name" : "Robert Herjavec",
           "invested" : "16,598,333",
           "deals" : 57,
           "episodes" : 126,
           "picture" : "https://amp.businessinsider.com/images/56ad203b58c3238d008b69be-750-562.jpg?resize=1080"
         },
         {
           "name" : "Jeff Foxworthy",
           "invested" : "75,000",
           "deals" : 2,
           "episodes" : 2,
           "picture" : "https://cdn1.edgedatg.com/aws/v2/abc/SharkTank/episode/248748/dd11ddb14c1c532d471586d92c7c99c7/1228x691-Q90_dd11ddb14c1c532d471586d92c7c99c7.jpg?resize=1080"
         },
         {
           "name" : "Daymond John",
           "invested" : "8,567,000",
           "deals" : 61,
           "episodes" : 100,
           "picture" : "https://amp.businessinsider.com/images/55ad68802acae78b0e8b8204-750-562.jpg?resize=1080"
         }],
       "company": {
         "name" : "Hillbilly Brand",
         "episode" : "2-4",
         "founders" : ["Mike Abbaticchio", "Shon Lees"],
         "location" : "Parkland, FL",
         "description" : "A country-style apparel store sold through Sports Authority, truck stops and travel plazas.",
         "investment" : "75,000",
         "equity" : "100%",
         "picture" : "https://2paragraphs.com/wp-content/uploads/2017/05/Hill-Billy-Brand-620x373.jpg?resize=1080"
       }
   },

   {
       "sharks": [{
           "name" : "Robert Herjavec",
           "invested" : "16,598,333",
           "deals" : 57,
           "episodes" : 126,
           "picture" : "https://amp.businessinsider.com/images/56ad203b58c3238d008b69be-750-562.jpg?resize=1080"
         }],
       "company": {
         "name" : "Happy Feet",
         "episode" : "5-23",
         "founders" : ["Pat Yates"],
         "location" : "    Louisville, KY",
         "description" : "Happy Feet are the plushest, softest slippers that money can buy. These slippers don't apologize for being comfy, they flaunt it. Founded in 1995, the company started out with just a few styles but over the years have expanded to include hundreds of designs, including many in association with branding partners.",
         "investment" : "375,000",
         "equity" : "25%",
         "picture" : "https://www.robertherjavec.com/wp-content/uploads/2016/04/dreamworks_banner_red_carpet2.jpg?resize=1080"
       }
   },

   {
      "sharks": [{
          "name" : "Mark Cuban",
          "invested" : "19,850,000",
          "deals" : 85,
          "episodes" : 111,
          "picture" : "https://static.businessinsider.com/image/548a1d946bb3f7097aa03d8a-750.jpg?resize=1080"
        }],
      "company": {
        "name": "BeatBox Beverages",
        "episode" : "6-6",
        "founders" : ["Brad Schultz", "Aimy Steadman", "Justin Fenchel"],
        "location" : "Austin, TX",
        "description" : "Inexpensive and creatively-flavored box wine",
        "investment" : "1,000,000",
        "equity" : "33%",
        "picture" : "https://2paragraphs.com/wp-content/uploads/2015/09/MG_9741-620x375.jpg?resize=1080"
      }
    },

    {
      "sharks": [{
          "name" : "Mark Cuban",
          "invested" : "19,850,000",
          "deals" : 85,
          "episodes" : 111,
          "picture" : "https://static.businessinsider.com/image/548a1d946bb3f7097aa03d8a-750.jpg?resize=1080"
        }],
      "company": {
        "name": "Gameday Couture",
        "episode" : "6-11",
        "founders" : ["Shawna Feddersen", "Kurt Feddersen"],
        "location" : "Tulsa, OK",
        "description" : "Fashionable and affordably-priced apparel for female sports fans",
        "investment" : "500,000",
        "equity" : "30%",
        "picture" : "http://lionessmagazine.com/wp-content/uploads/2016/04/game-try.jpg?resize=1080"
      }
    },
    {
      "sharks": [{
          "name" : "Mark Cuban",
          "invested" : "19,850,000",
          "deals" : 85,
          "episodes" : 111,
          "picture" : "https://static.businessinsider.com/image/548a1d946bb3f7097aa03d8a-750.jpg"},
        {
          "name" : "Barbara Corcoran",
          "invested" : "5,465,000",
          "deals" : 53,
          "episodes" : 82,
          "picture" : "https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2013/11/26/101229657-shark-tank-barbara-corcoran.jpg?resize=1080"
        }],

      "company": {
        "name": "LOLIWARE",
        "episode" : "7-2",
        "founders" : ["Leigh Ann Tucker","Chelsea Briganti"],
        "location" : "New York, NY",
        "description" : "LOLIWARE are the first compostable, biodegradable cups that are also edible and delicious! These two college friends created these cups as an eco-friendly and fun alternative to party supplies. Made with vegetable gelatin, LOLIWARE is completely vegan",
        "investment" : "600,000",
        "equity" : "25%",
        "picture" : "http://youthindependent.com/wp-content/uploads/7233713498_9db1acc90a_b-660x330.jpg?resize=1080"
      }
    },

   {
      "sharks": [{
          "name" : "Mark Cuban",
          "invested" : "19,850,000",
          "deals" : 85,
          "episodes" : 111,
          "picture" : "https://static.businessinsider.com/image/548a1d946bb3f7097aa03d8a-750.jpg?resize=1080"
        },
        {
          "name" : "Barbara Corcoran",
          "invested": "5,465,000",
          "deals" : 53,
          "episodes" : 82,
          "picture" : "https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2013/11/26/101229657-shark-tank-barbara-corcoran.jpg?resize=1080"
        }],
      "company": {
        "name": "Villy Customs",
        "episode" : "3-13",
        "founders" : ["Fleetwood Hicks"],
        "location" : "Dallas, TX",
        "description" : "An online store for customizable bicycles",
        "investment" : "500,000",
        "equity" : "42%",
        "picture" : "https://cdn.shopify.com/s/files/1/0852/0412/products/Vander_6_2048x.jpg?resize=1080"
    }
  },
    {
      "sharks": [{
          "name" : "Daymond John",
          "invested" : "8,567,000",
          "deals" : 61,
          "episodes" : 100,
          "picture" : "https://amp.businessinsider.com/images/55ad68802acae78b0e8b8204-750-562.jpg?resize=1080"
        }],
      "company": {
        "name" : "TITIN",
        "episode" : "6-7",
        "founders" : ["Patrick Whaley"],
        "location" : "Atlanta, GA",
        "description" : "TITIN is patented form-fitting weighted compression gear using gel weights as inserts.",
        "investment" : "500,000",
        "equity" : "20%",
        "picture" : "https://gazettereview.com/wp-content/uploads/2016/04/titin2.jpg?resize=1080"
      }
    },
    {
      "sharks": [{
          "name" : "Daymond John",
          "invested" : "8,567,000",
          "deals" : 61,
          "episodes" : 100,
          "picture" : "https://amp.businessinsider.com/images/55ad68802acae78b0e8b8204-750-562.jpg?resize=1080"
        }],
      "company": {
        "name" : "One Sole",
        "episode" : "2-9",
        "founders" : ["Dominique McClain Barteet"],
        "location" : "Palm City, FL",
        "description" : "Shoes with interchangeable uppers allowing the user to easily vary their look.",
        "investment" : "500,000",
        "equity" : "35%",
        "picture" : "https://2paragraphs.com/wp-content/uploads/2017/08/OneSole-620x375.jpg?resize=1080"
      }
    },
    {
      "sharks": [{
          "name" : "Daymond John",
          "invested" : "8,567,000",
          "deals" : 61,
          "episodes" : 100,
          "picture" : "https://amp.businessinsider.com/images/55ad68802acae78b0e8b8204-750-562.jpg?resize=1080"
        }],
      "company": {
        "name" : "Hells Bells Helmet",
        "episode" : "1-11",
        "founders" : ["Marix Stone", "Dr. Nancy Tanchel"],
        "location" : "Philadelphia, PA",
        "description" : "Designer helmets. The company owns a utility patent to place 3D designs on motorcycle helmets as well as any other kind of sporting helmet.",
        "investment" : "500,000",
        "equity" : "50%",
        "picture" : "http://sharktankshopper.com/wp-content/uploads/2014/02/Hells-Bells-Helmets.jpg?resize=1080"
      }
    },
    {
      "sharks": [{
          "name" : "Daymond John",
          "invested" : "8,567,000",
          "deals" : 61,
          "episodes" : 100,
          "picture" : "https://amp.businessinsider.com/images/55ad68802acae78b0e8b8204-750-562.jpg?resize=1080"
        }],

      "company": {
        "name" : "Spikeball",
        "episode" : "6-29",
        "founders" : ["Chris Ruder"],
        "location" : "Chicago, IL",
        "description" : "Spikeball started out as a casual outdoors game, but has grown to become a national sensation. Played in a 2 vs. 2 format, teams compete to spike a ball into a bouncy net until one team can't return it, which awards their opposing team a point. This nascent sport is often described as a cross between beach volleyball and foursquare. Spikeball's popularity has been growing, and currently there are over a quarter million players in the United States, as well as over a thousand nationally ranked teams.",
        "investment" : "500,000",
        "equity" : "22%",
        "picture" : "http://productsofsharktank.com/wp-content/uploads/2015/05/spikeball.jpg?resize=1080"
      }
  }
]

with open('sharks.json', 'w') as fp:
    json.dump(sample, fp, indent=4)
#end of book.py
