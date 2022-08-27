# categorize new member
def open_or_senior(data):
    members_list = list(data)
    output = []
    for member in range(len(members_list)):
        if members_list[member][0] >= 55 and members_list[member][1] > 7:
            output.append('Senior')
        else:
            output.append('Open')
    return output