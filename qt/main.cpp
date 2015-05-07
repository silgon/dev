#include <stdio.h>
#include "my_form.h"

// GUI created with: uic widget_1.ui > widget.h
// needed files: main.cpp, widget.h and my_form.h

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    // QWidget *widget = new QWidget;
    // Ui::Form ui;
    // ui.setupUi(widget);
    // widget->show();
    MyForm ui;
    ui.show();
    return app.exec();
}
