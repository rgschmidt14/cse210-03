import random


class WordSelector:
    '''This class will be used to house our word bank and choose an individual word for each game (stored as an object)

    
    '''
    def __init__(self, category="fish"):
        self.new_word = self.__pick_a_word(category)

    def __pick_a_word(self, category):
        '''This is the method used to choose a word for the instance of the game that is being played.
        
        Will pick a word from a chosen list and return it as a string.capitalize()
        '''
        dictionary_of_words = {
            "fish":["anchovy","angelfish","angelshark","barb","barracuda","basking shark","bass","blenny","blowfish","blue shark","bluefin tuna","bonito","bony fish","bull shark",
                    "carp","catfish","chub","clownfish","cod","coelacanth","cookiecutter shark","crappie",
                    "darter","devil ray","dogfish","dory","dragonfish","Dunkleosteus",
                    "eel","electric eel","elver","Emperor angelfish","fish","flounder","flying fish",
                    "Galapagos shark","gar","glassfish","goby","goldfish","grayling","great white shark","Greenland shark","grouper","grunion","gulper eel","guppy",
                    "haddock","hagfish","hake","halibut","hammerhead shark","hatchetfish","herring","humuhumu-nukunuku-apua'a",
                    "icefish","jackfish","John Dory","koi","lake trout","lamprey","lanternfish","lemon shark","ling cod","loach","luminous shark","lungfish",
                    "mackerel","mako shark","manta ray","marlin","Megalodon","megamouth shark","minnow","monkfish","moray eel","mullet",
                    "needlefish","nurse shark","oarfish","orange roughy","Orthacanthus",
                    "paddlefish","parrotfish","perch","pike","pilot fish","piranha","pollock","pompano","porgy","Port Jackson shark","pufferfish","pupfish",
                    "queen triggerfish","quillfish","ray","remora","rockfish","roughy",
                    "sailfish","salmon","sardine","sawfish","sculpin","sea bass","seadragon","seahorse","shad","shark","skate","smelt","snapper","sole","stingray","sturgeon","sunfish","swordfish",
                    "tarpon","tetra","three-spine stickleback","thresher shark","tiger shark","triggerfish","trout","tuna","tunny","turbot",
                    "upside-down catfish","velvetfish","viperfish","walleye","whale shark","whiting","wrasse",
                    "x-ray tetra","yellow jack","yellowtail","zebra bullhead shark","zebrafish"],
            "metal":["alloy","aluminum","antimony","brass","bronze",
                    "chrome","chromium","copper","cupronickel","gold",
                    "iridium","iron","lead","magnesium","mercury","metal",
                    "pewter","platinum","silver","stainless steel","steel",
                    "tin","titanium","tungsten","uranium","yellow gold",
                    "zinc"]
        }
        word_count_in_category = len(dictionary_of_words[category])
        random_number_in_category = random.randrange(0,word_count_in_category)
        word = dictionary_of_words[category][random_number_in_category].lower()  #.capitalize() is what I want to display, but for referencing purposes in all the lists in this program we will use lower() method here. Thank you.
        return word

# Testing - APPROVED         
# new_word1 = WordSelector.__pick_a_word("self","metal")
# new_word2 = WordSelector.__pick_a_word("self","fish")
# print(new_word1,new_word2)