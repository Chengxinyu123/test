#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <conio.h> // windows系统下的头文件，用于实现 getch() 函数

using namespace std;

const int WIDTH = 20; // 场景宽度
const int HEIGHT = 20; // 场景高度

enum Direction { NONE, UP, LEFT, DOWN, RIGHT }; // 定义枚举类型表示方向

class Snake {
public:
    Snake(int x, int y) : direction(NONE) {
        cells.push_back(make_pair(x, y)); // 初始化蛇身
    }
    bool move() {
        if (direction == NONE) return false; // 当前方向为NONE则直接返回
        auto head = cells.front(); // 获取蛇头
        switch (direction) {
            case UP: head.second--; break;
            case LEFT: head.first--; break;
            case DOWN: head.second++; break;
            case RIGHT: head.first++; break;
        }
        if (head.first < 0 || head.first >= WIDTH || head.second < 0 || head.second >= HEIGHT) {
            // 碰到边界，游戏结束
            return true;
        }
        cells.insert(cells.begin(), head); // 将新的蛇头加入到 cells 的最前面
        if (head == food) {
            generateFood(); // 吃到食物，重新生成一个新的食物
        } else {
            cells.pop_back(); // 没有吃到食物，将 cells 的最后一个元素（即蛇尾）弹出
        }
        return false;
    }
    void changeDirection(Direction dir) {
        // 判断是否在相反方向移动
        if (direction != NONE && abs(direction - dir) == 2) return;
        direction = dir;
    }
    const vector<pair<int, int>>& getCells() const {
        return cells;
    }
    void generateFood() {
        srand(time(NULL));
        do {
            food.first = rand() % WIDTH;
            food.second = rand() % HEIGHT;
        } while (find(cells.begin(), cells.end(), food) != cells.end());
        // 生成的食物位置不能与蛇身相同
    }
    const pair<int, int>& getFood() const {
        return food;
    }
private:
    Direction direction; // 蛇的当前方向
    vector<pair<int, int>> cells; // 蛇身体的所有 cell，第一个为蛇头
    pair<int, int> food; // 食物的位置
};

int main() {
    Snake snake(WIDTH / 2, HEIGHT / 2); // 初始化蛇的位置在中央
    snake.generateFood(); // 生成初始食物
    while (true) {
        system("cls"); // 清空屏幕
        cout << "Score: " << snake.getCells().size() - 1 << endl;
        cout << "+";
        for (int i = 0; i < WIDTH; i++) {
            cout << "-";
        }
        cout << "+" << endl;
        for (int y = 0; y < HEIGHT; y++) {
            cout << "|";
            for (int x = 0; x < WIDTH; x++) {
                auto cells = snake.getCells();
                if (make_pair(x, y) == snake.getFood()) {
                    cout << "F"; // 食物位置
                } else if (find(cells.begin(), cells.end(), make_pair(x, y)) != cells.end()) {
                    cout << "O"; // 蛇身
                } else {
                    cout << " "; // 空白处
                }
            }
            cout << "|" << endl;
        }
        cout << "+";
        for (int i = 0; i < WIDTH; i++) {
            cout << "-";
        }
        cout << "+" << endl;
        if (snake.move()) {
            cout << "Game over!" << endl;
            break;
        }
        if (_kbhit()) { // 有按键输入
            switch (_getch()) {
                case 'w': snake.changeDirection(UP); break;
                case 'a': snake.changeDirection(LEFT); break;
                case 's': snake.changeDirection(DOWN); break;
                case 'd': snake.changeDirection(RIGHT); break;
            }
        }
        // 控制速度，例如 usleep(1000) 等
    }
    return 0;
}