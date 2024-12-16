from tkinter import messagebox
from customtkinter import *
from PIL import Image
from web3 import Web3
from Web3Helper import Web3Helper
from register import create_register_frame
from DoctorDashboard import create_doctordash_frame
from PatientDashboard import create_patientdash_frame

# Initialize blockchain and IPFS clients
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545/'))  # Replace with your Ganache/RPC URL

# Initialize Web3 helper
web3_helper = Web3Helper()

# Add this near the top of your file, with other global variables
current_user_address = None
# Function to create the Doctor login view
def create_doctor_login_view(frame, main_frame):
    # Clear the previous view
    for widget in frame.winfo_children():
        widget.destroy()
    
    address_icon_data = Image.open("Images/user.png")
    password_icon_data = Image.open("Images/padlock.png")
    patient_icon_data = Image.open("Images/people.png")
    doctor_icon_data = Image.open("Images/doctor.png")
    
    address_icon = CTkImage(dark_image=address_icon_data, light_image=address_icon_data, size=(20, 20))
    password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))
    patient_icon = CTkImage(dark_image=patient_icon_data, light_image=patient_icon_data, size=(20, 20))
    doctor_icon = CTkImage(dark_image=doctor_icon_data, light_image=doctor_icon_data, size=(20, 20))
    # Add "Welcome Back!" label
    welcome_label = CTkLabel(
        master=frame,
        text="Welcome Back!",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 26),
    )
    welcome_label.place(x=220, y=160)

    # Add "Sign in to your account" label
    sign_in_label = CTkLabel(
        master=frame,
        text="Sign in to your account",
        text_color="#7E7E7E",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12),
    )
    sign_in_label.place(x=250, y=200)
        # Create buttons to switch between Doctor and Patient
    doctor_button = CTkButton(
        master=frame,
        text="Doctor",
        command=lambda: switch_login_view("doctor", frame, main_frame),
        image=doctor_icon,
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
    )
    doctor_button.place(x=160, y=250)

    patient_button = CTkButton(
        master=frame,
        text="Patient",
        command=lambda: switch_login_view("patient", frame, main_frame),
        image=patient_icon,
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
    )
    patient_button.place(x=320, y=250)
    # Disable buttons appropriately
    patient_button.configure(state="normal")
    doctor_button.configure(state="disabled")
    # Add Address label and entry
    address_label = CTkLabel(
        master=frame,
        text="  Address:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=address_icon,
        compound="left",
    )
    address_label.place(x=160, y=300)

    address_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    address_entry.place(x=160, y=330)

    # Add Password label and entry
    password_label = CTkLabel(
        master=frame,
        text="  Password:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=password_icon,
        compound="left",
    )
    password_label.place(x=160, y=380)

    password_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
        show="*",
    )
    password_entry.place(x=160, y=410)
def login_user(address, password, user_type="doctor"):
    """Handle user login"""
    global current_user_address
    if not address or not password:
        messagebox.showerror("Error", "Please fill in all fields")
        return
        
    if not Web3.is_address(address):
        messagebox.showerror("Error", "Invalid Ethereum address")
        return
        
    if user_type == "doctor":
        success, message = web3_helper.login_doctor(address, password)
        if success:
            # Store the address in session
            
            current_user_address = address
            switch_to_doctordash(app, main_frame)
        else:
            messagebox.showerror("Error", message)
            
    else:  # patient
        success, message = web3_helper.login_patient(address, password)
        if success:
            
            current_user_address = address
            switch_to_patientdash(app, main_frame)
        else:
            messagebox.showerror("Error", message)
    # Add Login button
    login_button = CTkButton(
        master=frame,
        text="Login",
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
        text_color="#ffffff",
        width=300,
        # command=lambda: switch_to_doctordash(app, main_frame),
        command=lambda: login_user(address_entry.get(), password_entry.get()),
    )
    login_button.place(x=160, y=470)
    register_label = CTkLabel(
        master=frame,
        text="Don't have an account yet ?",
        text_color="#7E7E7E",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12),
    )
    register_label.place(x=200, y=510)
    register_label2 = CTkLabel(
        master=frame,
        text="Register",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12, "underline"),
        cursor="hand2",
    )
    register_label2.place(x=360, y=510)
    # Function to underline the label text on hover
    def on_hover(event):
      register_label2.configure(
         text="Register",  # Ensure consistent text
        text_color="#601E88",  # Hover color
        font=("Arial Bold", 12, "underline"),  # Add underline
      )

    # Function to remove the underline when not hovering
    def on_leave(event):
     register_label2.configure(
        text="Register",
        text_color="#0080FF",  # Original color
        font=("Arial Bold", 12, "underline"),  # Remove underline
     )

    # Bind the label to the click event
    register_label2.bind("<Button-1>", lambda event: switch_to_register(app, main_frame))

    # Bind hover effects
    register_label2.bind("<Enter>", on_hover)  # Mouse enters the label
    register_label2.bind("<Leave>", on_leave)  # Mouse leaves the label



