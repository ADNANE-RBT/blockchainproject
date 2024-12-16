from tkinter import messagebox
from customtkinter import *
from PIL import Image
import tkinter
from tkinter import StringVar
from Web3Helper import Web3Helper

def create_home_frame(main_view):
    # Clear the previous view
    for widget in main_view.winfo_children():
        widget.destroy()
    
    doc_icon_data = Image.open("Images/doctor2.png")
    doc_icon = CTkImage(dark_image=doc_icon_data, light_image=doc_icon_data, size=(77.68, 85.42))

    clients_img_data = Image.open("Images/patient.png")
    clients_img = CTkImage(dark_image=clients_img_data, light_image=clients_img_data, size=(30, 30))

    home_img_data = Image.open("Images/home.png")
    home_img = CTkImage(dark_image=home_img_data, light_image=home_img_data, size=(30, 30))

    history_img_data = Image.open("Images/file.png")
    history_img = CTkImage(dark_image=history_img_data, light_image=history_img_data, size=(30, 30))

    logout_img_data = Image.open("Images/exit.png")
    logout_img = CTkImage(dark_image=logout_img_data, light_image=logout_img_data, size=(30, 30))
    

    title_frame = CTkFrame(master=main_view, fg_color="transparent", width=846, height=50)
    title_frame.place(x=27, y=29)

    CTkLabel(master=title_frame, text="Home", font=("Arial Black", 25), text_color="#0080FF").place(relx=0.47, rely=0)



    metrics_frame = CTkFrame(master=main_view, fg_color="transparent", width=846, height=60)
    metrics_frame.place(x=27, y=115)



    doctor_metric = CTkFrame(master=metrics_frame, fg_color="#0080FF", width=200, height=60)
    doctor_metric.place(x=220, y=0)

    doctor_img_data = Image.open("Images/doctor.png")
    doctor_img = CTkImage(light_image=doctor_img_data, dark_image=doctor_img_data, size=(43, 43))

    CTkLabel(master=doctor_metric, image=doctor_img, text="").place(x=12, y=10)
    CTkLabel(master=doctor_metric, text="Doctors", text_color="#fff", font=("Arial Black", 15)).place(x=60, y=10)
    CTkLabel(master=doctor_metric, text="9", text_color="#fff", font=("Arial Black", 15), justify="left").place(x=60, y=35)

    client_metric = CTkFrame(master=metrics_frame, fg_color="#0080FF", width=200, height=60)
    client_metric.place(x=440, y=0)

    client_img_data = Image.open("Images/patient.png")
    client_img = CTkImage(light_image=client_img_data, dark_image=client_img_data, size=(43, 43))

    CTkLabel(master=client_metric, image=client_img, text="").place(x=12, y=10)
    CTkLabel(master=client_metric, text="Patients", text_color="#fff", font=("Arial Black", 15)).place(x=60, y=10)
    CTkLabel(master=client_metric, text="23", text_color="#fff", font=("Arial Black", 15), justify="left").place(x=60, y=35)

    search_container = CTkFrame(master=main_view, fg_color="#F0F0F0", width=846, height=50)
    search_container.place(x=27, y=200)

    CTkEntry(master=search_container, width=365, placeholder_text="Search Patient", border_color="#0080FF", border_width=2).place(x=13, y=10)

    CTkComboBox(master=search_container, width=125, values=[" ", "My Patients", "Others"],
                button_color="#0080FF", border_color="#0080FF", border_width=2, button_hover_color="#E44982",
                dropdown_hover_color="#E44982", dropdown_fg_color="#0080FF", dropdown_text_color="#fff").place(x=390, y=10)

    CTkComboBox(master=search_container, width=125, values=[" ", "Alive", "Dead"],
                button_color="#0080FF", border_color="#0080FF", border_width=2, button_hover_color="#E44982",
                dropdown_hover_color="#E44982", dropdown_fg_color="#0080FF", dropdown_text_color="#fff").place(x=530, y=10)
    
    CTkButton(master=search_container, text="Search", font=("Arial Black", 15), text_color="#fff", fg_color="#0080FF", 
              hover_color="#E44982", width=125).place(x=670, y=10)
        # Create a scrollable frame for patients
    patientsframe = CTkScrollableFrame(master=main_view, fg_color="#F0F0F0", width=825, height=500)
    patientsframe.place(x=27, rely=0.34)

    


