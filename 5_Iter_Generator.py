"""Iter"""
"""Generator"""

Player=['Freeman','Ohtani','Betts','Muncy']

def generator():
  Player=['Freeman','Ohtani','Betts','Muncy']
  for i in Player:
    yield i

if __name__ == "__main__":
  my_iter=iter(Player)
  for i in range (0,len(Player),1):
    print(next(my_iter))
  for gen in generator():
    print(gen)

   


