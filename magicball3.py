import tkinter as tk
import random
import time

# Define the list of Magic 8 Ball-style responses
responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# Define a variable to store the last question asked
last_question = ""

# Define a function to generate a Magic 8 Ball-style response
def generate_response():
    global last_question
    
    # Clear the previous response
    canvas.delete("response")
    
    # Check if the user has asked the same question twice in a row
    question = question_entry.get().strip()
    if question == last_question:
        response_label.config(text="Ask a different question")
        return
    
    # Update the label to display a message indicating that the Magic 8 Ball is generating a response
    response_label.config(text="Magic 8 Ball is doing its magic...")
    root.update()
    
    # Wait for 2 seconds before generating a response
    time.sleep(2)
    
    prediction = random.choice(responses)
    
    # Create a blue triangle to display the response
    triangle_coords = (img_width/2-100, img_height/2+100, img_width/2+100, img_height/2+100, img_width/2, img_height/2)
    triangle = canvas.create_polygon(triangle_coords, fill="blue", outline="white", width=3, tags="response")
    animate_triangle(triangle)
    canvas.create_text(img_width/2, img_height/2+90, text=prediction, fill="white", font=("Arial", 14), justify="center", tags="response")
    
    # Update the last_question variable
    last_question = question
    
    # Clear the question entry widget
    question_entry.delete(0, tk.END)
    
    # Set the text of the response label to an empty string
    response_label.config(text="")


# Define a function to animate the blue triangle
def animate_triangle(triangle, i=0):
    if i < 10:
        # Set the color of the rectangle to a shade of blue
        color = "#0000" + hex(51+i*20)[2:] # shade of blue based on i
        canvas.itemconfig(triangle, fill=color)
        
        # Set the opacity of the rectangle to decrease with each iteration
        alpha = (10-i)/10.0
        canvas.itemconfig(triangle, outline="", tags="triangle")
        canvas.itemconfigure("triangle", fill=color, outline="", stipple="gray50")
        
        # Schedule the next update
        canvas.after(100, animate_triangle, triangle, i+1)

# Create the main window
root = tk.Tk()
root.title("Magic 8 Ball")

# Load the Magic 8 Ball image and get its size
img = tk.PhotoImage(file="magic8ball.gif")
img_width = img.width()
img_height = img.height()

# Create a canvas to display the Magic 8 Ball image
canvas = tk.Canvas(root, width=img_width, height=img_height)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=img)

# Create a text box for the user to input their question
question_entry = tk.Entry(root, width=30)
question_entry.pack(pady=10)

# Create a button to generate a response
button = tk.Button(root, text="Ask the Magic 8 Ball!", command=generate_response)
button.pack(pady=10)

# Create a label to display the response
response_label = tk.Label(root, text="")
response_label.pack()

# Run the GUI
root.mainloop()