def create_Client_frame(main_view):
    # Clear the previous view
    for widget in main_view.winfo_children():
        widget.destroy()

    title_frame = CTkFrame(master=main_view, fg_color="transparent", width=846, height=50)
    title_frame.place(x=27, y=29)

    CTkLabel(master=title_frame, text="Patients", font=("Arial Black", 25), text_color="#0080FF").place(relx=0.47, rely=0)

    CTkButton(master=title_frame, text="+ Add Patient", font=("Arial Black", 15), text_color="#fff", fg_color="#0080FF", 
              hover_color="#E44982", width=120, height=40,command=lambda: create_addpatient_frame(main_view)).place(x=700, y=0)
    

    patients_data = [
        {"name": "John Doe", "age": 45, "status": "Alive"},
        {"name": "Jane Smith", "age": 36, "status": "Alive"},
        {"name": "Michael Brown", "age": 50, "status": "Dead"},
        {"name": "Emily Davis", "age": 29, "status": "Alive"},

     ]



    # Create a scrollable frame for patients
    patientsframe = CTkScrollableFrame(master=main_view, fg_color="#F0F0F0", width=825, height=650)
    patientsframe.place(x=27, y=115)

    # Configure grid layout
    patientsframe.grid_rowconfigure(0, weight=1)
    for col in range(4):  # 4 columns for Full Name, Age, Status, Action
        patientsframe.grid_columnconfigure(col, weight=1)

# Define column widths
    column_widths = [300, 100, 150, 150]  # Adjust these widths as needed

# Add header row
    header_font = ("Arial Black", 20)
    CTkLabel(patientsframe, text="Full Name", font=header_font, anchor="w", text_color="#0080FF", width=column_widths[0]).grid(
    row=0, column=0, padx=15, pady=15, sticky="w"
)
    CTkLabel(patientsframe, text="Age", font=header_font, anchor="center", text_color="#0080FF", width=column_widths[1]).grid(
    row=0, column=1, padx=5, pady=15, sticky="w"
)
    CTkLabel(patientsframe, text="Status", font=header_font, anchor="center", text_color="#0080FF", width=column_widths[2]).grid(
    row=0, column=2, padx=5, pady=15, sticky="w"
)
    CTkLabel(patientsframe, text="Action", font=header_font, anchor="center", text_color="#0080FF", width=column_widths[3]).grid(
    row=0, column=3, padx=5, pady=15, sticky="w"
)

