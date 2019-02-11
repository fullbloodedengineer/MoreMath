from PyQt5.QtWidgets import QApplication,QTableView,QItemDelegate,QStyle
import pandas as pd
from PyQt5.QtGui import QPen,QBrush
from PyQt5.QtCore import Qt,QAbstractTableModel,QVariant

PD_DATA_ROLE = 9001

class BaseDelegate(QItemDelegate):
    """
    A Custom delegate to view the data within the model
    Custom coloring can be provided based on data values
    """
    def __init__(self, parent=None, *args):
        QItemDelegate.__init__(self, parent, *args)
        self.range = (10,20)

    def paint(self, painter, option, index):
        painter.save()

        # set background color
        painter.setPen(QPen(Qt.NoPen))
        if option.state & QStyle.State_Selected:
            painter.setBrush(QBrush(Qt.red))
        else:
            painter.setBrush(QBrush(Qt.blue))
        painter.drawRect(option.rect)
        # set text color
        painter.setPen(QPen(Qt.red))
        value = index.data(PD_DATA_ROLE)
        print type(value),value
        text = str(value)
        painter.drawText(option.rect, Qt.AlignLeft, text)

        painter.restore()

class DataFrameModel(QAbstractTableModel):
    """
    Create a basic model of a pandas dataframe
    """
    def __init__(self, data, parent=None):
        super(DataFrameModel,self).__init__(parent)
        self.data_frame = data
        self.headers = list(data)

    def headerData(self,section,orientation,role):
     if role == Qt.DisplayRole:
        if orientation == Qt.Horizontal:
            return str(self.headers[section])

     return QVariant();

    def rowCount(self, parent=None):
        return len(self.data_frame.values)

    def columnCount(self, parent=None):
        return self.data_frame.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self.data_frame.values[index.row()][index.column()])
            elif role == PD_DATA_ROLE:
                return self.data_frame.values[index.row()][index.column()]
        return QVariant()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    df = pd.DataFrame(data=[[1,True,'String'],[2,2,2]],columns=['C1','C2','C3'])
    model = DataFrameModel(df)
    view = QTableView()
    view.setModel(model)
    view.setItemDelegate(BaseDelegate())
    view.show()

    sys.exit(app.exec_())
