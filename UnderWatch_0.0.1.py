import sys #sys helps because there are usefull commands 
#this is a text base strategy game 
"""
this is a simple way to make games, 
You could try it your self,
We will going to use python,
So lest start
"""


class main():
    def __init__(self):
        self.basecomms= ("yes","no", "quit", "-q")
        self.quit= ("quit","-q")

    def user_input(self,commands):
        while True:
            inp = input(("input your command:"+str(commands)))
            if self.is_com(inp,commands):
                return inp
            print("wrong input!..")
                
    
    def is_com(self,inp,commands):
        
        if inp not in commands:
            return False
        else:
            return True

    def run(self):
        while True:
            com = self.user_input(self.basecomms)

            if com in (self.quit):
                sys.exit()
"""
oky are base code is ready 
this is a dum terminal basicly you may ask
why you didn't make a terminal app other ways 
python is easy so you make the differ ok?

we need a story our code need to call differet pages
so our choise will make a effect on our stategy
how could be?

this game inspared as a distopian world of 1884
so our caracter could have a job in this worl

so in a poin in this game our caracter will have a job
what kinda job suited for our caracter lest think about that?

maybe a police?
more like force on separatatonist terrorist
we love our big broders so this could be?

so maybe a intigration office asking questions to 
people
this is getting some where,
there is some system update in this world people could 
reported different ways,
even while sleeping you are not safe,
you look some one wrong you get flaged, 

some neighbor kid report or your kid,
your wife or husband,
your television,
your co-workers or wokers,
some one you look argue
some one you look bad
some one just for fun
maybe you are realy part of some organization but 
terror deffined by who had control 
big brother is whaching you whit every step

so lest do mechanize, and whire a sudo code,
working,
    take a look the reports, 
        choice a reported name from files 
        or 
        begin integrating directly
    integrating
        see details of the person
        
        ask predefind questions 
        get ansers from suspect

        take a desition about suspect file reports

        if you are a wrong
            "increse number of bad people"
        if you are right 
            "decrice number of the bad people"

endings, 
        crate a rebelion "lose because you are a terrorist" 
        crashing soul of the rebelion "lose your life they think you are double"
        being avarage "lose your life because you proclaimed as a terrorist"
        run away from the country
        dying from a sickness
    

economics,
    "you are trying to survive in this world so"
    "gain base money for every day"
    "gain money every time you are correct"
    "lose money every time you are wrong"
    "you need base nesasity like 
    
    "there is a change if you do not pay these"
    "paying heat," 
    paying water, 
    buying food, 

    paying electricty,!! if you do not pay electricty lose drectly
    paying rent, !! if you do not pay rent lose drectly

    paying medicene "decrese chance of dying while scick

effects
    sick "if you are sick there is a change to becaming not to
    and dying

         
ok maybe I take some inspration from game named papers plase...
you sould play it!

and 
"sorry for my bad english"

ok we have 4M and 2W for this game date of today 2.01.26

oky we need to make a game 10/4 
this isn't hard but lest sea what is wrong abot this game
I need a exel table ok

lest save our game right now for fist day I think this is enough
"""

                
ru = main()
ru.run()








