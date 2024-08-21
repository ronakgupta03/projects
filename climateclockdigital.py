
import turtle
import datetime
import time

# Set the climate threshold and target date (change to your desired threshold and target date)
# threshold = 1.5
n = int(input("Enter the year: "))
target_date = datetime.datetime(n, 1, 1)
if 2024<= n <= 2030:
    threshold = 1.5
elif n < 2050:
    threshold = range(1, 2)
elif n == 2050:
    threshold = 2
else:
    print("can't pridict")

# Create the turtle window and set the clock face
window = turtle.Screen()
window.bgcolor("white")
window.title("Climate Clock")
clock = turtle.Turtle()


# Define a function to calculate the time remaining in years, months, days, hours, minutes, and seconds
def time_remaining():
    now = datetime.datetime.now()
    time_diff = target_date - now
    years = time_diff.days // 365
    months = (time_diff.days % 365) // 30
    days = time_diff.days % 30
    hours = time_diff.seconds // 3600
    minutes = (time_diff.seconds % 3600) // 60
    seconds = time_diff.seconds % 60

    if years > 30:
        impact = "Severe climate disruption"
        solution = "Shift to renewable sources of energy, promote afforestation, and reduce carbon footprint through sustainable lifestyle choices."
    elif years > 20:
        impact = "Major climate disruption"
        solution = "Promote energy-efficient buildings, promote sustainable agriculture, promote public transportation, and reduce reliance on fossil fuels."
    elif years > 10:
        impact = "Significant climate disruption"
        solution = "Promote carbon-neutral and carbon-negative technologies, reduce deforestation, promote renewable energy, and develop green cities."
    elif years > 5:
        impact = "Moderate climate disruption"
        solution = "Promote sustainable living through education and awareness, promote biodiversity conservation, and promote responsible use of natural resources."
    elif years > 1:
        impact = "Minor climate disruption"
        solution = "Promote recycling and waste reduction, promote clean energy, and promote sustainable tourism."
    else:
        impact = "No significant impact"
        solution = "Continue sustainable lifestyle choices and environmental conservation efforts."

    return years, months, days, hours, minutes, seconds, impact, solution
    

# Loop to update the clock face with the time remaining
while True:
    years, months, days, hours, minutes, seconds, impact, solution = time_remaining()
    if years < 0:
        clock.clear()
        clock.write("We've exceeded the climate threshold!", align="center", font=("Arial", 24, "normal"))
        break
    clock.clear()
    clock.write(f"{years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds left until {threshold} degree C threshold\nImpact: {impact}\nSolution:{solution}", align="center", font=("Arial", 10, "normal"))
    time.sleep(1) # Sleep for one second before updating


















