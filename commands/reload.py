async def function(bot, event):
  bot.reload_modules()
  await event.sendReply("Modules reloaded.")

config = dict(
  name = "reload",
  author = "Christopher",
  function = function,
  adminOnly = True
)