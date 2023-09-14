class player:
  def play(self):
    print("The player is playing cricket.")
class Batman(player):
  def play(self):
    print("The batsman is batting.")
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")


batsman=Batman()
bowler=Bowler()

batsman.play()
bowler.play()