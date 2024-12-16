from customtkinter import *
from PIL import Image
import tkinter
from tkinter import StringVar

def create_home_frame(main_view):
    # Clear the previous view
    for widget in main_view.winfo_children():
        widget.destroy()



    req_img_data = Image.open("Images/demande.png")
    req_img = CTkImage(dark_image=req_img_data, light_image=req_img_data, size=(30, 30))


    
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
    CTkLabel(master=doctor_metric, text="My Doctors", text_color="#fff", font=("Arial Black", 15)).place(x=60, y=10)
    CTkLabel(master=doctor_metric, text="4", text_color="#fff", font=("Arial Black", 15), justify="left").place(x=60, y=35)

    client_metric = CTkFrame(master=metrics_frame, fg_color="#0080FF", width=200, height=60)
    client_metric.place(x=440, y=0)

    client_img_data = Image.open("Images/patient.png")
    client_img = CTkImage(light_image=client_img_data, dark_image=client_img_data, size=(43, 43))

    CTkLabel(master=client_metric, image=req_img, text="").place(x=12, y=10)
    CTkLabel(master=client_metric, text="My requests", text_color="#fff", font=("Arial Black", 15)).place(x=60, y=10)
    CTkLabel(master=client_metric, text="3", text_color="#fff", font=("Arial Black", 15), justify="left").place(x=60, y=35)

    search_container = CTkFrame(master=main_view, fg_color="#F0F0F0", width=846, height=50)
    search_container.place(x=27, y=200)

    CTkEntry(master=search_container, width=600, placeholder_text="Search Doctor", border_color="#0080FF", border_width=2).place(x=13, y=10)

    
    CTkButton(master=search_container, text="Search", font=("Arial Black", 15), text_color="#fff", fg_color="#0080FF", 
              hover_color="#E44982", width=125).place(x=670, y=10)
    # Create a scrollable frame for patients
    mydocsframe = CTkScrollableFrame(master=main_view, fg_color="#F0F0F0", width=825, height=500)
    mydocsframe.place(x=27, rely=0.34)

    mydocs_data = [
        {"name": "Dr. Edwards", "id": 'D25', "Speciality": "Dermatologist"},
        {"name": "Dr. Samuels", "id": 'F26', "Speciality": "Cardiologist"},
        {"name": "Dr. Jackson", "id": 'S11', "Speciality": "Neurologist"},
        {"name": "Dr. Samantha", "id": 'K98', "Speciality": "Allergist"},

     ]
    # Configure grid layout
    mydocsframe.grid_rowconfigure(0, weight=1)
    for col in range(4):  # 4 columns for Full Name, Age, Status, Action
        mydocsframe.grid_columnconfigure(col, weight=1)

# Define column widths
    column_widths = [300, 100, 150, 150]  # Adjust these widths as needed

# Add header row
    header_font = ("Arial Black", 20)
    CTkLabel(mydocsframe, text="Full Name", font=header_font, anchor="w", text_color="#0080FF", width=column_widths[0]).grid(
    row=0, column=0, padx=15, pady=15, sticky="w"
)
    CTkLabel(mydocsframe, text="ID", font=header_font, anchor="center", text_color="#0080FF", width=column_widths[1]).grid(
    row=0, column=1, padx=5, pady=15, sticky="w"
)
    CTkLabel(mydocsframe, text="Speciality", font=header_font, anchor="center", text_color="#0080FF", width=column_widths[2]).grid(
    row=0, column=2, padx=5, pady=15, sticky="w"
)
    CTkLabel(mydocsframe, text="Action", font=header_font, anchor="center", text_color="#0080FF", width=column_widths[3]).grid(
    row=0, column=3, padx=5, pady=15, sticky="w"
)

