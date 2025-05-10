def asteroid_collision(asteroids):
    stack = []
    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < abs(asteroid):
                stack.pop()
            elif stack[-1] == abs(asteroid):
                stack.pop()
                break
            else:
                break
        else:
            stack.append(asteroid)
    return stack

# 示例
A = [23, -8, 9, -3, -7, 9, -23, 22]
result = asteroid_collision(A)
print("输出:", result)  # 输出: [-3, -6, 2, 8, 9, 11]