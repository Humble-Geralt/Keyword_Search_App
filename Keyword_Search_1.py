import tkinter
import time
from tkinter import *
from tkinter import filedialog

class doc_edit():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        self.init_window_name.title("DocEdit")
        self.init_window_name.geometry('1080x720+20+20')
        #self.begin_window_name["bg"] = "pink"
        #标签
        self.file_path_label = Label(self.init_window_name,text = "文件路径")
        self.file_path_label.grid(row = 0, column = 5)
        self.key_word_label = Label(self.init_window_name,text = "搜索内容")
        self.key_word_label.grid(row = 4, column = 5)
        self.log_label = Label(self.init_window_name,text = "日志")
        self.log_label.grid(row =8, column = 5 )
        self.out_file_label = Label(self.init_window_name,text = "输出内容")
        self.out_file_label.grid(row=0,column = 75)
        self.file_cut_label = Label(self.init_window_name,text = "注：切分文档会直接保存切分后的文档")
        self.file_cut_label.grid(row=20,column = 5)

        #文本框
        self.file_path_Text = Text(self.init_window_name,width=30, height=3)#路径文本框
        self.file_path_Text.grid(row=1, column=5)
        self.key_word_Text = Entry(self.init_window_name,width = 30)#搜索
        self.key_word_Text.grid(row=5, column=5)
        self.log_label_Text = Text(self.init_window_name,width=60,height=15)#日志框
        self.log_label_Text.grid(row=9, column=5,columnspan=1,rowspan=7)
        self.log_label_Text.insert(END,'欢迎使用本软件,版本号Beta v0.1\n')
        self.out_file_Text = Text(self.init_window_name,width=65,height=40)#输出结果
        self.out_file_Text.grid(row=1,column=70,rowspan=10,columnspan=10)

        #按钮
        self.flie_choice = Button(self.init_window_name,text="选择文件",bg="lightblue",width=6,command=self.path_catch)
        self.flie_choice.grid(row=1,column=8)
        self.in_trans_out_English = Button(self.init_window_name, text="英文文件搜索",bg="lightblue",width=12,command=self.main_search_English)
        self.in_trans_out_English.grid(row=4,column=15)
        self.in_trans_out_Chinese = Button(self.init_window_name, text="中文文件搜索",bg="lightblue",width=12,command=self.main_search_Chinese)
        self.in_trans_out_Chinese.grid(row=6,column=15)
        self.file_save_Button = Button(self.init_window_name, text="保存搜索后文档",bg="lightblue",width=15,command=self.file_save)
        self.file_save_Button.grid(row=8,column=15)
        self.file_cut_Button = Button(self.init_window_name, text="切分文档",bg="lightblue",width=15,command=self.file_cut)
        self.file_cut_Button.grid(row=10,column=15)

    #功能函数

    global simplify_str
    global search
    global filter_str

    def simplify_str(list):
        if ''in data:
            data.remove('')
        i=0
        while (i<len(list)):
            temp=str(list[i])
            temp = " ".join(temp.split())
            list[i] = temp
            i+=1
    #简化器，简化字符串（删除换行，长短空格,剔除空列表且重新整理为列表）

    def filter_str(list,str):
        simplify_str(list)
        p=0
        global all_temp
        all_temp = []#声明全局变量，使得主函数中可以取得结果值
        while(p<len(list)):
            temp_list=[]
            temp = list[p]
            temp_list = temp.split(str)
            t=0
            while(t<len(temp_list)):
                all_temp.append(temp_list[t])
                t+=1
            p+=1
    #细分器，筛选指定列表内以str为分隔符后再次整理为列表

    def search(list,str):
        i=0
        result_lines=[]
        search_obj=str
        while(i<len(list)):
            temp_str = ''.join(list[i])
            if((temp_str.find(search_obj))>-1):
                result_lines.append(temp_str+'\n')
            i+=1
        return result_lines
    #搜索器，搜索以str为关键字的独立语句并输出此关键字有关所有语句的列表,默认处理后每句添加换行符

    def main_search_English(self):
        
        global keyword
        keyword =self.key_word_Text.get()
        
        f = open(file_path,'r',encoding='UTF-8')

        global data
        data=[]
        for each_lines in f:
            data.append(each_lines)
        simplify_str(data)
        str_lines = ''.join(data)
        data = str_lines.split('.')

        filter_str(data,'!')
        data=all_temp

        filter_str(data,'?')
        data=all_temp

        simplify_str(data)

        self.out_file_Text.delete(1.0,END)
        self.out_file_Text.insert(1.0,search(data,keyword))
        current_time = self.get_current_time()
        E_oversearch_remind = str(current_time)+'英文文档搜索完成'+'\n'
        self.log_label_Text.insert(END,E_oversearch_remind)
    #封包后的主体英文文档搜索功能
    def main_search_Chinese(self):

        global keyword
        keyword =self.key_word_Text.get()
   
        f = open(file_path,'r',encoding='UTF-8')

        global data
        data=[]
        for each_lines in f:
            data.append(each_lines)
        simplify_str(data)
        str_lines = ''.join(data)
        data = str_lines.split('。')

        filter_str(data,'！')
        data=all_temp

        filter_str(data,'？')
        data=all_temp

        simplify_str(data)

        self.out_file_Text.delete(1.0,END)
        self.out_file_Text.insert(1.0,search(data,keyword))
        current_time = self.get_current_time()
        C_oversearch_remind = str(current_time)+'中文文档搜索完成'+'\n'
        self.log_label_Text.insert(END,C_oversearch_remind)
    #封包后的主体中文文档搜索功能

    def file_cut(self):
        f = open(file_path,'r',encoding='UTF-8')

        global data
        data=[]
        count=0

        for each_line in f:
            data.append(each_line)
        print(data)
        simplify_str(data)
            
        while (count<len(data)):
            file_name_Result = 'Result_' + str(count) + '.txt'

            Result_file = open(file_name_Result,'w')
            Result_file.writelines(data[count])

            count += 1
            current_time = self.get_current_time()
            overcut_remind = str(current_time)+'文章第'+str(count)+'段落切分完成'+'\n'
            self.log_label_Text.insert(END,overcut_remind)
    #段落切分器

    def path_catch(self):
        global file_path
        file_path=filedialog.askopenfilename()
        self.file_path_Text.delete(1.0,END)
        self.file_path_Text.insert(1.0,file_path)
        current_time = self.get_current_time()
        getpath_remind = str(current_time)+'已获取文件路径'+'\n'
        self.log_label_Text.insert(END,getpath_remind)
    #抓取文档路径

    def file_save(self):
        file_name_Result = 'Result_' +keyword+ '.txt'
        Result_file = open(file_name_Result,'w')
        Result_file.writelines(search(data,keyword))
        current_time = self.get_current_time()
        save_remind =str(current_time)+ '已保存文件至本脚本根目录'+'\n'
        self.log_label_Text.insert(END,save_remind)
    #保存输出后的文档

    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time
    #获取当前时间

