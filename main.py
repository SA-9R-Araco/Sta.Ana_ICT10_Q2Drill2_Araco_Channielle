from pyscript import document

#WHY DO I HAVE TO SUFFER THIS CODING PYTHON U SUCK
#python hates me sm oh my days
#im lazy to add members
members = ["Dave", "Pablo", "Idk", "Someone", "Bob"]

#how to add members 101:
#ok so ts is hthe event thing)
def button_btn(event):
    #remember that doc.getElId is basically checking ur element so that python can change em
    first_input = document.getElementById("first_name")
    last_input = document.getElementById("last_name")
    output_box = document.getElementById("sku_output")
#value - grabs the actual text while strip - removes the unnsecary stuff
    first = first_input.value.strip()
    last = last_input.value.strip()

#ts basically make sure that the thingy has smth before adding the item
    if first or last:
        #the f string combines both first and last name w/ space
        full_name = f"{first} {last}".strip()
        members.append(full_name)
        members.sort()


#idk i think building list display
        #html content is basically the header thing
        html_content = "<h4>Theater Members:</h4><ul>"
        #member in members checks every name on the lis and wraps em in item tags
        for member in members:
            html_content += f"<li>{member}</li>"
        html_content += f"</ul><p>Total Members: {len(members)}</p>" #<- len members counts the total of members in a list

        # display thingy 
        output_box.innerHTML = html_content #<- basically makes 10x faster

        # clears out thing
        first_input.value = ""
        last_input.value = ""