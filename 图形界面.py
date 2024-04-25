import sys

import sympy
from PySide6.QtWidgets import QMainWindow, QApplication,QComboBox
from sympy import *
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    label_list=[]#存放条件标签
    line_list=[]#存放条件名
    label_var_list=[]#存放变量名标签
    line_var_list=[]#存放变量名
    zero=[]
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #list=["1","2","3","4"]
        self.setWindowTitle("求条件极值")
        self.number_of_index.addItem("1")
        self.number_of_index.addItem("2")
        self.number_of_index.addItem("3")
        self.number_of_index.addItem("4")
        # self.number_of_condition.addItems(list)
        self.number_of_index.activated.connect(self.slot)
        self.condition1_label.close()
        self.condition2_label.close()
        self.condition3_label.close()
        self.condition4_label.close()
        self.condition_line1.close()
        self.condition_line2.close()
        self.condition_line3.close()
        self.condition_line4.close()
        self.label_list.append(self.condition1_label)
        self.label_list.append(self.condition2_label)
        self.label_list.append(self.condition3_label)
        self.label_list.append(self.condition4_label)
        self.line_list.append(self.condition_line1)
        self.line_list.append(self.condition_line2)
        self.line_list.append(self.condition_line3)
        self.line_list.append(self.condition_line4)
        self.line_var_list.append(self.condition_name_1)
        self.line_var_list.append(self.condition_name_2)
        self.line_var_list.append(self.condition_name_3)
        self.line_var_list.append(self.condition_name_4)
        self.label_var_list.append(self.label_condition_number1)
        self.label_var_list.append(self.label_condition_number2)
        self.label_var_list.append(self.label_condition_number3)
        self.label_var_list.append(self.label_condition_number4)
        self.Activicate.clicked.connect(self.calculate)
        self.zero.append(self.zero_1)
        self.zero.append(self.zero_2)
        self.zero.append(self.zero_3)
        self.zero.append(self.zero_4)
        for i in self.label_var_list:
            i.close()
        for i in self.line_var_list:
            i.close()
        for i in self.zero:
            i.close()
    def slot(self):
        text=self.number_of_index.currentText()
        number=int(text)
        print(number)
        for i in range(4):
            if(i<number-1):
                self.label_list[i].show()
                self.line_list[i].show()
                self.zero[i].show()
            else:
                self.label_list[i].close()
                self.line_list[i].close()
                self.zero[i].close()
        for i in range(4):
            if (i < number):
                self.label_var_list[i].show()
                self.line_var_list[i].show()
            else:
                self.label_var_list[i].close()
                self.line_var_list[i].close()

    def calculate(self):
        try:
            self.result.setText("")

            print("calculate")
            x1,x2,x3,x4,k1,k2,k3=symbols("x1,x2,x3,x4,k1,k2,k3")
            norlist=["x1","x2","x3","x4"]
            k_list=[k1,k2,k3]
            symbol_list=[x1,x2,x3,x4]
            symbols_var,symbols_fu=[],[]
            symbols_var.append(x1)
            symbols_var.append(x2)
            symbols_var.append(x3)
            symbols_var.append(x4)
            symbols_fu.append(k1)
            symbols_fu.append(k2)
            symbols_fu.append(k3)
            var_number=int(self.number_of_index.currentText())
            var_dict={}
            var_dict_2={}
            for i in range(var_number):
                var_dict[self.line_var_list[i].text()]=norlist[i]
                var_dict_2[norlist[i]]=self.line_var_list[i].text()
            print(var_dict)
            condition_text=[]
            for i in range(var_number-1):
                text_temp = self.line_list[i].text()
                for index in range(var_number):
                    text_temp=text_temp.replace(self.line_var_list[index].text(),var_dict[self.line_var_list[index].text()])
                print(text_temp)
                condition_text.append(sympy.sympify(text_temp))
                print(text_temp)
            ftext=self.lineEdit.text()
            for index in range(var_number):
                ftext= ftext.replace(self.line_var_list[index].text(), var_dict[self.line_var_list[index].text()])
            f=sympy.sympify(ftext)
            L=f
            print("df")
            for i in range(var_number-1):
               L+=k_list[i]*condition_text[i]
            print("L="+str(L))
            diff_list=[]
            result_var_list=[]
            for i in range(var_number):
                diff_list.append(diff(L,symbol_list[i]))
                result_var_list.append(symbol_list[i])
            for i in range(var_number-1):
                diff_list.append(diff(L,k_list[i]))
                result_var_list.append(k_list[i])
            m=solve(diff_list,result_var_list)
            print(m)
            print("stop")
            min=10e9
            max=-10e9
            max_result={}
            min_result={}
            for i in m:
                result_xx_list={}
                for j in range(var_number):
                    result_xx_list[symbol_list[j]]=i[j]
                print(f.subs(result_xx_list))
                if(float(f.subs(result_xx_list))>max):
                    max=f.subs(result_xx_list)
                    max_result=result_xx_list
                if(float(f.subs(result_xx_list))<min):
                    min=f.subs(result_xx_list)
                    min_result=result_xx_list

            if(min!=10e9):
                text="最小值为"+str(min)+"\n"
                for i in range(len(min_result)):
                    text+=(str(var_dict_2[norlist[i]])+"="+str(min_result[symbol_list[i]])+"\n")
            if (max != 10e9):
                text += "最大值为" + str(max) + "\n"
                for i in range(len(max_result)):
                    text += (str(var_dict_2[norlist[i]]) + "=" + str(max_result[symbol_list[i]]) + "\n")
            self.result.setText(text)
        except Exception as e:
            self.result.setText(str(e))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
