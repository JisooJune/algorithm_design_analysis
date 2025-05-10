from typing import List


def time_to_min(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def min_to_time(m):
    h = m // 60
    mi = m % 60
    return f"{h:02d}:{mi:02d}"

# 输入课程时间并转换为分钟
courses_str = [
    ('9:00', '12:30'),
    ('11:00', '14:00'),
    ('13:00', '14:30'),
    ('9:00', '10:30'),
    ('13:00', '14:30'),
    ('14:00', '16:30'),
    ('15:00', '16:30'),
    ('15:00', '16:30'),
    ('9:00', '10:30'),
]

courses = []
for start, end in courses_str:
    start_min = time_to_min(start)
    end_min = time_to_min(end)
    courses.append((start_min, end_min))

# 按开始时间和结束时间排序
sorted_courses = sorted(courses, key=lambda x: (x[0], x[1]))

# 分配教室
classrooms = []
for course in sorted_courses:
    start, end = course
    # 按教室的结束时间排序，优先检查结束早的教室
    classrooms.sort(key=lambda room: room['end_time'])
    allocated = False
    for room in classrooms:
        if room['end_time'] <= start:
            room['courses'].append(course)
            room['end_time'] = end
            allocated = True
            break
    if not allocated:
        classrooms.append({'end_time': end, 'courses': [course]})

# 输出结果
print(f"最少需要 {len(classrooms)} 间教室")
for i, room in enumerate(classrooms, 1):
    print(f"\n教室{i}安排的课程：")
    for c in room['courses']:
        start_time = min_to_time(c[0])
        end_time = min_to_time(c[1])
        print(f"({start_time}, {end_time})", end=" ")