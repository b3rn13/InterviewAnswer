#Import the models module from models package
from models import models

#the template to be rendered
html = "<!DOCTYPE html><html><head lang=\"en\"><meta charset=\"UTF-8\"><title>GOT Character Profile</title><style>" \
       "table, th, td {border: 1px solid black;}</style></head><body><h1>GOT Character Profiles</h1><table><tr><th>Name</th><th>District</th><" \
       "th>Mother's Name</th><th>Father's Name</th><th>Date Added</th><th>Episodes Per Season</th><th>Died in Se" \
       "ason</th></tr>%s</table></body></html>"

#the controllers modules to handle data from the models
user_appearance = []
for character in models.characters:
    name = character.get('name')
    character_episodes = []
    for appearance in models.appearances:
        if appearance.get('user') == name:
            character_episodes.append("%s Episodes in Season %s" %
                                      (appearance.get('no of episodes'),
                                          appearance.get('season')))
            if int(appearance.get('died in this season')):
                character['Death Season'] = appearance.get('season')
    character['Episodes Per Season'] = character_episodes

page_data = []
for character in models.characters:
    data = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>Season %s</td></tr>" % \
           (character.get('name'), character.get('district'),
            character.get('mothers name') or 'Unidentified',
            character.get('fathers name') or 'Unidentified',
            character.get('date registered'),
            '<br/><hr/>'.join(character.get('Episodes Per Season')),
            character.get('Death Season'))
    page_data.append(data)

#file operations
page = open('index.html', 'w')
page.write(html % (''.join(page_data)))
page.close()
