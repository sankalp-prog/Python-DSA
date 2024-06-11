NEXT_DIRECTION = {None: 'right', 'right': 'down', 'down': 'left', 'left': 'up', 'up': None}
DIRECTIONS = {'up': (-1,0), 'left': (0,-1), 'right':(0,1), 'down': (1,0)}
BLOCKAGE = 1

def dfs(maze, starting_pointer):
  def is_valid_coordinate():
    if current_i < 0 or current_i >= len(maze):
      # i is out of bounds
      return False
    if current_j < 0 or current_j >= len(maze[0]):
      # j is out of bounds
      return False
    if maze[current_i][current_j] == BLOCKAGE:
      # Blockage
      return False
    if (current_i, current_j) in in_path:
      # Don't go in a loop
      return False
    if next_direction is None:
      # Exhausted all directions, go back
      return False

    return True
  
  num_columns = len(maze[0])
  num_rows = len(maze)
  end_point = (num_rows-1, num_columns-1)
  current_i, current_j = starting_pointer
  last_used_direction = None
  history = []
  in_path = set()

  while (current_i, current_j) != end_point:
    next_direction = NEXT_DIRECTION[last_used_direction]

    if is_valid_coordinate():
      history.append((current_i, current_j, next_direction))
      in_path.add((current_i, current_j))

      # Walk in new direction
      delta_i, delta_j = DIRECTIONS[next_direction]
      current_i += delta_i
      current_j += delta_j
      # Reset direction so next node starts with 'right' again
      last_used_direction = None
    else:
      # Can't backtrack any further
      if not history:
        return 'No solution'
      # Backtrack
      (current_i, current_j, last_used_direction) = history.pop()
      in_path.remove((current_i, current_j))

  return history
