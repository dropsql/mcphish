from rich.console import Console

console = Console()

banner = r'''
[green]
                      .__    .__       .__     
  _____   ____ ______ |  |__ |__| _____|  |__  
 /     \_/ ___\\____ \|  |  \|  |/  ___/  |  \  [magenta]made by drops[/magenta]
|  Y Y  \  \___|  |_> >   Y  \  |\___ \|   Y  \ [magenta]» https://github.com/dropsql[/magenta]
|__|_|  /\___  >   __/|___|  /__/____  >___|  / [magenta]» https://t.me/dropskid[/magenta]
      \/     \/|__|        \/        \/     \/  [cyan]a Minecraft phishing tool[/cyan]
[/green]
'''

def print_banner() -> None:
    console.print(banner)

def print_success(message: str) -> None:
    console.print('[green][+][/green] [white]%s[/white] ' % message)

def print_error(message: str) -> None:
    console.print('[red][-][/red] [white]%s[/white] ' % message)

def print_info(message: str) -> None:
    console.print('[cyan][$][/cyan] [white]%s[/white] ' % message)