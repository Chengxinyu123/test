import pygame
import random

# 游戏窗口的大小
width = 600
height = 480

# 蛇和食物的大小和颜色
snake_size = 10
food_size = 10
snake_color = (0, 255, 0)
food_color = (255, 0, 0)

# 初始化pygame
pygame.init()

# 创建游戏窗口
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇")

# 随机生成食物的位置
def generate_food():
    x = round(random.randrange(0, width - food_size) / 10.0) * 10.0
    y = round(random.randrange(0, height - food_size) / 10.0) * 10.0
    return x, y

# 绘制蛇
def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(window, snake_color, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

# 绘制食物
def draw_food(food_pos):
    pygame.draw.rect(window, food_color, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size))

# 游戏循环
def game_loop():
    # 初始化蛇和食物的位置和速度
    snake_x = 300
    snake_y = 240
    snake_speed = 10
    snake_body = [[snake_x, snake_y], [snake_x - 10, snake_y], [snake_x - 20, snake_y]]
    food_pos = generate_food()
    score = 0

    while True:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 判断按键
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake_x -= snake_speed
        if keys[pygame.K_RIGHT]:
            snake_x += snake_speed
        if keys[pygame.K_UP]:
            snake_y -= snake_speed
        if keys[pygame.K_DOWN]:
            snake_y += snake_speed

        # 更新蛇的身体
        snake_body.insert(0, [snake_x, snake_y])
        if snake_x == food_pos[0] and snake_y == food_pos[1]:
            food_pos = generate_food()
            score += 10
        else:
            snake_body.pop()

        # 绘制界面
        window.fill((0, 0, 0))
        draw_snake(snake_body)
        draw_food(food_pos)
        pygame.display.update()

        # 判断游戏结束
        if snake_x < 0 or snake_x > width - snake_size or snake_y < 0 or snake_y > height - snake_size:
            print('Game Over!')
            break
        if [snake_x, snake_y] in snake_body[1:]:
            print('Game Over!')
            break

    # 重新开始游戏
    game_loop()

# 开始游戏
game_loop()
提示用户游戏已经结束 def gameover_screen(): font = pygame.font.Font(None, 50) text = font.render("Game Over!", True, (255, 0, 0)) window.blit(text, (width/2 - 80, height/2 - 30)) pygame.display.update() # 清空分数和蛇的身体 def reset_game(): snake_body.clear() snake_body.append([snake_x, snake_y]) snake_body.append([snake_x - 10, snake_y]) snake_body.append([snake_x - 20, snake_y]) score = 0 # 绘制蛇 def draw_snake(snake_body, direction): head = snake_body[0] if direction == 'UP': head_img = pygame.image.load('snakehead_up.png') head[1] -= snake_speed elif direction == 'DOWN': head_img = pygame.image.load('snakehead_down.png') head[1] += snake_speed elif direction == 'LEFT': head_img = pygame.image.load('snakehead_left.png') head[0] -= snake_speed elif direction == 'RIGHT': head_img = pygame.image.load('snakehead_right.png') head[0] += snake_speed window.blit(head_img, head) for pos in snake_body[1:]: pygame.draw.rect(window, snake_color, pygame.Rect(pos[0], pos[1], snake_size, snake_size)) # 绘制食物 def draw_food(food_pos, food_type): if food_type == 'normal': pygame.draw.rect(window, food_color, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size)) elif food_type == 'special': special_food_img = pygame.image.load('special_food.png') window.blit(special_food_img, food_pos) # 加入音效和背景音乐 pygame.mixer_music.load('bg_music.mp3') pygame.mixer_music.play(-1) food_sound = pygame.mixer.Sound('eat_food.wav') gameover_sound = pygame.mixer.Sound('gameover.wav') # 初始化pygame pygame.init() # 创建游戏窗口 window = pygame.display.set_mode((width, height)) pygame.display.set_caption("贪吃蛇") # 随机生成食物的位置 def generate_food(): x = round(random.randrange(0, width - food_size) / 10.0) * 10.0 y = round(random.randrange(0, height - food_size) / 10.0) * 10.0 return x, y # 游戏循环 def game_loop(): # 初始化蛇和食物的位置和速度 global snake_x, snake_y, snake_speed, snake_body, food_pos, score snake_x = 300 snake_y = 240 snake_speed = 10 snake_body = [[snake_x, snake_y], [snake_x - 10, snake_y], [snake_x - 20, snake_y]] food_pos = generate_food() score = 0 direction = 'RIGHT' while True: # 处理事件 for event in pygame.event.get(): if event.type == pygame.QUIT: pygame.quit() quit() # 判断按键 keys = pygame.key.get_pressed() if keys[pygame.K_LEFT] and direction != 'RIGHT': direction = 'LEFT' elif keys[pygame.K_RIGHT] and direction != 'LEFT': direction = 'RIGHT' elif keys[pygame.K_UP] and direction != 'DOWN': direction = 'UP' elif keys[pygame.K_DOWN] and direction != 'UP': direction = 'DOWN' # 更新蛇的身体 draw_snake(snake_body, direction) # 判断是否吃到食物 if snake_x == food_pos[0] and snake_y == food_pos[1]: food_pos = generate_food() score += 10 food_type = 'normal' if score % 50 == 0: food_type = 'special' food_sound.play() if food_type == 'special': score += 20 elif score == 0: direction = 'RIGHT' else: snake_body.pop() # 绘制界面 window.fill((0, 0, 0)) draw_snake(snake_body, direction) draw_food(food_pos, food_type) # 显示分数 font = pygame.font.Font(None, 30) text = font.render("Score: " + str(score), True, (255, 255, 255)) window.blit(text, (20, 20)) pygame.display.update() # 判断游戏结束 if snake_x 0 or snake_x > width - snake_size or snake_y 0 or snake_y > height - snake_size: gameover_sound.play() reset_game() gameover_screen() pygame.display.update() pygame.time.wait(3000) # 等待3秒重新开始 game_loop() if [snake_x, snake_y] in snake_body[1:]: gameover_sound.play() reset_game() gameover_screen() pygame.display.update() pygame.time.wait(3000) # 等待3秒重新开始 game_loop() # 开始游戏 game_loop()