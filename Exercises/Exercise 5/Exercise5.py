prev_members = open("members.txt", "r")
members_list = prev_members.readlines()
prev_members.close()

new_member = input("Please enter name and surname of new member: ") + "\n"
members_list.append(new_member)

new_members_list = open("members.txt", "w")
new_members_list.writelines(members_list)
new_members_list.close()
