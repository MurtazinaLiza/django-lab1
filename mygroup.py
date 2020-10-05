groupmates = [
	{
		"name": "Александр",
		"surname": "Иванов",
		"exams": ["Информатика", "ЭЭиС", "Web"],
		"marks": [4, 3, 5]
	},
	{
		"name": "Иван",
		"surname": "Петров",
		"exams": ["История", "АиГ", "КТП"],
		"marks": [4, 4, 4]
	},
	{
		"name": "Кирилл",
		"surname": "Смирнов",
		"exams": ["Философия", "ИС", "КТП"],
		"marks": [5, 5, 2]
	},
	{
		"name": "Максим",
		"surname": "Вадимов",
		"exams": ["Философия", "ИС", "История"],
		"marks": [5, 3, 5]
	},
	{
		"name": "Лида",
		"surname": "Романова",
		"exams": ["Web", "История", "КТП"],
		"marks": [5, 4, 4]
	},
	{
		"name": "Виктор",
		"surname": "Лазаев",
		"exams": ["Информатика", "Web", "Философия"],
		"marks": [3, 4, 5]
	}
]


def print_students(students):
	print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(40), u"Оценки".ljust(20))
	for student in students:
		print(student["name"].ljust(15), student["surname"].ljust(10),
		      str(student["exams"]).ljust(40), str(student["marks"]).ljust(20))


def filter_avg_mark(students, avg):
	filtered = []
	for student in students:
		if sum(student["marks"]) / len(student["marks"]) > avg:
			filtered.append(student)

	return filtered


avg_mark = float(input("Введите среднюю оценку: "))
print_students(filter_avg_mark(groupmates, avg_mark))
