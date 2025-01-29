import os
import importlib
from rich.console import Console
from rich.panel import Panel

commands = {}
def loadCommands(_prefix, log=None, isReload=False):
  global commands
  if commands:
    if isReload:
      commands = {}
    else:
      return commands
  
  def Log(message, isError=False):
    if log:
      log(message, "COMMAND", "#0A5EB0" if not isError else 'red')
  console = Console()
  files = list(filter(lambda file: file.endswith('.py') and file!='__init__.py',os.listdir('./commands')))
  message = ""
  #log('---------------------------------------------'*2)
  for file in files:
    filepath = f"commands.{os.path.splitext(file)[0]}"
    module = importlib.import_module(filepath)
    importlib.reload(module)
    config = getattr(module, 'config', None)
    if config:
      name = config.get('name')
      function = config.get('def')
      if config.get('function'):
        function = config.get('function')
        config['def'] = config.get('function')
        del config['function']
      if not name:
        Log(f"{file} - Missing command name", True)
        message += f"[bold red]ERROR[/bold red] [red]{file} [white]- Missing command name\n"
      elif not function:
        Log(f"{file} - Missing command function", True)
        message += f"[bold red]ERROR[/bold red] [red]{file} [white]- Missing command function\n"
      else:
        usePrefix = config.get('usePrefix', True)
        adminOnly = config.get('adminOnly', False)
        if not name.isalnum():
          Log(f"{file} - Invalid command name", True)
          message += f"[bold red]ERROR[/bold red] [red]{file} [white]- Invalid command name\n"
        elif name.lower() in commands:
          Log(f"{file} - Command '{name}' already exist", True)
          message += f"[bold red]ERROR[/bold red] [red]{file} [white]- Command '{name}' already exist\n"
        elif usePrefix not in [True, False]:
          Log(f"{file} - Invalid usePrefix value", True)
          message += f"[bold red]ERROR[/bold red] [red]{file} [white]- Invalid usePrefix value\n"
        elif adminOnly not in [True,False]:
          Log(f"{file} - Invalid adminOnly value", True)
          message += f"[bold red]ERROR[/bold red] [red]{file} [white]- Invalid adminOnly value\n"
        else:
          Log(f"Loaded <span style='color:#FEEE91'>{name.lower()}</span> - <i>({file})</i>")
          message += f"[blue]COMMAND[/blue] Loaded [yellow]{name.lower()}[/yellow] - {file}\n"
          if adminOnly not in [True,False]:
            adminOnly = False
            message += f"╰─── Invalid usePrefix value\n"
          config['adminOnly'] = adminOnly if adminOnly in [True, False] else False
          config["usage"] = config.get("usage", "").replace('{p}', _prefix)
          config["description"] = config.get("description", 'No description.').replace('{p}', _prefix)
          commands[name.lower()] = config
  panel = Panel(message[:-1], title="COMMANDS", border_style='royal_blue1')
  console.print(panel)
  return commands