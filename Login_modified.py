from tkinter import messagebox
from customtkinter import *
from PIL import Image
from web3 import Web3
from Web3Helper import Web3Helper
from register import create_register_frame
from DoctorDashboard import create_doctordash_frame
from PatientDashboard import create_patientdash_frame

# Initialize Web3 helper
web3_helper = Web3Helper()

# Global variable to store current user's address
current_user_address = None
current_user_private_key = None
def login_user(address, password, app, main_frame, user_type="doctor"):
    """Handle user login with Web3 integration"""
    global current_user_address
    global current_user_private_key
    if not address or not password:
        messagebox.showerror("Error", "Please fill in all fields")
        return
        
    if not Web3.is_address(address):
        messagebox.showerror("Error", "Invalid Ethereum address")
        return
        
    try:
        if user_type == "doctor":
            success, message = web3_helper.login_doctor(password, address)
            if success:
                current_user_address = address
                current_user_private_key = password
                # Get doctor details from contract
                doctor_details = web3_helper.get_doctor_details(address)
                # Store details if needed for dashboard
                switch_to_doctordash(app, main_frame)
            else:
                messagebox.showerror("Login Failed", message)
        else:  # patient
            success, message = web3_helper.login_patient(password, address)
            if success:
                current_user_address = address
                current_user_private_key = password
                # Get patient details from contract
                patient_details = web3_helper.get_patient_details(address)
                # Store details if needed for dashboard
                switch_to_patientdash(app, main_frame)
            else:
                messagebox.showerror("Login Failed", message)
    except Exception as e:
        messagebox.showerror("Error", f"Login failed: {str(e)}")

def create_doctor_login_view(frame, main_frame):
    """Create the doctor login view"""
    # Clear the previous view
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Load icons
    address_icon_data = Image.open("Images/user.png")
    password_icon_data = Image.open("Images/padlock.png")
    patient_icon_data = Image.open("Images/people.png")
    doctor_icon_data = Image.open("Images/doctor.png")
    
    address_icon = CTkImage(dark_image=address_icon_data, light_image=address_icon_data, size=(20, 20))
    password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))
    patient_icon = CTkImage(dark_image=patient_icon_data, light_image=patient_icon_data, size=(20, 20))
    doctor_icon = CTkImage(dark_image=doctor_icon_data, light_image=doctor_icon_data, size=(20, 20))

    # UI Components
    welcome_label = CTkLabel(
        master=frame,
        text="Doctor Login",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 26)
    )
    welcome_label.place(x=220, y=160)

    sign_in_label = CTkLabel(
        master=frame,
        text="Sign in with your Ethereum address",
        text_color="#7E7E7E",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12)
    )
    sign_in_label.place(x=230, y=200)

    # Toggle buttons
    doctor_button = CTkButton(
        master=frame,
        text="Doctor",
        command=lambda: switch_login_view("doctor", frame, main_frame),
        image=doctor_icon,
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
        state="disabled"
    )
    doctor_button.place(x=160, y=250)

    patient_button = CTkButton(
        master=frame,
        text="Patient",
        command=lambda: switch_login_view("patient", frame, main_frame),
        image=patient_icon,
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12)
    )
    patient_button.place(x=320, y=250)

    # Address input
    address_label = CTkLabel(
        master=frame,
        text="  Ethereum Address:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=address_icon,
        compound="left"
    )
    address_label.place(x=160, y=300)

    address_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
        placeholder_text="0x..."
    )
    address_entry.place(x=160, y=330)

    # Password input
    password_label = CTkLabel(
        master=frame,
        text="  Password:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=password_icon,
        compound="left"
    )
    password_label.place(x=160, y=380)

    password_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
        show="*"
    )
    password_entry.place(x=160, y=410)

    # Login button
    login_button = CTkButton(
        master=frame,
        text="Login",
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
        text_color="#ffffff",
        width=300,
        command=lambda: login_user(address_entry.get(), password_entry.get(), app, main_frame, "doctor")
    )
    login_button.place(x=160, y=470)

    # Register section
    register_label = CTkLabel(
        master=frame,
        text="Don't have an account yet?",
        text_color="#7E7E7E",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12)
    )
    register_label.place(x=200, y=510)

    register_link = CTkLabel(
        master=frame,
        text="Register",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12, "underline"),
        cursor="hand2"
    )
    register_link.place(x=360, y=510)

    # Hover effects
    def on_hover(event):
        register_link.configure(
            text_color="#601E88",
            font=("Arial Bold", 12, "underline")
        )

    def on_leave(event):
        register_link.configure(
            text_color="#0080FF",
            font=("Arial Bold", 12, "underline")
        )

    register_link.bind("<Button-1>", lambda event: switch_to_register(app, main_frame))
    register_link.bind("<Enter>", on_hover)
    register_link.bind("<Leave>", on_leave)

