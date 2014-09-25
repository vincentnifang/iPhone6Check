__author__ = 'vincent'

store = {
"R409":"Causeway Bay",
"R428":"ifc mall",
"R485":"Festival Walk"}
Model= {
"MGAF2ZP/A" : "6plus 128g gold",
"MG492ZP/A" : "6 16g gold",
"MGAC2ZP/A" : "6plus 128g black",
"MGA92ZP/A" : "6plus 16g sliver",
"MG4F2ZP/A" : "6 64g black",
"MG472ZP/A" : "6 16g black",
"MG4A2ZP/A" : "6 128g black",
"MGAK2ZP/A" : "6plus 64g gold",
"MGAA2ZP/A" : "6plus 16g sliver",
"MG4J2ZP/A" : "6 64g gold",
"MGAJ2ZP/A" : "6plus 64g sliver",
"MG4H2ZP/A" : "6 64g sliver",
"MGAE2ZP/A" : "6plus 128g sliver",
"MG4E2ZP/A" : "6 128 gold",
"MG482ZP/A" : "6 16g sliver",
"MGAH2ZP/A" : "6plus 64g black",
"MG4C2ZP/A" : "6 128g sliver",
"MGA82ZP/A" : "6plus 16g black"
}

def getStore(s):
    return store[s]

def getMode(m):
    return Model[m]