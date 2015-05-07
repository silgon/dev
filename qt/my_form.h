#include <iostream>
#include <stdio.h>
#include "widget.h"
#include <QString>

class MyForm : public QWidget, private Ui::Form{
    Q_OBJECT

public:
    MyForm(QWidget *parent = 0): QWidget(parent)
    {
        setupUi(this);
        connect(resetButton, SIGNAL(clicked()), this, SLOT(reset()));
        connect(x_vel, SIGNAL(valueChanged(int)), this, SLOT(set_x_label(int)));
        connect(y_vel, SIGNAL(valueChanged(int)), this, SLOT(set_y_label(int)));
    };
    virtual ~MyForm(){};
private slots:
    void reset(){
        x_vel->setValue(0);
        y_vel->setValue(0);
    }
    void set_x_label(int val){
        x_label->setText(QString::number(val));
    }
    void set_y_label(int val){
        y_label->setText(QString::number(val));
    }
};

