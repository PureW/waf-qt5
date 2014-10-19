#include "notepad.h"
#include "ui_notepad.h"

Notepad::Notepad(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Notepad)
{

    ui->setupUi(this);
}

Notepad::~Notepad()
{
    delete ui;
}

#if WAF
	#include "notepad.moc"
	#include "notepad.cpp.moc"
#endif

