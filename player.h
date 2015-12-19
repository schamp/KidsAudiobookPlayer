#ifndef PLAYER_H
#define PLAYER_H

#include <QMainWindow>

namespace Ui {
class Player;
}

class Player : public QMainWindow
{
    Q_OBJECT

public:
    explicit Player(QWidget *parent = 0);
    ~Player();

private:
    Ui::Player *ui;
};

#endif // PLAYER_H
