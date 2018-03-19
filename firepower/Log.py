import logging

class DBTool:
    def __init__(self):
        #請你給我一個 Log 的分身，他的名字叫做.... __name__ (function 的名稱)！！
        self.logger = logging.getLogger( 'wwww' )
        #設定這個log 分身他要處理的情報等級
        self.logger.setLevel(logging.INFO)
        #關於 log 將要輸出的檔案，請你按照下面的設定，幫我處理一下
        fh = logging.FileHandler('receive.log', 'w', 'utf-8')
        #設定這個檔案要處理的情報等級，只要是 debug 等級或以上的就寫入檔案
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        #關於 console(也就是cmd 那個黑黑的畫面)，請你按照下面的設定，幫我處理一下
        ch = logging.StreamHandler()
        #設定 Console 要處理的情報等級，只要是 Info 等級的就印出來
        ch.setLevel(logging.INFO)
        # create formatter and add it to the handlers
        # log 印出來的格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #將 印出來的格式和 File Handle, Console Handle 物件組合在一起
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        #log 的分身組合 File Handle 和 Console Handle
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
 


