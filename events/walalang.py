async def function(bot, data):
  message = data.message or ''
  tid = data.thread_id
  typ = data.thread_type
  mid = data.mid
  def check(text):
    return True if text in message.lower() else False
  if check("junmar"):
    return await bot.sendMessage("Junmar bakla!!", tid, typ, reply_to_id=mid)
  elif check("greegmon") or check(' greeg '):
    return await bot.sendMessage("Wala si Gregemon, naga lulu pa", tid, typ, reply_to_id=mid)
  elif check('prince har'):
    return await bot.sendMessage("No need facebook chat application programming interface.", tid, typ, reply_to_id=mid)

config = {
  "event": 'type:messaging',
  "def": function,
  "author": 'Muhammad Greeg'
}