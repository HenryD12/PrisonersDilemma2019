import random

team_name = 'Unicorns'
strategy_Unicorns = 'random number 1-3 inclusive. 2 are collude, 1 is betray. If score is < -1,500 or they betrayed in the last 2 games:random number 1-3 inclusive.  2 are betray 1 is collude'

strategy_description = 'Only a random number generator can keep people on their toes. We want it to not be completely random though. By tilting the odds towards betray or collude, we have a solid strategy while eliminating human error.'

def move(my_history, their_history, my_score, their_score):
  choice = random.randint(1,3)
  if len(my_history) == 0:
    return 'c'
  while my_score <= -1000:
    if choice == 1:
      return 'c'
    else:
      return 'b'

  if their_history[-1] == 'b':
    choice = random.randint(1,3)
    if choice == 1:
      return 'c'
    else:
      return 'b'
    
  
  elif choice == 3:
    return 'b'
  else:
    return 'c'
  



def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Collude on the first move
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Turn 1 test passed'
     # Test 2: if they betrayed last time, i should betray this time
    if test_move(my_history='bcbc',
              their_history='cccb', 
              # Note the scores are for testing move()
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b'):       
      print 'vengeance test successful.'
