from cassandra.cluster import Cluster

# default cassandra docker is 127.0.0.1:9042
cluster = Cluster()
session = cluster.connect('student_keyspace')

student_insert_str = "INSERT INTO student_by_department (department, id, name) VALUES ('%s', %d, '%s');"

new_si_student = ['ilham', 'Sasa', 'Kevin']
for student_id, student_name in zip(range(len(new_si_student)), new_si_student):
    session.execute(student_insert_str % ('si', student_id, student_name))

si_students = session.execute("SELECT * FROM student_by_department WHERE department='si' ORDER BY id DESC;")
for student in si_students:
    print(student.department, student.id, student.name)