# Function to create Patient login view
def create_patient_login_view(frame,main_frame):
    # Clear the previous view
    for widget in frame.winfo_children():
        widget.destroy()
    
    address_icon_data = Image.open("Images/user.png")
    password_icon_data = Image.open("Images/padlock.png")
    patient_icon_data = Image.open("Images/people.png")
    doctor_icon_data = Image.open("Images/doctor.png")
    
    address_icon = CTkImage(dark_image=address_icon_data, light_image=address_icon_data, size=(20, 20))
    password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))
    patient_icon = CTkImage(dark_image=patient_icon_data, light_image=patient_icon_data, size=(20, 20))
    doctor_icon = CTkImage(dark_image=doctor_icon_data, light_image=doctor_icon_data, size=(20, 20))
    # Add "Welcome Back!" label
    welcome_label = CTkLabel(
        master=frame,
        text="Welcome Back!",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 26),
    )
    welcome_label.place(x=220, y=160)

    # Add "Sign in to your account" label
    sign_in_label = CTkLabel(
        master=frame,
        text="Sign in to your account",
        text_color="#7E7E7E",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12),
    )
    sign_in_label.place(x=250, y=200)
        # Create buttons to switch between Doctor and Patient
    doctor_button = CTkButton(
        master=frame,
        text="Doctor",
        command=lambda: switch_login_view("doctor", frame, main_frame),
        image=doctor_icon,
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
    )
    doctor_button.place(x=160, y=250)

    patient_button = CTkButton(
        master=frame,
        text="Patient",
        command=lambda: switch_login_view("patient", frame, main_frame),
        image=patient_icon,
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
    )
    patient_button.place(x=320, y=250)
    # Disable buttons appropriately
    patient_button.configure(state="disabled")
    doctor_button.configure(state="normal")
    # Add Address label and entry
    address_label = CTkLabel(
        master=frame,
        text="  Address:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=address_icon,
        compound="left",
    )
    address_label.place(x=160, y=300)

    address_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    address_entry.place(x=160, y=330)

    # Add Password label and entry
    password_label = CTkLabel(
        master=frame,
        text="  Password:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=password_icon,
        compound="left",
    )
    password_label.place(x=160, y=380)

    password_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
        show="*",
    )
    password_entry.place(x=160, y=410)

    # Add Login button
    login_button = CTkButton(
        master=frame,
        text="Login",
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
        text_color="#ffffff",
        width=300,
        command=lambda: login_user(address_entry.get(), password_entry.get()),
    )
    login_button.place(x=160, y=470)


# Function to dynamically switch between the Doctor and Patient login views
def switch_login_view(view_type, content_frame, main_frame):
    if view_type == "doctor":
        create_doctor_login_view(content_frame, main_frame) 
    elif view_type == "patient":
        create_patient_login_view(content_frame, main_frame)

