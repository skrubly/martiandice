"""
Martian dice impelmentation.
"""
import random

class Cube(object):
  def __init__(self, up=None):
    self.up = up

  def roll(self):
    sides = ['tank', 'deathray', 'deathray', 'human', 'cow', 'chicken']
    self.up = random.choice(sides)

  def __repr__(self):
    return str(self.up)

  def __str__(self):
    return self.up

  def __eq__(self, other):
    return self.up == other.up

class Player(object):
  def __init__(self,name):
    self.name = name
    self.score = 0

  def pick(self):
    choicedict = {'k': 'chicken', 'c': 'cow', 'h': 'human', 'd': 'deathray', 's': 'stop'}
    if not self.dice:
      return 
    valid_choice = False
    while not valid_choice:
      selected = raw_input('Choice? k, c, d, h, s')
      if selected == 's':
        self.dice = []
        return
      elif selected not in choicedict.keys():
        print('invalid choice!')
      elif choicedict[selected] not in [str(x) for x in self.dice]:
        print('There are no %s to pick' % choicedict[selected])
      elif selected in ['k', 'c', 'h']:
        # Check to see if they've already saved the selected type
        if choicedict[selected] in [str(x) for x in self.saved]:
          print("Sorry, you've already saved %s" % choicedict[selected])
        else:
          for index, d in enumerate(self.dice):
            if d.up == choicedict[selected]:
              self.saved.append(d)
          self.dice[:] = (value for value in self.dice if value.up != choicedict[selected])
          valid_choice = True
      elif selected == 'd':
        for index, d in enumerate(self.dice):
          if d.up == 'deathray':
            self.saved.append(d)
        self.dice[:] = (value for value in self.dice if value.up != 'deathray')
        valid_choice = True

  def take_turn(self):
    self.dice = [Cube() for x in range(0,13)]
    self.tanks = []
    self.saved = []
    while self.dice:
      for d in self.dice:
        d.roll()
      for index, d in enumerate(self.dice):
        if d.up == 'tank':
          self.tanks.append(d)
      # Now remove all the tanks
      self.dice[:] = (value for value in self.dice if value.up != 'tank')
      print('Rolled: %s' % self.dice)
      print('Saved: %s' % self.saved)
      print('Tanks: %s' % self.tanks)
      self.pick()
    self.score_dice()  

  def score_dice(self):
    score = 0
    score_dict = {'chicken': 0, 'human': 0, 'cow': 0, 'deathray': 0}
    for d in self.saved:
      score_dict[d.up] += 1
    if score_dict['deathray'] < len(self.tanks):
      print('Too many tanks, not enough deathrays! NO SCORE!')
      exit(0)
    else:
      if score_dict['chicken'] and score_dict['human'] and score_dict['cow']:
        print('Bonus points! You got one of each type of creature! +3')
        score += 3 # Bonus points
      score += score_dict['chicken']
      score += score_dict['human']
      score += score_dict['cow']
    print('You scored: %s' % score)
    exit()

def main():
  steve = Player('Steve')
  steve.take_turn()

if __name__ == '__main__':
  main()
