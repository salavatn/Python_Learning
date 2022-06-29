from jinja2 import Environment, FileSystemLoader


myTemplate = FileSystemLoader('venv/template')
env = Environment(loader=myTemplate)

wedding_guests = input("Enter names of guests: \t")
wedding_date_time = input("Enter date and time: \t")
wedding_address = input("Enter wedding address: \t")
message_from = input("Enter your name: \t")


wedding_Invitation = env.get_template('template_invitation.txt')

output_msg = wedding_Invitation.render(
    wedding_guests = wedding_guests,
    wedding_date_time = wedding_date_time,
    wedding_address = wedding_address,
    message_from = message_from)

print("\n",output_msg)
