TEMPLATE = app
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
CONFIG += qt warn_on release
HEADERS = widget.h my_form.h
SOURCES = main.cpp
TARGET = main
