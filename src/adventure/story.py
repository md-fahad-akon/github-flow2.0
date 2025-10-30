from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

# Create a console instance for rich output
console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    # Use rich to display the intro with styling
    intro_text = Text("You wake up in a dark forest. You can go left or right.", style="bold cyan")
    console.print(Panel(intro_text, title="🌲 Adventure Begins", border_style="green"))
    
    while True:
        # Replace input() with Prompt.ask() from rich
        choice = Prompt.ask(
            "\n[bold yellow]Which direction do you choose?[/bold yellow]",
            choices=["left", "right", "exit"],
            default="exit"
        )
        choice = choice.strip().lower()
        
        if choice == 'exit':
            print("Goodbye! Thanks for playing!")
            break
        
        # Display the result with color
        result = step(choice, events)
        console.print(f"[bold magenta]{result}[/bold magenta]")