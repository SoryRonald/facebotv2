async def Run(bot, event):
  if not event.args:
    return await event.sendMessage("Lagay ka ng message b0b0.")
  if event.thread_id == '7772407499516639':
    await bot.sendMessage(
      event.args,
      "7617738784941507",
      bot.ThreadType.GROUP
    )
  else:
    await bot.sendMessage(
      f"{event.author_name}\n\n{event.args}",
      "7772407499516639",
      bot.ThreadType.GROUP
    )
  #await bot.addUsersToGroup(event.author_id, "7617738784941507")

config = dict(
  name = "test",
  function = Run,
  adminOnly = True
)