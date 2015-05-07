#include <QApplication>
#include <QLabel>
// process with: qmake hello.pro

int main(int argc, char **argv)
{
    QApplication app(argc, argv);
    QLabel hello("Hello world!");

    hello.show();
    return app.exec();
}
