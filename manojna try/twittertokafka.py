from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from datetime import datetime
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
kafka =  KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)

class listener(StreamListener):

    def __init__(self):
        self.kafka = KafkaClient("localhost:9092")    
        self.ckey = "6ytBi3BUnfn1yQ4p2gJ74fwk8"
        self.csecret="5MgYpZmbMbBzGFsXaK2t88uIMuOTiF0wgxbwgFnu3kh55BNzqe"
        self.atoken="4327472303-UjkzRmCD41jU581AyrRc08k3FLKq2aMdR2HhztT"
        self.asecret="Xk2TrVWrBQ55PXtM1PvGZU52i4sE3XSOlAUMBNJ54Se8D"
        self.producer = SimpleProducer(self.kafka)
        self.auth = OAuthHandler(self.ckey, self.csecret)
        self.auth.set_access_token(self.atoken, self.asecret)

    def on_data(self, data):
        print(data)
        producer.send_messages("test", data)
        return True 

    def on_error(self, status):
        print status
        print "Error"

if __name__ == "__main__":
    lt = listener()
    twitterStream = Stream(lt.auth, listener())
    twitterStream.filter(track=['Hillary Clinton', '@hillaryclinton', '@ClintonNews', '@HRClinton', '@voteHillary2016', '@AllThingsHill', '@hillaryRussia', '@danmericaCNN', '@KThomasDC', '@anniekarni', '@AndrewStilesUSA', '@Madam_President', '@hillarynews1', '@FaithVotersPAC', '@HillDawgClinton', '@ABCLiz', '@NICKWALSH', '#Hillary2016', '@HillaryIn2016', 'Bernie Sanders', '@SenSanders', '@BernieSanders', '@ajbends', '@Bobby_Budds', '@Sanders4Potus', '@VoteBernie2016', 'Jeb Bush', '@JebBush', '@TeamJebBush', '@EliStokols', '@TomBeaumont', '@JBushNews', '@JBushNews', '@jebbushnews', '@VoteJeb', '@Bush', '@r2rusa', '@JebBushforPres', '@JebHillary2016', 'Donald Trump', '@realDonaldTrump', '@Writeintrump', '@Vote_For_Trump', '@NoahGrayCNN', '@DanScavino', 'John Kasich', '@JohnKasich', '@JohnKasichNews', '@TeamJohnKasich', '@GovernorKasich', 'Marco Rubio', '@marcorubio', '@TeamMarco', '@PoliticsTBTimes', '@MarcoRubioNews', 'Scott Walker', '@ScottWalker', '@GovWalker', '@wpjenna', '@ScottWalkerHQ'])