# Add rows for patients
    row_font = ("Arial Bold", 16)
    for i, patient in enumerate(mydocs_data):
     row_frame = CTkFrame(mydocsframe, fg_color="#FFFFFF", corner_radius=5, border_width=2, border_color="#C0C0C0")
     row_frame.grid(row=i + 1, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

    # Configure grid layout for the row_frame
     row_frame.grid_rowconfigure(0, weight=1)
     for col in range(4):  # 4 columns
        row_frame.grid_columnconfigure(col, weight=1)

    # Add widgets inside the row_frame
     CTkLabel(row_frame, text=patient["name"], font=row_font, anchor="w", width=column_widths[0]).grid(
        row=0, column=0, padx=5, pady=10, sticky="w"
    )
     CTkLabel(row_frame, text=str(patient["id"]), font=row_font, anchor="center", width=column_widths[1]).grid(
        row=0, column=1, padx=5, pady=10, sticky="w"
    )
     CTkLabel(row_frame, text=patient["Speciality"], font=row_font, anchor="center", width=column_widths[2]).grid(
        row=0, column=2, padx=5, pady=10, sticky="w"
    )
     CTkButton(
        row_frame,
        text="Revoke Access",
        font=row_font,
        width=column_widths[3],
        fg_color="transparent", border_color="#0080FF", hover_color="#eee", border_width=2, text_color="#0080FF"
        
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

def create_req_frame(main_view):
    # Clear the previous view
    for widget in main_view.winfo_children():
        widget.destroy()

    # Title Frame
    title_frame = CTkFrame(master=main_view, fg_color="transparent", width=846, height=50)
    title_frame.place(x=27, y=29)

    CTkLabel(master=title_frame, text="Requests", font=("Arial Black", 25), text_color="#0080FF").place(relx=0.47, rely=0)

    # Scrollable Frame for Requests
    reqframe = CTkScrollableFrame(master=main_view, fg_color="#F0F0F0", width=825, height=650)
    reqframe.place(x=27, y=115)

    # Sample Data
    myreq_data = [
        {"name": "Dr. Aaron", "id": 'A35', "Speciality": "Dermatologist"},
        {"name": "Dr. Mark", "id": 'L16', "Speciality": "Allergist"},
        {"name": "Dr. Poppy", "id": 'M51', "Speciality": "Gastroenterologist"},
    ]

    # Configure the overall grid layout
    for col in range(5):  # 5 Columns: Full Name, ID, Speciality, Accept, Refuse
        reqframe.grid_columnconfigure(col, weight=1, uniform="column")

    # Header Row
    header_font = ("Arial Black", 20)
    headers = ["Full Name", "ID", "Speciality", "", ""]
    for col, header in enumerate(headers):
        CTkLabel(
            reqframe,
            text=header,
            font=header_font,
            text_color="#0080FF",
            anchor="center",
        ).grid(row=0, column=col, padx=5, pady=10, sticky="nsew")

    # Data Rows
    row_font = ("Arial Bold", 16)
    button_width = 100  # Fixed button width
    button_height = 35  # Fixed button height

    for i, req in enumerate(myreq_data):
        # Alternating Row Colors
        row_bg = "#FFFFFF" if i % 2 == 0 else "#F8F8F8"
        
        # Frame for Row (with border and shadow effect)
        row_frame = CTkFrame(
            master=reqframe,
            fg_color=row_bg,
            corner_radius=10,
            border_width=2,
            border_color="#C0C0C0"  # Light gray border
        )
        row_frame.grid(row=i + 1, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")

        # Configure layout inside row frame
        for col in range(5):
            row_frame.grid_columnconfigure(col, weight=1, uniform="column")

        # Add Widgets to the Row Frame
        CTkLabel(row_frame, text=req["name"], font=row_font, anchor="center").grid(
            row=0, column=0, padx=5, pady=10, sticky="nsew"
        )
        CTkLabel(row_frame, text=req["id"], font=row_font, anchor="center").grid(
            row=0, column=1, padx=5, pady=10, sticky="nsew"
        )
        CTkLabel(row_frame, text=req["Speciality"], font=row_font, anchor="center").grid(
            row=0, column=2, padx=5, pady=10, sticky="nsew"
        )

        # Accept Button
        CTkButton(
            row_frame,
            text="Accept",
            font=row_font,
            width=button_width,
            height=button_height,
            text_color="#FFFFFF",
            fg_color="#2A8C55",
            hover_color="#207244",
            corner_radius=5
        ).grid(row=0, column=3, padx=5, pady=10, sticky="nsew")

        # Refuse Button
        CTkButton(
            row_frame,
            text="Refuse",
            font=row_font,
            width=button_width,
            height=button_height,
            text_color="#FFFFFF",
            fg_color="#FF5733",
            hover_color="#E44982",
            corner_radius=5
        ).grid(row=0, column=4, padx=5, pady=10, sticky="nsew")



def create_mr_frame(main_view):
        # Clear the previous view
    for widget in main_view.winfo_children():
        widget.destroy()

    from tkinter import StringVar, Text
    from PIL import Image



    # Title Frame
    title_frame = CTkFrame(master=main_view, fg_color="transparent", width=846, height=50)
    title_frame.place(x=27, y=29)

    CTkLabel(master=title_frame, text="Medical Record", font=("Arial Black", 25), text_color="#0080FF").place(relx=0.37, rely=0)


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


    # Initially display the record in read-only mode
    display_record(editable=False)




# Function to dynamically switch between the Doctor and Patient login views
def switch_mainframe_view(view_type, main_frame):
    if view_type == "Home":
        create_home_frame(main_frame) 

    elif view_type == "MedicalRecord":
        create_mr_frame(main_frame)

    elif view_type == "history":
       create_history_frame(main_frame)

    elif view_type == "request":
       create_req_frame(main_frame)


def create_patientdash_frame(app, current_frame):



    patient_icon_data = Image.open("Images/patient2.png")
    patient_icon = CTkImage(dark_image=patient_icon_data, light_image=patient_icon_data, size=(77.68, 85.42))

    clients_img_data = Image.open("Images/patient.png")
    clients_img = CTkImage(dark_image=clients_img_data, light_image=clients_img_data, size=(30, 30))

    req_img_data = Image.open("Images/demande.png")
    req_img = CTkImage(dark_image=req_img_data, light_image=req_img_data, size=(30, 30))

    home_img_data = Image.open("Images/home.png")
    home_img = CTkImage(dark_image=home_img_data, light_image=home_img_data, size=(30, 30))
    
    mr_img_data = Image.open("Images/bilan-de-sante.png")
    mr_img = CTkImage(dark_image=mr_img_data, light_image=mr_img_data, size=(30, 30))

    history_img_data = Image.open("Images/file.png")
    history_img = CTkImage(dark_image=history_img_data, light_image=history_img_data, size=(30, 30))

    logout_img_data = Image.open("Images/exit.png")
    logout_img = CTkImage(dark_image=logout_img_data, light_image=logout_img_data, size=(30, 30))

    frame = CTkFrame(app, width=1200, height=800)
    frame.place(x=0, y=0)

    sidebar_frame = CTkFrame(master=frame, fg_color="#0080FF", width=300, height=800, corner_radius=0)
    sidebar_frame.place(x=0, y=0)

    CTkLabel(master=sidebar_frame, text="", image=patient_icon).place(x=111, y=38)

    Homebutton=CTkButton(master=sidebar_frame, image=home_img, text="Home", fg_color="transparent", font=("Arial Black", 18), 
              hover_color="#E44982", anchor="center", width=300, height=50, command=lambda: switch_mainframe_view("Home", main_view)).place(x=0, y=210)

    mrbutton=CTkButton(master=sidebar_frame, image=mr_img, text="Medical Record", fg_color="transparent", font=("Arial Black", 18),
              hover_color="#E44982", anchor="center", width=300, height=50, command=lambda: switch_mainframe_view("MedicalRecord", main_view)).place(x=0, y=270)

    Requestbutton=CTkButton(master=sidebar_frame, image=req_img, text="Requests", fg_color="transparent", font=("Arial Black", 18),
              hover_color="#E44982", anchor="center", width=300, height=50, command=lambda: switch_mainframe_view("request", main_view)).place(x=0, y=330)
    
    Historybutton=CTkButton(master=sidebar_frame, image=history_img, text="History", fg_color="transparent", font=("Arial Black", 18),
              hover_color="#E44982", anchor="center", width=300, height=50, command=lambda: switch_mainframe_view("history", main_view)).place(x=0, y=390)

    CTkButton(master=sidebar_frame, image=logout_img, text="Sign Out", command=lambda: log_out(current_frame, frame),
              fg_color="transparent", font=("Arial Black", 18), hover_color="#E44982", anchor="center", width=300, height=40).place(x=0, y=610)

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
    CTkLabel(master=doctor_metric, text="My Doctors", text_color="#fff", font=("Arial Black", 15)).place(x=60, y=10)
    CTkLabel(master=doctor_metric, text="4", text_color="#fff", font=("Arial Black", 15), justify="left").place(x=60, y=35)

    client_metric = CTkFrame(master=metrics_frame, fg_color="#0080FF", width=200, height=60)
    client_metric.place(x=440, y=0)

    client_img_data = Image.open("Images/patient.png")
    client_img = CTkImage(light_image=client_img_data, dark_image=client_img_data, size=(43, 43))

    CTkLabel(master=client_metric, image=req_img, text="").place(x=12, y=10)
    CTkLabel(master=client_metric, text="My requests", text_color="#fff", font=("Arial Black", 15)).place(x=60, y=10)
    CTkLabel(master=client_metric, text="3", text_color="#fff", font=("Arial Black", 15), justify="left").place(x=60, y=35)

    search_container = CTkFrame(master=main_view, fg_color="#F0F0F0", width=846, height=50)
    search_container.place(x=27, y=200)

    CTkEntry(master=search_container, width=600, placeholder_text="Search Doctor", border_color="#0080FF", border_width=2).place(x=13, y=10)

    
    CTkButton(master=search_container, text="Search", font=("Arial Black", 15), text_color="#fff", fg_color="#0080FF", 
              hover_color="#E44982", width=125).place(x=670, y=10)
    # Create a scrollable frame for patients
    mydocsframe = CTkScrollableFrame(master=main_view, fg_color="#F0F0F0", width=825, height=500)
    mydocsframe.place(x=27, rely=0.34)

    mydocs_data = [
        {"name": "Dr. Edwards", "id": 'D25', "Speciality": "Dermatologist"},
        {"name": "Dr. Samuels", "id": 'F26', "Speciality": "Cardiologist"},
        {"name": "Dr. Jackson", "id": 'S11', "Speciality": "Neurologist"},
        {"name": "Dr. Samantha", "id": 'K98', "Speciality": "Allergist"},

     ]
    # Configure grid layout
    mydocsframe.grid_rowconfigure(0, weight=1)
    for col in range(4):  # 4 columns for Full Name, Age, Status, Action
        mydocsframe.grid_columnconfigure(col, weight=1)

# Define column widths
    column_widths = [300, 100, 150, 150]  # Adjust these widths as needed

# Add header row
    header_font = ("Arial Black", 20)
    CTkLabel(mydocsframe, text="Full Name", font=header_font, anchor="w", text_color="#0080FF", width=column_widths[0]).grid(
    row=0, column=0, padx=15, pady=15, sticky="w"
)
    CTkLabel(mydocsframe, text="ID", font=header_font, anchor="center", text_color="#0080FF", width=column_widths[1]).grid(
    row=0, column=1, padx=5, pady=15, sticky="w"
)
    CTkLabel(mydocsframe, text="Speciality", font=header_font, anchor="center", text_color="#0080FF", width=column_widths[2]).grid(
    row=0, column=2, padx=5, pady=15, sticky="w"
)
    CTkLabel(mydocsframe, text="Action", font=header_font, anchor="center", text_color="#0080FF", width=column_widths[3]).grid(
    row=0, column=3, padx=5, pady=15, sticky="w"
)

# Add rows for patients
    row_font = ("Arial Bold", 16)
    for i, patient in enumerate(mydocs_data):
     row_frame = CTkFrame(mydocsframe, fg_color="#FFFFFF", corner_radius=5, border_width=2, border_color="#C0C0C0")
     row_frame.grid(row=i + 1, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

    # Configure grid layout for the row_frame
     row_frame.grid_rowconfigure(0, weight=1)
     for col in range(4):  # 4 columns
        row_frame.grid_columnconfigure(col, weight=1)

    # Add widgets inside the row_frame
     CTkLabel(row_frame, text=patient["name"], font=row_font, anchor="w", width=column_widths[0]).grid(
        row=0, column=0, padx=5, pady=10, sticky="w"
    )
     CTkLabel(row_frame, text=str(patient["id"]), font=row_font, anchor="center", width=column_widths[1]).grid(
        row=0, column=1, padx=5, pady=10, sticky="w"
    )
     CTkLabel(row_frame, text=patient["Speciality"], font=row_font, anchor="center", width=column_widths[2]).grid(
        row=0, column=2, padx=5, pady=10, sticky="w"
    )
     CTkButton(
        row_frame,
        text="Revoke Access",
        font=row_font,
        width=column_widths[3],
        fg_color="transparent", border_color="#0080FF", hover_color="#eee", border_width=2, text_color="#0080FF"
        
     ).grid(row=0, column=3, padx=5, pady=10, sticky="w")


    

    return frame



def log_out(current_frame, frame):
    frame.place_forget()
    current_frame.place(x=0, y=0)