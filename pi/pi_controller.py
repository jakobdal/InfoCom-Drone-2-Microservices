import requests
import time
import random
import click
from sense_hat import SenseHat

sense = SenseHat()


# Replace with your own function in Part 1
def get_direction():
    
    d_long = 0
    d_la = 0
    send_vel = False
    
    for event in sense.stick.get_events():
        if event.action in ("pressed", "held"):
            if event.direction == "left":
                d_long = -1
                d_la = 0
                send_vel = True
                click.echo("Left")
            elif event.direction == "right":
                d_long = 1
                d_la = 0
                send_vel = True
                click.echo("Right")
            elif event.direction == "up":
                d_long = 0
                d_la = 1
                send_vel = True
                click.echo("Up")
            elif event.direction == "down":
                d_long = 0
                d_la = -1
                send_vel = True
                click.echo("Down")
            else:
                d_long = 0
                d_la = 0
                send_vel = False
                click.echo("Invalid output :(")
                
            return d_long, d_la, send_vel
        
    return 0,0, False


if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"
    while True:
        d_long, d_la, send_vel = get_direction()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)
