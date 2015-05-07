/********************************************************************************
** Form generated from reading UI file 'widget_1.ui'
**
** Created by: Qt User Interface Compiler version 5.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WIDGET_1_H
#define UI_WIDGET_1_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QSlider *x_vel;
    QSlider *y_vel;
    QPushButton *resetButton;
    QTextEdit *y_label;
    QTextEdit *x_label;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QStringLiteral("Form"));
        Form->setEnabled(true);
        Form->resize(328, 300);
        x_vel = new QSlider(Form);
        x_vel->setObjectName(QStringLiteral("x_vel"));
        x_vel->setGeometry(QRect(80, 200, 160, 21));
        x_vel->setMinimum(-5);
        x_vel->setMaximum(5);
        x_vel->setOrientation(Qt::Horizontal);
        y_vel = new QSlider(Form);
        y_vel->setObjectName(QStringLiteral("y_vel"));
        y_vel->setGeometry(QRect(150, 20, 21, 160));
        y_vel->setMinimum(-5);
        y_vel->setMaximum(5);
        y_vel->setOrientation(Qt::Vertical);
        resetButton = new QPushButton(Form);
        resetButton->setObjectName(QStringLiteral("resetButton"));
        resetButton->setGeometry(QRect(110, 240, 87, 27));
        y_label = new QTextEdit(Form);
        y_label->setObjectName(QStringLiteral("y_label"));
        y_label->setEnabled(false);
        y_label->setGeometry(QRect(210, 80, 104, 21));
        x_label = new QTextEdit(Form);
        x_label->setObjectName(QStringLiteral("x_label"));
        x_label->setEnabled(false);
        x_label->setGeometry(QRect(210, 120, 104, 21));

        retranslateUi(Form);

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QApplication::translate("Form", "First QT", 0));
        resetButton->setText(QApplication::translate("Form", "Reset Vals", 0));
        y_label->setHtml(QApplication::translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Droid Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", 0));
        x_label->setHtml(QApplication::translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Droid Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", 0));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui


QT_END_NAMESPACE

#endif // UI_WIDGET_1_H

