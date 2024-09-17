import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.title("Flashcards")
root.geometry("800x600")
root.configure(bg='#2e2e2e')

# Sample flashcards data for biology (ai made questions )
one_marker_flashcards = [
    {"question": "Which word means a change in the environment? [1 mark]\n\nA. Neurone\nB. Reflex\nC. Stimulus", "answer": "C. Stimulus"},
    {"question": "Give two examples of effectors. Select the two correct answers. [2 marks]\n\nA. Glands\nB. Muscles\nC. Neurones\nD. Synapse", "answer": "A. Glands, B. Muscles"},
    {"question": "What type or types of neurone carry electrical signals towards the central nervous system?\n\nA. Sensory\nB. Relay\nC. Motor\nD. All three", "answer": "A. Sensory"},
    {"question": "What is the function of neurons?", "answer": "Neurons transmit nerve impulses."},
    {"question": "What part of the brain controls movement?", "answer": "The cerebellum controls movement."},
    {"question": "What is the main function of the eye?", "answer": "The eye detects light and converts it into neural signals."},
    {"question": "What is the role of the cochlea in the ear?", "answer": "The cochlea converts sound waves into nerve impulses."},
    {"question": "What is the basic unit of life?", "answer": "The cell is the basic unit of life."},
    {"question": "What is the function of the optic nerve?", "answer": "The optic nerve transmits visual information from the retina to the brain."},
    {"question": "What part of the brain is responsible for memory?", "answer": "The hippocampus is responsible for memory."},
    {"question": "What is the function of the auditory nerve?", "answer": "The auditory nerve carries sound information from the cochlea to the brain."},
    {"question": "What are neurotransmitters?", "answer": "Neurotransmitters are chemicals that transmit signals across synapses between neurons."},
    {"question": "What is the function of the retina?", "answer": "The retina detects light and converts it into neural signals."},
    {"question": "What part of the brain regulates heartbeat and breathing?", "answer": "The medulla oblongata regulates heartbeat and breathing."},
    {"question": "What is the role of Schwann cells?", "answer": "Schwann cells produce the myelin sheath around neuronal axons."},
    {"question": "What is the function of the lens in the eye?", "answer": "The lens focuses light onto the retina."},
    {"question": "What is a synapse?", "answer": "A synapse is a junction between two neurons where signals are transmitted."},
    {"question": "What is the function of rods in the retina?", "answer": "Rods are responsible for vision in low light conditions."},
    {"question": "What is the role of the hypothalamus?", "answer": "The hypothalamus regulates various autonomic functions, including hunger, thirst, and body temperature."},
    {"question": "What is the function of the eardrum?", "answer": "The eardrum vibrates in response to sound waves and transmits these vibrations to the ossicles."},
    {"question": "What are the ossicles?", "answer": "The ossicles are three tiny bones in the middle ear that transmit sound vibrations from the eardrum to the cochlea."},
    {"question": "What is the function of the semicircular canals?", "answer": "The semicircular canals are responsible for maintaining balance and detecting head movement."},
    {"question": "What is an axon?", "answer": "An axon is a long, slender projection of a neuron that conducts electrical impulses away from the neuron's cell body."}
]

six_marker_flashcards = [
    {"question": "Describe what happens at a synapse. [6 marks]", "answer": """
        Where two neurones meet there is a small gap, a synapse.
        An electrical impulse travels along the first axon.
        This triggers the nerve-ending of a neurone to release chemical messengers called neurotransmitters into the synapse.
        These chemicals diffuse across the synapse (the gap) and bind with receptor molecules on the membrane of the second neurone.
        The receptor molecules on the second neurone bind only to the specific neurotransmitters released from the first neurone.
        This stimulates the second neurone to transmit the electrical impulse.
    """},
    {"question": "The diagram shows a bee flying towards a man's eye. Describe the pathway taken by the nerve impulse in the blink reflex. Explain why we have this reflex. [6 marks]", "answer": """
        Light from the bee enters the eye/hits the retina.
        (Electrical) impulses go from light-sensitive cells to the sensory neurone/optic nerve.
        The sensory neurone/optic nerve connects to the brain or CNS (central nervous system).
        The brain or CNS (relay neurone or spinal cord is accepted) connects to the motor neurone.
        The motor neurone connects to the eyelid muscle.
        The eyelid muscle makes the eye blink.
        The main reason for this blink reflex is the protection of the eye.
    """},
    {"question": "A person accidentally touches a hot pan. Describe fully how the structures shown in the diagram bring about this reflex action. [6 marks]", "answer": """
        Stimulus / heat detected by temperature receptors in skin.
        Impulses travel along sensory neurone to spinal cord / CNS.
        Chemical transmission across synapse.
        Via relay neurone.
        Impulses to muscle / effector via motor neurone.
        Muscle / effector contracts, moving the hand away.
    """}
]

