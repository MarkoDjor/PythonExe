#jIspod je kao primer dat recnik (dictionary) koji se zove ghostlyd. Umesto ghostlyd napravi neki drugi recnik koji ima unose koji su ti zanimljivi. Zatim odstampaj sadrza recnika na ekranu kao u zadatku "stampanje recnika".

ghostlyd = {'A': 'A is for Alfred, poisoned to death.',
'B': 'B is for Bertrand, consumed by meth.',
'C': 'C is for Cornell, who ate some glass.',
'D': 'D is for Donald, who died from gas.',
'E': 'E is for Edward, hanged by the neck.',
'F': 'F is for Freddy, crushed in a wreck.',
'I': 'I is for Ingrid, who tripped down a stair.',
'J': 'J is for Jered, who fell off a chair,',
'K': 'K is for Kevin, bit by a snake.',
'L': 'L is for Lauryl, impaled on a stake.',
'M': 'M is for Moira, hit by a brick.',
'N': 'N is for Norbert, who swallowed a stick.',
'O': 'O is for Orville, who fell in a canyon,',
'P': 'P is for Paul, strangled by his banyan,',
'R': 'R is for Robert, who died of spite,',
'S': 'S is for Susan, stung by a jelly,',
'T': 'T is for Terrange, kicked in the belly,',
'U': "U is for Uma, who's life was vanquished,",
'V': 'V is for Victor, consumed by anguish,',
'X': 'X is for Xavier, stuck through with a prong,',
'Y': 'Y is for Yoeman, too fat by a piece,',
'Z': 'Z is for Zora, smothered by a fleece.'}

for kljuc,vrednost in ghostlyd.items():
    print( f"{kljuc:2} {vrednost:2}" )