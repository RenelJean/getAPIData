/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 2.15
import QtQuick.Controls 2.15
import Cube 1.0

Rectangle {
    width: 2000
    height: 1500
    color: "#2b2b2b"


    Column {
        id: column
        x: 0
        y: 0
        width: 450
        height: 1469

        Button {
            id: button
            width: 450
            height: 100
            text: qsTr("Button")
            font.pointSize: 12
        }

        Button {
            id: button1
            width: 450
            height: 100
            text: qsTr("Button")
            font.pointSize: 12
        }

        Button {
            id: button2
            width: 450
            height: 100
            text: qsTr("Button")
            font.pointSize: 12
        }

        Button {
            id: button3
            width: 450
            height: 100
            text: qsTr("Button")
            font.pointSize: 12
        }

        Button {
            id: button4
            width: 450
            height: 100
            text: qsTr("Button")
            font.pointSize: 12
        }

        Button {
            id: button5
            width: 450
            height: 100
            text: qsTr("Button")
            font.pointSize: 12
        }

        Button {
            id: button6
            width: 450
            height: 100
            text: qsTr("Button")
            font.pointSize: 12
        }

        Button {
            id: button7
            width: 450
            height: 100
            text: qsTr("Button")
            font.pointSize: 12
        }

        Button {
            id: button8
            width: 450
            height: 100
            text: qsTr("Button")
            font.pointSize: 12
        }

        Button {
            id: button9
            width: 450
            height: 100
            text: qsTr("Button")
            font.pointSize: 12
        }

        Button {
            id: button10
            width: 450
            height: 100
            text: qsTr("Button")
            font.pointSize: 12
        }
    }

    Label {
        id: label2
        x: 481
        y: 323
        width: 182
        height: 70
        text: qsTr("Organization:")
        font.bold: true
        font.pointSize: 12
    }

    Label {
        id: label1
        x: 481
        y: 194
        width: 132
        height: 50
        text: qsTr("First Name:")
        font.bold: true
        font.pointSize: 12
    }

    Label {
        id: label
        x: 481
        y: 69
        width: 70
        height: 43
        text: qsTr("Position:")
        font.bold: true
        font.pointSize: 12
    }

    Label {
        id: label3
        x: 1333
        y: 60
        width: 82
        height: 44
        text: qsTr("Prefix:")
        font.bold: true
        font.pointSize: 12
    }

    Label {
        id: label4
        x: 1271
        y: 202
        width: 113
        height: 33
        text: qsTr("Last Name:")
        font.bold: true
        font.pointSize: 12
    }

    Label {
        id: label5
        x: 1348
        y: 329
        width: 67
        height: 44
        text: qsTr("Email:")
        font.bold: true
        font.pointSize: 12
    }

    TextArea {
        id: textArea
        x: 739
        y: 42
        width: 487
        height: 96
        font.pointSize: 17
        placeholderText: qsTr("Text Area")
    }

    TextArea {
        id: textArea1
        x: 739
        y: 173
        width: 487
        height: 91
        font.pointSize: 17
        placeholderText: qsTr("Text Area")
    }

    TextArea {
        id: textArea2
        x: 739
        y: 298
        width: 495
        height: 120
        font.pointSize: 17
        placeholderText: qsTr("Text Area")
    }

    TextArea {
        id: textArea3
        x: 1483
        y: 33
        width: 492
        height: 97
        font.pointSize: 17
        placeholderText: qsTr("Text Area")
    }

    TextArea {
        id: textArea4
        x: 1483
        y: 168
        width: 492
        height: 101
        font.pointSize: 17
        placeholderText: qsTr("Text Area")
    }

    TextArea {
        id: textArea5
        x: 1483
        y: 298
        width: 501
        height: 120
        font.pointSize: 18
        placeholderText: qsTr("Text Area")
    }

    CheckDelegate {
        id: checkDelegate
        x: 622
        y: 499
        width: 362
        height: 44
        text: qsTr("Course Project")
        font.pointSize: 15
    }

    CheckDelegate {
        id: checkDelegate1
        x: 623
        y: 547
        width: 361
        height: 44
        text: qsTr("Guest Speaker")
        font.pointSize: 15
    }

    CheckDelegate {
        id: checkDelegate2
        x: 629
        y: 597
        width: 355
        height: 44
        text: qsTr("Site Visit")
        font.pointSize: 15
    }

    CheckDelegate {
        id: checkDelegate3
        x: 623
        y: 647
        width: 361
        height: 44
        text: qsTr("Job Shadow")
        font.pointSize: 15
    }

    CheckDelegate {
        id: checkDelegate4
        x: 623
        y: 704
        width: 361
        height: 44
        text: qsTr("Internship")
        font.pointSize: 17
    }

    CheckDelegate {
        id: checkDelegate5
        x: 622
        y: 764
        width: 362
        height: 44
        text: qsTr("Career Panel")
        font.pointSize: 17
    }

    CheckDelegate {
        id: checkDelegate6
        x: 623
        y: 801
        width: 361
        height: 105
        text: qsTr("Network Event")
        font.pointSize: 17
        antialiasing: false
        checkable: false
    }

    Label {
        id: label6
        x: 655
        y: 996
        width: 303
        height: 85
        text: qsTr("Description:")
        font.bold: true
        font.pointSize: 20
    }

    TextArea {
        id: textArea6
        x: 655
        y: 1112
        width: 1287
        height: 325
        font.pointSize: 30
        placeholderText: qsTr("Text Area")
    }


}