# Add rows for patients
    row_font = ("Arial Bold", 16)
    for i, patient in enumerate(patients_data):
     row_frame = CTkFrame(patientsframe, fg_color="#FFFFFF", corner_radius=5, border_width=2, border_color="#C0C0C0")
     row_frame.grid(row=i + 1, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

    # Configure grid layout for the row_frame
     row_frame.grid_rowconfigure(0, weight=1)
     for col in range(4):  # 4 columns
        row_frame.grid_columnconfigure(col, weight=1)

    # Add widgets inside the row_frame
     CTkLabel(row_frame, text=patient["name"], font=row_font, anchor="w", width=column_widths[0]).grid(
        row=0, column=0, padx=5, pady=10, sticky="w"
    )
     CTkLabel(row_frame, text=str(patient["age"]), font=row_font, anchor="center", width=column_widths[1]).grid(
        row=0, column=1, padx=5, pady=10, sticky="w"
    )
     CTkLabel(row_frame, text=patient["status"], font=row_font, anchor="center", width=column_widths[2]).grid(
        row=0, column=2, padx=5, pady=10, sticky="w"
    )
     CTkButton(
        row_frame,
        text="Consult",
        font=row_font,
        width=column_widths[3],
        command=lambda: create_Consult_frame(main_view),
     ).grid(row=0, column=3, padx=5, pady=10, sticky="w")

    

def create_history_frame(main_view):
    # Clear the previous view
    for widget in main_view.winfo_children():
        widget.destroy()

    title_frame = CTkFrame(master=main_view, fg_color="transparent", width=846, height=50)
    title_frame.place(x=27, y=29)

    CTkLabel(master=title_frame, text="History", font=("Arial Black", 25), text_color="#0080FF").place(relx=0.47, rely=0)

    historyframe = CTkScrollableFrame(master=main_view, fg_color="#F0F0F0", width=825, height=650)
    historyframe.place(x=27, y=115)

    
# Function to dynamically switch between the Doctor and Patient login views
def switch_mainframe_view(view_type, main_frame):
    if view_type == "Home":
        create_home_frame(main_frame) 

    elif view_type == "Client":
        create_Client_frame(main_frame)

    elif view_type == "history":
       create_history_frame(main_frame)

def create_addpatient_frame(main_view):
    # Clear the previous view
    for widget in main_view.winfo_children():
        widget.destroy()

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
    patient_icon_data = Image.open("Images/people.png")
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
    doc_icon = CTkImage(dark_image=patient_icon_data, light_image=patient_icon_data, size=(60, 60))
    back_icon = CTkImage(dark_image=back_icon_data, light_image=back_icon_data, size=(20, 20))

    CTkLabel(
        master=main_view,
        text="",
        text_color="#1E90FF",  # Dodger blue
        anchor="w",
        image=doc_icon,
        justify="left",
        font=("Arial Bold", 32)
    ).place(relx=0.45, rely=0.04)

    # Add the title label
    CTkLabel(
        master=main_view,
        text="Add Patient",
        text_color="#1E90FF",  # Dodger blue
        anchor="w",
        justify="left",
        font=("Arial Black", 32)
    ).place(relx=0.38, rely=0.13)


       
    fn_label = CTkLabel(
        master=main_view,
        text=" First Name:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=name_icon,
        compound="left",
    )
    fn_label.place(relx=0.1, rely=0.25)

    fn_entry = CTkEntry(
        master=main_view,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    fn_entry.place(relx=0.1, rely=0.29)
    ln_label = CTkLabel(
        master=main_view,
        text=" Last Name:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=name_icon,
        compound="left",
    )
    ln_label.place(relx=0.50, rely=0.25)

    ln_entry = CTkEntry(
        master=main_view,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    ln_entry.place(relx=0.50, rely=0.29)

    bd_label = CTkLabel(
        master=main_view,
        text=" Birthday:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=dob_icon,
        compound="left",
    )
    bd_label.place(relx=0.10, rely=0.35)

    bd_entry = CTkEntry(
        master=main_view,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    bd_entry.place(relx=0.10, rely=0.39)

    pob_label = CTkLabel(
        master=main_view,
        text=" Place of Birth:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=pob_icon,
        compound="left",
    )
    pob_label.place(relx=0.50, rely=0.35)

    pob_entry = CTkEntry(
        master=main_view,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    pob_entry.place(relx=0.50, rely=0.39)

    pnumber_label = CTkLabel(
        master=main_view,
        text=" Phone Number:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=phone_icon,
        compound="left",
    )
    pnumber_label.place(relx=0.10, rely=0.45)

    pnumber_entry = CTkEntry(
        master=main_view,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    pnumber_entry.place(relx=0.10, rely=0.49)

    emergencynumber_label = CTkLabel(
        master=main_view,
        text=" Emergency Contact:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=phone_icon,
        compound="left",
    )
    emergencynumber_label.place(relx=0.50, rely=0.45)

    emergencynumber_entry = CTkEntry(
        master=main_view,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    emergencynumber_entry.place(relx=0.50, rely=0.49)

    sexe_label = CTkLabel(
        master=main_view,
        text=" Sexe:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=sexe_icon,
        compound="left",
    )
    sexe_label.place(relx=0.50, rely=0.55)

    optionmenu = CTkComboBox(main_view, values=["Male", "Female"],
                                         width=150,button_color="#0080FF", border_color="#0080FF", border_width=2, button_hover_color="#207244",
                dropdown_hover_color="#E44982", dropdown_fg_color="#0080FF", dropdown_text_color="#fff")
    
    optionmenu.place(relx=0.50, rely=0.59)

    cin_label = CTkLabel(
        master=main_view,
        text=" CIN:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=cin_icon,
        compound="left",
    )
    cin_label.place(relx=0.70, rely=0.55)

    cin_entry = CTkEntry(
        master=main_view,
        width=150,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    cin_entry.place(relx=0.70, rely=0.59)

    wa_label = CTkLabel(
        master=main_view,
        text=" Wallet Address:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=address_icon,
        compound="left",
    )
    wa_label.place(relx=0.10, rely=0.55)

    wa_entry = CTkEntry(
        master=main_view,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    wa_entry.place(relx=0.10, rely=0.59)

    mrid_label = CTkLabel(
        master=main_view,
        text=" Medical Record ID:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=id_icon,
        compound="left",
    )
    mrid_label.place(relx=0.3, rely=0.65)

    mrid_entry = CTkEntry(
        master=main_view,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
    )
    mrid_entry.place(relx=0.3, rely=0.69)


    pass_label = CTkLabel(
        master=main_view,
        text=" Password:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=password_icon,
        compound="left",
    )
    pass_label.place(relx=0.10, rely=0.75)

    pass_entry = CTkEntry(
        master=main_view,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
        show="*",
    )
    pass_entry.place(relx=0.10, rely=0.79)

    confpass_label = CTkLabel(
        master=main_view,
        text=" Confirm Password:",
        text_color="#0080FF",
        anchor="w",
        justify="left",
        font=("Arial Bold", 14),
        image=password_icon,
        compound="left",
    )
    confpass_label.place(relx=0.50, rely=0.75)

    confpass_entry = CTkEntry(
        master=main_view,
        width=300,
        fg_color="#EEEEEE",
        border_color="#0080FF",
        border_width=1,
        text_color="#000000",
        show="*",
    )
    confpass_entry.place(relx=0.50, rely=0.79)
    def validate_and_register_patient():
        web3_helper = Web3Helper()
        # Collect all input values
        patient_data = {
            'wallet_address': wa_entry.get().strip(),
            'first_name': fn_entry.get().strip(),
            'last_name': ln_entry.get().strip(),
            'date_of_birth': bd_entry.get().strip(),
            'gender': optionmenu.get(),
            'place_of_birth': pob_entry.get().strip(),
            'cin': cin_entry.get().strip(),
            'phone_number': pnumber_entry.get().strip(),
            'emergency_contact': emergencynumber_entry.get().strip(),
            'medical_record_id': mrid_entry.get().strip()
        }

        # Password validation
        password = pass_entry.get()
        print(password)
        confirm_password = confpass_entry.get()

        # Comprehensive validation
        error_messages = []

        # Check password match
        if password != confirm_password:
            error_messages.append("Passwords do not match")

        # Check password strength (optional, but recommended)
        if len(password) < 8:
            error_messages.append("Password must be at least 8 characters long")

        # Validate required fields
        required_fields = [
            ('Wallet Address', 'wallet_address'),
            ('First Name', 'first_name'),
            ('Last Name', 'last_name'),
            ('Date of Birth', 'date_of_birth'),
            ('Gender', 'gender'),
            ('Place of Birth', 'place_of_birth'),
            ('CIN', 'cin'),
            ('Phone Number', 'phone_number'),
            ('Emergency Contact', 'emergency_contact'),
            ('Medical Record ID', 'medical_record_id')
        ]

        for field_name, field_key in required_fields:
            if not patient_data[field_key]:
                error_messages.append(f"{field_name} cannot be empty")

        # Display errors if any
        if error_messages:
            messagebox.showerror("Validation Error", "\n".join(error_messages))
            return

        # Attempt patient registration
        try:
            print(password)
            print(len(password))
            patient_wallet = web3_helper.create_account(password)
            
            # Update wallet address with the newly created address
            patient_data['wallet_address'] = patient_wallet['address']
            print(web3_helper.get_current_user_adress())
            print(web3_helper.get_current_private_key())
            print("Private Key:", web3_helper.get_current_private_key())
            print("Length:", len(web3_helper.get_current_private_key()))

            print(patient_data)
            # Register patient
            success, message = web3_helper.register_patient(
                web3_helper.get_current_private_key(), 
                web3_helper.get_current_user_adress(), 
                patient_data
            )

            if success:
                # Show success message
                messagebox.showinfo("Registration Successful", message)
            
                
                # Switch back to main view or patient list
                switch_mainframe_view("Client", main_view)
            else:
                # Show error message
                messagebox.showerror("Registration Failed", message)

        except Exception as e:
            messagebox.showerror("Error", str(e))
    CTkButton(master=main_view, text="Back", width=300, fg_color="transparent", font=("Arial Bold", 17), border_color="#0080FF", hover_color="#eee", border_width=2, text_color="#0080FF", command=lambda: switch_mainframe_view("Client", main_view)) \
        .place(relx=0.10, rely=0.89)
    CTkButton(
        master=main_view, 
        text="Create", 
        width=300, 
        font=("Arial Bold", 17), 
        hover_color="#E44982", 
        fg_color="#0080FF", 
        text_color="#fff",
        command=validate_and_register_patient
    ).place(relx=0.50, rely=0.89)
def create_Consult_frame(main_view):
    # Clear the previous view
    for widget in main_view.winfo_children():
        widget.destroy()

    from tkinter import StringVar, Text
    from PIL import Image

    # Icons
    back_icon_data = Image.open("Images/back-arrow.png")
    edit_icon_data = Image.open("Images/editer.png")

    back_icon = CTkImage(dark_image=back_icon_data, light_image=back_icon_data, size=(20, 20))
    edit_icon = CTkImage(dark_image=edit_icon_data, light_image=edit_icon_data, size=(20, 20))

    # Title Frame
    title_frame = CTkFrame(master=main_view, fg_color="transparent", width=846, height=50)
    title_frame.place(x=27, y=29)

    CTkLabel(master=title_frame, text="Medical Record", font=("Arial Black", 25), text_color="#0080FF").place(relx=0.37, rely=0)

    CTkButton(master=title_frame, text="Back", font=("Arial Black", 15), text_color="#fff", fg_color="#0080FF", 
              hover_color="#E44982", width=120, image=back_icon, height=40, 
              command=lambda: switch_mainframe_view("Client", main_view)).place(x=27, y=0)

    edit_button = CTkButton(master=title_frame, text="Edit", font=("Arial Black", 15), text_color="#fff", fg_color="#0080FF", 
                             hover_color="#E44982", width=120, image=edit_icon, height=40)
    edit_button.place(x=700, y=0)

    # Scrollable Frame
    patientsframe = CTkScrollableFrame(master=main_view, fg_color="#F8F9FA", width=825, height=650, corner_radius=10)
    patientsframe.place(x=27, y=115)
    patientsframe.grid_rowconfigure(0, weight=1)
    for col in range(4):  # 4 columns for Full Name, Age, Status, Action
        patientsframe.grid_columnconfigure(col, weight=1)


    # Patient Medical Record Data
    patient_data = {
        "Full Name": StringVar(value="John Doe"),
        "Date of Birth": StringVar(value="1990-05-14"),
        "Place of Birth": StringVar(value="New York, USA"),
        "Description": StringVar(value="Patient suffers from seasonal allergies."),
        "Weight": StringVar(value="70 kg"),
        "Height": StringVar(value="175 cm"),
        "Medical Record ID": StringVar(value="MR123456"),
        "Medical Insurance": StringVar(value="Yes"),
        "Status": StringVar(value="Active"),
        "Active Problems": StringVar(value="Hypertension, Seasonal Allergies"),
        "Allergies": StringVar(value="Peanuts, Pollen"),
        "Medications": StringVar(value="Lisinopril, Cetirizine")
    }

    def display_record(editable=False):
        for widget in patientsframe.winfo_children():
            widget.destroy()

        row = 0
        for key, value_var in patient_data.items():
            # Create a bordered section for each field
            section_frame = CTkFrame(master=patientsframe, fg_color="#FFFFFF", corner_radius=10, width=780, height=50)
            section_frame.grid(row=row, column=0, columnspan=4 ,padx=10, pady=5, sticky="nsew")
            section_frame.grid_columnconfigure(1, weight=1)

            label = CTkLabel(master=section_frame, text=f"{key}:", font=("Arial Bold", 15), text_color="#0080FF")
            label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

            if editable:
                    entry = CTkEntry(master=section_frame, fg_color="#FFF", font=("Arial", 14), textvariable=value_var)
                    entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
            else:
                    value_label = CTkLabel(master=section_frame, text=value_var.get(), font=("Arial", 14), text_color="#000")
                    value_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

            row += 1

        if editable:
            # Add Save and Cancel Buttons at the bottom
            button_frame = CTkFrame(master=patientsframe, fg_color="#FFFFFF", corner_radius=10)
            button_frame.grid(row=row, column=2, padx=10, pady=10, sticky="w")

            cancel_button = CTkButton(master=button_frame, text="Cancel", fg_color="transparent", font=("Arial Bold", 17), border_color="#0080FF", hover_color="#eee", border_width=2, text_color="#0080FF", command=cancel_edit)
            cancel_button.pack(side="left", padx=10, pady=10)

            save_button = CTkButton(master=button_frame, text="Save", font=("Arial Bold", 17), hover_color="#E44982", fg_color="#0080FF", text_color="#fff", command=save_record)
            save_button.pack(side="left", padx=10, pady=10)



    def save_record():
        print("Saving the updated record:")
        for key, value_var in patient_data.items():
            print(f"{key}: {value_var.get()}")
        display_record(editable=False)

    def cancel_edit():
        display_record(editable=False)

    def toggle_edit_mode():
        display_record(editable=True)

    edit_button.configure(command=toggle_edit_mode)

    # Initially display the record in read-only mode
    display_record(editable=False)




def create_doctordash_frame(app, current_frame):

    doc_icon_data = Image.open("Images/doctor2.png")
    doc_icon = CTkImage(dark_image=doc_icon_data, light_image=doc_icon_data, size=(77.68, 85.42))

    clients_img_data = Image.open("Images/patient.png")
    clients_img = CTkImage(dark_image=clients_img_data, light_image=clients_img_data, size=(30, 30))

    home_img_data = Image.open("Images/home.png")
    home_img = CTkImage(dark_image=home_img_data, light_image=home_img_data, size=(30, 30))

    history_img_data = Image.open("Images/file.png")
    history_img = CTkImage(dark_image=history_img_data, light_image=history_img_data, size=(30, 30))

    logout_img_data = Image.open("Images/exit.png")
    logout_img = CTkImage(dark_image=logout_img_data, light_image=logout_img_data, size=(30, 30))

    frame = CTkFrame(app, width=1200, height=800)
    frame.place(x=0, y=0)

    sidebar_frame = CTkFrame(master=frame, fg_color="#0080FF", width=300, height=800, corner_radius=0)
    sidebar_frame.place(x=0, y=0)

    CTkLabel(master=sidebar_frame, text="", image=doc_icon).place(x=111, y=38)

    Homebutton=CTkButton(master=sidebar_frame, image=home_img, text="Home", fg_color="transparent", font=("Arial Black", 18), 
              hover_color="#E44982", anchor="center", width=300, height=50,command=lambda: switch_mainframe_view("Home",main_view)).place(x=0, y=210)

    Clientbutton=CTkButton(master=sidebar_frame, image=clients_img, text="Patients", fg_color="transparent", font=("Arial Black", 18),
              hover_color="#E44982", anchor="center", width=300, height=50,command=lambda: switch_mainframe_view("Client",main_view)).place(x=0, y=270)

    Historybutton=CTkButton(master=sidebar_frame, image=history_img, text="History", fg_color="transparent", font=("Arial Black", 18),
              hover_color="#E44982", anchor="center", width=300, height=50,command=lambda: switch_mainframe_view("history",main_view)).place(x=0, y=330)

    CTkButton(master=sidebar_frame, image=logout_img, text="Sign Out", command=lambda: log_out(current_frame, frame),
              fg_color="transparent", font=("Arial Black", 18), hover_color="#E44982", anchor="center", width=300, height=40).place(x=0, y=550)

    main_view = CTkFrame(master=frame, fg_color="#fff", width=900, height=800, corner_radius=0)
    main_view.place(x=300, y=0)

    title_frame = CTkFrame(master=main_view, fg_color="transparent", width=846, height=50)
    title_frame.place(x=27, y=29)

    CTkLabel(master=title_frame, text="Home", font=("Arial Black", 25), text_color="#0080FF").place(relx=0.47, rely=0)



    metrics_frame = CTkFrame(master=main_view, fg_color="transparent", width=846, height=60)
    metrics_frame.place(x=27, y=115)



    doctor_metric = CTkFrame(master=metrics_frame, fg_color="#0080FF", width=200, height=60)
    doctor_metric.place(x=220, y=0)

    doctor_img_data = Image.open("Images/doctor.png")
    doctor_img = CTkImage(light_image=doctor_img_data, dark_image=doctor_img_data, size=(43, 43))

    CTkLabel(master=doctor_metric, image=doctor_img, text="").place(x=12, y=10)
    CTkLabel(master=doctor_metric, text="Doctors", text_color="#fff", font=("Arial Black", 15)).place(x=60, y=10)
    CTkLabel(master=doctor_metric, text="9", text_color="#fff", font=("Arial Black", 15), justify="left").place(x=60, y=35)

    client_metric = CTkFrame(master=metrics_frame, fg_color="#0080FF", width=200, height=60)
    client_metric.place(x=440, y=0)

    client_img_data = Image.open("Images/patient.png")
    client_img = CTkImage(light_image=client_img_data, dark_image=client_img_data, size=(43, 43))

    CTkLabel(master=client_metric, image=client_img, text="").place(x=12, y=10)
    CTkLabel(master=client_metric, text="Patients", text_color="#fff", font=("Arial Black", 15)).place(x=60, y=10)
    CTkLabel(master=client_metric, text="23", text_color="#fff", font=("Arial Black", 15), justify="left").place(x=60, y=35)

    search_container = CTkFrame(master=main_view, fg_color="#F0F0F0", width=846, height=50)
    search_container.place(x=27, y=200)

    CTkEntry(master=search_container, width=365, placeholder_text="Search Patient", border_color="#0080FF", border_width=2).place(x=13, y=10)

    CTkComboBox(master=search_container, width=125, values=[" ", "My Patients", "Others"],
                button_color="#0080FF", border_color="#0080FF", border_width=2, button_hover_color="#E44982",
                dropdown_hover_color="#E44982", dropdown_fg_color="#0080FF", dropdown_text_color="#fff").place(x=390, y=10)

    CTkComboBox(master=search_container, width=125, values=[" ", "Alive", "Dead"],
                button_color="#0080FF", border_color="#0080FF", border_width=2, button_hover_color="#E44982",
                dropdown_hover_color="#E44982", dropdown_fg_color="#0080FF", dropdown_text_color="#fff").place(x=530, y=10)
    
    CTkButton(master=search_container, text="Search", font=("Arial Black", 15), text_color="#fff", fg_color="#0080FF", 
              hover_color="#E44982", width=125).place(x=670, y=10)
    # Create a scrollable frame for patients
    patientsframe = CTkScrollableFrame(master=main_view, fg_color="#F0F0F0", width=825, height=500)
    patientsframe.place(x=27, rely=0.34)


    return frame



def log_out(current_frame, frame):
    frame.place_forget()
    current_frame.place(x=0, y=0)