def gui_start():
    init_window = Tk()
    KEY_SEARCH = doc_edit(init_window)
    KEY_SEARCH.set_init_window()

    init_window.mainloop()#实例化

gui_start()





'''def simplify_str(list):
    if ''in data:
        data.remove('')
    i=0
    while (i<len(list)):
        temp=str(list[i])
        temp = " ".join(temp.split())
        list[i] = temp
        i+=1
#简化器，简化字符串（删除换行，长短空格,剔除空列表且重新整理为列表）

def filter_str(list,str):
    simplify_str(list)
    p=0
    global all_temp
    all_temp = []#声明全局变量，使得主函数中可以取得结果值
    while(p<len(list)):
        temp_list=[]
        temp = list[p]
        temp_list = temp.split(str)
        t=0
        while(t<len(temp_list)):
            all_temp.append(temp_list[t])
            t+=1
        p+=1
#细分器，筛选指定列表内以str为分隔符后再次整理为列表

def search(list,str):
    i=0
    result_lines=[]
    search_obj=str
    while(i<len(list)):
        temp_str = ''.join(list[i])
        if((temp_str.find(search_obj))>-1):
            result_lines.append(temp_str+'\n')
        i+=1
    return result_lines
#搜索器，搜索以str为关键字的独立语句并输出此关键字有关所有语句的列表,默认处理后每句添加换行符

def main_search_English(file_path,keyword):
   
    f = open(file_path,'r',encoding='UTF-8')

    global data
    data=[]
    for each_lines in f:
        data.append(each_lines)
    simplify_str(data)
    str_lines = ''.join(data)
    data = str_lines.split('.')

    filter_str(data,'!')
    data=all_temp

    filter_str(data,'?')
    data=all_temp

    simplify_str(data)

    file_name_Result = 'Result_' +keyword+ '.txt'
    Result_file = open(file_name_Result,'w')
    Result_file.writelines(search(data,keyword))

    self.out_file_Text.clear()
    self.out_file_Text.insert(1.0,search(data,keyword))
#封包后的主体英文文档搜索功能
def main_search_Chinese(file_path,keyword):
   
    f = open(file_path,'r',encoding='UTF-8')

    global data
    data=[]
    for each_lines in f:
        data.append(each_lines)
    simplify_str(data)
    str_lines = ''.join(data)
    data = str_lines.split('。')

    filter_str(data,'！')
    data=all_temp

    filter_str(data,'？')
    data=all_temp

    simplify_str(data)

    print(search(data,keyword))

    file_name_Result = 'Result_' +keyword+ '.txt'
    Result_file = open(file_name_Result,'w')
    Result_file.writelines(search(data,keyword))
    print('目标文档已创建完成')
#封包后的主体中文文档搜索功能

word =input('请输入需要搜索的内容：')
type_num = 'C'
type_num = input('中文文件输入C 英文文件输入E（默认中文）：')
if type_num == 'C':
    print('请选择文件路径')
    time.sleep(1.5)
    main_search_Chinese(filedialog.askopenfilename(),word)
else:
    print('请选择文件路径')
    time.sleep(1.5)
    main_search_English(filedialog.askopenfilename(),word)'''#旧代码