current_flashcard_index = 0
current_flashcards = []

# Function to clear the window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Function to show the main menu
def show_main_menu():
    clear_window()
    main_menu_frame = ttk.Frame(root, style="Dark.TFrame")
    main_menu_frame.pack(expand=True)

    ttk.Label(main_menu_frame, text="Select Topic", font=("Helvetica", 20), background='#2e2e2e', foreground='white').pack(pady=20)
    
    topics = ["Biology"]
    for topic in topics:
        ttk.Button(main_menu_frame, text=topic, command=lambda t=topic: show_topic_options(t), style="Dark.TButton").pack(pady=10)

# Function to show the options for the selected topic
def show_topic_options(topic):
    clear_window()
    options_frame = ttk.Frame(root, style="Dark.TFrame")
    options_frame.pack(expand=True)

    ttk.Label(options_frame, text=f"Select Question Type for {topic}", font=("Helvetica", 20), background='#2e2e2e', foreground='white').pack(pady=20)
    
    question_types = ["1 Marker Questions", "Full Paragraph Questions"]
    for qtype in question_types:
        ttk.Button(options_frame, text=qtype, command=lambda qt=qtype: show_flashcards(topic, qt), style="Dark.TButton").pack(pady=10)

# Function to show flashcards based on topic and question type
def show_flashcards(topic, question_type):
    clear_window()
    global current_flashcards
    if topic == "Biology":
        if question_type == "1 Marker Questions":
            current_flashcards = one_marker_flashcards
        elif question_type == "Full Paragraph Questions":
            current_flashcards = six_marker_flashcards
    
    global current_flashcard_index
    current_flashcard_index = 0
    display_flashcard(random.choice(current_flashcards))

# Function to display a flashcard
def display_flashcard(flashcard):
    clear_window()
    
    flashcard_frame = ttk.Frame(root, style="Dark.TFrame")
    flashcard_frame.pack(expand=True)

    ttk.Label(flashcard_frame, text=flashcard["question"], font=("Helvetica", 16), wraplength=700, background='#2e2e2e', foreground='white').pack(pady=20)

    ttk.Button(flashcard_frame, text="Show Answer", command=lambda: show_answer(flashcard), style="Dark.TButton").pack(pady=10)
    ttk.Button(flashcard_frame, text="Next", command=next_flashcard, style="Dark.TButton").pack(side="left", padx=10)
    ttk.Button(flashcard_frame, text="Previous", command=prev_flashcard, style="Dark.TButton").pack(side="right", padx=10)
    ttk.Button(flashcard_frame, text="Back to Menu", command=show_main_menu, style="Dark.TButton").pack(pady=20)

# Function to show the answer of a flashcard
def show_answer(flashcard):
    clear_window()
    
    flashcard_frame = ttk.Frame(root, style="Dark.TFrame")
    flashcard_frame.pack(expand=True)

    ttk.Label(flashcard_frame, text=flashcard["question"], font=("Helvetica", 16), wraplength=700, background='#2e2e2e', foreground='white').pack(pady=20)
    ttk.Label(flashcard_frame, text=flashcard["answer"], font=("Helvetica", 14), wraplength=700, background='#2e2e2e', foreground='white').pack(pady=20)

    ttk.Button(flashcard_frame, text="Next", command=next_flashcard, style="Dark.TButton").pack(side="left", padx=10)
    ttk.Button(flashcard_frame, text="Previous", command=prev_flashcard, style="Dark.TButton").pack(side="right", padx=10)
    ttk.Button(flashcard_frame, text="Back to Menu", command=show_main_menu, style="Dark.TButton").pack(pady=20)

# Function to navigate to the next flashcard
def next_flashcard():
    global current_flashcard_index
    current_flashcard_index = (current_flashcard_index + 1) % len(current_flashcards)
    display_flashcard(current_flashcards[current_flashcard_index])

# Function to navigate to the previous flashcard
def prev_flashcard():
    global current_flashcard_index
    current_flashcard_index = (current_flashcard_index - 1) % len(current_flashcards)
    display_flashcard(current_flashcards[current_flashcard_index])

# Define custom styles
style = ttk.Style()
style.configure("Dark.TFrame", background='#2e2e2e')
style.configure("Dark.TButton", background='#4a4a4a', foreground='white', font=("Helvetica", 12))
style.map("Dark.TButton",
    background=[('active', 'white')],
    foreground=[('active', 'white')]
)

show_main_menu()
root.mainloop()