def create_login_frame(app):
    side_img_data = Image.open("Images/doctorpatientlogin.jpg")
    address_icon_data = Image.open("Images/user.png")
    password_icon_data = Image.open("Images/padlock.png")
    patient_icon_data = Image.open("Images/people.png")
    doctor_icon_data = Image.open("Images/doctor.png")

    side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(600, 800))
    address_icon = CTkImage(dark_image=address_icon_data, light_image=address_icon_data, size=(20, 20))
    password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))
    patient_icon = CTkImage(dark_image=patient_icon_data, light_image=patient_icon_data, size=(20, 20))
    doctor_icon = CTkImage(dark_image=doctor_icon_data, light_image=doctor_icon_data, size=(20, 20))

    main_frame = CTkFrame(master=app, width=1200, height=800)
    main_frame.place(x=0, y=0)
    # Add side image label
    side_label = CTkLabel(master=main_frame, text="", image=side_img)
    side_label.place(x=0, y=0)

    # Create frame for login form
    frame = CTkFrame(master=main_frame, width=600, height=800, fg_color="#ffffff")
    frame.place(x=600, y=0)

    # Add "Welcome Back!" label
    welcome_label = CTkLabel(
        master=frame,
        text="Welcome Back!",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 26),
    )
    welcome_label.place(x=220, y=160)

    # Add "Sign in to your account" label
    sign_in_label = CTkLabel(
        master=frame,
        text="Sign in to your account",
        text_color="#7E7E7E",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12),
    )
    sign_in_label.place(x=250, y=200)
        # Create buttons to switch between Doctor and Patient
    doctor_button = CTkButton(
        master=frame,
        text="Doctor",
        command=lambda: switch_login_view("doctor", frame, main_frame),
        image=doctor_icon,
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
    )
    doctor_button.place(x=160, y=250)

    patient_button = CTkButton(
        master=frame,
        text="Patient",
        command=lambda: switch_login_view("patient", frame, main_frame),
        image=patient_icon,
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
    )
    patient_button.place(x=320, y=250)
    # Disable buttons appropriately
    patient_button.configure(state="normal")
    doctor_button.configure(state="disabled")
    # Add Address label and entry
    address_label = CTkLabel(
        master=frame,
        text="  Address:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=address_icon,
        compound="left",
    )
    address_label.place(x=160, y=300)

    address_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    address_entry.place(x=160, y=330)

    # Add Password label and entry
    password_label = CTkLabel(
        master=frame,
        text="  Password:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=password_icon,
        compound="left",
    )
    password_label.place(x=160, y=380)

    password_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
        show="*",
    )
    password_entry.place(x=160, y=410)

    # Add Login button
    login_button = CTkButton(
        master=frame,
        text="Login",
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
        text_color="#ffffff",
        width=300,
        command=lambda: switch_to_doctordash(app, main_frame),
        
        
    )
    login_button.place(x=160, y=470)
    register_label = CTkLabel(
        master=frame,
        text="Don't have an account yet ?",
        text_color="#7E7E7E",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12),
    )
    register_label.place(x=200, y=510)
    register_label2 = CTkLabel(
        master=frame,
        text="Register",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12, "underline"),
        cursor="hand2",
    )
    register_label2.place(x=360, y=510)
    # Function to underline the label text on hover
    def on_hover(event):
      register_label2.configure(
         text="Register",  # Ensure consistent text
        text_color="#601E88",  # Hover color
        font=("Arial Bold", 12, "underline"),  # Add underline
      )

    # Function to remove the underline when not hovering
    def on_leave(event):
     register_label2.configure(
        text="Register",
        text_color="#0080FF",  # Original color
        font=("Arial Bold", 12, "underline"),  # Remove underline
     )

    # Bind the label to the click event
    register_label2.bind("<Button-1>", lambda event: switch_to_register(app, main_frame))

    # Bind hover effects
    register_label2.bind("<Enter>", on_hover)  # Mouse enters the label
    register_label2.bind("<Leave>", on_leave)  # Mouse leaves the label


def switch_to_register(main_app, main_frame):
    # Hide the main frame
    main_frame.place_forget()
    
    # Create and place the new frame
    create_register_frame(main_app, main_frame).place(x=200, y=0)

def switch_to_doctordash(main_app, main_frame):
    # Hide the main frame
    main_frame.place_forget()
    
    # Create and place the new frame
    create_doctordash_frame(main_app, main_frame).place(x=0, y=0)

def switch_to_patientdash(main_app, main_frame):
    # Hide the main frame
    main_frame.place_forget()
    
    # Create and place the new frame
    create_patientdash_frame(main_app, main_frame).place(x=0, y=0)


if __name__ == "__main__":
    app = CTk()
    app.title("Login")
    app.geometry("1200x800")
    app.resizable(0, 0)

    create_login_frame(app)

    app.mainloop()
