from tkinter import messagebox
from customtkinter import *
from PIL import Image
from web3 import Web3
from eth_account import Account
from Web3Helper import Web3Helper


def create_register_frame(app, current_frame):
    # Create the main scrollable frame with custom styles and positioning
    frame = CTkFrame(app, width=800, height=800, fg_color="#ffffff")  # White background
    address_icon_data = Image.open("Images/user.png")
    password_icon_data = Image.open("Images/padlock.png")
    dob_icon_data = Image.open("Images/date-of-birth.png")
    pob_icon_data = Image.open("Images/placeholder.png")
    name_icon_data = Image.open("Images/label.png")
    id_icon_data = Image.open("Images/id.png")
    phone_icon_data = Image.open("Images/telephone.png")
    speciality_icon_data = Image.open("Images/medicine.png")
    sexe_icon_data = Image.open("Images/sex.png")
    cin_icon_data = Image.open("Images/id-card.png")
    doc_icon_data = Image.open("Images/doctor2.png")
    back_icon_data = Image.open("Images/back-arrow.png")

    address_icon = CTkImage(dark_image=address_icon_data, light_image=address_icon_data, size=(20, 20))
    password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))
    dob_icon = CTkImage(dark_image=dob_icon_data, light_image=dob_icon_data, size=(20, 20))
    pob_icon = CTkImage(dark_image=pob_icon_data, light_image=pob_icon_data, size=(20, 20))    
    name_icon = CTkImage(dark_image=name_icon_data, light_image=name_icon_data, size=(20, 20))    
    id_icon = CTkImage(dark_image=id_icon_data, light_image=id_icon_data, size=(20, 20))    
    phone_icon = CTkImage(dark_image=phone_icon_data, light_image=phone_icon_data, size=(20, 20))
    speciality_icon = CTkImage(dark_image=speciality_icon_data, light_image=speciality_icon_data, size=(20, 20))
    sexe_icon = CTkImage(dark_image=sexe_icon_data, light_image=sexe_icon_data, size=(20, 20))
    cin_icon = CTkImage(dark_image=cin_icon_data, light_image=cin_icon_data, size=(20, 20))
    doc_icon = CTkImage(dark_image=doc_icon_data, light_image=doc_icon_data, size=(60, 60))
    back_icon = CTkImage(dark_image=back_icon_data, light_image=back_icon_data, size=(20, 20))

    back_button = CTkButton(
        master=frame,
        text="Back",
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
        image=back_icon,
        text_color="#ffffff",
        width=100,
        command=lambda: back_to_login(current_frame, frame),
        
    )
    back_button.place(relx=0.10, rely=0.05)

        
    CTkLabel(
        master=frame,
        text="",
        text_color="#1E90FF",  # Dodger blue
        anchor="w",
        image=doc_icon,
        justify="left",
        font=("Arial Bold", 32)
    ).place(relx=0.45, rely=0.07)

    # Add the title label
    CTkLabel(
        master=frame,
        text="Registration form",
        text_color="#1E90FF",  # Dodger blue
        anchor="w",
        justify="left",
        font=("Arial Black", 32)
    ).place(relx=0.31, rely=0.15)
       
    fn_label = CTkLabel(
        master=frame,
        text=" First Name:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=name_icon,
        compound="left",
    )
    fn_label.place(relx=0.1, rely=0.3)

    fn_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    fn_entry.place(relx=0.1, rely=0.34)
    ln_label = CTkLabel(
        master=frame,
        text=" Last Name:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=name_icon,
        compound="left",
    )
    ln_label.place(relx=0.50, rely=0.3)

    ln_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    ln_entry.place(relx=0.50, rely=0.34)

    bd_label = CTkLabel(
        master=frame,
        text=" Birthday:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=dob_icon,
        compound="left",
    )
    bd_label.place(relx=0.10, rely=0.4)

    bd_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    bd_entry.place(relx=0.10, rely=0.44)

    pob_label = CTkLabel(
        master=frame,
        text=" Place of Birth:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=pob_icon,
        compound="left",
    )
    pob_label.place(relx=0.50, rely=0.4)

    pob_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    pob_entry.place(relx=0.50, rely=0.44)

    pnumber_label = CTkLabel(
        master=frame,
        text=" Phone Number:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=phone_icon,
        compound="left",
    )
    pnumber_label.place(relx=0.10, rely=0.5)

    pnumber_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    pnumber_entry.place(relx=0.10, rely=0.54)

    sexe_label = CTkLabel(
        master=frame,
        text=" Sexe:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=sexe_icon,
        compound="left",
    )
    sexe_label.place(relx=0.50, rely=0.5)

    optionmenu = CTkComboBox(frame, values=["Male", "Female"],
                                         width=150,button_color="#0080FF", border_color="#0080FF", border_width=2, button_hover_color="#207244",
                dropdown_hover_color="#E44982", dropdown_fg_color="#0080FF", dropdown_text_color="#fff")
    
    optionmenu.place(relx=0.50, rely=0.54)

    cin_label = CTkLabel(
        master=frame,
        text=" CIN:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=cin_icon,
        compound="left",
    )
    cin_label.place(relx=0.70, rely=0.5)

    cin_entry = CTkEntry(
        master=frame,
        width=150,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    cin_entry.place(relx=0.70, rely=0.54)

    wa_label = CTkLabel(
        master=frame,
        text=" Wallet Address:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=address_icon,
        compound="left",
    )
    wa_label.place(relx=0.10, rely=0.6)

    wa_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    wa_entry.place(relx=0.10, rely=0.64)

    did_label = CTkLabel(
        master=frame,
        text=" Doctor ID:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=id_icon,
        compound="left",
    )
    did_label.place(relx=0.50, rely=0.6)

    did_entry = CTkEntry(
        master=frame,
        width=150,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    did_entry.place(relx=0.50, rely=0.64)

    spe_label = CTkLabel(
        master=frame,
        text=" Speciality:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=speciality_icon,
        compound="left",
    )
    spe_label.place(relx=0.70, rely=0.6)

    spe_entry = CTkEntry(
        master=frame,
        width=150,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    spe_entry.place(relx=0.70, rely=0.64)

    pass_label = CTkLabel(
        master=frame,
        text=" Password:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=password_icon,
        compound="left",
    )
    pass_label.place(relx=0.10, rely=0.7)

    pass_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
        show="*",
    )
    pass_entry.place(relx=0.10, rely=0.74)

    confpass_label = CTkLabel(
        master=frame,
        text=" Confirm Password:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=password_icon,
        compound="left",
    )
    confpass_label.place(relx=0.50, rely=0.7)

    confpass_entry = CTkEntry(
        master=frame,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
        show="*",
    )
    confpass_entry.place(relx=0.50, rely=0.74)
        
    register_button = CTkButton(
        master=frame,
        text="Register",
        fg_color="#0080FF",
        hover_color="#E44982",
        font=("Arial Bold", 12),
        text_color="#ffffff",
        width=150,
    )


    def validate_and_register():
        # Get all form values
        first_name = fn_entry.get().strip()
        last_name = ln_entry.get().strip()
        birthday = bd_entry.get().strip()
        place_of_birth = pob_entry.get().strip()
        phone = pnumber_entry.get().strip()
        gender = optionmenu.get()
        cin = cin_entry.get().strip()
        wallet_address = wa_entry.get().strip()
        doctor_id = did_entry.get().strip()
        speciality = spe_entry.get().strip()
        password = pass_entry.get()
        confirm_password = confpass_entry.get()
        
        # Validate required fields
        if not all([first_name, last_name, birthday, place_of_birth, 
                gender, cin, wallet_address, speciality, 
                password, confirm_password]):
            messagebox.showerror("Error", "All required fields must be filled")
            return
            
        # Validate password match
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return
            
        # Validate wallet address format
        if not Web3.is_address(wallet_address):
            messagebox.showerror("Error", "Invalid wallet address format")
            return
            
        try:
            # Initialize Web3Helper
            web3_helper = Web3Helper()
            
            # Create new account or import existing one
            account = Account.from_key(password)  # Assuming password is the private key for testing
            wallet_address = account.address
            
            # Attempt to register the doctor
            success, message = web3_helper.register_doctor(
                password,  # This should be the private key
                wallet_address,
                first_name,
                last_name,
                birthday,
                gender,
                place_of_birth,
                cin,
                speciality
            )
            
            if success:
                messagebox.showinfo("Success", "Doctor registered successfully!")
                # Return to login screen
                back_to_login(current_frame, frame)
            else:
                messagebox.showerror("Error", message)
                
        except ValueError as ve:
            messagebox.showerror("Error", "Invalid private key format. Please check your password/private key.")
        except Exception as e:
            messagebox.showerror("Error", f"Registration failed: {str(e)}")
    
    # Update register button command
    register_button.configure(command=validate_and_register)
    register_button.place(relx=0.40, rely=0.85)
    return frame


def back_to_login(current_frame, frame):
    # Hide the current registration frame and show the login screen
    frame.place_forget()
    current_frame.place(x=0, y=0)
