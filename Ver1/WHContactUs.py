import tkinter as tk
import WHConfig as cf

class ContactUs:
    def __init__(self, root, on_back_callback=None):
        self.root = root
        self.contact_us_tk()
        self.on_back_callback = on_back_callback

    # Contact us
    def contact_us_tk(self):
        title = tk.Label(self.root, text="Contact Us")
        title.grid(row=0, column=0)
        email_lbl = tk.Label(self.root, text="Email: jacob.wu@my.bdsc.school.nz")
        email_lbl.grid(row=1, column=0)
        phone_lbl = tk.Label(self.root, text="Phone: 028 947 2643")
        phone_lbl.grid(row=2, column=0)
        address_lbl = tk.Label(self.root, text="Address: 575 Chapel Road, East Tamaki, Auckland 1022, New Zealand")
        address_lbl.grid(row=3, column=0)
        back_button = tk.Button(self.root, text="Back", command=self.go_back)
        back_button.grid(row=4, column=0)

    # Back button
    def go_back(self):
        cf.clear_screen(self.root)
        if self.on_back_callback:
            self.on_back_callback()

"""
# For testing
if __name__ == "__main__":
    root = cf.create_window()
    app = ContactUs(root)
    root.mainloop()
"""

if __name__ == "__main__":
    print("Please run 'WHMain.py' to use this program!")
