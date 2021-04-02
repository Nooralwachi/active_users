def active_users(filename, filename2):
	with open(filename, 'r') as file, open(filename2, 'r') as file2:
		users= {}
		active_dic={}
		num = '(444) 123-1233'
		for line in file:
			items = line.split()
			email = items[0].split('@')
			username=email[0]
			comp=email[1]
			phone= ' '.join(items[1:])
			if comp == 'yaboo.com':
				users[username] = phone
		file2.readline()
		for line in file2:
			active= line.split()
			if active[1] == 'Yes':
				if active[0] in users:
					active_dic[active[0]]= users[active[0]]
				else:
					active_dic[active[0]]= num
	for (user, phone) in active_dic.items():
		print(user +' --> '+phone)

active_users('file_a.txt', 'file_b.txt')
