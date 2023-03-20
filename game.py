from PyQt6.QtWidgets import QPushButton
class Game:
    def __init__(self,ls = [[QPushButton]]) -> None:
        self.btns = ls
    def reset_game(self):
        for i in range(len(self.btns)):
            for btn in self.btns[i]:
                btn.setText("")
                btn.setEnabled(True)
    def false_game(self):
        for i in range(len(self.btns)):
            for btn in self.btns[i]:
                btn.setText("")
                btn.setEnabled(False)
    
    def check_win(self,ans:str):
        if ans.lower()=="xxx":
            return "X"
        elif ans.lower() == "ooo":
            return "O"
        return False

    def win_rows(self):
        for i in range(len(self.btns)):
            txt = ""
            for btn in self.btns[i]:
                txt+=btn.text()
            ch = self.check_win(txt)
            if ch!=False:
                return ch
    def win_cols(self):
        for i in range(len(self.btns)):
            txt = ""
            for j in range(len(self.btns)):
                txt += self.btns[j][i].text()
            ans = self.check_win(txt)
            if ans != False:
                return ans
    def win_dig(self):
        txt = ""
        for i in range(len(self.btns)):
            txt += self.btns[i][i].text()
        ans = self.check_win(txt)
        if ans in ["X","O"]:
            return ans
        txt = ""
        for i in range(len(self.btns)):
            txt+=self.btns[i][len(self.btns)-i-1].text()
        ans = self.check_win(txt)
        if ans in["X","O"]:
            return ans
        return False
    def check_game(self):
        ans = self.win_rows()
        if ans not in [False,None]:
            return ans
        ans = self.win_cols()
        if ans not in [False,None]:
            return ans
        ans = self.win_dig()
        if ans not in [False,None]:
            return ans
        return False
    def chek_draw(self):
        b =0
        for i in self.btns:
            for j in i:
                if j.text()!='':
                    b+=1
        if b==9:
            return True
        else:
            return False

