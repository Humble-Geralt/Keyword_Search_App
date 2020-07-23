from tkinter import filedialog
import time

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

    print(search(data,keyword))

    file_name_Result = 'Result_' +keyword+ '.txt'
    Result_file = open(file_name_Result,'w')
    Result_file.writelines(search(data,keyword))
    print('目标文档已创建完成')
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
    main_search_English(filedialog.askopenfilename(),word)def simplify_str(list):
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
            result_lines.append(temp_str)
        i+=1
    return result_lines
#搜索器，搜索以str为关键字的独立语句并输出此关键字有关所有语句的列表

f = open('Test.txt','r',encoding='UTF-8')

keyword =input('请输入需要搜索的内容：')

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
print(data)

print(search(data,keyword))

file_name_Result = 'Result_' +keyword+ '.txt'
Result_file = open(file_name_Result,'w')
Result_file.writelines(search(data,keyword))