def create_patient_login_view(frame, main_frame):
    """Create the patient login view"""
    # Clear the previous view
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Load icons
    address_icon_data = Image.open("Images/user.png")
    password_icon_data = Image.open("Images/padlock.png")
    patient_icon_data = Image.open("Images/people.png")
    doctor_icon_data = Image.open("Images/doctor.png")
    
    address_icon = CTkImage(dark_image=address_icon_data, light_image=address_icon_data, size=(20, 20))
    password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))
    patient_icon = CTkImage(dark_image=patient_icon_data, light_image=patient_icon_data, size=(20, 20))
    doctor_icon = CTkImage(dark_image=doctor_icon_data, light_image=doctor_icon_data, size=(20, 20))

    # UI Components
    welcome_label = CTkLabel(
        master=frame,
        text="Patient Login",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 26)
    )
    welcome_label.place(x=220, y=160)

    sign_in_label = CTkLabel(
        master=frame,
        text="Sign in with your Ethereum address",
        text_color="#7E7E7E",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12)
    )
    sign_in_label.place(x=230, y=200)

    # Toggle buttons
    doctor_button = CTkButton(
        master=frame,
        text="Doctor",
        command=lambda: switch_login_view("doctor", frame, main_frame),
        image=doctor_icon,
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12)
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
        state="disabled"
    )
    patient_button.place(x=320, y=250)

    # Address input
    address_label = CTkLabel(
        master=frame,
        text="  Ethereum Address:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=address_icon,
        compound="left"
    )
    address_label.place(x=160, y=300)

    address_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
        placeholder_text="0x..."
    )
    address_entry.place(x=160, y=330)

    # Password input
    password_label = CTkLabel(
        master=frame,
        text="  Password:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=password_icon,
        compound="left"
    )
    password_label.place(x=160, y=380)

    password_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
        show="*"
    )
    password_entry.place(x=160, y=410)

    # Login button
    login_button = CTkButton(
        master=frame,
        text="Login",
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
        text_color="#ffffff",
        width=300,
        command=lambda: login_user(address_entry.get(), password_entry.get(), app, main_frame, "patient")
    )
    login_button.place(x=160, y=470)

    # Register section
    register_label = CTkLabel(
        master=frame,
        text="Don't have an account yet?",
        text_color="#7E7E7E",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12)
    )
    register_label.place(x=200, y=510)

    register_link = CTkLabel(
        master=frame,
        text="Register",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 12, "underline"),
        cursor="hand2"
    )
    register_link.place(x=360, y=510)

    def on_hover(event):
        register_link.configure(
            text_color="#601E88",
            font=("Arial Bold", 12, "underline")
        )

    def on_leave(event):
        register_link.configure(
            text_color="#0080FF",
            font=("Arial Bold", 12, "underline")
        )

    register_link.bind("<Button-1>", lambda event: switch_to_register(app, main_frame))
    register_link.bind("<Enter>", on_hover)
    register_link.bind("<Leave>", on_leave)

def create_login_frame(app):
    """Create the main login frame"""
    # Load images
    side_img_data = Image.open("Images/doctorpatientlogin.jpg")
    side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(600, 800))

    # Create main frame
    main_frame = CTkFrame(master=app, width=1200, height=800)
    main_frame.place(x=0, y=0)

    # Add side image
    side_label = CTkLabel(master=main_frame, text="", image=side_img)
    side_label.place(x=0, y=0)

    # Create login form frame
    frame = CTkFrame(master=main_frame, width=600, height=800, fg_color="#ffffff")
    frame.place(x=600, y=0)

    # Create doctor login view by default
    create_doctor_login_view(frame, main_frame)

    return main_frame

def switch_login_view(view_type, content_frame, main_frame):
    """Switch between doctor and patient login views"""
    if view_type == "doctor":
        create_doctor_login_view(content_frame, main_frame)
    elif view_type == "patient":
        create_patient_login_view(content_frame, main_frame)

def switch_to_register(main_app, main_frame):
    """Switch to registration view"""
    main_frame.place_forget()
    create_register_frame(main_app, main_frame).place(x=200, y=0)

def switch_to_doctordash(main_app, main_frame):
    """Switch to doctor dashboard"""
    main_frame.place_forget()
    create_doctordash_frame(main_app, main_frame).place(x=0, y=0)

def switch_to_patientdash(main_app, main_frame):
    """Switch to patient dashboard"""
    main_frame.place_forget()
    create_patientdash_frame(main_app, main_frame).place(x=0, y=0)

if __name__ == "__main__":
    app = CTk()
    app.title("Login")
    app.geometry("1200x800")
    app.resizable(0, 0)

    create_login_frame(app)

    app.mainloop()