"""
from database import User
from util import get_name

async def handler_points(bot, event):
  uid = event.get('author_id')
  mid = event.get('mid')
  tid = event.get('thread_id')
  typ = event.get('thread_type')
  
  user = User(uid)
  
  rew = 1
  try:
    user.addPoints(rew)
    pts = user.points
    if (pts%50) == 0:
      level = pts/50
      name = get_name(uid)
      messsge = "[bold blue]USER [/bold blue]"
  except ValueError as e:
    bot.error(e, "./events/points.py")
"""