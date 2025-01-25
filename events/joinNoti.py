import urllib.parse

async def bagong_tao(bot, event):
  try:
    data = event.msg
    tid = event.thread_id
    typ = event.hread_type
    for fbuser in event.addedParticipants:
      if fbuser['userFbId'] == bot.uid:
        await bot.shareContact("Thank you for adding me.", bot.uid, tid)
    else:
      if bot.uid not in event.added_ids:
        fbuser = event.addedParticipants[0]
        name = fbuser['fullName']
        await bot.shareContact(f"Welcome! {name} to the group.", event.added_ids[0], tid)
  except Exception as err:
    bot.error(err)

config = {
  "event": "type:peopleAdded",
  "def": bagong_tao,
  "author": "Muhammad Greeg"
}