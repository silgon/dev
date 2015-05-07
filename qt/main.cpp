#include <stdio.h>
#include "widget.h"
#include <QMainWindow>
#include <QLabel>

// GUI created with: uic widget_1.ui > widget.h

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QWidget *widget = new QWidget;
    Ui::Form ui;
    ui.setupUi(widget);
    widget->show();
    return app.exec();
}
