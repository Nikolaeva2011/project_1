import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1164</width>
    <height>863</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>500</width>
    <height>550</height>
   </size>
  </property>
  <property name="font">
   <font>
    <pointsize>8</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>WordWise Mini</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: #F5F3E9</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="styleSheet">
    <string notr="true"/>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <property name="spacing">
     <number>12</number>
    </property>
    <property name="leftMargin">
     <number>40</number>
    </property>
    <property name="topMargin">
     <number>50</number>
    </property>
    <property name="rightMargin">
     <number>40</number>
    </property>
    <property name="bottomMargin">
     <number>50</number>
    </property>
    <item>
     <spacer name="verticalSpacer">
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>20</width>
        <height>40</height>
       </size>
      </property>
     </spacer>
    </item>
    <item>
     <widget class="QLabel" name="title_label">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="font">
       <font>
        <pointsize>41</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #33382B</string>
      </property>
      <property name="text">
       <string>WordWise Mini</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="subtitle_label">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="font">
       <font>
        <pointsize>15</pointsize>
        <weight>50</weight>
        <italic>true</italic>
        <bold>false</bold>
        <strikeout>false</strikeout>
        <kerning>true</kerning>
       </font>
      </property>
      <property name="styleSheet">
       <string notr="true">color: #33382B</string>
      </property>
      <property name="text">
       <string>Твой маленький помощник в изучении анлийского</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QWidget" name="widget" native="true">
      <property name="font">
       <font>
        <pointsize>6</pointsize>
       </font>
      </property>
      <layout class="QVBoxLayout" name="verticalLayout_2">
       <item alignment="Qt::AlignHCenter">
        <widget class="QPushButton" name="dictionary_pushButton">
         <property name="minimumSize">
          <size>
           <width>380</width>
           <height>65</height>
          </size>
         </property>
         <property name="maximumSize">
          <size>
           <width>350</width>
           <height>65</height>
          </size>
         </property>
         <property name="font">
          <font>
           <pointsize>-1</pointsize>
           <weight>75</weight>
           <bold>true</bold>
          </font>
         </property>
         <property name="styleSheet">
          <string notr="true">QPushButton {
    background-color: #E5E3D4;
    color: #33382B;
    border: none;
    border-radius: 12px;
    font-size: 16px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #D8D6C5;
}</string>
         </property>
         <property name="text">
          <string>Мой словарь</string>
         </property>
        </widget>
       </item>
       <item alignment="Qt::AlignHCenter">
        <widget class="QPushButton" name="start_pushButton">
         <property name="minimumSize">
          <size>
           <width>380</width>
           <height>65</height>
          </size>
         </property>
         <property name="maximumSize">
          <size>
           <width>350</width>
           <height>65</height>
          </size>
         </property>
         <property name="styleSheet">
          <string notr="true">QPushButton {
    background-color: #68734A;
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 16px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #7C895A;
}</string>
         </property>
         <property name="text">
          <string>Начало теста</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
    <item>
     <spacer name="verticalSpacer_2">
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>20</width>
        <height>40</height>
       </size>
      </property>
     </spacer>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1164</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QToolBar" name="toolBar">
   <property name="windowTitle">
    <string>toolBar</string>
   </property>
   <attribute name="toolBarArea">
    <enum>TopToolBarArea</enum>
   </attribute>
   <attribute name="toolBarBreak">
    <bool>false</bool>
   </attribute>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.start_pushButton.clicked.connect(self.run)

    def run(self):
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())
